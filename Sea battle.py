# https://github.com/legionic/skillfactory-module-B_7_5--Lavrenko.git
# Флаг очерёдности хода. Если True, то очередь хода моя, иначе ходит программа
flag_step = True
#============ Координаты кораблей =====================
enemy = [
    {
        "deck": True,
        "X": [5],
        "Y": [1],
    },
    {
        "deck": True,
        "X": [6],
        "Y": [4],
    },
    {
        "deck": True,
        "X": [6],
        "Y": [6],
    },
    {
        "deck": True,
        "X": [4],
        "Y": [4],
    },
    {
        "deck": True,
        "X": [1, 2],
        "Y": [6, 6],
    },
    {
        "deck": True,
        "X": [3, 3],
        "Y": [1, 2],
    },
    {
        "deck": True,
        "X": [1, 1, 1],
        "Y": [1, 2, 3],
    },
]
friendly = [
    {
        "deck": True,
        "X": [1],
        "Y": [4],
    },
    {
        "deck": True,
        "X": [1],
        "Y": [6],
    },
    {
        "deck": True,
        "X": [2],
        "Y": [2],
    },
    {
        "deck": True,
        "X": [6],
        "Y": [4],
    },
    {
        "deck": True,
        "X": [5, 5],
        "Y": [1, 2],
    },
    {
        "deck": True,
        "X": [5, 6],
        "Y": [6, 6],
    },
    {
        "deck": True,
        "X": [3, 3, 3],
        "Y": [4, 5, 6],
    },
] # friendly = список библиотек с координатами дружеских кораблей
#=================== ПОЛЕ БОЯ =====текущее положение=====================================
# pole_my - список координат ДРУЖЕСКОГО поля в консоли с кораблями и выстрелами. Картинка "Дружеское поле"
pole_my = {
    1: ["O", "O", "O", "O", "O", "O"],
    2: ["O", "O", "O", "O", "O", "O"],
    3: ["O", "O", "O", "O", "O", "O"],
    4: ["O", "O", "O", "O", "O", "O"],
    5: ["O", "O", "O", "O", "O", "O"],
    6: ["O", "O", "O", "O", "O", "O"],
}
# pol_wor - список координат ВРАЖЕСКОГО поля в консоли с кораблями и выстрелами. Картинка "Вражеское поле"
pol_wor = {
    1: ["O", "O", "O", "O", "O", "O"],
    2: ["O", "O", "O", "O", "O", "O"],
    3: ["O", "O", "O", "O", "O", "O"],
    4: ["O", "O", "O", "O", "O", "O"],
    5: ["O", "O", "O", "O", "O", "O"],
    6: ["O", "O", "O", "O", "O", "O"],
}
#=============================================================
#   в Doska() выводит итоговое отображение в консоль
def Doska(flag_step):
    # =========== Проверка количества подбитых кораблей ==============
    count_wor = []
    count_my = []
    for i in range(7):
        contr = enemy[i]
        if contr.get("deck") == False:
            count_wor.append(contr.get("deck"))
    for i in range(7):
        contr = friendly[i]
        if contr.get("deck") == False:
            count_my.append(contr.get("deck"))

    if len(count_wor) == 7 or len(count_my) == 7:
        print(f"{' ' * 12} Игра окончена")
        print(f"  Подбито {len(count_my)} кораблей {' ' * 9}Подбито {len(count_wor)} кораблей")
        flag_step = None
        if count_wor > count_my:
            print(f"{' ' * 12} Победил Игрок!")
        else:
            print(f"{' ' * 12} Игрок проиграл!")
            print(f"{' ' * 10} Победа компьютера!")
    else:
        print(f"   Подбито {len(count_my)} кораблей {' '* 8}Подбито {len(count_wor)} кораблей")
    #=========== Проверили количество подбитыз кораблей ==============

    print("       Мои корабли                 Вражеские")
    print("    1  2  3  4  5  6            1  2  3  4  5  6")
    print("   ------------------         ------------------")
    #=========================
    for i in range(1, 7):
        test_my = pole_my[i][0] + pole_my[i][1] + pole_my[i][2] + pole_my[i][3] + pole_my[i][4] + pole_my[i][5]
        test_wor = pol_wor[i][0] + pol_wor[i][1] + pol_wor[i][2] + pol_wor[i][3] + pol_wor[i][4] + pol_wor[i][5]
        print(f"{i} |  {'  '.join(str(test_my))}      {i} |  {'  '.join(str(test_wor))}")
    #=========================

    if flag_step == True:
        Batl(flag_step)
    elif flag_step == False:
        Random(flag_step)
    else:
        print(f"\n{' ' * 14}Конец игры!")
        if count_my > count_wor:
            print(f"{' ' * 14}Выиграла программа!\n{' ' * 16} Вы проиграли!")
        else:
            print(f"\n{' ' * 14}Вы выиграли!")
    return

def Prog(ix, iy, sm, pol, flag_step): # Сюда хочется запихнуть штатные вычисления
    st_x = pol[ix]  # присвоили строку значения вражеского корабля из библиотеки pol_wor
    st_x.pop(iy - 1)
    st_x.insert(iy - 1, sm)
    raw = {ix: st_x}

    if pol == pol_wor:
        pol_wor.pop(ix)
        pol_wor.update(raw)
    else:
        pole_my.pop(ix)
        pole_my.update(raw)

    return Doska(flag_step)

#в Ship задаю класс для кораблей
class Ship:
    def __init__(self, deck, X, Y):
        self.deck = deck
        self.X = X
        self.Y = Y

    # Сюда кладём рутинные вычисления:
    @staticmethod
    def one_desk(ix, iy, pol, flag_step):
        contr_a = pol[ix]
        if [contr_a[iy - 1]] == ['O'] or [contr_a[iy - 1]] == ["■"]:
            test_sh = [False, ix, iy]
            if pol == pol_wor:
                for i in range(4):
                    kot = enemy[i]
                    if kot.get('X') == [test_sh[1]] and kot.get('Y') == [test_sh[2]]:
                        enemy[i]["deck"] = False
                        print(f"{' '*28}~=^ Убил Одиночный ^=~")
                        Prog(ix, iy, "X", pol, flag_step)
            else:
                for i in range(4):
                    kot = friendly[i]

                    if kot.get('X') == [test_sh[1]] and kot.get('Y') == [test_sh[2]]:
                        friendly[i]["deck"] = False
                        print("~=^ Убил Одиночный ^=~")
                        Prog(ix, iy, "X", pol, flag_step)

    @staticmethod
    def too_desk(ix, iy, it, pol, flag_step):
        if pol == pol_wor:
            for i in range(2):
                kot = enemy[i + 4]

                if kot.get('X')[it] == ix and kot.get('Y')[it] == iy:
                    if enemy[i + 4]["deck"] == True:
                        enemy[i + 4]["deck"] = None
                        print(f"{' ' * 26}~^\ Ранен двух-палубный /^~")
                        Prog(ix, iy, "X", pol, flag_step)

                    elif enemy[i + 4]["deck"] == None:
                        enemy[i + 4]["deck"] = False
                        print(f"{' ' * 28} ~УБИТ двух-палубный~ ")
                        Prog(ix, iy, "X", pol, flag_step)

                    else:
                        print(f"{' ' * 28}Вы сюда уже нажимали! Этот корабль мёртв!")
                        print(f"{' ' * 28}Введите координаты заново!")
                        Doska(flag_step)
        else:
            for i in range(2):
                kot = friendly[i + 4]
                if kot.get('X')[it] == ix and kot.get('Y')[it] == iy:
                    if friendly[i + 4]["deck"] == True:
                        friendly[i + 4]["deck"] = None
                        print("~^\ Ранен двух-палубный /^~")
                        Prog(ix, iy, "X", pol, flag_step)

                    elif friendly[i + 4]["deck"] == None:
                        friendly[i + 4]["deck"] = False
                        print(" ~УБИТ двух-палубный~ ")
                        Prog(ix, iy, "X", pol, flag_step)

                    else:
                        print("Вы сюда уже нажимали! Этот корабль мёртв!")
                        print("Введите координаты заново!")
                        Doska(flag_step)
    @staticmethod
    def three_desk(ix, iy, it, pol, flag_step):  # 1 1 1 1
        if pol == pol_wor:
            linrkor = enemy[6]  # {'deck': True, 'X': [1, 1, 1], 'Y': [1, 2, 3]}
        else:
            linrkor = friendly[6]

        x_x = linrkor.get('X')      # [1, 1, 1]
        y_y = linrkor.get('Y')      # [1, 2, 3]
        #***** поиск [] in [] *******
        trans = []                  # Список значений сравнивания
        for i in range(3):
            if x_x[i] == ix and y_y[i] == iy:
                if i == it:
                    trans.insert(i, 'X')  # вставили нужный символ
            else:
                trans.insert(i, pol[x_x[i]][y_y[i]-1])

        if trans.count('O') > 0 or trans.count('■') > 0:                  # если количество элементов со значением 'O'
            if pol == pol_wor:
                print(f"{' ' * 26}~^\ Ранен ТРЁХ-палубный /^~")
                enemy[6]["deck"] = None
                Prog(ix, iy, "X", pol_wor, flag_step)
            else:
                print("~^\ Ранен ТРЁХ-палубный /^~")
                friendly[6]["deck"] = None
                Prog(ix, iy, "X", pole_my, flag_step)

        else:
            if pol == pol_wor:
                print(f"{' ' * 26}~^\ Убит ТРЁХ-палубный /^~")
                enemy[6]["deck"] = False
                Prog(ix, iy, "X", pol_wor, flag_step)
            else:
                print("~^\ Убит ТРЁХ-палубный /^~")
                friendly[6]["deck"] = False
                Prog(ix, iy, "X", pole_my, flag_step)

    @staticmethod
    def repet_lock(pola, ix, iy, flag_step):    # Проврка на битое поле
        if flag_step == True:
            if pol_wor[ix][iy - 1] == 'O':
                print("")
            else:
                print(f"{' ' * 25}Вы уже стреляли по той клетке")
                Doska(flag_step)
        else:
            if pole_my[ix][iy - 1] == 'O' or pole_my[ix][iy - 1] == "■":
                print("")
            else:
                print("Вы уже стреляли по той клетке")
                Doska(flag_step)

# ======= Расставили свои корабли по friendly ===========
for ship in friendly:
    ship_obj = Ship(deck=ship.get("deck"),
                    X=ship.get("X"),
                    Y=ship.get("Y"))

    if len(ship_obj.X) == 1:
        st_x = pole_my[ship_obj.X[0]]  # присвоили строку значения вражеского корабля из библиотеки pol_wor
        st_x.pop(ship_obj.Y[0] - 1)
        st_x.insert(ship_obj.Y[0] - 1, "■")

        raw = {ship_obj.X[0]: st_x}
        pole_my.pop(ship_obj.X[0])
        pole_my.update(raw)
        #
    elif len(ship_obj.X) == 2:
        st_x = pole_my[ship_obj.X[0]]  # присвоили строку значения вражеского корабля из библиотеки pol_wor
        st_x.pop(ship_obj.Y[0] - 1)
        st_x.insert(ship_obj.Y[0] - 1, "■")

        raw = {ship_obj.X[0]: st_x}
        pole_my.pop(ship_obj.X[0])
        pole_my.update(raw)
        #
        st_x = pole_my[ship_obj.X[1]]  # присвоили строку значения вражеского корабля из библиотеки pol_wor
        st_x.pop(ship_obj.Y[1] - 1)
        st_x.insert(ship_obj.Y[1] - 1, "■")

        raw = {ship_obj.X[1]: st_x}
        pole_my.pop(ship_obj.X[1])
        pole_my.update(raw)
        #
    elif len(ship_obj.X) == 3:
        st_x = pole_my[ship_obj.X[0]]  # присвоили строку значения вражеского корабля из библиотеки pol_wor
        st_x.pop(ship_obj.Y[0] - 1)
        st_x.insert(ship_obj.Y[0] - 1, "■")

        raw = {ship_obj.X[0]: st_x}
        pole_my.pop(ship_obj.X[0])
        pole_my.update(raw)
        #
        st_x = pole_my[ship_obj.X[1]]  # присвоили строку значения вражеского корабля из библиотеки pol_wor
        st_x.pop(ship_obj.Y[1] - 1)
        st_x.insert(ship_obj.Y[1] - 1, "■")

        raw = {ship_obj.X[1]: st_x}
        pole_my.pop(ship_obj.X[1])
        pole_my.update(raw)
        #
        st_x = pole_my[ship_obj.X[2]]  # присвоили строку значения вражеского корабля из библиотеки pol_wor
        st_x.pop(ship_obj.Y[2] - 1)
        st_x.insert(ship_obj.Y[2] - 1, "■")

        raw = {ship_obj.X[2]: st_x}
        pole_my.pop(ship_obj.X[2])
        pole_my.update(raw)
    else:
        continue
#  в Batl() кладу карту действий и обработки координат
def Batl(flag_step):
    print(f"\n        Ваш ход ... ")
    try:
        place = input(f"Введите две координаты:").split()
        X, Y = map(int, place)
    except ValueError as e:
        print("       Вы не правильно ввели координаты...\n")
        Doska(flag_step)
    except KeyError as e:
        print("       Вы не правильно ввели координаты...\n")
        Doska(flag_step)

    inspekt = []
    # Проверка поля на битое значение
    Ship.repet_lock(pol_wor[X][Y-1], X, Y, flag_step)

    if flag_step == True: # Проверили чья очерёдность хода
        for ship in enemy:
            ship_obj = Ship(deck=ship.get("deck"),
                            X=ship.get("X"),
                            Y=ship.get("Y"))
        # ============================ ОДНО-палубные =====================================
            if len(ship_obj.X) == 1:
                if [X] == ship_obj.X and [Y] == ship_obj.Y:
                    Ship.one_desk(X, Y, pol_wor, flag_step)
                else:
                    inspekt.append(False)
        # ============================ ДВУХ-палубные =====================================
            if len(ship_obj.X) == 2:
                if [X] == [ship_obj.X[0]] and [Y] == [ship_obj.Y[0]]:
                    Ship.too_desk(X, Y, 0, pol_wor, flag_step)
                elif [X] == [ship_obj.X[1]] and [Y] == [ship_obj.Y[1]]:
                    Ship.too_desk(X, Y, 1, pol_wor, flag_step)
                else:
                    inspekt.append(False)
        # ============================ ТРЁХ-палубные =====================================
            if len(ship_obj.X) == 3:
                if [X] == [ship_obj.X[0]] and [Y] == [ship_obj.Y[0]]:
                    Ship.three_desk(X, Y, 0, pol_wor, flag_step)

                elif [X] == [ship_obj.X[1]] and [Y] == [ship_obj.Y[1]]:
                    Ship.three_desk(X, Y, 1, pol_wor, flag_step)

                elif [X] == [ship_obj.X[2]] and [Y] == [ship_obj.Y[2]]:
                    Ship.three_desk(X, Y, 2, pol_wor, flag_step)
                else:
                    inspekt.append(False)
    else:
        Random(flag_step)
    # +++ Проверил, а не мимо ли пульнул? +++
    if len(inspekt) == 7:
        print("Промазал !!! Ох!")
        if flag_step == True:
            flag_step = False
            Prog(X, Y, "T", pol_wor, flag_step)
        else:
            flag_step = True
            Prog(X, Y, "T", pole_my, flag_step)
    return
# / ============= R A N D O M ================ /
def Random(flag_step):
    import random
    X = random.randint(1, 6)
    Y = random.randint(1, 6)
    print(f"\n{' ' * 14}Ходит программа ...")
    print(f"{' ' * 13}Ба-Бах! X, Y = {X, Y}")
    inspekt = []
    # Проверка на стрелянное поле:
    Ship.repet_lock(pole_my[X][Y - 1], X, Y, flag_step)

    for ship in friendly:
        ship_obj = Ship(deck=ship.get("deck"),
                        X=ship.get("X"),
                        Y=ship.get("Y"))

        if len(ship_obj.X) == 1:
            if [X] == ship_obj.X and [Y] == ship_obj.Y:
                Ship.one_desk(X, Y, pole_my, flag_step)
            else:
                inspekt.append(False)

        if len(ship_obj.X) == 2:
            if [X] == [ship_obj.X[0]] and [Y] == [ship_obj.Y[0]]:
                Ship.too_desk(X, Y, 0, pole_my, flag_step)
            elif [X] == [ship_obj.X[1]] and [Y] == [ship_obj.Y[1]]:
                Ship.too_desk(X, Y, 1, pole_my, flag_step)
            else:
                inspekt.append(False)

        if len(ship_obj.X) == 3:
            if [X] == [ship_obj.X[0]] and [Y] == [ship_obj.Y[0]]:
                Ship.three_desk(X, Y, 0, pole_my, flag_step)

            elif [X] == [ship_obj.X[1]] and [Y] == [ship_obj.Y[1]]:
                Ship.three_desk(X, Y, 1, pole_my, flag_step)

            elif [X] == [ship_obj.X[2]] and [Y] == [ship_obj.Y[2]]:
                Ship.three_desk(X, Y, 2, pole_my, flag_step)
            else:
                inspekt.append(False)

    if len(inspekt) == 7:
        print("   Промазал !!! Ох!")

        if flag_step == True:
            flag_step = False
            Prog(X, Y, "T", pol_wor, flag_step)
        else:
            flag_step = True
            Prog(X, Y, "T", pole_my, flag_step)

    return

Doska(flag_step)