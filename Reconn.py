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

#function for active scanning
def activeScan():
    option = ["1. Local Network", "2. Port Scanning", "3. Stack Fingerprinting", "4. Packet Tracing", "5. Remote Network", "6. Online Targets"]
    print("\n".join(option))
    try:
        attackType = int(input("Select option: "))
        match attackType:
            case 1:
                os.system("sudo nmap -F "+obtain_ip())
            case 2:
                portNum = int(input("Port Number: "))
                os.system("sudo nmap -sV -p "+str(portNum)+ str(obtain_ip())+" - open")
                exit()
            case 3:
                os.system("sudo nmap -o -v "+obtain_ip())
                exit()
            case 4:
                targetIP = int(input("Target IP: "))
                os.system("sudo nmap -vv -n -sn -PE -T4 --packet-trace "+str(targetIP))
            case 5:
                remoteNet = int(input("Remote network or site: "))
                os.system("sudo nmap -F "+remoteNet)
                exit()
            case 6:
                portNum = int(input("Port Number: "))
                os.system("sudo nmap -PR "+portNum)
                spcprt0 = "sudo nmap -p"+str(portNum)+" -oG - "+obtain_ip()+" -D"
                spcprt1 = "sudo nmap -p "+str(portNum)+" -oG - "+obtain_ip()+" -D| awk "+"/"+str(portNum)+"\/open/{print $2}"+">> ports.txt"
                spcprt2 = "sudo nmap -o -iL ports.txt"
                print(f'[OS ID:] {spcprt2}')
                scn = subprocess.run([spcprt0,spcprt1,spcprt2])
                exit()
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

index()

    





    
 