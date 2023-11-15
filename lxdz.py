# coding:utf-8 
import time
import random
import keyboard
import sys
from pymouse import PyMouse
from pykeyboard import PyKeyboard

# 全局实例化对象
m=PyMouse()
k=PyKeyboard()

def setgetMouse(s):
    time.sleep(s)#间隔100ms
    a=m.position()
    m.click(a[0],a[1])

def random1():
    print(0)
    r=random.randint(10,50) #控制连点次数
    i=1
    while i<r:
        setgetMouse(0.1)
        i=i+1
    setgetMouse(0.5)
    rs=random.uniform(0,2) 
    setgetMouse(rs) # 暂停0-2秒

if __name__ == '__main__':
    time.sleep(2)
    while True:
        random1()