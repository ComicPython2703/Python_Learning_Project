# vim: set fileencoding=utf-8 :
def random(homework):
    print(f'Hi, {homework}')


import random
b = 2
food = ["病欺凌", '热牛奶', '啊华田', '酸奶', '士力架']
a = random.choice(food)
for i in range(2):
    a = random.choice(food)
    if a == "病欺凌":
        if __name__ == '__main__':
            print("你可以吃了")
        break
    else:
        if __name__ == '__main__':
            print("不可以吃了")
