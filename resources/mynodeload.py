#coding=utf-8
import re
import os
import subprocess

if __name__ == "__main__":
    files=os.listdir('/root/mydata/node_images')
    for filename in files:
        if '.tar' in filename:
            print(filename)
            newfilepath='/root/mydata/node_images/'+filename
            os.system('sudo docker load -i %s'%newfilepath)
