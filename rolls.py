def setrate(roll, rate, fslist):
    for fscount in fslist:
        for fsrate in range(rate):
            roll += [fscount]
    return roll

roll0 = []
for u01 in range(23):
    roll0 += ["Crab Long Bao"]
    roll0 += ["Gingerbread"]
for u02 in range(61):
    roll0 += ["Bamboo Rice"]
    roll0 += ["Peking Duck"]
    roll0 += ["B-52"]
for u03 in range(62):
    roll0 += ["Foie Gras"]
for uf4 in range(5):
    roll0 += ["Boston Lobster"]
    roll0 += ["Double Scoop"]
for s01 in range(103):
    roll0 += ["Tiramisu"]
    roll0 += ["Escargot"]
    roll0 += ["Hotdog"]
for s02 in range(104):
    roll0 += ["Mango Pudding"]
    roll0 += ["Hamburger"]
    roll0 += ["Steak"]
    roll0 += ["Tangyuan"]
    roll0 += ["Sanma"]
    roll0 += ["Napoleon Cake"]
    roll0 += ["Salad"]
    roll0 += ["Pastel de nata"]
    roll0 += ["Yuxiang"]
    roll0 += ["Sukiyaki"]
    roll0 += ["Brownie"]
    roll0 += ["Red Wine"]
    roll0 += ["Gyoza"]
for r01 in range(413):
    roll0 += ["Long Bao"]
    roll0 += ["Coffee"]
    roll0 += ["Sashimi"]
    roll0 += ["Macaron"]
    roll0 += ["Zongzi"]
    roll0 += ["Sakuramochi"]
    roll0 += ["Tom Yum"]
    roll0 += ["Taiyaki"]
    roll0 += ["Milk"]
    roll0 += ["Dorayaki"]
    roll0 += ["Sake"]
    roll0 += ["Tempura"]
    roll0 += ["Spicy Gluten"]
for r02 in range(414):
    roll0 += ["Jiuniang"]
    roll0 += ["Omurice"]
    roll0 += ["Orange Juice"]
    roll0 += ["Ume Ochazuke"]
    roll0 += ["Miso Soup"]
    roll0 += ["Yellow Wine"]
for m01 in range(62):
    roll0 += ["Pancake"]
    roll0 += ["Jello"]
for m02 in range(61):
    roll0 += ["Skewer"]

roll1 = []
for u11 in range(23):
    roll1 += ["Crab Long Bao"]
    roll1 += ["Gingerbread"]
for u12 in range(61):
    roll1 += ["Foie Gras"]
    roll1 += ["Peking Duck"]
    roll1 += ["B-52"]
for u13 in range(62):
    roll1 += ["Bamboo Rice"]
for u14 in range(5):
    roll1 += ["Boston Lobster"]
    roll1 += ["Double Scoop"]
for s11 in range(83):
    roll1 += ["Tiramisu"]
    roll1 += ["Escargot"]
    roll1 += ["Hotdog"]
    roll1 += ["Mango Pudding"]
    roll1 += ["Hamburger"]
    roll1 += ["Steak"]
    roll1 += ["Tangyuan"]
    roll1 += ["Sanma"]
    roll1 += ["Napoleon Cake"]
    roll1 += ["Salad"]
    roll1 += ["Pastel de nata"]
    roll1 += ["Yuxiang"]
    roll1 += ["Sukiyaki"]
    roll1 += ["Brownie"]
    roll1 += ["Red Wine"]
    roll1 += ["Gyoza"]
    roll1 += ["Chocolate"]
for r11 in range(413):
    roll1 += ["Long Bao"]
    roll1 += ["Coffee"]
    roll1 += ["Sashimi"]
    roll1 += ["Macaron"]
    roll1 += ["Zongzi"]
    roll1 += ["Sakuramochi"]
    roll1 += ["Tom Yum"]
    roll1 += ["Taiyaki"]
    roll1 += ["Milk"]
    roll1 += ["Dorayaki"]
    roll1 += ["Sake"]
    roll1 += ["Tempura"]
    roll1 += ["Spicy Gluten"]
for r12 in range(414):
    roll1 += ["Jiuniang"]
    roll1 += ["Omurice"]
    roll1 += ["Orange Juice"]
    roll1 += ["Ume Ochazuke"]
    roll1 += ["Miso Soup"]
    roll1 += ["Yellow Wine"]
for m11 in range(46):
    roll1 += ["Skewer"]
    roll1 += ["Jello"]
    roll1 += ["Pancake"]
for m12 in range(47):
    roll1 += ["Popcorn"]

roll2 = []
for u21 in range(23):
    roll2 += ["Crab Long Bao"]
    roll2 += ["Gingerbread"]
for u22 in range(61):
    roll2 += ["Foie Gras"]
    roll2 += ["Peking Duck"]
    roll2 += ["B-52"]
for u23 in range(62):
    roll2 += ["Bamboo Rice"]
for u24 in range(5):
    roll2 += ["Boston Lobster"]
    roll2 += ["Double Scoop"]
for s21 in range(80):
    roll2 += ["Tiramisu"]
    roll2 += ["Escargot"]
    roll2 += ["Hotdog"]
    roll2 += ["Mango Pudding"]
    roll2 += ["Hamburger"]
    roll2 += ["Steak"]
    roll2 += ["Tangyuan"]
    roll2 += ["Sanma"]
    roll2 += ["Napoleon Cake"]
    roll2 += ["Salad"]
    roll2 += ["Pastel de nata"]
    roll2 += ["Yuxiang"]
    roll2 += ["Sukiyaki"]
    roll2 += ["Brownie"]
    roll2 += ["Red Wine"]
    roll2 += ["Gyoza"]
    roll2 += ["Chocolate"]
for s22 in range(150):
    roll2 += ["Eggette"]
for s23 in range(151):
    roll2 += ["Pineapple Cake"]
for r21 in range(413):
    roll2 += ["Long Bao"]
    roll2 += ["Coffee"]
    roll2 += ["Sashimi"]
    roll2 += ["Macaron"]
    roll2 += ["Zongzi"]
    roll2 += ["Sakuramochi"]
    roll2 += ["Tom Yum"]
    roll2 += ["Taiyaki"]
    roll2 += ["Milk"]
    roll2 += ["Dorayaki"]
    roll2 += ["Sake"]
    roll2 += ["Tempura"]
    roll2 += ["Spicy Gluten"]
for r22 in range(414):
    roll2 += ["Jiuniang"]
    roll2 += ["Omurice"]
    roll2 += ["Orange Juice"]
    roll2 += ["Ume Ochazuke"]
    roll2 += ["Miso Soup"]
    roll2 += ["Yellow Wine"]
for m21 in range(46):
    roll2 += ["Skewer"]
    roll2 += ["Jello"]
    roll2 += ["Pancake"]
for m22 in range(47):
    roll2 += ["Popcorn"]

roll3 = []
for u31 in range(23):
    roll3 += ["Crab Long Bao"]
    roll3 += ["Gingerbread"]
for u32 in range(61):
    roll3 += ["Foie Gras"]
    roll3 += ["Peking Duck"]
    roll3 += ["B-52"]
for u33 in range(62):
    roll3 += ["Bamboo Rice"]
for u34 in range(5):
    roll3 += ["Boston Lobster"]
    roll3 += ["Double Scoop"]
for s31 in range(76):
    roll3 += ["Tiramisu"]
    roll3 += ["Escargot"]
    roll3 += ["Hotdog"]
    roll3 += ["Mango Pudding"]
    roll3 += ["Hamburger"]
    roll3 += ["Steak"]
    roll3 += ["Tangyuan"]
    roll3 += ["Sanma"]
    roll3 += ["Napoleon Cake"]
    roll3 += ["Salad"]
    roll3 += ["Pastel de nata"]
    roll3 += ["Yuxiang"]
    roll3 += ["Sukiyaki"]
    roll3 += ["Brownie"]
    roll3 += ["Red Wine"]
    roll3 += ["Gyoza"]
    roll3 += ["Chocolate"]
    roll3 += ["Udon"]
for s32 in range(146):
    roll3 += ["Eggette"]
for s33 in range(147):
    roll3 += ["Pineapple Cake"]
for r31 in range(413):
    roll3 += ["Long Bao"]
    roll3 += ["Coffee"]
    roll3 += ["Sashimi"]
    roll3 += ["Macaron"]
    roll3 += ["Zongzi"]
    roll3 += ["Sakuramochi"]
    roll3 += ["Tom Yum"]
    roll3 += ["Taiyaki"]
    roll3 += ["Milk"]
    roll3 += ["Dorayaki"]
    roll3 += ["Sake"]
    roll3 += ["Tempura"]
    roll3 += ["Spicy Gluten"]
for r32 in range(414):
    roll3 += ["Jiuniang"]
    roll3 += ["Omurice"]
    roll3 += ["Orange Juice"]
    roll3 += ["Ume Ochazuke"]
    roll3 += ["Miso Soup"]
    roll3 += ["Yellow Wine"]
for m31 in range(46):
    roll3 += ["Skewer"]
    roll3 += ["Jello"]
    roll3 += ["Pancake"]
for m32 in range(47):
    roll3 += ["Popcorn"]

roll4 = []
for u41 in range(23):
    roll4 += ["Crab Long Bao"]
    roll4 += ["Gingerbread"]
for u42 in range(61):
    roll4 += ["Foie Gras"]
    roll4 += ["Peking Duck"]
    roll4 += ["B-52"]
for u43 in range(62):
    roll4 += ["Bamboo Rice"]
for u44 in range(5):
    roll4 += ["Boston Lobster"]
    roll4 += ["Double Scoop"]
for s41 in range(72):
    roll4 += ["Tiramisu"]
    roll4 += ["Escargot"]
    roll4 += ["Hotdog"]
    roll4 += ["Mango Pudding"]
    roll4 += ["Hamburger"]
    roll4 += ["Steak"]
    roll4 += ["Tangyuan"]
    roll4 += ["Sanma"]
    roll4 += ["Napoleon Cake"]
    roll4 += ["Salad"]
    roll4 += ["Pastel de nata"]
    roll4 += ["Yuxiang"]
    roll4 += ["Sukiyaki"]
    roll4 += ["Brownie"]
    roll4 += ["Red Wine"]
    roll4 += ["Gyoza"]
    roll4 += ["Chocolate"]
    roll4 += ["Udon"]
    roll4 += ["Sweet Tofu"]
for s42 in range(146):
    roll4 += ["Eggette"]
for s43 in range(147):
    roll4 += ["Pineapple Cake"]
for r41 in range(413):
    roll4 += ["Long Bao"]
    roll4 += ["Coffee"]
    roll4 += ["Sashimi"]
    roll4 += ["Macaron"]
    roll4 += ["Zongzi"]
    roll4 += ["Sakuramochi"]
    roll4 += ["Tom Yum"]
    roll4 += ["Taiyaki"]
    roll4 += ["Milk"]
    roll4 += ["Dorayaki"]
    roll4 += ["Sake"]
    roll4 += ["Tempura"]
    roll4 += ["Spicy Gluten"]
for r42 in range(414):
    roll4 += ["Jiuniang"]
    roll4 += ["Omurice"]
    roll4 += ["Orange Juice"]
    roll4 += ["Ume Ochazuke"]
    roll4 += ["Miso Soup"]
    roll4 += ["Yellow Wine"]
for m41 in range(46):
    roll4 += ["Skewer"]
    roll4 += ["Jello"]
    roll4 += ["Pancake"]
for m42 in range(47):
    roll4 += ["Popcorn"]

roll5 = []
for u51 in range(23):
    roll5 += ["Crab Long Bao"]
    roll5 += ["Gingerbread"]
for u52 in range(61):
    roll5 += ["Foie Gras"]
    roll5 += ["Peking Duck"]
    roll5 += ["B-52"]
for u53 in range(62):
    roll5 += ["Bamboo Rice"]
for u54 in range(5):
    roll5 += ["Boston Lobster"]
    roll5 += ["Double Scoop"]
for s51 in range(72):
    roll5 += ["Tiramisu"]
    roll5 += ["Escargot"]
    roll5 += ["Hotdog"]
    roll5 += ["Mango Pudding"]
    roll5 += ["Hamburger"]
    roll5 += ["Steak"]
    roll5 += ["Tangyuan"]
    roll5 += ["Sanma"]
    roll5 += ["Napoleon Cake"]
    roll5 += ["Salad"]
    roll5 += ["Pastel de nata"]
    roll5 += ["Yuxiang"]
    roll5 += ["Sukiyaki"]
    roll5 += ["Brownie"]
    roll5 += ["Red Wine"]
    roll5 += ["Gyoza"]
    roll5 += ["Chocolate"]
    roll5 += ["Udon"]
    roll5 += ["Sweet Tofu"]
for s52 in range(146):
    roll5 += ["Eggette"]
for s53 in range(147):
    roll5 += ["Pineapple Cake"]
for r51 in range(392):
    roll5 += ["Long Bao"]
    roll5 += ["Coffee"]
    roll5 += ["Sashimi"]
    roll5 += ["Macaron"]
    roll5 += ["Zongzi"]
    roll5 += ["Sakuramochi"]
    roll5 += ["Cold Rice Shrimp"]
for r52 in range(393):
    roll5 += ["Tom Yum"]
    roll5 += ["Taiyaki"]
    roll5 += ["Milk"]
    roll5 += ["Dorayaki"]
    roll5 += ["Sake"]
    roll5 += ["Tempura"]
    roll5 += ["Spicy Gluten"]
    roll5 += ["Jiuniang"]
    roll5 += ["Omurice"]
    roll5 += ["Orange Juice"]
    roll5 += ["Ume Ochazuke"]
    roll5 += ["Miso Soup"]
    roll5 += ["Yellow Wine"]
for m51 in range(46):
    roll5 += ["Skewer"]
    roll5 += ["Jello"]
    roll5 += ["Pancake"]
for m52 in range(47):
    roll5 += ["Popcorn"]

roll6 = []
for u61 in range(13):
    roll6 += ["Crab Long Bao"]
    roll6 += ["Gingerbread"]
for u62 in range(36):
    roll6 += ["Foie Gras"]
    roll6 += ["Peking Duck"]
    roll6 += ["B-52"]
    roll6 += ["Bamboo Rice"]
for u63 in range(5):
    roll6 += ["Boston Lobster"]
    roll6 += ["Double Scoop"]
for s61 in range(46):
    roll6 += ["Tiramisu"]
    roll6 += ["Escargot"]
    roll6 += ["Hotdog"]
    roll6 += ["Mango Pudding"]
    roll6 += ["Hamburger"]
    roll6 += ["Steak"]
    roll6 += ["Tangyuan"]
    roll6 += ["Sanma"]
    roll6 += ["Napoleon Cake"]
    roll6 += ["Salad"]
    roll6 += ["Pastel de nata"]
    roll6 += ["Yuxiang"]
    roll6 += ["Sukiyaki"]
    roll6 += ["Brownie"]
    roll6 += ["Red Wine"]
    roll6 += ["Gyoza"]
    roll6 += ["Chocolate"]
    roll6 += ["Udon"]
    roll6 += ["Sweet Tofu"]
    roll6 += ["Milk Tea"]
    roll6 += ["Yunnan Noodles"]
for s62 in range(98):
    roll6 += ["Eggette"]
    roll6 += ["Pineapple Cake"]
for r61 in range(392):
    roll6 += ["Long Bao"]
    roll6 += ["Coffee"]
    roll6 += ["Sashimi"]
    roll6 += ["Macaron"]
    roll6 += ["Zongzi"]
    roll6 += ["Sakuramochi"]
    roll6 += ["Cold Rice Shrimp"]
for r62 in range(393):
    roll6 += ["Tom Yum"]
    roll6 += ["Taiyaki"]
    roll6 += ["Milk"]
    roll6 += ["Dorayaki"]
    roll6 += ["Sake"]
    roll6 += ["Tempura"]
    roll6 += ["Spicy Gluten"]
    roll6 += ["Jiuniang"]
    roll6 += ["Omurice"]
    roll6 += ["Orange Juice"]
    roll6 += ["Ume Ochazuke"]
    roll6 += ["Miso Soup"]
    roll6 += ["Yellow Wine"]
for m61 in range(46):
    roll6 += ["Skewer"]
    roll6 += ["Jello"]
    roll6 += ["Pancake"]
for m62 in range(47):
    roll6 += ["Popcorn"]

roll7 = []
for u71 in range(23):
    roll7 += ["Crab Long Bao"]
    roll7 += ["Gingerbread"]
for u72 in range(61):
    roll7 += ["Foie Gras"]
    roll7 += ["Peking Duck"]
    roll7 += ["B-52"]
for u73 in range(62):
    roll7 += ["Bamboo Rice"]
for u74 in range(5):
    roll7 += ["Boston Lobster"]
    roll7 += ["Double Scoop"]
for s71 in range(62):
    roll7 += ["Tiramisu"]
    roll7 += ["Escargot"]
    roll7 += ["Hotdog"]
    roll7 += ["Mango Pudding"]
    roll7 += ["Hamburger"]
    roll7 += ["Steak"]
    roll7 += ["Tangyuan"]
    roll7 += ["Sanma"]
    roll7 += ["Napoleon Cake"]
    roll7 += ["Salad"]
    roll7 += ["Pastel de nata"]
    roll7 += ["Yuxiang"]
    roll7 += ["Sukiyaki"]
    roll7 += ["Brownie"]
    roll7 += ["Red Wine"]
    roll7 += ["Gyoza"]
    roll7 += ["Chocolate"]
    roll7 += ["Udon"]
for s72 in range(61):
    roll7 += ["Sweet Tofu"]
for s73 in range(65):
    roll7 += ["Milk Tea"]
    roll7 += ["Yunnan Noodles"]
for s74 in range(118):
    roll7 += ["Eggette"]
    roll7 += ["Pineapple Cake"]
    roll7 += ["Laba Congee"]
for r71 in range(392):
    roll7 += ["Long Bao"]
    roll7 += ["Coffee"]
    roll7 += ["Sashimi"]
    roll7 += ["Macaron"]
    roll7 += ["Zongzi"]
    roll7 += ["Sakuramochi"]
    roll7 += ["Cold Rice Shrimp"]
for r72 in range(393):
    roll7 += ["Tom Yum"]
    roll7 += ["Taiyaki"]
    roll7 += ["Milk"]
    roll7 += ["Dorayaki"]
    roll7 += ["Sake"]
    roll7 += ["Tempura"]
    roll7 += ["Spicy Gluten"]
    roll7 += ["Jiuniang"]
    roll7 += ["Omurice"]
    roll7 += ["Orange Juice"]
    roll7 += ["Ume Ochazuke"]
    roll7 += ["Miso Soup"]
    roll7 += ["Yellow Wine"]
for m71 in range(46):
    roll7 += ["Skewer"]
    roll7 += ["Jello"]
    roll7 += ["Pancake"]
for m72 in range(47):
    roll7 += ["Popcorn"]

roll8 = []
for u81 in range(21):
    roll8 += ["Crab Long Bao"]
    roll8 += ["Gingerbread"]
for u82 in range(60):
    roll8 += ["Foie Gras"]
    roll8 += ["Peking Duck"]
    roll8 += ["B-52"]
    roll8 += ["Bamboo Rice"]
for u83 in range(9):
    roll8 += ["Bibimbap"]
for u84 in range(5):
    roll8 += ["Boston Lobster"]
    roll8 += ["Double Scoop"]
for s81 in range(62):
    roll8 += ["Tiramisu"]
    roll8 += ["Escargot"]
    roll8 += ["Hotdog"]
    roll8 += ["Mango Pudding"]
    roll8 += ["Hamburger"]
    roll8 += ["Steak"]
    roll8 += ["Tangyuan"]
    roll8 += ["Sanma"]
    roll8 += ["Napoleon Cake"]
    roll8 += ["Salad"]
    roll8 += ["Pastel de nata"]
    roll8 += ["Yuxiang"]
    roll8 += ["Sukiyaki"]
    roll8 += ["Brownie"]
    roll8 += ["Red Wine"]
    roll8 += ["Gyoza"]
    roll8 += ["Chocolate"]
    roll8 += ["Udon"]
for s82 in range(61):
    roll8 += ["Sweet Tofu"]
for s83 in range(65):
    roll8 += ["Milk Tea"]
    roll8 += ["Yunnan Noodles"]
for s84 in range(118):
    roll8 += ["Eggette"]
    roll8 += ["Pineapple Cake"]
    roll8 += ["Laba Congee"]
for r81 in range(392):
    roll8 += ["Long Bao"]
    roll8 += ["Coffee"]
    roll8 += ["Sashimi"]
    roll8 += ["Macaron"]
    roll8 += ["Zongzi"]
    roll8 += ["Sakuramochi"]
    roll8 += ["Cold Rice Shrimp"]
for r82 in range(393):
    roll8 += ["Tom Yum"]
    roll8 += ["Taiyaki"]
    roll8 += ["Milk"]
    roll8 += ["Dorayaki"]
    roll8 += ["Sake"]
    roll8 += ["Tempura"]
    roll8 += ["Spicy Gluten"]
    roll8 += ["Jiuniang"]
    roll8 += ["Omurice"]
    roll8 += ["Orange Juice"]
    roll8 += ["Ume Ochazuke"]
    roll8 += ["Miso Soup"]
    roll8 += ["Yellow Wine"]
for m81 in range(46):
    roll8 += ["Skewer"]
    roll8 += ["Jello"]
    roll8 += ["Pancake"]
for m82 in range(47):
    roll8 += ["Popcorn"]

roll9 = []
for u91 in range(21):
    roll9 += ["Crab Long Bao"]
    roll9 += ["Gingerbread"]
for u92 in range(60):
    roll9 += ["Foie Gras"]
    roll9 += ["Peking Duck"]
    roll9 += ["B-52"]
    roll9 += ["Bamboo Rice"]
for u93 in range(9):
    roll9 += ["Bibimbap"]
for u94 in range(5):
    roll9 += ["Boston Lobster"]
    roll9 += ["Double Scoop"]
for s91 in range(58):
    roll9 += ["Milk Tea"]
    roll9 += ["Yunnan Noodles"]
    roll9 += ["Tiramisu"]
    roll9 += ["Escargot"]
    roll9 += ["Hotdog"]
    roll9 += ["Mango Pudding"]
    roll9 += ["Hamburger"]
    roll9 += ["Steak"]
    roll9 += ["Tangyuan"]
    roll9 += ["Sanma"]
    roll9 += ["Napoleon Cake"]
    roll9 += ["Salad"]
    roll9 += ["Pastel de nata"]
    roll9 += ["Yuxiang"]
    roll9 += ["Sukiyaki"]
    roll9 += ["Brownie"]
    roll9 += ["Red Wine"]
    roll9 += ["Gyoza"]
    roll9 += ["Chocolate"]
    roll9 += ["Udon"]
for s92 in range(57):
    roll9 += ["Sweet Tofu"]
    roll9 += ["Kimchi"]
    roll9 += ["Ddeokbokki"]
for s93 in range(110):
    roll9 += ["Eggette"]
    roll9 += ["Pineapple Cake"]
    roll9 += ["Laba Congee"]
for r91 in range(392):
    roll9 += ["Long Bao"]
    roll9 += ["Coffee"]
    roll9 += ["Sashimi"]
    roll9 += ["Macaron"]
    roll9 += ["Zongzi"]
    roll9 += ["Sakuramochi"]
    roll9 += ["Cold Rice Shrimp"]
for r92 in range(393):
    roll9 += ["Tom Yum"]
    roll9 += ["Taiyaki"]
    roll9 += ["Milk"]
    roll9 += ["Dorayaki"]
    roll9 += ["Sake"]
    roll9 += ["Tempura"]
    roll9 += ["Spicy Gluten"]
    roll9 += ["Jiuniang"]
    roll9 += ["Omurice"]
    roll9 += ["Orange Juice"]
    roll9 += ["Ume Ochazuke"]
    roll9 += ["Miso Soup"]
    roll9 += ["Yellow Wine"]
for m91 in range(46):
    roll9 += ["Skewer"]
    roll9 += ["Jello"]
    roll9 += ["Pancake"]
for m92 in range(47):
    roll9 += ["Popcorn"]

roll10 = []
for u101 in range(21):
    roll10 += ["Crab Long Bao"]
    roll10 += ["Gingerbread"]
for u102 in range(60):
    roll10 += ["Foie Gras"]
    roll10 += ["Peking Duck"]
    roll10 += ["B-52"]
    roll10 += ["Bamboo Rice"]
for u103 in range(9):
    roll10 += ["Bibimbap"]
for u104 in range(5):
    roll10 += ["Boston Lobster"]
    roll10 += ["Double Scoop"]
for s101 in range(56):
    roll10 += ["Fried Chicken"]
    roll10 += ["Milk Tea"]
    roll10 += ["Yunnan Noodles"]
    roll10 += ["Tiramisu"]
    roll10 += ["Escargot"]
    roll10 += ["Hotdog"]
    roll10 += ["Mango Pudding"]
    roll10 += ["Hamburger"]
    roll10 += ["Steak"]
    roll10 += ["Tangyuan"]
    roll10 += ["Sanma"]
    roll10 += ["Napoleon Cake"]
    roll10 += ["Salad"]
    roll10 += ["Pastel de nata"]
    roll10 += ["Yuxiang"]
    roll10 += ["Sukiyaki"]
    roll10 += ["Brownie"]
    roll10 += ["Red Wine"]
    roll10 += ["Gyoza"]
    roll10 += ["Chocolate"]
    roll10 += ["Udon"]
    roll10 += ["Sweet Tofu"]
    roll10 += ["Kimchi"]
for s102 in range(55):
    roll10 += ["Ddeokbokki"]
for s103 in range(106):
    roll10 += ["Eggette"]
    roll10 += ["Pineapple Cake"]
    roll10 += ["Laba Congee"]
for r101 in range(374):
    roll10 += ["Long Bao"]
    roll10 += ["Coffee"]
    roll10 += ["Sashimi"]
    roll10 += ["Macaron"]
    roll10 += ["Zongzi"]
    roll10 += ["Sakuramochi"]
    roll10 += ["Cold Rice Shrimp"]
    roll10 += ["Tom Yum"]
    roll10 += ["Taiyaki"]
    roll10 += ["Milk"]
    roll10 += ["Dorayaki"]
    roll10 += ["Sake"]
    roll10 += ["Tempura"]
    roll10 += ["Spicy Gluten"]
    roll10 += ["Jiuniang"]
    roll10 += ["Omurice"]
    roll10 += ["Orange Juice"]
    roll10 += ["Ume Ochazuke"]
    roll10 += ["Miso Soup"]
    roll10 += ["Yellow Wine"]
for r102 in range(373):
    roll10 += ["Eclair"]
for m101 in range(46):
    roll10 += ["Skewer"]
    roll10 += ["Jello"]
    roll10 += ["Pancake"]
for m102 in range(47):
    roll10 += ["Popcorn"]

roll11 = []
for u111 in range(18):
    roll11 += ["Crab Long Bao"]
    roll11 += ["Gingerbread"]
for u112 in range(9):
    roll11 += ["Bibimbap"]
for u113 in range(5):
    roll11 += ["Boston Lobster"]
    roll11 += ["Double Scoop"]
for u114 in range(17):
    roll11 += ["Rum"]
    roll11 += ["Dragon's Beard Candy"]
for s111 in range(106):
    roll11 += ["Eggette"]
    roll11 += ["Pineapple Cake"]
    roll11 += ["Laba Congee"]
for s112 in range(54):
    roll11 += ["Fried Chicken"]
    roll11 += ["Milk Tea"]
    roll11 += ["Yunnan Noodles"]
    roll11 += ["Tiramisu"]
    roll11 += ["Escargot"]
    roll11 += ["Hotdog"]
    roll11 += ["Mango Pudding"]
    roll11 += ["Hamburger"]
    roll11 += ["Steak"]
    roll11 += ["Tangyuan"]
    roll11 += ["Sanma"]
    roll11 += ["Napoleon Cake"]
    roll11 += ["Salad"]
    roll11 += ["Pastel de nata"]
    roll11 += ["Yuxiang"]
    roll11 += ["Sukiyaki"]
    roll11 += ["Brownie"]
    roll11 += ["Red Wine"]
for us113 in range(53):
    roll11 += ["Foie Gras"]
    roll11 += ["Peking Duck"]
    roll11 += ["B-52"]
    roll11 += ["Bamboo Rice"]
    roll11 += ["Gyoza"]
    roll11 += ["Chocolate"]
    roll11 += ["Udon"]
    roll11 += ["Sweet Tofu"]
    roll11 += ["Kimchi"]
    roll11 += ["Ddeokbokki"]
    roll11 += ["Pineapple Bun"]
for r111 in range(374):
    roll11 += ["Long Bao"]
    roll11 += ["Coffee"]
    roll11 += ["Sashimi"]
    roll11 += ["Macaron"]
    roll11 += ["Zongzi"]
    roll11 += ["Sakuramochi"]
    roll11 += ["Cold Rice Shrimp"]
    roll11 += ["Tom Yum"]
    roll11 += ["Taiyaki"]
    roll11 += ["Milk"]
    roll11 += ["Dorayaki"]
    roll11 += ["Sake"]
    roll11 += ["Tempura"]
    roll11 += ["Spicy Gluten"]
    roll11 += ["Jiuniang"]
    roll11 += ["Omurice"]
    roll11 += ["Orange Juice"]
    roll11 += ["Ume Ochazuke"]
    roll11 += ["Miso Soup"]
    roll11 += ["Yellow Wine"]
for r112 in range(373):
    roll11 += ["Eclair"]
for m111 in range(46):
    roll11 += ["Skewer"]
    roll11 += ["Jello"]
    roll11 += ["Pancake"]
for m112 in range(47):
    roll11 += ["Popcorn"]

roll12 = []
roll12 = setrate(roll12, 5, ["Double Scoop", "Boston Lobster"])
roll12 = setrate(roll12, 9, ["Bibimbap"])
roll12 = setrate(roll12, 17, ["Rum", "Dragon's Beard Candy"])
roll12 = setrate(roll12, 18, ["Crab Long Bao", "Gingerbread"])
roll12 = setrate(roll12, 46, ["Jello", "Pancake", "Skewer"])
roll12 = setrate(roll12, 47, ["Popcorn"])
roll12 = setrate(roll12, 51, ["Escargot", "Fried Chicken",
                              "Hamburger", "Hotdog", "Milk Tea",
                              "Sanma", "Steak", "Tangyuan",
                              "Yunnan Noodles"])
roll12 = setrate(roll12, 52, ["Brownie", "Chocolate", "Ddeokbokki",
                              "Gyoza", "Kimchi", "Mango Pudding",
                              "Napoleon Cake", "Pastel de nata",
                              "Pineapple Bun", "Red Wine", "Salad",
                              "Sukiyaki", "Soft Serve Cone",
                              "Sweet Tofu", "Tiramisu", "Udon",
                              "Yuxiang"])
roll12 = setrate(roll12, 53, ["Foie Gras", "Peking Duck", "B-52",
                              "Bamboo Rice"])
roll12 = setrate(roll12, 106, ["Eggette", "Pineapple Cake", "Laba Congee"])
roll12 = setrate(roll12, 373, ["Eclair"])
roll12 = setrate(roll12, 374, ["Coffee", "Cold Rice Shrimp", "Dorayaki",
                               "Jiuniang", "Long Bao", "Macaron",
                               "Milk", "Miso Soup", "Omurice",
                               "Orange Juice", "Sake", "Sakuramochi",
                               "Sashimi", "Spicy Gluten", "Taiyaki",
                               "Tempura", "Tom Yum", "Ume Ochazuke",
                               "Yellow Wine", "Zongzi"])
