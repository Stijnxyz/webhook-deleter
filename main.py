import time
import os
try:
    from colorama import Fore, init
except:
    os.system("py -m pip install colorama")
    from colorama import Fore, init
try:
    import requests
except:
    os.system("py -m pip instamm requests")
    import requests

init()

os.system("title Webhook Deleter | SS")

print("Made by Sample Services. | .gg/sample")
webhook = input("Enter webhook url: ")
def delete():
    requests.delete(webhook)
    check = requests.get(webhook)
    if check.status_code == 404:
        print("\n ok, deleted")
        os.system("pause >nul") 
    elif check.status_code == 200:
        print("\n Ok, did not delete. error (If you believe this is not an error contact SS Owner if you want lol (: )")
        os.system("pause >nul")

test = requests.get(webhook)
if test.status_code == 404:
    print("\n webhook...")
    os.system("pause >nul")
elif test.status_code == 200:
    print("\n webhook...")
    delete()