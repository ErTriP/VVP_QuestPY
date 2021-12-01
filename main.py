import random

hp = 100
respect = 20
homeLength = 10
weight = 30
Error = ""
DayCounter = 0

def FightResult(i,r,h):
    global hp
    global respect
    if i == 1:
        print("Победа")
        print("Респект увеличился на", r)
        respect += r
        print("Жизни уменьшились на", h)
        hp += h
    else:
        print("Поражение")
        print("Респект уменьшился на", r)
        respect += r
        print("Жизни уменьшились на", h)
        hp += h
def ShowStats():
    print("\033[34m Жизни ", hp)
    print("\033[35m Респект ", respect)
    print("\033[36m Глубина норы ", homeLength)
    print("\033[32m Вес ", weight)
    print("\033[37m День номер ", DayCounter)

def Night():
    global homeLength
    homeLength -= 2
    global hp
    hp += 20
    global respect
    respect -= 2
    global weight
    weight -= 5

def Digging():
    print('Копать интенсивно(1) или лениво(2)?')
    Answer = int(input())
    global homeLength
    global hp
    if Answer == 1:
        print('Длина норы увеличилась на 5, Здоровье уменьшилось на 30')
        homeLength += 5
        hp -= 30
    elif Answer == 2:
        print('Длина норы увеличилась на 2, Здоровье уменьшилось на 10')
        homeLength += 2
        hp -= 10
    else:
        global Error
        Error += "Ошибка ввода данных"

def Figting():
    print('{1}Подраться со слабым существом(вес 30)\n{2} со средним (вес 50)(2)\n{2} с сильным(вес 70)(3)\n')
    Answer = int(input())
    Resp = 0
    Health = 0
    Enemy = 0
    if Answer == 1:
        Enemy = 30
        print('Шанс на победу =', weight / (weight + Enemy))
        chance = weight / (weight + Enemy)
        result = random.uniform(0, 1)
        if result <= chance:
            Resp = 10*((weight + Enemy)//weight)
            Health = -1 * Resp/2
            FightResult(1,Resp,Health)
        else:
            Resp = -10 * ((weight + Enemy) // Enemy)
            Health = Resp
            FightResult(0, Resp, Health)

    elif Answer == 2:
        Enemy = 50
        print('Шанс на победу =', weight / (weight + Enemy))
        chance = weight / (weight + Enemy)
        result = random.uniform(0, 1)
        if result <= chance:
            Resp = 10 * ((weight + Enemy) // weight)
            Health = -1 * Resp / 2
            FightResult(1, Resp, Health)
        else:
            Resp = -10 * ((weight + Enemy) // Enemy)
            Health = Resp
            FightResult(0, Resp, Health)
    elif Answer == 3:
        Enemy = 70
        print('Шанс на победу =', weight / (weight + Enemy))
        chance = weight / (weight + Enemy)
        result = random.uniform(0, 1)
        if result <= chance:
            Resp = 10 * ((weight + Enemy) // weight)
            Health = -1 * Resp / 2
            FightResult(1, Resp, Health)
        else:
            Resp = -10 * ((weight + Enemy) // Enemy)
            Health = Resp
            FightResult(0, Resp, Health)
    else:
        global Error
        Error += "Ошибка ввода данных"

def Eating():
    print('Поесть травки жухлой(1) или зелёной(2)?')
    Answer = int(input())
    global hp
    global weight
    global respect
    global Error
    if Answer == 1:
        print('Здоровье увеличилось на 10, вес увеличился на 15')
        hp += 10
        weight += 15
    elif Answer == 2:
        if respect < 30:
            print('Лохов не пускают на лужайку. здоровье уменьшилось 30')
            hp -= 30
        else:
            print('Здоровье увеличилось на 30, вес увеличился на 30')
            hp += 30
            weight += 30
    else:
        Error += "Ошибка ввода данных"

while True:
    print("Наступила ночь")
    Night()
    DayCounter += 1
    ShowStats()
    print("Наступил день")


    print("\033[31m         {1} Копать нору")
    print("\033[31m         {2} Идти кушать травку")
    print("\033[31m         {3} Идти драться")
    print("\033[31m         {4} Проспать весь день")

    Answer = int(input())

    if Answer == 1:
        Digging()
    elif Answer == 2:
        Eating()
    elif Answer == 3:
        Figting()
    elif Answer == 4:
        print("Вы проспали весь день")
        Night()
    else:
        Error += "Ошибка ввода данных"
    if hp <= 0 or respect <= 0 or homeLength <= 0 or weight <= 0:
        print("Game Over!")
        exit()
    if respect >= 100:
        print("Victory")
        exit()
    if len(Error) != 0:
        print(Error)
        exit()
