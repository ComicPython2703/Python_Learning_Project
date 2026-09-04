# coding=utf-8
def kaoshi(homework):
    print(f'Hi, {homework}')


a = [33, 55, 22, 77]
a.sort()
for i in a:
    if __name__ == '__main__':
        print(i)
b = eval(input("年龄："))
if b > 10:
    c = 35
else:
    c = 15
if __name__ == '__main__':
    print("票价：", c)

# noinspection PyDictCreation
d = {'gj': 'China', 'nl': 12, 'xb': "女"}
d['nl'] = 11
del d['gj']
d['xm'] = 'xxs'
if __name__ == '__main__':
    print(d)
c = 0
for i in range(1, 100):
    if i % 2 == 0:
        c = c + 1
if __name__ == '__main__':
    print(c)

s = 'Kevin likes English'
new = ''
for i in range(len(s)):
    if i % 3 == 0:
        new += s[i]
if __name__ == '__main__':
    print(new)

tup = ('富强', '民主', '文明', '和谐', "爱国")
# A.tup[2:4:2]= '敬业'
# tup[4]='敬业'
# del tup[4]
# tup*3

dic = {12: 34}

stu = {202101: '嚣冥', 202102: '啸黉', 202103: '潇荔'}
if __name__ == '__main__':
    print(len(stu))

massage = {'name': 'TOMM', 'age': 14, 'city': 'Shanghai'}
for i in massage.values():
    if __name__ == '__main__':
        print(i, end='')
if __name__ == '__main__':
    print()
tup1 = ('中国', '电子学会', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7)
if __name__ == '__main__':
    print(tup1[-1], tup2[1:5])
ls = [[1, 2, 3], 'python', [[4, 5, 'ABC'], 6], [7, 8]]
if __name__ == '__main__':
    print(ls[2][1])

name = ['Amir', 'Betty', 'Chales', 'Tao']
# name.index
# ('Edward')Traceback (most recent call last):
#   File "E:\我的世界教育版Pro_V2.0_Windows\qweqwe.py", line 65, in <module>
#     name.index('Edward')
# ValueError: 'Edward' is not in list
e = [[1, 2, 3], [4, 5, 6]]
e.sort(reverse=True)
if __name__ == '__main__':
    print('结果：', e)
f = list("zhangsan")
if __name__ == '__main__':
    print(f[1:7:2])

q = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
del q[1:]
if __name__ == '__main__':
    print(q)

# noinspection PyListCreation
l = [1, 3.14, 'laowang', [1, 2]]
l.append('we')
if __name__ == '__main__':
    print(l)
t1 = (2, 3)
t2 = (4, 5, 6)
if __name__ == '__main__':
    print("它是：", t2 + t1 * 2)

s1 = 'hi'
s2 = 'lanxi'
s3 = '!'
if __name__ == '__main__':
    print(s1 + s2 + s3)

g = [1, 2, 3, 4, 5, 6, 7, 8, 9]
if __name__ == '__main__':
    print([1, 2] in g)

for i in 'Hello world':
    if i == 'w':
        break
if __name__ == '__main__':
    print(i, end='')

if __name__ == '__main__':
    print()

t3 = 1, 2, 3
if __name__ == '__main__':
    print(type(t3))

# 停车场收费题目
while True:
    money = 0
    time = int(input("时间："))
    if time <= 2:
        money = 5
        if __name__ == '__main__':
            print(money)
    elif time >= 2:
        money += 5
        money *= time
        if __name__ == '__main__':
            print(money)
