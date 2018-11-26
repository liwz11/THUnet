import requests, sys, os, hashlib

if len(sys.argv) != 3:
    print("Usage: python ./login.py <username> <password>\n");
    os._exit(1);

username = sys.argv[1];
password = sys.argv[2];

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
