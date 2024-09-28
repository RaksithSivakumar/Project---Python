import time
from datetime import datetime as dt

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"  
redirect = "127.0.0.1"

websites_to_block = ["www.facebook.com", "facebook.com", "www.youtube.com", "youtube.com"]

def block_websites(start_hour, end_hour):
    while True:
        if start_hour < dt.now().hour < end_hour:
            print("Blocking websites...")
            with open(hosts_path, 'r+') as file:
                content = file.read()
                for website in websites_to_block:
                    if website not in content:
                        file.write(f"{redirect} {website}\n")
        else:
            print("Unblocking websites...")
            with open(hosts_path, 'r+') as file:
                content = file.readlines()
                file.seek(0)
                for line in content:
                    if not any(website in line for website in websites_to_block):
                        file.write(line)
                file.truncate()
        time.sleep(60)  

block_websites(9, 17)  