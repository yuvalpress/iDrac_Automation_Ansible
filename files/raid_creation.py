#!/usr/bin/env python3
import json
import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('192.168.26.134', username='root', password='Customer1!')

stdin, stdout, stderr = client.exec_command('racadm -r 192.168.0.140 -u root -p Customer1! storage get pdisks -o -p size')

for line in stdout:
    print(line.strip('\n'))

client.close()
