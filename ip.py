#!/usr/bin/env python
# -*- coding:utf-8 -*-
import subprocess
import shlex

def judge(cmd):
    cmd = "ping"+" "+cmd
    args = shlex.split(cmd)

    try:
	    subprocess.check_call(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	    print cmd+"   success"
    except subprocess.CalledProcessError:
	    print cmd+"   failed"

if __name__ == '__main__':
   for i in range(256):
       ip = '172.16.0.'+str(255-i)
       judge(ip);