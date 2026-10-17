# coding=utf-8
"""
Title=勇者斗🤡
"""
# noinspection PyPep8Naming
def Copyright():
    print(
        "\nCopyright (c) 2010-2024 ComicPython6405 Foundation.\nAll Rights Reserved.")


def lesson(python):
    print(f'Hi,{python}')


if __name__ == '__main__':
    Copyright()
    print()
# =========={准备工作}==================
import random
import subprocess


if __name__ == '__main__':
    
    print("////////////////勇者斗周克\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
    print('<------------------[Ender-Dragon]---------------------------->')
a = random.randint(1, 10)
b = random.randint(1, 4)
c = 0 # 诅咒次数


# ============{分隔符}==================
# ###############{创建函数或类}###################


class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100000
        self.mp = 20000
        self.level = 114514
        self.atk = random.randint(21460, 100000)
        self.use_mp = random.randint(3000,5000)
        self.critical_hit = random.randint(1,100)
        self.defend = 2426

    def attack(self, ender_dragon):
        if self.critical_hit >= 50:
            shanghai = self.atk - ender_dragon.dfs
            ender_dragon.health = ender_dragon.health - shanghai
        else:
            print("暴击!")
            shanghai = self.atk * 5
            ender_dragon.health = ender_dragon.health - shanghai
            
        print(f'成功的对{ender_dragon.name}造成了{shanghai}伤害')

    def curse(self, ender_dragon):
        global c
        r = random.randint(0, 1)
        if r == 0 and c == 0:
            shanghai = self.atk * 2
            ender_dragon.health -= shanghai
            self.mp -= self.use_mp
            
            print('诅咒成功!,造成了%d伤害,诅咒已结束,退出代码：0' % shanghai)
            c += 1
        else:
            
            print('[ERROR]非零退出诅咒！退出代码：1')

    def treatment(self):  # 治疗
        if self.mp > 0:
            self.health += 327670
            self.mp -= self.use_mp
            
            print('治疗成功!,当前生命值：%d,治疗已结束,退出代码：0' % self.health)
        else:
            
            print('[ERROR]非零退出治疗！退出代码：1')

    @staticmethod
    def persuade(ender_dragon):
        a = random.randint(10, 100)
        if ender_dragon.health <= 30000 and a <= 10:
            return True
        else:
            return False

    @staticmethod
    def master_ball(ender_dragon):
        if a >= 5:
            
            print(f"你收容了{ender_dragon.name}，退出代码：0")
            exit()
        else:
            
            print(f"收容失败，退出代码：1")

    @staticmethod
    def escape():
        print("[WARNING]Mission Failed")
        print("\nTraceback (most recent call last):")
        print('  File "E:\Python\PPPPPYTHOOOOOOOON\9.15(庸者逗Joker).py", line 96, in <module>')
        print("illegalescaped")
        print("进程已结束，退出代码为 -114514191 (0xC000014B: interrupted by Escape)")
        return True


# noinspection PyPep8Naming
class Ender_Dragon:
    def __init__(self, name):
        self.name = name
        self.health = 1000000
        self.afk = random.randint(23487, 30584)
        self.dfs = random.randint(10, 500)
        self.afkforlongxi = random.randint(3000, 6000)

    def attack(self, hero):
        damage = self.afk - hero.defend
        hero.health -= damage
        print(f"[WARNING]{self.name}对你造成了{damage}伤害，退出代码：0")

    def fire(self, hero):
        r = random.randint(1, 2)
        if r == 1:
            damage = self.afk * 2
            hero.health = hero.health - self.afk        
            print('ender_dragon喷火了，造成了%d的伤害' % damage)

    def treatment(self):
        if self.health < 100:
            return True
        else:
            return False

    def spit_Dragon_Breath(self, hero):
        r = random.randint(1, 4)
        if r == 1:
            damage = self.afkforlongxi
            hero.health = hero.health - damage            
            print('ender_dragon喷龙息，造成了%d的伤害' % damage)
        elif r == 3:
            damage = self.afkforlongxi
            hero.health = hero.health - damage
            print('ender_dragon暴击龙息，造成了%d的伤害' % damage)


# =========={诸城市}=================
hero = Hero("Hero")
ender_dragon = Ender_Dragon("Ender_Dragon")
i = 1
if __name__ == '__main__':
    while True:
        print("=-=-=-=-=-=-=ROUND%d=-=-=-=-=-=-=-=" % i)
        print(f"========ender_dragon：{ender_dragon.health}==============")
        print("Health=", hero.health)
        print('MP=', hero.mp)
        i += 1
        key = input("请栓则：1.攻击🗡🏹 2.治疗 3.诅咒🤬 4.劝降 5.逃跑 6.大师球   ：")
        # hero
        if key == "1":
            hero.attack(ender_dragon)
        elif key == "2":
            hero.treatment()
        elif key == "3":
            hero.curse(ender_dragon)
        elif key == "4":
            if hero.persuade(ender_dragon):
                
                print("劝降成功，退出代码：0")
                break
            else:
                
                print("[ERROR]非零退出劝降！退出代码：1")
                continue

        elif key == "5":
            hero.escape()
            break
        elif key == "6":
            hero.master_ball(ender_dragon)
        else:
            print("[WARNING]请重新输入")
            continue

        ender_dragon.attack(hero)
        ender_dragon.fire(hero)
        ender_dragon.treatment()
        ender_dragon.spit_Dragon_Breath(hero)

        if hero.health <= 0:
            print("[ERROR]Mission Failed")
            print("\nTraceback (most recent call last):")
            print('  File "E:\Python\PPPPPYTHOOOOOOOON\9.15(庸者逗Joker).py", line 136, in <module>')
            print("Youdied")
            print("进程已结束，退出代码为 -5483957738 (0xC000035A: interrupted by Health==0)")
            exit()
        if ender_dragon.health <= 0:
            print("[INFO]Mission Complete")
            print('========={THE+END}===========')
            lesson("python")
            exit()
    print("\n Done")
