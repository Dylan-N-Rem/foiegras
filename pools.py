ur_pool = ["Bamboo Rice", "Foie Gras", "Peking Duck", "B-52", "Gingerbread", "Crab Long Bao", "Dragon's Beard Candy", "Rum", "Bibimbap", "Double Scoop", "Boston Lobster"]
sr_pool = ["Pineapple Bun", "Fried Chicken", "Pineapple Cake", "Eggette", "Laba Congee", "Milk Tea", "Yunnan Noodles", "Escargot", "Hotdog", "Hamburger", "Steak", "Tangyuan", "Sanma", "Sukiyaki", "Brownie", "Napoleon Cake", "Salad", "Pastel de nata", "Yuxiang", "Tiramisu", "Mango Pudding", "Red Wine", "Gyoza", "Chocolate", "Udon", "Sweet Tofu", "Ddeokbokki", "Kimchi"]
r_pool = ["Long Bao", "Coffee", "Sashimi", "Cold Rice Shrimp", "Macaron", "Zongzi", "Sakuramochi", "Tom Yum", "Taiyaki", "Milk", "Dorayaki", "Sake", "Tempura", "Spicy Gluten", "Jiuniang", "Omurice", "Orange Juice", "Ume Ochazuke", "Miso Soup", "Yellow Wine", "Eclair"]
m_pool = ["Skewer", "Jello", "Pancake", "Popcorn"]
summon_pool = ur_pool + sr_pool + r_pool + m_pool

nur_pool = ["Cloud Tea", "Canele", "Pizza", "Apple Pie", "Nagashi Somen", "Mapo Tofu"]
nsr_pool = ["Black Tea", "Lion's Head", "American Corn Bread", "Qingtuan", "Eggnog", "Zitui Bun", "Salty Tofu", "Spaghetti", "Donut", "Tortoise Jelly", "Sweet & Sour Fish", "Beggar's Chicken", "Mung Bean Soup", "Bloody Mary", "Vodka", "Wonton", "Yogurt", "Surstromming"]
nr_pool = ["Nasi Lemak", "Cola", "Plum Juice", "Crepe"]
nm_pool = ["Hawthorne Ball", "Rice", "Cheese", "Toast"]
none_pool = nur_pool + nsr_pool + nr_pool + nm_pool

eur_pool = ["Stargazy Pie", "Osechi", "Buddha's Temptation", "Turkey", "Butter Tea", "Huangshan Maofeng Tea", "Champagne", "Sichuan Hotpot", "Toso", "Raindrop Cake", "Milt", "Caviar"]
esr_pool = ["Black Pudding", "Unadon", "Mandarin Squirrel Fish", "Green Curry", "Cassata", "Bonito Rice", "Seaweed Soup", "Beer", "Moon Cake", "Sushi", "Osmanthus Cake", "Fondant Cake"]
em_pool = ["Pudding", "Sandwich", "Strawberry Daifuku"]
event_pool = eur_pool + esr_pool + em_pool

unre_pool = ["Whiskey", "Oyster"]

all_pool = summon_pool + none_pool + event_pool
all_ur = ur_pool + nur_pool + eur_pool
all_sr = sr_pool + nsr_pool + esr_pool
all_r = r_pool + nr_pool
all_m = m_pool + nm_pool + em_pool
