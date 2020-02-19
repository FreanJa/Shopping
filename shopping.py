#! python3
#键入 商品种数 顾客余额
#自动生成 商品名称（三个字母） 商品数量 商品价格（1--1000）


class product():
    def __init__(self,name,price,inventory):
        self.n = name
        self.p = price
        self.i = inventory
    def buy(self):
        self.i -= 1

class balance():
    def __init__(self,bal):
        self.b = bal
    def buy(self,price):
        self.b -= price

def rN():
    r1 = chr(int(random.random()*26)+65)
    r2 = chr(int(random.random()*26)+97)
    r3 = chr(int(random.random()*26)+97)
    return r1+r2+r3

def rP():
    r = int(random.random()*999+1)
    return r

def rI():
    r = int(random.random()*9+1)
    return r


import random
print('********************')
print('****** 购物车 ******')
print('***** Shopping *****')
print('********************')
sum = int(input('生成商品种类数:'))
p = []
while sum <= 0:
    sum =int(input('请重新输入:'))
for i in range(sum):
    name = rN()
    price = rP()
    inventory = rI()
    p.append(i)
    p[i] = product(name,price,inventory)
print('********************')

bal = int(input('您的余额:'))
while bal <= 0:
    bal =int(input('请重新输入:'))
cus = balance(bal)
print('********************')

for i in range(sum):
    print('%d.%s %d %d'%((i+1),p[i].n,p[i].p,p[i].i))

l = {}
print('********************')
print('若需要结束购物请输入“0”')
while cus.b >= 0:
    if cus.b == 0:
        print('您的当前余额为0,已自动结束购物')
        break
    sel = int(input('请输入您要购买的商品编号:'))-1
    if sel == -1:
        break
    if p[sel].i > 0:
        if p[sel].p <= cus.b:
            p[sel].buy()
            cus.buy(p[sel].p)
            if not(l.get(p[sel].n)):
                l[p[sel].n] = 1
            else:
                l[p[sel].n] += 1
            print('您的余额为%s'%(cus.b))
        else:
            sel = int(input('您的余额不足以购买该商品，请重新选择:'))-1
            if sel == -1:
                break
    else:
        sel = int(input('该商品已售罄，请重新选择:'))-1
        if sel == -1:
            break
print('********************')
print('您购买的商品有:')
for i,j in l.items():
    print(i,':\t',j)
print('您的余额为:',cus.b)
print('******谢谢惠顾******')