import os, sys
import subprocess
import requests
import time
import hashlib

def is_net_ok():
    null = open(os.devnull, 'w');
    res = subprocess.call('ping 8.8.8.8', shell = True, stdout = null, stderr = null);
        
    if res:
        # print('Ping failed.');
        return False;
    else:
        # print('Ping success.');
        return True;

def wlan_connect():
    null = open(os.devnull, 'w');
    res = subprocess.call('netsh wlan connect name=Tsinghua', shell = True, stdout = null, stderr = null);
        
    if res:
        print('Connect wlan-Tsinghua failed.');
        return False;
    else:
        print('Connect wlan-Tsinghua success.');
        return True;
    
def login(username, password):
    data = {
        'action' : 'login',
        'username' : username,
        'password' : '{MD5_HEX}' + hashlib.md5(password.encode()).hexdigest(),
        'ac_id' : '1'
    }; # 不用自己进行urlencode

    headers = {
        'Host': 'net.tsinghua.edu.cn',
        'Origin': 'http://net.tsinghua.edu.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Referer': 'http://net.tsinghua.edu.cn/wireless/',
    };
 
    response = requests.post('http://net.tsinghua.edu.cn/do_login.php', data=data, headers=headers);
    print(response.text);

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python ./connect.py <username> <password>\n");
        os._exit(1);

    username = sys.argv[1];
    password = sys.argv[2];

    while True:
        if not is_net_ok():
            print("\n");
            print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())));
            print('The network is disconnected.');
            if wlan_connect():
                time.sleep(2); # Win10连接wlan之后会立即自动弹出登录页面，造成"getaddrinfo failed"
                login(username, password);
        time.sleep(3);
        