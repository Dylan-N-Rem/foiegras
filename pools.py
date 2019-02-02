def ur_pool():
    ur_pool = ["Bamboo Rice", "Foie Gras", "Peking Duck", "B-52", "Gingerbread", "Crab Long Bao", "Bibimbap", "Double Scoop", "Boston Lobster"]
    return ur_pool

def sr_pool():
    sr_pool = ["Pineapple Cake", "Eggette", "Laba Congee", "Milk Tea", "Yunnan Noodles", "Escargot", "Hotdog", "Hamburger", "Steak", "Tangyuan", "Sanma", "Sukiyaki", "Brownie", "Napoleon Cake", "Salad", "Pastel de nata", "Yuxiang", "Tiramisu", "Mango Pudding", "Red Wine", "Gyoza", "Chocolate", "Sweet Tofu", "Udon"]
    return sr_pool

def r_pool():
    r_pool = ["Long Bao", "Coffee", "Sashimi", "Cold Rice Shrimp", "Macaron", "Zongzi", "Sakuramochi", "Tom Yum", "Taiyaki", "Milk", "Dorayaki", "Sake", "Tempura", "Spicy Gluten", "Jiuniang", "Omurice", "Orange Juice", "Ume Ochazuke", "Miso Soup", "Yellow Wine"]
    return r_pool

def m_pool():
    m_pool = ["Skewer", "Jello", "Pancake", "Popcorn"]
    return m_pool

def summon_pool():
    summon_pool = ur_pool() + sr_pool() + r_pool() + m_pool()
    return summon_pool

def none_pool():
    none_pool = ["Cloud Tea", "Canele", "Pizza", "Turkey", "Apple Pie", "Black Tea", "Eggnog", "Mooncake", "Salty Tofu", "Spaghetti", "Donut", "Sushi", "Tortoise Jelly", "Sweet & Sour Fish", "Beggar's Chicken", "Mung Bean Soup", "Bloody Mary", "Vodka", "Wonton", "Yogurt", "Cola", "Plum Juice", "Crepe", "Rice", "Cheese", "Toast"]
    return none_pool

def event_pool():
    event_pool = ["Huangshan Maofeng Tea", "Champagne", "Sichuan Hotpot", "Toso", "Raindrop Cake", "Milt", "Cassata", "Caviar", "Bonito Rice", "Seaweed Soup", "Beer", "Osmanthus Cake", "Fondant Cake", "Strawberry Daifuku"]
    return event_pool

def unre_pool():
    unre_pool = ["Eclair Puff", "Green Curry", "Matcha Rice"]
    return unre_pool
