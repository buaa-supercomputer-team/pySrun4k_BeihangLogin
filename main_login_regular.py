import os, time
from Login import *

user = os.environ['user']
pwd = os.environ['pwd']

# t = 0.25 # hour

while True:
    ret = check_online(gatewayUrl)
    print(ret)
    if not ret['online']:
        retlogin = do_login(gatewayUrl, user, pwd)
        print("try login:")
        print(retlogin)
    time.sleep(5)

    # os.system("python Login.py login {} {}".format(user, pwd))
    # time.sleep(t*3600)