import os, sys, time, chardet
import subprocess
import requests
import hashlib

def is_net_ok(ping_target):
    #null = open(os.devnull, 'w');
    #res = subprocess.call('ping 8.8.8.8', shell = True, stdout = null, stderr = null);
    
    p = subprocess.Popen("ping " + ping_target, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE);
    (stdoutput, erroutput) = p.communicate();
    encoding = chardet.detect(stdoutput)['encoding'];
    output = stdoutput.decode(encoding);
    retcode = p.returncode;
    res = ("ms TTL=" not in output);
    
    if res:
        # print('Ping failed.');
        return False;
    else:
        # print('Ping success.');
        return True;

def wlan_connect(name, interface):
    null = open(os.devnull, 'w');
    res = subprocess.call('netsh wlan connect name="' + name + '" interface="' + interface + '"', shell = True, stdout = null, stderr = null);
        
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
 
    try:
        response = requests.post('http://net.tsinghua.edu.cn/do_login.php', data=data, headers=headers, timeout=10);
        print(response.text);
    except:
        print("Unfortunitely -- An error happended on requests.post()")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('\nUsage: python ./connect.py <username> <password> [wlan-interface]\n');
        print('Examp: python ./connect.py test 1234567');
        print('Examp: python ./connect.py test 1234567 "Wireless Network Connection"\n');
        print('Examp: python ./connect.py test 1234567 "无线网络连接 4"\n');
        os._exit(1);
    
    username = sys.argv[1];
    password = sys.argv[2];
    interface = "无线网络连接" # "Wireless Network Connection"
    name = "Tsinghua"
    
    if len(sys.argv) > 3:
        interface = sys.argv[3]

    while True:
        if not is_net_ok("info.tsinghua.edu.cn"):
            print("\n");
            print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())));
            print('The network is disconnected.');
            if wlan_connect(name, interface):
                time.sleep(5); # Win10连接wlan之后会立即自动弹出登录页面，造成"getaddrinfo failed"
                login(username, password);
        else:
            time.sleep(1);
        



