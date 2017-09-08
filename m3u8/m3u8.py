#!/bin/python
import subprocess
import sys
import os
import time
import shutil
path = os.path.dirname(os.path.abspath(sys.argv[0]))
def fun1(url, alias):
    url = "curl -s "+url
    a=subprocess.getstatusoutput([url])
    time1 = time.strftime('%Y/%m/%d %H:%M:%S',time.localtime(time.time()))
    of = open("error.log","a")
    if a[0] != 0:
        time.sleep(5)
        of.write("{} {} can't touch\n".format(alias, time1))
        return 1
    else:
        return 0
    of.close()

def fun2(url, alias):
    url1="curl -s "+url+" | md5sum"
    old=subprocess.getoutput([url1])
#    print(old)
    time.sleep(5)
    new=subprocess.getoutput([url1])
#    print(new)
    of = open("file.log", "a")
    time1 = time.strftime('%Y/%m/%d %H:%M:%S',time.localtime(time.time()))
    if new == old:
        of.write("{} {}\n".format(alias, time1))


#fun2("www.baidu.com", "baidu")
#jinxingbeifen
copy_time=time.strftime('%d',time.localtime(time.time()))
if copy_time == 1:
    shutil.copy("file1.log", "file2.log")
    shutil.copy("file.log", "file1.log")

of = open("m3u81.conf")
lists = of.readlines()
list_temp = []
for h in lists:
    if h.strip():
        list_temp.append(h)
lists = list_temp[:]
l = len(lists)
if l <= 0:
    os.sys("clear")
    print("[Warning]Please add the host server")

while 1:
    for i in range(0, l):
        v_list = lists[i].strip().split(" ")
        if fun1(v_list[0], v_list[1]) == 0:
            fun2(v_list[0], v_list[1])
                

    

        
        




    
    
    
