import os, socket, subprocess

#function to obtain the ip address
def obtain_ip():
    stp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        stp.connect(("10.255.255.255", 1))
        IP = stp.getsockname()[0]
    except Exception:
        IP = "127.0.0.1"
    finally:
        stp.close()
    return IP

#port scanning function
def portScans():
    portNum = int(input("Port Number: "))
    option = ["1. Port selection", "2. Port Scan Types"]
    print("\n".join(option))
    try:
        pOption = int(input("Option: "))
        match pOption:
            case 1:
                portScan = ["1. Specific port", "2. Scan common ports", "3. Scan all 65535 ports", "4. Scan a range of ports [1-100]"]
                print("\n".join(portScan))
                pScan = int(input("Option: "))
                match pScan:
                    case 1:
                        os.system("sudo nmap -p "+portNum+ obtain_ip())
                    case 2:
                        os.system("sudo nmap -F "+obtain_ip())
                    case 3:
                        os.system("sudo nmap -p- "+obtain_ip())
                    case 4:
                        os.system("sudo nmap -p 1-100 "+obtain_ip())
                    case _:
                        print("Option does not exist")
                        portScans()
            case 2:
                Soption = ["1. TCP connect", "2. TCP SYN", "3. UDP ports", "4. Selected ports[IGNORE DISCOVERY]]"]
                print("\n".join(Soption))
                Scoption = int(input("Option: "))
                match Scoption:
                    case 1:
                        os.system("sudo nmap -sT "+obtain_ip())
                    case 2:
                        os.system("sudo nmap -sS "+obtain_ip())
                    case 3:
                        os.system("sudo nmap -sU -p 123,161,162 "+obtain_ip())
                    case 4:
                        os.system("sudo nmap -Pn -F "+obtain_ip())
                    case _:
                        print("Option does not exist")
                        portScans()
    except:
        print("Option does not exist")
        portScans()

#service and os detection
def SoD():
    option = ["1. OS Fingerprinting", "2. Standard Service ", "3. Aggressive Service", "4. Lighter Banner Grabbing"]
    print("\n".join(option))
    try:
        Soption = int(input("Option: "))
        match Soption:
            case 1:
                os.system("sudo nmap -A "+obtain_ip())
            case 2:
                os.system("sudo nmap -sV "+obtain_ip())
            case 3: 
                os.system("sudo nmap -sV --version-intensity 5 "+obtain_ip())
            case 4:
                os.system("sudo nmap -sV --version-intensity 0 "+obtain_ip())
            case _:
                print("Option does not exist")
                SoD()
    except:
        print("Option does not exist")
        SoD()
#user output option
def Uoo():
    option = ["1. To file", "2. To XML", "3. To GREP", "4. All formats"]
    print("\n".join(option))
    try:
        Uoption = int(input("Option: "))
        match Uoption:
            case 1:
                os.system("sudo nmap -oN outputfile.txt "+obtain_ip())
            case 2:
                os.system("sudo nmap -oX outputfile.xml "+obtain_ip())
            case 3:
                os.system("sudo nmap -oG outputfile.txt "+obtain_ip())
            case 4:
                os.system("sudo nmap -oA outputfile.txt "+obtain_ip())
            case _:
                print("Option does not exist")
                Uoo()
    except:
        print("Option does not exist")
        Uoo()

#advanced scanning using NSE scripts
def AsU():
    scriptType = ["1. Default safe scripts","2. Help", "3. Specific NSE script", "4. Set of scripts"]
    print("\n".join(scriptType))
    try:
        scriptOption = int(input("Option: "))
        match scriptOption:
            case 1:
                os.system("sudo -sV -sC "+obtain_ip())
            case 2:
                os.system("sudo --script-help=ssl-heartbleed")
            case 3:
                os.system("sudo nmap -sV -p 443 -script=ssl-hearbleed.nse "+obtain_ip())
            case 4:
                os.system("sudo nmap -sV --script=smb* "+obtain_ip())
    except:
        print("Option does not exist")
        AsU()

#function for active scanning
def activeScan():
    option = ["1. Local Network", "2. Port Scanning", "3. Service and OS Detection", "4. Packet Tracing", "5. Remote Network", "6. DDOS Reflection UDP Services", "Advanced Scanning with NSE"]
    print("\n".join(option))
    try:
        attackType = int(input("Select option: "))
        match attackType:
            case 1:
                os.system("sudo nmap -F "+obtain_ip())
            case 2:
                portScans()
                print("")
                Uoo()
            case 3:
                SoD()
                Uoo()
                exit()
            case 4:
                targetIP = int(input("Target IP: "))
                os.system("sudo nmap -vv -n -sn -PE -T4 --packet-trace "+str(targetIP))
                Uoo()
            case 5:
                remoteNet = int(input("Remote network or site: "))
                os.system("sudo nmap -F "+remoteNet)
                exit()
            case 6:
                CID = str(input("Enter IP with CIDR: "))
                os.system("sudo nmap -sU -A -PN -n -pU:19,53,123,161 -script=ntp-monlist, dns-recursion,snmp-sysdescr "+CID)
                
            case 7:
                AsU()

            case _:
                print("Option does not exist")
                activeScan()
    except:
        print("Option does not exist")
        activeScan()

#function for passive scanning
def passiveScan():
    pScan = str(input("Enter the domain name or IP: "))
    option = ["1. Stealth Scan", "2. IDS Evasion"]
    for options in option:
        print(options)
    try:
        attackType = int(input("Select Option: "))
        match attackType:
            case 1:
                os.system("sudo nmap -sS "+pScan)
            case 2:
                os.system("sudo nmap -ss -T2 "+pScan)
            case _:
                print("Option does not exist")
                passiveScan()
    except:
        print("Option does not exist")
        passiveScan()


#initial function
def index():
    scanType = ['1. Active Scanning', '2. Passive Scanning']
    print("\n".join(scanType))
    try:
        infoScan = int(input("Scan Type: "))
        match infoScan:
            case 1:
                activeScan()
            case 2:
                passiveScan()
            case _:
                print("Option does not exist")
                index()
    except:
        print("Option does not exist")
        index()










        

    





    
 