from rolls import *

def autounav(roll_num, eur_pool, esr_pool, er_pool, em_pool, unav_pool):
    if roll_num <= 10:
        unav_pool = []
    if roll_num <= 9:
        er_pool = ["Eclair"]
        esr_pool = ["Fried Chicken"]
        unav_pool = ["Eclair", "Fried Chicken"]
    if roll_num <= 8:
        esr_pool.remove("Ddeokbokki")
        esr_pool.remove("Kimchi")
        unav_pool += ["Ddeokbokki", "Kimchi"]
    if roll_num <= 7:
        eur_pool.remove("Bibimbap")
        unav_pool += ["Bibimbap"]
    if roll_num <= 6:
        esr_pool.remove("Laba Congee")
        unav_pool += ["Laba Congee"]
    if roll_num <= 5:
        esr_pool.remove("Milk Tea")
        esr_pool.remove("Yunnan Noodles")
        unav_pool += ["Milk Tea", "Yunnan Noodles"]
    if roll_num <= 4:
        er_pool.remove("Cold Rice Shrimp")
        unav_pool += ["Cold Rice Shrimp"]
    if roll_num <= 3:
        esr_pool.remove("Sweet Tofu")
        unav_pool += ["Sweet Tofu"]
    if roll_num <= 2:
        esr_pool.remove("Udon")
        unav_pool += ["Udon"]
    if roll_num <= 1:
        esr_pool.remove("Eggette")
        esr_pool.remove("Pineapple Cake")
        unav_pool += ["Eggette", "Pineapple Cake"]
    if roll_num <= 0:
        esr_pool.remove("Chocolate")
        em_pool.remove("Popcorn")
        unav_pool += ["Chocolate", "Popcorn"]
    return unav_pool

def eventfs(foodsoul, fs_type, eevent_pool, eur_pool, esr_pool, er_pool, em_pool):
    eevent_pool.remove(foodsoul)
    if fs_type == 1:
        eur_pool += [foodsoul]
    if fs_type == 2:
        esr_pool += [foodsoul]
    if fs_type == 3:
        er_pool += [foodsoul]
    if fs_type == 4:
        em_pool += [foodsoul]
    return eevent_pool

def removefs(foodsoul, fs_type, eur_pool, esr_pool, er_pool, em_pool, unav_pool):
    unav_pool += [foodsoul]
    if fs_type == 1:
        eur_pool.remove(foodsoul)
    if fs_type == 2:
        esr_pool.remove(foodsoul)
    if fs_type == 3:
        er_pool.remove(foodsoul)
    if fs_type == 4:
        em_pool.remove(foodsoul)
    return unav_pool

def autoroll(eroll, roll_num, eur_pool, esr_pool, er_pool, em_pool, unav_pool):
    unav_pool = autounav(roll_num, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    if roll_num == 0:
        eroll += roll0
    if roll_num == 1:
        eroll += roll1
    elif roll_num == 2:
        eroll += roll2
    elif roll_num == 3:
        eroll += roll3
    elif roll_num == 4:
        eroll += roll4
    elif roll_num == 5:
        eroll += roll5
    elif roll_num == 6:
        eroll += roll6
    elif roll_num == 7:
        eroll += roll7
    elif roll_num == 8:
        eroll += roll8
    elif roll_num == 9:
        eroll += roll9
    elif roll_num == 10:
        eroll += roll10
    return eroll, unav_pool

def index0entry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool):
    eroll, unav_pool = autoroll(eroll, 1, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    for e1 in range(10):
        eroll.remove("Crab Long Bao")
    for e2 in range(22):
        eroll.remove("Bamboo Rice")
    for e3 in range(21):
        eroll.remove("Foie Gras")
        eroll.remove("Peking Duck")
    for e4 in range(23):
        eroll.remove("B-52")
    for e5 in range(97):
        eroll += ["Gingerbread"]
    for e6 in range(250):
        eroll += ["Chocolate"]
    return eroll

def index1entry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool):
    eroll, unav_pool = autoroll(eroll, 2, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    return eroll

def index2entry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool):
    eroll, unav_pool = autoroll(eroll, 2, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    eevent_pool = eventfs("Toso", 1, eevent_pool, eur_pool, esr_pool, er_pool, em_pool)
    esr_pool += ["Sweet Tofu"]
    unav_pool.remove("Sweet Tofu")
    for e0 in range(12):
        eroll.remove("Gingerbread")
    for e1 in range(150):
        eroll += ["Toso"]
    for e2 in range(31):
        eroll.remove("B-52")
    for e3 in range(32):
        eroll.remove("Foie Gras")
    for e4 in range(12):
        eroll.remove("Crab Long Bao")
    for e5 in range(32):
        eroll.remove("Bamboo Rice")
    for e6 in range(31):
        eroll.remove("Peking Duck")
    for e7 in range(661):
        eroll += ["Sweet Tofu"]
    for e8 in range(50):
        eroll.remove("Pineapple Cake")
        eroll.remove("Eggette")
        eroll.remove("Tiramisu")
        eroll.remove("Escargot")
        eroll.remove("Hotdog")
        eroll.remove("Mango Pudding")
        eroll.remove("Hamburger")
        eroll.remove("Steak")
        eroll.remove("Tangyuan")
        eroll.remove("Sanma")
        eroll.remove("Napoleon Cake")
        eroll.remove("Salad")
        eroll.remove("Pastel de nata")
        eroll.remove("Yuxiang")
        eroll.remove("Sukiyaki")
        eroll.remove("Brownie")
        eroll.remove("Red Wine")
        eroll.remove("Chocolate")
    for e9 in range(32):
        eroll.remove("Gyoza")
    return eroll

def index3entry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool):
    eroll, unav_pool = autoroll(eroll, 2, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    eevent_pool = eventfs("Raindrop Cake", 1, eevent_pool, eur_pool, esr_pool, er_pool, em_pool)
    eevent_pool = eventfs("Strawberry Daifuku", 4, eevent_pool, eur_pool, esr_pool, er_pool, em_pool)
    for e1 in range(120):
        eroll += ["Raindrop Cake"]
    for e2 in range(31):
        eroll += ["Strawberry Daifuku"]
    for e3 in range(25):
        eroll.remove("B-52")
        eroll.remove("Foie Gras")
        roll.remove("Peking Duck")
    for e4 in range(26):
        eroll.remove("Bamboo Rice")
    for e5 in range(7):
        eroll.remove("Pancake")
    for e6 in range(8):
        eroll.remove("Popcorn")
        eroll.remove("Jello")
        eroll.remove("Skewer")
        eroll.remove("Crab Long Bao")
        eroll.remove("Gingerbread")
    return eroll

def index4aentry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool):
    eroll, unav_pool = autoroll(eroll, 3, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    eevent_pool = eventfs("Milt", 1, eur_pool, eevent_pool, esr_pool, er_pool, em_pool)
    eevent_pool = eventfs("Bonito Rice", 2, eevent_pool, eur_pool, esr_pool, er_pool, em_pool)
    for e1 in range(48):
        eroll += ["Milt"]
    for e2 in range(96):
        eroll += ["Bonito Rice"]
    for e3 in range(4):
        eroll.remove("Yuxiang")
        eroll.remove("Sukiyaki")
        eroll.remove("Brownie")
        eroll.remove("Red Wine")
        eroll.remove("Gyoza")
        eroll.remove("Chocolate")
        eroll.remove("Udon")
    for e4 in range(5):
        eroll.remove("Tiramisu")
        eroll.remove("Escargot")
        eroll.remove("Hotdog")
        eroll.remove("Mango Pudding")
        eroll.remove("Hamburger")
        eroll.remove("Steak")
        eroll.remove("Tangyuan")
        eroll.remove("Sanma")
        eroll.remove("Napoleon Cake")
        eroll.remove("Salad")
        eroll.remove("Pastel de nata")
        eroll.remove("Crab Long Bao")
        eroll.remove("Gingerbread")
    for e5 in range(6):
        eroll.remove("Eggette")
    for e6 in range(7):
        eroll.remove("Pineapple Cake")
    for e7 in range(8):
        eroll.remove("Peking Duck")
    for e8 in range(9):
        eroll.remove("Foie Gras")
        eroll.remove("B-52")
    for e9 in range(10):
        eroll.remove("Bamboo Rice")
    return eroll

def index5aentry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool):
    eroll, unav_pool = autoroll(eroll, 4, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    for e1 in range(89):
        eroll += ["Peking Duck"]
    for e2 in range(12):
        eroll.remove("Crab Long Bao")
        eroll.remove("Gingerbread")
    for e3 in range(21):
        eroll.remove("Foie Gras")
        eroll.remove("B-52")
    for e4 in range(23):
        eroll.remove("Bamboo Rice")
    return eroll

def index6entry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool):
    eroll, unav_pool = autoroll(eroll, 4, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    eevent_pool = eventfs("Cassata", 2, eevent_pool, eur_pool, esr_pool, er_pool, em_pool)
    for e1 in range(59):
        eroll += ["B-52"]
    eroll.remove("Gingerbread")
    for e2 in range(9):
        eroll.remove("Foie Gras")
        eroll.remove("Peking Duck")
    for e3 in range(10):
        eroll.remove("Bamboo Rice")
    for e4 in range(332):
        eroll += ["Cassata"]
    for e5 in range(15):
        eroll.remove("Tiramisu")
        eroll.remove("Escargot")
        eroll.remove("Hotdog")
        eroll.remove("Mango Pudding")
        eroll.remove("Hamburger")
        eroll.remove("Steak")
        eroll.remove("Tangyuan")
        eroll.remove("Sanma")
        eroll.remove("Napoleon Cake")
        eroll.remove("Salad")
        eroll.remove("Pastel de nata")
        eroll.remove("Yuxiang")
        eroll.remove("Sukiyaki")
        eroll.remove("Brownie")
        eroll.remove("Red Wine")
        eroll.remove("Gyoza")
        eroll.remove("Chocolate")
        eroll.remove("Udon")
        eroll.remove("Sweet Tofu")
    for e6 in range(24):
        eroll.remove("Pineapple Cake")
    for e7 in range(23):
        eroll.remove("Eggette")
    return eroll

def index7entry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool):
    eroll, unav_pool = autoroll(eroll, 4, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    eevent_pool = eventfs("Cassata", 2, eevent_pool, eur_pool, esr_pool, er_pool, em_pool)
    for e1 in range(97):
        eroll += ["Crab Long Bao"]
    for e2 in range(4):
        eroll.remove("Gingerbread")
    for e3 in range(23):
        eroll.remove("Foie Gras")
        eroll.remove("Peking Duck")
        eroll.remove("B-52")
    for e4 in range(24):
        eroll.remove("Bamboo Rice")
    for e5 in range(332):
        eroll += ["Cassata"]
    for e6 in range(15):
        eroll.remove("Tiramisu")
        eroll.remove("Escargot")
        eroll.remove("Hotdog")
        eroll.remove("Mango Pudding")
        eroll.remove("Hamburger")
        eroll.remove("Steak")
        eroll.remove("Tangyuan")
        eroll.remove("Sanma")
        eroll.remove("Napoleon Cake")
        eroll.remove("Salad")
        eroll.remove("Pastel de nata")
        eroll.remove("Yuxiang")
        eroll.remove("Sukiyaki")
        eroll.remove("Brownie")
        eroll.remove("Red Wine")
        eroll.remove("Gyoza")
        eroll.remove("Chocolate")
        eroll.remove("Udon")
        eroll.remove("Sweet Tofu")
    for e7 in range(24):
        eroll.remove("Pineapple Cake")
    for e8 in range(23):
        eroll.remove("Eggette")
    return eroll

def index8entry(eroll, eevent_pool, esummon_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool):
    eroll, unav_pool = autoroll(eroll, 4, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    eevent_pool = eventfs("Cassata", 2, eevent_pool, eur_pool, esr_pool, er_pool, em_pool)
    for e1 in range(25):
        eroll += ["Double Scoop"]
    for e2 in range(2):
        eroll.remove("Gingerbread")
        eroll.remove("Crab Long Bao")
    for e3 in range(5):
        eroll.remove("Foie Gras")
        eroll.remove("Peking Duck")
        eroll.remove("B-52")
    for e4 in range(6):
        eroll.remove("Bamboo Rice")
    for e5 in range(332):
        eroll += ["Cassata"]
    for e6 in range(15):
        eroll.remove("Tiramisu")
        eroll.remove("Escargot")
        eroll.remove("Hotdog")
        eroll.remove("Mango Pudding")
        eroll.remove("Hamburger")
        eroll.remove("Steak")
        eroll.remove("Tangyuan")
        eroll.remove("Sanma")
        eroll.remove("Napoleon Cake")
        eroll.remove("Salad")
        eroll.remove("Pastel de nata")
        eroll.remove("Yuxiang")
        eroll.remove("Sukiyaki")
        eroll.remove("Brownie")
        eroll.remove("Red Wine")
        eroll.remove("Gyoza")
        eroll.remove("Chocolate")
        eroll.remove("Udon")
        eroll.remove("Sweet Tofu")
    for e7 in range(24):
        eroll.remove("Pineapple Cake")
    for e8 in range(23):
        eroll.remove("Eggette")
    return eroll

def index9entry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool):
    eroll, unav_pool = autoroll(eroll, 4, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    eevent_pool = eventfs("Cassata", 2, eevent_pool, eur_pool, esr_pool, er_pool, em_pool)
    for e1 in range(58):
        eroll += ["Bamboo Rice"]
    for e2 in range(19):
        eroll.remove("B-52")
        eroll.remove("Foie Gras")
        eroll.remove("Peking Duck")
    eroll.remove("Gingerbread")
    for e3 in range(332):
        eroll += ["Cassata"]
    for e4 in range(15):
        eroll.remove("Tiramisu")
        eroll.remove("Escargot")
        eroll.remove("Hotdog")
        eroll.remove("Mango Pudding")
        eroll.remove("Hamburger")
        eroll.remove("Steak")
        eroll.remove("Tangyuan")
        eroll.remove("Sanma")
        eroll.remove("Napoleon Cake")
        eroll.remove("Salad")
        eroll.remove("Pastel de nata")
        eroll.remove("Yuxiang")
        eroll.remove("Sukiyaki")
        eroll.remove("Brownie")
        eroll.remove("Red Wine")
        eroll.remove("Gyoza")
        eroll.remove("Chocolate")
        eroll.remove("Udon")
        eroll.remove("Sweet Tofu")
    for e5 in range(24):
        eroll.remove("Pineapple Cake")
    for e6 in range(23):
        eroll.remove("Eggette")
    return eroll

def index10entry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool):
    eroll, unav_pool = autoroll(eroll, 4, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    eevent_pool = eventfs("Cassata", 2, eevent_pool, eur_pool, esr_pool, er_pool, em_pool)
    for e1 in range(120):
        eroll += ["Toso"]
    for e2 in range(5):
        eroll.remove("Crab Long Bao")
    for e3 in range(6):
        eroll.remove("Gingerbread")
    for e4 in range(27):
        eroll.remove("B-52")
        eroll.remove("Foie Gras")
        eroll.remove("Peking Duck")
    for e5 in range(28):
        eroll.removve("Bamboo Rice")
    for e6 in range(332):
        eroll += ["Cassata"]
    for e7 in range(15):
        eroll.remove("Tiramisu")
        eroll.remove("Escargot")
        eroll.remove("Hotdog")
        eroll.remove("Mango Pudding")
        eroll.remove("Hamburger")
        eroll.remove("Steak")
        eroll.remove("Tangyuan")
        eroll.remove("Sanma")
        eroll.remove("Napoleon Cake")
        eroll.remove("Salad")
        eroll.remove("Pastel de nata")
        eroll.remove("Yuxiang")
        eroll.remove("Sukiyaki")
        eroll.remove("Brownie")
        eroll.remove("Red Wine")
        eroll.remove("Gyoza")
        eroll.remove("Chocolate")
        eroll.remove("Udon")
        eroll.remove("Sweet Tofu")
    for e8 in range(24):
        eroll.remove("Pineapple Cake")
    for e9 in range(23):
        eroll.remove("Eggette")
    return eroll

def index11aentry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool):
    eroll, unav_pool = autoroll(eroll, 4, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    for e1 in range(127):
        eroll += ["Gingerbread"]
    for e2 in range(28):
        eroll.remove("Foie Gras")
        eroll.remove("Peking Duck")
    for e3 in range(29):
        eroll.remove("B-52")
    for e4 in range(30):
        eroll.remove("Bamboo Rice")
    for e5 in range(12):
        eroll.remove("Crab Long Bao")
    return eroll

def index12entry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool):
    eroll, unav_pool = autoroll(eroll, 5, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    eevent_pool = eventfs("Caviar", 1, eevent_pool, eur_pool, esr_pool, er_pool, em_pool)
    eevent_pool = eventfs("Seaweed Soup", 2, eevent_pool, eur_pool, esr_pool, er_pool, em_pool)
    for e1 in range(498):
        eroll += ["Seaweed Soup"]
    for e2 in range(121):
        eroll += ["Caviar"]
    for e3 in range(10):
        eroll.remove("Gingerbread")
        eroll.remove("Crab Long Bao")
    for e4 in range(25):
        eroll.remove("B-52")
        eroll.remove("Foie Gras")
        eroll.remove("Peking Duck")
    for e5 in range(26):
        eroll.remove("Bamboo Rice")
    for e6 in range(40):
        eroll.remove("Eggette")
        eroll.remove("Pineapple Cake")
    for e7 in range(22):
        eroll.remove("Tiramisu")
        eroll.remove("Escargot")
        eroll.remove("Hotdog")
        eroll.remove("Mango Pudding")
        eroll.remove("Hamburger")
        eroll.remove("Steak")
        eroll.remove("Tangyuan")
        eroll.remove("Sanma")
        eroll.remove("Napoleon Cake")
        eroll.remove("Salad")
        eroll.remove("Pastel de nata")
        eroll.remove("Yuxiang")
        eroll.remove("Sukiyaki")
        eroll.remove("Brownie")
        eroll.remove("Red Wine")
        eroll.remove("Gyoza")
        eroll.remove("Chocolate")
        eroll.remove("Udon")
        eroll.remove("Sweet Tofu")
    return eroll

def index13entry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool):
    eroll, unav_pool = autoroll(eroll, 5, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    eevent_pool = eventfs("Raindrop Cake", 1, eevent_pool, eur_pool, esr_pool, er_pool, em_pool)
    for e1 in range(426):
        eroll += ["Sanma"]
    for e2 in range(121):
        eroll += ["Raindrop Cake"]
    for e3 in range(10):
        eroll.remove("Gingerbread")
        eroll.remove("Crab Long Bao")
    for e4 in range(25):
        eroll.remove("B-52")
        eroll.remove("Foie Gras")
        eroll.remove("Peking Duck")
    for e5 in range(26):
        eroll.remove("Bamboo Rice")
    for e6 in range(39):
        eroll.remove("Eggette")
    for e7 in range(40):
        eroll.remove("Pineapple Cake")
    for e8 in range(20):
        eroll.remove("Tiramisu")
        eroll.remove("Escargot")
        eroll.remove("Hotdog")
        eroll.remove("Mango Pudding")
        eroll.remove("Hamburger")
    for e9 in range(19):
        eroll.remove("Steak")
        eroll.remove("Tangyuan")
        eroll.remove("Sanma")
        eroll.remove("Napoleon Cake")
        eroll.remove("Salad")
        eroll.remove("Pastel de nata")
        eroll.remove("Yuxiang")
        eroll.remove("Sukiyaki")
        eroll.remove("Brownie")
        eroll.remove("Red Wine")
        eroll.remove("Gyoza")
        eroll.remove("Chocolate")
        eroll.remove("Udon")
        eroll.remove("Sweet Tofu")
    return eroll

def index5bentry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool):
    eroll, unav_pool = autoroll(eroll, 5, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    for e1 in range(89):
        eroll += ["Peking Duck"]
    for e2 in range(12):
        eroll.remove("Crab Long Bao")
        eroll.remove("Gingerbread")
    for e3 in range(21):
        eroll.remove("Foie Gras")
        eroll.remove("B-52")
    for e4 in range(23):
        eroll.remove("Bamboo Rice")
    return eroll

def index14entry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool):
    eroll, unav_pool = autoroll(eroll, 6, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    eevent_pool = eventfs("Sichuan Hotpot", 1, eevent_pool, eur_pool, esr_pool, er_pool, em_pool)
    eevent_pool = eventfs("Beer", 2, eevent_pool, eur_pool, esr_pool, er_pool, em_pool)
    for e1 in range(499):
        eroll += ["Beer"]
    for e2 in range(121):
        eroll += ["Sichuan Hotpot"]
    return eroll

def index4bentry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool):
    eroll, unav_pool = autoroll(eroll, 6, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    eevent_pool = eventfs("Milt", 1, eevent_pool, eur_pool, esr_pool, er_pool, em_pool)
    eevent_pool = eventfs("Bonito Rice", 2, eevent_pool, eur_pool, esr_pool, er_pool, em_pool)
    for e1 in range(499):
        eroll += ["Bonito Rice"]
    for e2 in range(121):
        eroll += ["Milt"]
    return eroll

def index11bentry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool):
    eroll, unav_pool = autoroll(eroll, 7, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    for e1 in range(127):
        eroll += ["Gingerbread"]
    for e2 in range(28):
        eroll.remove("Foie Gras")
        eroll.remove("Peking Duck")
    for e3 in range(29):
        eroll.remove("B-52")
    for e4 in range(30):
        eroll.remove("Bamboo Rice")
    for e5 in range(12):
        eroll.remove("Crab Long Bao")
    return eroll

def index15entry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool):
    eroll, unav_pool = autoroll(eroll, 8, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    for e1 in range(112):
        eroll += ["Bibimbap"]
    for e2 in range(12):
        eroll.remove("Gingerbread")
        eroll.remove("Crab Long Bao")
    for e3 in range(22):
        eroll.remove("Foie Gras")
        eroll.remove("Peking Duck")
        eroll.remove("Bamboo Rice")
        eroll.remove("B-52")
    return eroll

def index16entry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool):
    eroll, unav_pool = autoroll(eroll, 8, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    eevent_pool = eventfs("Champagne", 1, eevent_pool, eur_pool, esr_pool, er_pool, em_pool)
    eevent_pool = eventfs("Raindrop Cake", 1, eevent_pool, eur_pool, esr_pool, er_pool, em_pool)
    eevent_pool = eventfs("Bonito Rice", 2, eevent_pool, eur_pool, esr_pool, er_pool, em_pool)
    eevent_pool = eventfs("Beer", 2, eevent_pool, eur_pool, esr_pool, er_pool, em_pool)
    unav_pool = removefs("Foie Gras", 1, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    unav_pool = removefs("B-52", 1, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    unav_pool = removefs("Boston Lobster", 1, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    unav_pool = removefs("Gingerbread", 1, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    for e1 in range(121):
        eroll += ["Champagne"]
    for e2 in range(44):
        eroll += ["Crab Long Bao"]
    for e3 in range(5):
        eroll += ["Double Scoop"]
        eroll += ["Bamboo Rice"]
        eroll += ["Peking Duck"]
        eroll.remove("Boston Lobster")
        eroll.remove("Cold Rice Shrimp")
        eroll.remove("Zongzi")
        eroll.remove("Sakuramochi")
        eroll.remove("Tom Yum")
        eroll.remove("Taiyaki")
        eroll.remove("Milk")
        eroll.remove("Dorayaki")
        eroll.remove("Sake")
        eroll.remove("Tempura")
        eroll.remove("Spicy Gluten")
        eroll.remove("Jiuniang")
        eroll.remove("Omurice")
    for e4 in range(16):
        eroll += ["Bibimbap"]
    for e5 in range(50):
        eroll += ["Raindrop Cake"]
    for e6 in range(60):
        eroll.remove("Foie Gras")
        eroll.remove("B-52")
    for e7 in range(21):
        eroll.remove("Gingerbread")
    for e8 in range(17):
        eroll.remove("Laba Congee")
        eroll.remove("Eggette")
        eroll.remove("Pineapple Cake")
    for e9 in range(36):
        eroll += ["Milk Tea"]
        eroll += ["Yunnan Noodles"]
    for e10 in range(2):
        eroll += ["Escargot"]
        eroll += ["Hotdog"]
        eroll += ["Mango Pudding"]
        eroll += ["Hamburger"]
        eroll += ["Napoleon Cake"]
        eroll += ["Salad"]
        eroll += ["Red Wine"]
        eroll += ["Pastel de nata"]
        eroll += ["Yuxiang"]
        eroll += ["Tiramisu"]
        eroll += ["Brownie"]
        eroll += ["Chocolate"]
    for e11 in range(19):
        eroll.remove("Tangyuan")
        eroll.remove("Sanma")
        eroll.remove("Sukiyaki")
        eroll.remove("Udon")
        eroll.remove("Gyoza")
    for e12 in range(43):
        eroll += ["Beer"]
        eroll += ["Bonito Rice"]
    for e13 in range(18):
        eroll.remove("Steak")
        eroll.remove("Sweet Tofu")
    for e14 in range(4):
        eroll.remove("Long Bao")
        eroll.remove("Coffee")
        eroll.remove("Sashimi")
        eroll.remove("Macaron")
    for e15 in range(6):
        eroll.remove("Orange Juice")
        eroll.remove("Ume Ochazuke")
        eroll.remove("Miso Soup")
        eroll.remove("Yellow Wine")
    return eroll

def index17entry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool):
    eroll, unav_pool = autoroll(eroll, 8, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    eevent_pool = eventfs("Toso", 1, eevent_pool, eur_pool, esr_pool, er_pool, em_pool)
    eevent_pool = eventfs("Milt", 1, eevent_pool, eur_pool, esr_pool, er_pool, em_pool)
    eevent_pool = eventfs("Bonito Rice", 2, eevent_pool, eur_pool, esr_pool, er_pool, em_pool)
    eevent_pool = eventfs("Beer", 2, eevent_pool, eur_pool, esr_pool, er_pool, em_pool)
    eevent_pool = eventfs("Strawberry Daifuku", 4, eevent_pool, eur_pool, esr_pool, er_pool, em_pool)
    unav_pool = removefs("Peking Duck", 1, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    unav_pool = removefs("Bamboo Rice", 1, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    unav_pool = removefs("Double Scoop", 1, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    unav_pool = removefs("Crab Long Bao", 1, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    unav_pool = removefs("Skewer", 4, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    for e1 in range(121):
        eroll += ["Toso"]
    for e2 in range(44):
        eroll += ["Gingerbread"]
    for e3 in range(5):
        eroll += ["Boston Lobster"]
        eroll += ["Foie Gras"]
        eroll += ["B-52"]
        eroll.remove("Double Scoop")
        eroll.remove("Cold Rice Shrimp")
        eroll.remove("Zongzi")
        eroll.remove("Sakuramochi")
        eroll.remove("Tom Yum")
        eroll.remove("Taiyaki")
        eroll.remove("Milk")
        eroll.remove("Dorayaki")
        eroll.remove("Sake")
        eroll.remove("Tempura")
        eroll.remove("Spicy Gluten")
        eroll.remove("Jiuniang")
        eroll.remove("Omurice")
    for e4 in range(16):
        eroll += ["Bibimbap"]
    for e5 in range(50):
        eroll += ["Milt"]
    for e6 in range(60):
        eroll.remove("Peking Duck")
        eroll.remove("Bamboo Rice")
    for e7 in range(21):
        eroll.remove("Crab Long Bao")
    for e8 in range(17):
        eroll.remove("Laba Congee")
        eroll.remove("Eggette")
        eroll.remove("Pineapple Cake")
    for e9 in range(36):
        eroll += ["Milk Tea"]
        eroll += ["Yunnan Noodles"]
    for e10 in range(2):
        eroll += ["Escargot"]
        eroll += ["Hotdog"]
        eroll += ["Mango Pudding"]
        eroll += ["Hamburger"]
        eroll += ["Napoleon Cake"]
        eroll += ["Salad"]
        eroll += ["Red Wine"]
        eroll += ["Pastel de nata"]
        eroll += ["Yuxiang"]
        eroll += ["Tiramisu"]
        eroll += ["Brownie"]
        eroll += ["Chocolate"]
    for e11 in range(19):
        eroll.remove("Tangyuan")
        eroll.remove("Sanma")
        eroll.remove("Sukiyaki")
        eroll.remove("Udon")
        eroll.remove("Gyoza")
    for e12 in range(43):
        eroll += ["Beer"]
        eroll += ["Bonito Rice"]
    for e13 in range(18):
        eroll.remove("Steak")
        eroll.remove("Sweet Tofu")
    for e14 in range(4):
        eroll.remove("Long Bao")
        eroll.remove("Coffee")
        eroll.remove("Sashimi")
        eroll.remove("Macaron")
    for e15 in range(6):
        eroll.remove("Orange Juice")
        eroll.remove("Ume Ochazuke")
        eroll.remove("Miso Soup")
        eroll.remove("Yellow Wine")
    for e16 in range(46):
        eroll.remove("Skewer")
    for e17 in range(47):
        eroll += ["Strawberry Daifuku"]
    eroll.remove("Popcorn")
    return eroll

def index18aentry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool):
    eroll, unav_pool = autoroll(eroll, 8, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    for e1 in range(60):
        eroll += ["B-52"]
    for e2 in range(2):
        eroll.remove("Bibimbap")
    for e3 in range(5):
        eroll.remove("Gingerbread")
        eroll.remove("Crab Long Bao")
    for e4 in range(16):
        eroll.remove("Foie Gras")
        eroll.remove("Bamboo Rice")
        eroll.remove("Peking Duck")
    return eroll

def index19entry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool):
    eroll, unav_pool = autoroll(eroll, 8, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    eevent_pool = eventfs("Huangshan Maofeng Tea", 1, eevent_pool, eur_pool, esr_pool, er_pool, em_pool)
    eevent_pool = eventfs("Osmanthus Cake", 2, eevent_pool, eur_pool, esr_pool, er_pool, em_pool)
    eevent_pool = eventfs("Fondant Cake", 2, eevent_pool, eur_pool, esr_pool, er_pool, em_pool)
    for e1 in range(120):
        eroll += ["Huangshan Maofeng Tea"]
    for e2 in range(58):
        eroll += ["Fondant Cake"]
    for e3 in range(57):
        eroll += ["Osmanthus Cake"]
    for e4 in range(2):
        eroll.remove("Bibimbap")
    for e5 in range(9):
        eroll.remove("Crab Long Bao")
        eroll.remove("Gingerbread")
    for e6 in range(25):
        eroll.remove("Foie Gras")
        eroll.remove("Peking Duck")
        eroll.remove("B-52")
        eroll.remove("Bamboo Rice")
    for e7 in range(4):
        eroll.remove("Pineapple Cake")
        eroll.remove("Eggette")
        eroll.remove("Laba Congee")
        eroll.remove("Escargot")
        eroll.remove("Hotdog")
        eroll.remove("Hamburger")
        eroll.remove("Steak")
        eroll.remove("Tangyuan")
        eroll.remove("Sweet Tofu")
    for e8 in range(7):
        eroll.remove("Milk Tea")
        eroll.remove("Yunnan Noodles")
    for e9 in range(5):
        eroll.remove("Sukiyaki")
        eroll.remove("Brownie")
        eroll.remove("Napoleon Cake")
        eroll.remove("Salad")
        eroll.remove("Pastel de nata")
        eroll.remove("Yuxiang")
        eroll.remove("Tiramisu")
        eroll.remove("Mango Pudding")
        eroll.remove("Red Wine")
        eroll.remove("Gyoza")
        eroll.remove("Chocolate")
        eroll.remove("Udon")
    return eroll

def index20entry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool):
    eroll, unav_pool = eroll, unav_pool = autoroll(eroll, 8, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    eevent_pool = eventfs("Caviar", 1, eevent_pool, eur_pool, esr_pool, er_pool, em_pool)
    eevent_pool = eventfs("Seaweed Soup", 2, eevent_pool, eur_pool, esr_pool, er_pool, em_pool)
    eevent_pool = eventfs("Fondant Cake", 2, eevent_pool, eur_pool, esr_pool, er_pool, em_pool)
    eevent_pool = eventfs("Strawberry Daifuku", 4, eevent_pool, eur_pool, esr_pool, er_pool, em_pool)
    unav_pool = removefs("Skewer", 4, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    for e1 in range(120):
        eroll += ["Caviar"]
    for e2 in range(58):
        eroll += ["Fondant Cake"]
    for e3 in range(57):
        eroll += ["Seaweed Soup"]
    for e4 in range(2):
        eroll.remove("Bibimbap")
    for e5 in range(9):
        eroll.remove("Crab Long Bao")
        eroll.remove("Gingerbread")
    for e6 in range(25):
        eroll.remove("Foie Gras")
        eroll.remove("Peking Duck")
        eroll.remove("B-52")
        eroll.remove("Bamboo Rice")
    for e7 in range(4):
        eroll.remove("Pineapple Cake")
        eroll.remove("Eggette")
        eroll.remove("Laba Congee")
        eroll.remove("Escargot")
        eroll.remove("Hotdog")
        eroll.remove("Hamburger")
        eroll.remove("Steak")
        eroll.remove("Tangyuan")
        eroll.remove("Sweet Tofu")
    for e8 in range(7):
        eroll.remove("Milk Tea")
        eroll.remove("Yunnan Noodles")
    for e9 in range(5):
        eroll.remove("Sanma")
        eroll.remove("Sukiyaki")
        eroll.remove("Brownie")
        eroll.remove("Napoleon Cake")
        eroll.remove("Salad")
        eroll.remove("Pastel de nata")
        eroll.remove("Yuxiang")
        eroll.remove("Tiramisu")
        eroll.remove("Mango Pudding")
        eroll.remove("Red Wine")
        eroll.remove("Gyoza")
        eroll.remove("Chocolate")
        eroll.remove("Udon")
    for e10 in range(46):
        eroll.remove("Skewer")
        eroll += ["Strawberry Daifuku"]
    return eroll

def index21entry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool):
    eroll, unav_pool = eroll, unav_pool = autoroll(eroll, 8, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    for e1 in range(60):
        eroll += ["Bamboo Rice"]
    for e2 in range(16):
        eroll.remove("Foie Gras")
        eroll.remove("B-52")
        eroll.remove("Peking Duck")
    for e3 in range(5):
        eroll.remove("Gingerbread")
        eroll.remove("Crab Long Bao")
    for e4 in range(2):
        eroll.remove("Bibimbap")
    return eroll

def index22entry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool):
    eroll, unav_pool = eroll, unav_pool = autoroll(eroll, 9, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    for e1 in range(275):
        eroll += ["Ddeokbokki"]
        eroll += ["Kimchi"]
    for e2 in range(42):
        eroll.remove("Eggette")
        eroll.remove("Pineapple Cake")
        eroll.remove("Laba Congee")
    for e3 in range(23):
        eroll.remove("Milk Tea")
        eroll.remove("Yunnan Noodles")
    for e4 in range(20):
        eroll.remove("Escargot")
        eroll.remove("Hotdog")
        eroll.remove("Hamburger")
        eroll.remove("Steak")
        eroll.remove("Tangyuan")
        eroll.remove("Sanma")
        eroll.remove("Sukiyaki")
        eroll.remove("Brownie")
        eroll.remove("Napoleon Cake")
        eroll.remove("Salad")
        eroll.remove("Pastel de nata")
        eroll.remove("Yuxiang")
        eroll.remove("Tiramisu")
        eroll.remove("Mango Pudding")
        eroll.remove("Sweet Tofu")
    for e5 in range(21):
        eroll.remove("Red Wine")
        eroll.remove("Gyoza")
        eroll.remove("Chocolate")
        eroll.remove("Udon")
    return eroll

def index23entry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool):
    eroll, unav_pool = eroll, unav_pool = autoroll(eroll, 9, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    for e1 in range(99):
        eroll += ["Crab Long Bao"]
    for e2 in range(23):
        eroll.remove("Foie Gras")
        eroll.remove("B-52")
        eroll.remove("Peking Duck")
        eroll.remove("Bamboo Rice")
    for e3 in range(5):
        eroll.remove("Gingerbread")
    for e4 in range(2):
        eroll.remove("Bibimbap")
    for e5 in range(3):
        eroll += ["Milk Tea"]
        eroll += ["Yunnan Noodles"]
    eroll.remove("Tiramisu")
    eroll.remove("Mango Pudding")
    eroll.remove("Red Wine")
    eroll.remove("Gyoza")
    eroll.remove("Chocolate")
    eroll.remove("Udon")
    return eroll

def index24entry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool):
    eroll, unav_pool = eroll, unav_pool = autoroll(eroll, 9, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    eevent_pool = eventfs("Buddha's Temptation", 1, eevent_pool, eur_pool, esr_pool, er_pool, em_pool)
    eevent_pool = eventfs("Butter Tea", 1, eevent_pool, eur_pool, esr_pool, er_pool, em_pool)
    eevent_pool = eventfs("Milt", 1, eevent_pool, eur_pool, esr_pool, er_pool, em_pool)
    eevent_pool = eventfs("Mandarin Squirrel Fish", 2, eevent_pool, eur_pool, esr_pool, er_pool, em_pool)
    eevent_pool = eventfs("Green Curry", 2, eevent_pool, eur_pool, esr_pool, er_pool, em_pool)
    unav_pool = removefs("Foie Gras", 1, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    unav_pool = removefs("Kimchi", 2, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    for e1 in range(120):
        eroll += ["Buddha's Temptation"]
    for e2 in range(498):
        eroll += ["Mandarin Squirrel Fish"]
    for e3 in range(10):
        eroll += ["Butter Tea"]
        eroll += ["Milt"]
    for e4 in range(43):
        eroll += ["Green Curry"]
    for e5 in range(57):
        eroll.remove("Kimchi")
    for e6 in range(60):
        eroll.remove("Foie Gras")
    eroll += ["Bibimbap"]
    for e7 in range(7):
        eroll += ["Crab Long Bao"]
        eroll += ["Gingerbread"]
    for e8 in range(31):
        eroll.remove("Bamboo Rice")
    for e9 in range(32):
        eroll.remove("B-52")
        eroll.remove("Peking Duck")
    for e10 in range(49):
        eroll.remove("Eggette")
        eroll.remove("Pineapple Cake")
        eroll.remove("Laba Congee")
    for e11 in range(15):
        eroll.remove("Escargot")
        eroll.remove("Hotdog")
        eroll.remove("Mango Pudding")
        eroll.remove("Hamburger")
        eroll.remove("Steak")
        eroll.remove("Tangyuan")
        eroll.remove("Sanma")
        eroll.remove("Napoleon Cake")
        eroll.remove("Salad")
        eroll.remove("Red Wine")
        eroll.remove("Pastel de nata")
    for e12 in range(14):
        eroll.remove("Ddeokbokki")
        eroll.remove("Sweet Tofu")
    for e13 in range(16):
        eroll.remove("Yuxiang")
        eroll.remove("Tiramisu")
        eroll.remove("Udon")
        eroll.remove("Gyoza")
        eroll.remove("Yunnan Noodles")
        eroll.remove("Sukiyaki")
        eroll.remove("Brownie")
        eroll.remove("Chocolate")
        eroll.remove("Milk Tea")
    return eroll

def index18bentry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool):
    eroll, unav_pool = autoroll(eroll, 9, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    for e1 in range(3):
        eroll += ["Yunnan Noodles"]
        eroll += ["Milk Tea"]
    eroll.remove("Tiramisu")
    eroll.remove("Mango Pudding")
    eroll.remove("Red Wine")
    eroll.remove("Gyoza")
    eroll.remove("Chocolate")
    eroll.remove("Udon")
    for e2 in range(60):
        eroll += ["B-52"]
    for e3 in range(16):
        eroll.remove("Foie Gras")
        eroll.remove("Peking Duck")
        eroll.remove("Bamboo Rice")
    for e4 in range(5):
        eroll.remove("Crab Long Bao")
        eroll.remove("Gingerbread")
    for e5 in range(2):
        eroll.remove("Bibimbap")
    return eroll

def index25entry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool):
    eroll, unav_pool = autoroll(eroll, 10, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    for e1 in range(1982):
        eroll += ["Eclair"]
    for e2 in range(442):
        eroll += ["Fried Chicken"]
    for e3 in range(32):
        eroll.remove("Eggette")
        eroll.remove("Pineapple Cake")
        eroll.remove("Laba Congee")
    for e4 in range(15):
        eroll.remove("Milk Tea")
        eroll.remove("Yunnan Noodles")
        eroll.remove("Tiramisu")
        eroll.remove("Escargot")
        eroll.remove("Hotdog")
        eroll.remove("Mango Pudding")
        eroll.remove("Hamburger")
        eroll.remove("Steak")
        eroll.remove("Tangyuan")
        eroll.remove("Sanma")
        eroll.remove("Napoleon Cake")
        eroll.remove("Salad")
        eroll.remove("Pastel de nata")
        eroll.remove("Yuxiang")
        eroll.remove("Sukiyaki")
        eroll.remove("Brownie")
        eroll.remove("Red Wine")
        eroll.remove("Gyoza")
        eroll.remove("Chocolate")
        eroll.remove("Udon")
        eroll.remove("Sweet Tofu")
        eroll.remove("Ddeokbokki")
    for e5 in range(16):
        eroll.remove("Kimchi")
    for e6 in range(100):
        eroll.remove("Long Bao")
        eroll.remove("Coffee")
    for e7 in range(99):
        eroll.remove("Sashimi")
        eroll.remove("Macaron")
        eroll.remove("Zongzi")
        eroll.remove("Sakuramochi")
        eroll.remove("Cold Rice Shrimp")
        eroll.remove("Tom Yum")
        eroll.remove("Taiyaki")
        eroll.remove("Milk")
        eroll.remove("Dorayaki")
        eroll.remove("Sake")
        eroll.remove("Tempura")
        eroll.remove("Spicy Gluten")
        eroll.remove("Jiuniang")
        eroll.remove("Omurice")
        eroll.remove("Orange Juice")
        eroll.remove("Ume Ochazuke")
        eroll.remove("Miso Soup")
        eroll.remove("Yellow Wine")
    return eroll

def index26entry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool):
    eroll, unav_pool = autoroll(eroll, 10, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    eevent_pool = eventfs("Raindrop Cake", 1, eevent_pool, eur_pool, esr_pool, er_pool, em_pool)
    eevent_pool = eventfs("Moon Cake", 2, eevent_pool, eur_pool, esr_pool, er_pool, em_pool)
    eevent_pool = eventfs("Sushi", 2, eevent_pool, eur_pool, esr_pool, er_pool, em_pool)
    eevent_pool = eventfs("Osmanthus Cake", 2, eevent_pool, eur_pool, esr_pool, er_pool, em_pool)
    unav_pool = removefs("Foie Gras", 1, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    unav_pool = removefs("Bibimbap", 1, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    unav_pool = removefs("Gingerbread", 1, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    unav_pool = removefs("B-52", 1, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    unav_pool = removefs("Peking Duck", 1, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    unav_pool = removefs("Crab Long Bao", 1, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    unav_pool = removefs("Double Scoop", 1, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    unav_pool = removefs("Fried Chicken", 2, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    unav_pool = removefs("Ddeokbokki", 2, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    unav_pool = removefs("Kimchi", 2, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    unav_pool = removefs("Milk Tea", 2, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    unav_pool = removefs("Yunnan Noodles", 2, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    unav_pool = removefs("Eggette", 2, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    unav_pool = removefs("Pineapple Cake", 2, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    unav_pool = removefs("Gyoza", 2, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    unav_pool = removefs("Laba Congee", 2, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    unav_pool = removefs("Sweet Tofu", 2, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    unav_pool = removefs("Udon", 2, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    unav_pool = removefs("Salad", 2, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    unav_pool = removefs("Napoleon Cake", 2, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    unav_pool = removefs("Brownie", 2, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    unav_pool = removefs("Sukiyaki", 2, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    unav_pool = removefs("Tangyuan", 2, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    unav_pool = removefs("Steak", 2, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    unav_pool = removefs("Escargot", 2, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    unav_pool = removefs("Chocolate", 2, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    unav_pool = removefs("Tiramisu", 2, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    unav_pool = removefs("Miso Soup", 3, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    unav_pool = removefs("Ume Ochazuke", 3, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    unav_pool = removefs("Orange Juice", 3, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    unav_pool = removefs("Jiuniang", 3, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    unav_pool = removefs("Eclair", 3, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    unav_pool = removefs("Tempura", 3, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    unav_pool = removefs("Sake", 3, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    unav_pool = removefs("Dorayaki", 3, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    unav_pool = removefs("Milk", 3, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    unav_pool = removefs("Tom Yum", 3, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    unav_pool = removefs("Sakuramochi", 3, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    unav_pool = removefs("Macaron", 3, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    unav_pool = removefs("Coffee", 3, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    unav_pool = removefs("Long Bao", 3, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    unav_pool = removefs("Jello", 4, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    unav_pool = removefs("Popcorn", 4, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    for e1 in range(134):
        eroll += ["Raindrop Cake"]
    for e2 in range(73):
        eroll += ["Bamboo Rice"]
    for e3 in range(128):
        eroll += ["Boston Lobster"]
    for e4 in range(370):
        eroll += ["Osmanthus Cake"]
        eroll += ["Sushi"]
        eroll += ["Moon Cake"]
    for e5 in range(314):
        eroll += ["Hotdog"]
        eroll += ["Mango Pudding"]
        eroll += ["Hamburger"]
        eroll += ["Sanma"]
        eroll += ["Red Wine"]
        eroll += ["Pastel de nata"]
        eroll += ["Yuxiang"]
    for e6 in range(426):
        eroll += ["Yellow Wine"]
        eroll += ["Omurice"]
        eroll += ["Cold Rice Shrimp"]
        eroll += ["Spicy Gluten"]
        eroll += ["Taiyaki"]
        eroll += ["Zongzi"]
        eroll += ["Sashimi"]
    for e7 in range(104):
        eroll += ["Skewer"]
        eroll += ["Pancake"]
    for e8 in range(21):
        eroll.remove("Crab Long Bao")
        eroll.remove("Gingerbread")
    for e9 in range(60):
        eroll.remove("Foie Gras")
        eroll.remove("Peking Duck")
        eroll.remove("B-52")
    for e10 in range(9):
        eroll.remove("Bibimbap")
    for e11 in range(5):
        eroll.remove("Double Scoop")
    for e12 in range(56):
        eroll.remove("Fried Chicken")
        eroll.remove("Milk Tea")
        eroll.remove("Yunnan Noodles")
        eroll.remove("Tiramisu")
        eroll.remove("Escargot")
        eroll.remove("Steak")
        eroll.remove("Tangyuan")
        eroll.remove("Napoleon Cake")
        eroll.remove("Salad")
        eroll.remove("Sukiyaki")
        eroll.remove("Brownie")
        eroll.remove("Gyoza")
        eroll.remove("Chocolate")
        eroll.remove("Udon")
        eroll.remove("Sweet Tofu")
        eroll.remove("Kimchi")
    for e13 in range(55):
        eroll.remove("Ddeokbokki")
    for e14 in range(106):
        eroll.remove("Eggette")
        eroll.remove("Pineapple Cake")
        eroll.remove("Laba Congee")
    for e15 in range(374):
        eroll.remove("Long Bao")
        eroll.remove("Coffee")
        eroll.remove("Macaron")
        eroll.remove("Sakuramochi")
        eroll.remove("Tom Yum")
        eroll.remove("Milk")
        eroll.remove("Dorayaki")
        eroll.remove("Sake")
        eroll.remove("Tempura")
        eroll.remove("Jiuniang")
        eroll.remove("Orange Juice")
        eroll.remove("Ume Ochazuke")
        eroll.remove("Miso Soup")
    for e16 in range(373):
        eroll.remove("Eclair")
    for e17 in range(46):
        eroll.remove("Jello")
    for e10 in range(47):
        eroll.remove("Popcorn")
    return eroll

def eventindexcheck(eroll, event_index, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool):
    if event_index == "0":
        eroll = index0entry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    elif event_index == "1":
        eroll = index1entry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    elif event_index == "2":
        eroll = index2entry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    elif event_index == "3":
        eroll = index3entry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    elif event_index == "4a":
        eroll = index4aentry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    elif event_index == "4b":
        eroll = index4bentry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    elif event_index == "5a":
        eroll = index5aentry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    elif event_index == "5b":
        eroll = index5bentry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    elif event_index == "6":
        eroll = index6entry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    elif event_index == "7":
        eroll = index7entry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    elif event_index == "8":
        eroll = index8entry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    elif event_index == "9":
        eroll = index9entry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    elif event_index == "10":
        eroll = index10entry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    elif event_index == "11a":
        eroll = index11aentry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    elif event_index == "11b":
        eroll = index11bentry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    elif event_index == "12":
        eroll = index12entry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    elif event_index == "13":
        eroll = index13entry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    elif event_index == "14":
        eroll = index14entry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    elif event_index == "15":
        eroll = index15entry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    elif event_index == "16":
        eroll = index16entry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    elif event_index == "17":
        eroll = index17entry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    elif event_index == "18a":
        eroll = index18aentry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    elif event_index == "18b":
        eroll = index18bentry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    elif event_index == "19":
        eroll = index19entry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    elif event_index == "20":
        eroll = index20entry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    elif event_index == "21":
        eroll = index21entry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    elif event_index == "22":
        eroll = index22entry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    elif event_index == "23":
        eroll = index23entry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    elif event_index == "24":
        eroll = index24entry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    elif event_index == "25":
        eroll = index25entry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    elif event_index == "26":
        eroll = index26entry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    else:
        eroll = []
    return eroll

def eventlist():
    sadded = " has been added to the summoning pool"
    padded = " have been added to the summoning pool"
    srateup = " has an inceased summoning rate"
    prateup = " have increased summoning rates"
    eventlist = [["0", "Sweet Temptations", "Chocolate and Popcorn" + padded + " permanently; Gingerbread and Chocolate also" + prateup, "25th July to 30th July 2018", "Gingerbread: 0.23% -> 1.2%\nChocolate: 0.83% -> 3.33%\nPopcorn: 0.47%"],
                 ["1", "Promise of Youth", "Pineapple Cake and Eggette" + padded + " permanently", "August 8th 2018 onwards", "Pineapple Cake: 1.51%\nEggette: 1.50%"],
                 ["2", "Brewing Fine Wine", "Toso and Sweet Tofu" + padded, "13th August to 19th August 2018", "Toso: 1.50%\nSweet Tofu: 6.61%"],
                 ["3", "Sakura Falls", "Strawberry Daifuku and Raindrop Cake" + padded, "4th September to 17th September 2018", "Raindrop Cake: 1.20%\nStrawberry Daifuku: 0.31%"],
                 ["4a", "Autumn Memories", "Milt and Bonito Rice" + padded, "1st October to 14th October 2018", "Milt: 0.48%\nBonito Rice: 0.96%"],
                 ["4b", "Autumn Memories", "Milt and Bonito Rice" + padded, "17th December to 26th December 2018", "Milt: 1.21%\nBonito Rice: 4.99%"],
                 ["5a", "Come Have a Chat", "Peking Duck" + srateup, "15th October to 22nd October 2018", "Peking Duck: 0.61% -> 1.50%"],
                 ["5b", "Let's Chat", "Peking Duck" + srateup, "1st December to 9th December 2018", "Peking Duck: 0.61 -> 1.50%"],
                 ["6", "Amusement Park Sign Up! I", "Cassata" + sadded + " and B-52" + srateup, "24th October to 26th October 2018", "B-52: 0.61% -> 1.20%\nCassata: 3.32%"],
                 ["7", "Amusement Park Sign Up! II", "Cassata" + sadded + " and Crab Long Bao" + srateup, "27th October to 29th October 2018", "Crab Long Bao: 0.36% -> 1.2%\nCassata: 3.32%"],
                 ["8", "Amusement Park Sign Up! III", "Cassata" + sadded + " and Double Scoop" + srateup, "30th October to 1st November 2018", "Double Scoop: 0.05% -> 0.30%\nCassata: 3.32%"],
                 ["9", "Amusement Park Sign Up! IV", "Cassata" + sadded + " and Bamboo Rice" + srateup, "2nd November to 4th November 2018", "Bamboo Rice: 0.62% -> 1.20%\nCassata: 3.32%"],
                 ["10", "Amusement Park Sign Up! V", "Toso and Cassata" + padded, "5th November to 7th November 2018", "Toso: 1.20%\nCassata: 3.32%"],
                 ["11a", "Candy Strike!", "Gingerbread" + srateup, "8th November to 15th November 2018", "Gingerbread: 0.23%% -> 1.50%"],
                 ["11b", "Candy Strike!", "Gingerbread" + srateup, "27th December 2018 to 2nd January 2019", "Gingerbread: 0.23%% -> 1.50%"],
                 ["12", "Seaside Moon", "Caviar and Seaweed Soup" + padded, "16th November to 30th November 2018", "Caviar: 1.21%\nSeaweed Soup: 4.98%"],
                 ["13", "Breezy Snacks", "Raindrop Cake" + sadded + " and Sanma" + srateup, "16th November to 30th November 2018", "Raindrop: 1.21%\nSanma: 0.72% -> 4.98%"],
                 ["14", "No Spice No Dice", "Sichuan Hotpot and Beer" + padded, "17th December to 26th December 2018", "Sichuan Hotpot: 1.21%\nBeer: 4.99%"]]
    eventlist2 = [["15", "Flavor Frenzy", "Bibimbap" + sadded + " permanently and" + srateup, "3rd January to 10th January 2019", "Bibimbap: 0.09% -> 1.21%"],
                  ["16", "Fragrant Garden: Champagne", "Champagne, Raindrop Cake, Bonito Rice and Beer" + padded + " and URs have an overall increased summoning rate", "11th January to 20 January 2019", "Champagne: 1.21%\nRaindrop Cake: 0.50%\nBonito Rice: 0.43%\nBeer: 0.43%\nURs: 3.01% -> 4.01%"],
                  ["17", "Fragrant Garden: Toso", "Toso, Milt, Strawberry Daifuku, Bonito Rice and Beer" + padded + " and URs have an overall increased summoning rate", "11th January to 20 January 2019", "Toso: 1.21%\nMilt: 0.50%\nStrawberry Daifuku: 0.47%\nBonito Rice: 0.43%\nBeer: 0.43%\nURs: 3.01% -> 4.01%"],
                  ["18a", "Flame Storm", "B-52" + srateup, "25th January to 31st January 2019", "B-52: 0.60% -> 1.20%"],
                  ["18b", "Flame Storm", "B-52" + srateup, "15th March to 21st March 2019", "B-52: 0.60% -> 1.20%"],
                  ["19", "Memories Revisited: Huangshan Maofeng Tea", "Huangshan Maofeng Tea, Fondant Cake and Osmanthus Cake" + padded, "1st February to 11th February 2019", "Huangshan Maofeng Tea: 1.20%\nFondant Cake: 0.58%\nOsmanthus Cake: 0.57%"],
                  ["20", "Memories Revisited: Caviar", "Caviar, Fondant Cake, Seaweed Soup and Strawberry Daifuku" + padded, "1st February to 11th February 2019", "Caviar: 1.20%\nFondant Cake: 0.58%\nSeaweed Soup: 0.57%\nStrawberry Daifuku: 0.46%"],
                  ["21", "Bamboo Forest Exploration", "Bamboo Rice" + srateup, "12th February to 17th February 2019", "Bamboo Rice: 0.60% -> 1.20%"],
                  ["22", "Savory Feast", "Ddeokbokki and Kimchi" + padded + " permamently and" + prateup, "18th February to 24th February 2019", "Ddeokbokki: 0.57% -> 3.32%\nKimchi: 0.57% -> 3.32%"],
                  ["23", "Training Time!", "Crab Long Bao" + srateup, "25th Feburary to 28th February 2019", "Crab Long Bao: 0.21% -> 1.20%"],
                  ["24", "Spring Feast", "Buddha's Temptation, Butter Tea, Milt, Mandarin Squirrel Fish and Green Curry" + padded, "1st March to 14th March 2019", "Buddha's Temptation: 1.20%\nButter Tea: 0.10%\nMilt: 0.10%\nMandarin Squirrel Fish: 4.98%\nGreen Curry: 0.43%"],
                  ["25", "Snack Time!", "Eclair and Fried Chicken" + padded + " permanently and" + prateup, "21st March to 29th March 2019", "Eclair: 3.73% -> 25.33%\nFried Chicken 0.56% -> 4.98%"],
                  ["26", "Meaningful Amber", "This event only contains Strength Food Souls, including Raindrop Cake, Osmanthus Cake, Moon Cake and Sushi. URs, SRs and Ms are also increased", "30th March to 5th April 2019", "Raindrop Cake: 1.34%\nOsmanthus Cake: 3.70%\nMooncake: 3.70%\nSushi: 3.70%\nURs: 3.01% -> 4.00%\nSRs: 16.61% -> 37.00%\nMs: 1.85% -> 3.00%"]]
    return eventlist, eventlist2
