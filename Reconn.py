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
    for options in option:
        print(option)
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

#function for passive scanning
def passiveScan():
    pScan = input("Enter the domain name or IP: ")
    option = ["1. Stealth Scan", "2. IDS Evasion"]
    for options in option:
        print(options)
    attackType = int(input("Select Option: "))
    match attackType:
        case 1:
            os.system("sudo nmap -sS "+pScan)
        case 2:
            os.system("sudo nmap -ss -T2 "+pScan)
        case _:
            print("Option does not exist")

scanType = ['1. Active Scanning', '2. Passive Scanning']
for scanTypes in scanType:
    print(scanType)
infoScan = int(input("Scan Type: "))
if infoScan == 1:
    activeScan()


#passive scanning
elif infoScan == 2:
    passiveScan()


    





    
 