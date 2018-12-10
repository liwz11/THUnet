# THUnet

Tsinghua校园网连接脚本，只在Window 10中测试过。

Tsinghua校园网登录：

```
python ./login.py <username> <password>
```

Tsinghua校园网断开：

```
python ./logout.py
```

Tsinghua校园网掉线自动重连：

```
python ./connect.py <username> <password>
python ./connect.py <username> <password> [wlan-interface]

Examples: 

python ./connect.py test 1234567
python ./connect.py test 1234567 "Wireless Network Connection"
python ./connect.py test 1234567 "无线网络连接 4"
```
