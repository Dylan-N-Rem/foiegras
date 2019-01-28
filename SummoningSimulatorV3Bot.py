from discord.ext.commands import Bot
from discord import Game
from discord.ext import commands
import discord
import random
import time
import traceback
import sys
import os
import json

TOKEN = os.getenv("TOKEN")
prefix = ("f!", "F!")
client = Bot(command_prefix = prefix)

# Normal summoning:

ur_pool = ["Bibimbap", "Crab Long Bao", "Foie Gras", "Peking Duck", "B-52", "Bamboo Rice", "Gingerbread", "Boston Lobster", "Double Scoop"]
sr_pool = ["Milk Tea", "Yunnan Noodles", "Laba Congee", "Sweet Tofu", "Udon", "Tiramisu", "Escargot", "Hotdog", "Mango Pudding", "Hamburger", "Steak", "Tangyuan", "Sanma", "Napoleon Cake", "Salad", "Pastel de nata", "Yuxiang", "Sukiyaki", "Brownie", "Red Wine", "Gyoza", "Chocolate", "Eggette", "Pineapple Cake"]
r_pool = ["Long Bao", "Cold Rice Shrimp", "Coffee", "Sashimi", "Macaron", "Zongzi", "Sakuramochi", "Tom Yum", "Taiyaki", "Milk", "Dorayaki", "Sake", "Tempura", "Spicy Gluten", "Jiuniang", "Omurice", "Orange Juice", "Ume Ochazuke", "Miso Soup", "Yellow Wine"]
m_pool = ["Skewer", "Jello", "Pancake", "Popcorn"]
summon_pool = ur_pool + sr_pool + r_pool + m_pool
none_pool = ["Cloud Tea", "Canele", "Pizza", "Apple Pie", "Black Tea", "Mooncake", "Salty Tofu", "Spaghetti", "Donut", "Sushi", "Tortoise Jelly", "Sweet & Sour Fish", "Beggar's Chicken", "Mung Bean Soup", "Bloody Mary", "Vodka", "Wonton", "Yogurt", "Cola", "Plum Juice", "Crepe", "Cheese", "Toast"]
event_pool = ["Champagne", "Toso", "Raindrop Cake", "Strawberry Daifuku", "Bonito Rice", "Milt", "Cassata", "Caviar", "Seaweed Soup", "Sichuan Hotpot", "Beer"]
unre_pool = ["Eclair Puff", "Green Curry"]

roll0 = []
roll1 = []
roll2 = []
roll3 = []
roll4 = []
roll5 = []
roll6 = []
roll7 = []
roll8 = []
roll = roll8

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
    roll0 += ["Hamburger",]
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
    roll0 += ["Ume Ochazuke" ,]
    roll0 += ["Miso Soup" ,]
    roll0 += ["Yellow Wine"]
for m01 in range(62):
    roll0 += ["Pancake"]
    roll0 += ["Jello"]
for m02 in range(61):
    roll0 += ["Skewer"]

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
    roll1 += ["Hamburger",]
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
    roll1 += ["Ume Ochazuke" ,]
    roll1 += ["Miso Soup" ,]
    roll1 += ["Yellow Wine"]
for m11 in range(46):
    roll1 += ["Skewer"]
    roll1 += ["Jello"]
    roll1 += ["Pancake"]
for m12 in range(47):
    roll1 += ["Popcorn"]

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
    roll2 += ["Hamburger",]
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
    roll2 += ["Ume Ochazuke" ,]
    roll2 += ["Miso Soup" ,]
    roll2 += ["Yellow Wine"]
for m21 in range(46):
    roll2 += ["Skewer"]
    roll2 += ["Jello"]
    roll2 += ["Pancake"]
for m22 in range(47):
    roll2 += ["Popcorn"]

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
    roll3 += ["Hamburger",]
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
    roll3 += ["Ume Ochazuke" ,]
    roll3 += ["Miso Soup" ,]
    roll3 += ["Yellow Wine"]
for m31 in range(46):
    roll3 += ["Skewer"]
    roll3 += ["Jello"]
    roll3 += ["Pancake"]
for m32 in range(47):
    roll3 += ["Popcorn"]

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
    roll4 += ["Hamburger",]
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
    roll4 += ["Ume Ochazuke" ,]
    roll4 += ["Miso Soup" ,]
    roll4 += ["Yellow Wine"]
for m41 in range(46):
    roll4 += ["Skewer"]
    roll4 += ["Jello"]
    roll4 += ["Pancake"]
for m42 in range(47):
    roll4 += ["Popcorn"]

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
    roll5 += ["Hamburger",]
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
    roll5 += ["Ume Ochazuke" ,]
    roll5 += ["Miso Soup" ,]
    roll5 += ["Yellow Wine"]
for m51 in range(46):
    roll5 += ["Skewer"]
    roll5 += ["Jello"]
    roll5 += ["Pancake"]
for m52 in range(47):
    roll5 += ["Popcorn"]
    
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
    roll6 += ["Ume Ochazuke" ,]
    roll6 += ["Miso Soup" ,]
    roll6 += ["Yellow Wine"]
for m61 in range(46):
    roll6 += ["Skewer"]
    roll6 += ["Jello"]
    roll6 += ["Pancake"]
for m62 in range(47):
    roll6 += ["Popcorn"]
    
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
    roll7 += ["Hamburger",]
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
    roll7 += ["Ume Ochazuke" ,]
    roll7 += ["Miso Soup" ,]
    roll7 += ["Yellow Wine"]
for m71 in range(46):
    roll7 += ["Skewer"]
    roll7 += ["Jello"]
    roll7 += ["Pancake"]
for m72 in range(47):
    roll7 += ["Popcorn"]

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
    roll8 += ["Hamburger",]
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
    roll8 += ["Ume Ochazuke" ,]
    roll8 += ["Miso Soup" ,]
    roll8 += ["Yellow Wine"]
for m81 in range(46):
    roll8 += ["Skewer"]
    roll8 += ["Jello"]
    roll8 += ["Pancake"]
for m82 in range(47):
    roll8 += ["Popcorn"]

lsummon_pool = [items.lower() for items in summon_pool]
lnone_pool = [itemn.lower() for itemn in none_pool]
levent_pool = [itemv.lower() for itemv in event_pool]
lunre_pool = [itemu.lower() for itemu in unre_pool]

def output(summoned, valid, ur, sr, r, m, number, context):
    eachsummoned = set(summoned) & set(summon_pool)
    eachsummoned = list(eachsummoned)
    ursummoned = set(eachsummoned) & set(ur_pool)
    ursummoned = list(ursummoned)
    ursummoned.sort()
    srsummoned = set(eachsummoned) & set(sr_pool)
    srsummoned = list(srsummoned)
    srsummoned.sort()
    rsummoned = set(eachsummoned) & set(r_pool)
    rsummoned = list(rsummoned)
    rsummoned.sort()
    msummoned = set(eachsummoned) & set(m_pool)
    msummoned = list(msummoned)
    msummoned.sort()
    if valid == True:
        urline = ""
        srline = ""
        rline = ""
        mline = ""
        if ur >= 1:
            urline1 = "**\nURs summoned:**"
            urline2 = '\nYou summoned ' + '*, '.join([ str(summoned.count(uc)) + ' *' + str(uc) for uc in ursummoned ]) + '*.'
            urline += urline1 + urline2
        if sr >= 1:
            srline1 = "**\nSRs summoned:**"
            srline2 = '\nYou summoned ' + '*, '.join([ str(summoned.count(sc)) + ' *' + str(sc) for sc in srsummoned ]) + '*.'
            srline += srline1 + srline2
        if r >= 1:
            rline1 = "**\nRs summoned:**"
            rline2 = '\nYou summoned ' + '*, '.join([ str(summoned.count(rc)) + ' *' + str(rc) for rc in rsummoned ]) + '*.'
            rline += rline1 + rline2
        if m >= 1:
            mline1 = "**\nMs summoned:**"
            mline2 = '\nYou summoned ' + '*, '.join([ str(summoned.count(mc)) + ' *' + str(mc) for mc in msummoned ]) + '*.'
            mline += mline1 + mline2
        stats = "\nStatistics\n---------------------"
        stats2 = "\nYou summoned " + str(ur) + " URs in total, that is " + str(round((ur/number)*100, 2)) + "% of summons."
        stats3 = "\nYou summoned " + str(sr) + " SRs in total, that is " + str(round((sr/number)*100, 2)) + "% of summons."
        stats4 = "\nYou summoned " + str(r) + " Rs in total, that is " + str(round((r/number)*100, 2)) + "% of summons."
        stats5 = "\nYou summoned " + str(m) + " Ms in total, that is " + str(round((m/number)*100, 2)) + "% of summons."
        stats6 = "\nTo summon " + str(number) + " amount of times, you will have to spend " + str(number*150) + " Soul Embers or " + str(number*100) + " Crystals."
        return "Summoning results of {}:".format(context.message.author.mention) + urline + srline + rline + mline + stats + stats2 + stats3 + stats4 + stats5 + stats6

@client.command(name = 'summon',
                pass_context = True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def summon(context, number):
    summoned = []
    eachsummoned = []
    ur = 0
    sr = 0
    r = 0
    m = 0
    valid = False
    if not(number.isdigit()):
        await client.say("Error - Invalid input: Must be a positive integer")
    elif int(number) <= 0:
        await client.say("Error - Invalid number: Must be more than 0")
    elif int(number) > 1000000:
        await client.say ("Error - Invalid number: Must be less than 1000000")
    elif int(number) >= 1 and int(number) < 1000000:
        await client.say("Summoning food souls...")
        time.sleep(2)
        number = int(number)
        valid = True
        for x in range(number):
            foodsoul = random.choice(roll)
            summoned += [foodsoul]
            if foodsoul in ur_pool:
                ur += 1
            elif foodsoul in sr_pool:
                sr += 1
            elif foodsoul in r_pool:
                r += 1
            elif foodsoul in m_pool:
                m += 1
        bigline = output(summoned, valid, ur, sr, r, m, number, context)
        await client.say(bigline)

@client.command(name = 'foodsoul',
                pass_context = True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def summonfoodsoul(context, food_soul, amount):
    summoned = []
    eachsummoned = []
    ur = 0
    sr = 0
    r = 0
    m = 0
    number = 0
    valid = False
    ivalid = False
    food_soul = food_soul.replace(".", " ")
    lfood_soul = food_soul.lower()
    if not(amount.isdigit()):
        await client.say('Error - Invalid 1st input: Use "." instead of space')
    if int(amount) <= 0:
        await client.say("Error - Invalid 2nd input: Number must be more than 0")
    elif lfood_soul not in lsummon_pool:
        if lfood_soul in lnone_pool:
            ivalid = True
            await client.say("Error - Invalid food soul: " + lfood_soul.title() + " cannot be summoned")
        if lfood_soul in levent_pool:
            ivalid = True
            await client.say("Error - Invalid food soul: " + lfood_soul.title() + " is from an event; use ``f!efoodsoul`` instead")
        if lfood_soul in lunre_pool:
            ivalid = True
            await client.say("Error - Invalid food soul: " + lfood_soul.title() + " is not in the global server yet")
        elif ivalid == False:
            await client.say("Error - Invalid 1st input: Food Soul does not exsist or improper spelling")
    elif int(amount) > 1000:
        await client.say("Error - Invalid number: Must be less than 1000")
    elif lfood_soul in lsummon_pool and int(amount) >= 1 and int(amount) < 1000:
        await client.say("Summoning food souls...\n")
        time.sleep(2)
        count_foodsoul = 0
        while int(amount) != count_foodsoul:
            foodsoul = random.choice(roll)
            valid = True
            lfoodsoul = foodsoul.lower()
            summoned += [foodsoul]
            if foodsoul in ur_pool:
                ur += 1
                number += 1
            if foodsoul in sr_pool:
                sr += 1
                number += 1
            if foodsoul in r_pool:
                r += 1
                number += 1
            if foodsoul in m_pool:
                m += 1
                number += 1
            if lfood_soul == lfoodsoul:
                count_foodsoul += 1
    bigline = output(summoned, valid, ur, sr, r, m, number, context)
    await client.say(bigline)

@client.command(name = 'rates',
                pass_context = False)
@commands.cooldown(1, 10, commands.BucketType.user)
async def rates():
    urtotal = 0
    srtotal = 0
    rtotal = 0
    mtotal = 0
    urrateslist = []
    srrateslist = []
    rrateslist = []
    mrateslist = []
    for urfs in ur_pool:
        temp = 0
        for urcount in roll:
            if urfs == urcount:
                temp += 1
        urrateslist += [[urfs, temp/100]]
        urtotal += temp/100
    for srfs in sr_pool:
        temp = 0
        for srcount in roll:
            if srfs == srcount:
                temp += 1
        srrateslist += [[srfs, temp/100]]
        srtotal += temp/100
    for rfs in r_pool:
        temp = 0
        for rcount in roll:
            if rfs == rcount:
                temp += 1
        rrateslist += [[rfs, temp/100]]
        rtotal += temp/100
    for mfs in m_pool:
        temp = 0
        for mcount in roll:
            if mfs == mcount:
                temp += 1
        mrateslist += [[mfs, temp/100]]
        mtotal += temp/100
    embed = discord.Embed(title = "Feast of Creation:", color = 0xffb100)
    embed.add_field(name = "UR: " + str(round(urtotal, 2)) + "%", value = "\n".join([urc[0] + ": " + str(round(urc[1], 2)) + "%" for urc in urrateslist]), inline = False)
    embed.add_field(name = "SR: " + str(round(srtotal, 2)) + "%", value = "\n".join([src[0] + ": " + str(round(src[1], 2)) + "%" for src in srrateslist]), inline = False)
    embed.add_field(name = "R: " + str(round(rtotal, 2)) + "%", value = "\n".join([rrc[0] + ": " + str(round(rrc[1], 2)) + "%" for rrc in rrateslist]), inline = False)
    embed.add_field(name = "M: " + str(round(mtotal, 2)) + "%", value = "\n".join([mrc[0] + ": " + str(round(mrc[1], 2)) + "%" for mrc in mrateslist]), inline = False)
    await client.say(embed = embed)

# Event summoning:

def output2(summoned, valid, ur, sr, r, m, number, context, esummon_pool, eur_pool, esr_pool, er_pool, em_pool):
    eachsummoned = set(summoned) & set(esummon_pool)
    eachsummoned = list(eachsummoned)
    ursummoned = set(eachsummoned) & set(eur_pool)
    ursummoned = list(ursummoned)
    ursummoned.sort()
    srsummoned = set(eachsummoned) & set(esr_pool)
    srsummoned = list(srsummoned)
    srsummoned.sort()
    rsummoned = set(eachsummoned) & set(er_pool)
    rsummoned = list(rsummoned)
    rsummoned.sort()
    msummoned = set(eachsummoned) & set(em_pool)
    msummoned = list(msummoned)
    msummoned.sort()
    if valid == True:
        urline = ""
        srline = ""
        rline = ""
        mline = ""
        if ur >= 1:
            urline1 = "**\nURs summoned:**"
            urline2 = '\nYou summoned ' + '*, '.join([ str(summoned.count(uc)) + ' *' + str(uc) for uc in ursummoned ]) + '*.'
            urline += urline1 + urline2
        if sr >= 1:
            srline1 = "**\nSRs summoned:**"
            srline2 = '\nYou summoned ' + '*, '.join([ str(summoned.count(sc)) + ' *' + str(sc) for sc in srsummoned ]) + '*.'
            srline += srline1 + srline2
        if r >= 1:
            rline1 = "**\nRs summoned:**"
            rline2 = '\nYou summoned ' + '*, '.join([ str(summoned.count(rc)) + ' *' + str(rc) for rc in rsummoned ]) + '*.'
            rline += rline1 + rline2
        if m >= 1:
            mline1 = "**\nMs summoned:**"
            mline2 = '\nYou summoned ' + '*, '.join([ str(summoned.count(mc)) + ' *' + str(mc) for mc in msummoned ]) + '*.'
            mline += mline1 + mline2
        stats = "\nStatistics\n---------------------"
        stats2 = "\nYou summoned " + str(ur) + " URs in total, that is " + str(round((ur/number)*100, 2)) + "% of summons."
        stats3 = "\nYou summoned " + str(sr) + " SRs in total, that is " + str(round((sr/number)*100, 2)) + "% of summons."
        stats4 = "\nYou summoned " + str(r) + " Rs in total, that is " + str(round((r/number)*100, 2)) + "% of summons."
        stats5 = "\nYou summoned " + str(m) + " Ms in total, that is " + str(round((m/number)*100, 2)) + "% of summons."
        stats6 = "\nTo summon " + str(number) + " amount of times, you will have to spend " + str(number*150) + " Soul Embers or " + str(number*100) + " Crystals."
        return "Summoning results of {}:".format(context.message.author.mention) + urline + srline + rline + mline + stats + stats2 + stats3 + stats4 + stats5 + stats6

def autounav(roll_num, eur_pool, esr_pool, er_pool, em_pool, unav_pool):
    if roll_num <= 8:
        unav_pool = []
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
    unav_pool = autounav(roll_num, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    return eroll

def index0entry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool):
    eroll = autoroll(eroll, 1, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
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
    eroll = autoroll(eroll, 2, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    return eroll

def index2entry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool):
    eroll = autoroll(eroll, 2, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
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
    eroll = autoroll(eroll, 2, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
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
    eroll = autoroll(eroll, 3, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
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
    eroll = autoroll(eroll, 4, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
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
    eroll = autoroll(eroll, 4, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
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
    eroll = autoroll(eroll, 4, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
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
    eroll = autoroll(eroll, 4, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
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
    eroll = autoroll(eroll, 4, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
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
    eroll = autoroll(eroll, 4, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
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
    eroll = autoroll(eroll, 4, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
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
    eroll = autoroll(eroll, 5, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
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
    eroll = autoroll(eroll, 5, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
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
    eroll = autoroll(eroll, 5, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
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
    eroll = autoroll(eroll, 6, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    eevent_pool = eventfs("Sichuan Hotpot", 1, eevent_pool, eur_pool, esr_pool, er_pool, em_pool)
    eevent_pool = eventfs("Beer", 2, eevent_pool, eur_pool, esr_pool, er_pool, em_pool)
    for e1 in range(499):
        eroll += ["Beer"]
    for e2 in range(121):
        eroll += ["Sichuan Hotpot"]
    return eroll

def index4bentry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool):
    eroll = autoroll(eroll, 6, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    eevent_pool = eventfs("Milt", 1, eevent_pool, eur_pool, esr_pool, er_pool, em_pool)
    eevent_pool = eventfs("Bonito Rice", 2, eevent_pool, eur_pool, esr_pool, er_pool, em_pool)
    for e1 in range(499):
        eroll += ["Bonito Rice"]
    for e2 in range(121):
        eroll += ["Milt"]
    return eroll

def index11bentry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool):
    eroll = autoroll(eroll, 7, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
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
    eroll = autoroll(eroll, 8, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
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
    eroll = autoroll(eroll, 8, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
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
    eroll = autoroll(eroll, 8, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
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

def index18entry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool):
    eroll = autoroll(eroll, 8, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
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
    elif event_index == "18":
        eroll = index18entry(eroll, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    else:
        eroll = []
    return eroll

@client.command(name = "esummon",
                pass_context = True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def esummon(context, event_index, number):
    eroll = []
    eur_pool = []
    eur_pool += ur_pool
    esr_pool = []
    esr_pool += sr_pool
    er_pool = []
    er_pool += r_pool
    em_pool = []
    em_pool += m_pool
    eevent_pool = []
    eevent_pool += event_pool
    unav_pool = []
    eroll = eventindexcheck(eroll, event_index, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    if eroll == []:
        await client.say("Error - Invalid event index: Check the event index with ``f!eventindex``.")
    elif eroll != []:
        esummon_pool = eur_pool + esr_pool + er_pool + em_pool
        summoned = []
        eachsummoned = []
        ur = 0
        sr = 0
        r = 0
        m = 0
        valid = False
        if not(number.isdigit()):
            await client.say("Error - Invalid 2nd input: Must be a positive integer")
        elif int(number) <= 0:
            await client.say("Error - Invalid number: Must be more than 0")
        elif int(number) > 1000000:
            await client.say("Error - Invalid number: Must be less than 1000000")
        elif int(number) >= 1:
            await client.say("Summoning food souls...")
            time.sleep(2)
            number = int(number)
            valid = True
            for x1 in range(number):
                foodsoul = random.choice(eroll)
                summoned += [foodsoul]
                if foodsoul in eur_pool:
                    ur += 1
                elif foodsoul in esr_pool:
                    sr += 1
                elif foodsoul in er_pool:
                    r += 1
                elif foodsoul in em_pool:
                    m += 1
            bigline = output2(summoned, valid, ur, sr, r, m, number, context, esummon_pool, eur_pool, esr_pool, er_pool, em_pool)
            await client.say(bigline)

@client.command(name = "efoodsoul",
                pass_context = True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def efoodsoul(context, event_index, food_soul, amount):
    eroll = []
    eur_pool = []
    eur_pool += ur_pool
    esr_pool = []
    esr_pool += sr_pool
    er_pool = []
    er_pool += r_pool
    em_pool = []
    em_pool += m_pool
    eevent_pool = []
    eevent_pool += event_pool
    unav_pool = []
    eroll = eventindexcheck(eroll, event_index, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    if eroll == []:
        await client.say("Error - Invalid event index: Check the event index with ``f!eventindex``.")
    elif eroll != []:
        esummon_pool = eur_pool + esr_pool + er_pool + em_pool
        lesummon_pool = [iteme.lower() for iteme in esummon_pool]
        leevent_pool = [eventitem.lower() for eventitem in eevent_pool]
        lunav_pool = [unavitem.lower() for unavitem in unav_pool]
        summoned = []
        eachsummoned = []
        ur = 0
        sr = 0
        r = 0
        m = 0
        number = 0
        valid = False
        ivalid = False
        food_soul = food_soul.replace(".", " ")
        lfood_soul = food_soul.lower()
        if not(amount.isdigit()):
            await client.say('Error - Invalid 3rd input: Use "." instead of space')
        if int(amount) <= 0:
            await client.say("Error - Invalid 4th input: Number must be more than 0")
        elif lfood_soul not in lesummon_pool:
            if lfood_soul in lnone_pool:
                ivalid = True
                await client.say("Error - Invalid food soul: " + lfood_soul.title() + " cannot be summoned")
            if lfood_soul in leevent_pool:
                ivalid = True
                await client.say("Error - Invalid food soul: " + lfood_soul.title() + " is from another event; check your event index number with ``f!eventindex``")
            if lfood_soul in lunre_pool:
                ivalid = True
                await client.say("Error - Invalid food soul: " + lfood_soul.title() + " is not in the global server yet.")
            if lfood_soul in lunav_pool:
                await client.say("Error - Invalid food soul: " + lfood_soul.title() + " is not in the summoning pool during this event")
            elif ivalid == False:
                await client.say("Error - Invalid 3rd input: Food Soul does not exsist or improper spelling")
        elif int(amount) > 1000:
            await client.say("Error - Invalid 4th input: Number must be less than 1000")
        elif lfood_soul in lesummon_pool and int(amount) >= 1 and int(amount) < 1000000:
            await client.say("Summoning food souls...\n")
            time.sleep(2)
            count_foodsoul = 0
            while int(amount) != count_foodsoul:
                foodsoul = random.choice(eroll)
                valid = True
                lfoodsoul = foodsoul.lower()
                summoned += [foodsoul]
                if foodsoul in eur_pool:
                    ur += 1
                    number += 1
                if foodsoul in esr_pool:
                    sr += 1
                    number += 1
                if foodsoul in er_pool:
                    r += 1
                    number += 1
                if foodsoul in em_pool:
                    m += 1
                    number += 1
                if lfood_soul == lfoodsoul:
                    count_foodsoul += 1
        bigline = output2(summoned, valid, ur, sr, r, m, number, context, esummon_pool, eur_pool, esr_pool, er_pool, em_pool)
        await client.say(bigline)

@client.command(name = 'erates',
                pass_context = False)
@commands.cooldown(1, 30, commands.BucketType.user)
async def erates(event_index):
    eroll = []
    eur_pool = []
    eur_pool += ur_pool
    esr_pool = []
    esr_pool += sr_pool
    er_pool = []
    er_pool += r_pool
    em_pool = []
    em_pool += m_pool
    eevent_pool = []
    eevent_pool += event_pool
    unav_pool = []
    eroll = eventindexcheck(eroll, event_index, eevent_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    if eroll == []:
        await client.say("Error - Invalid event index: Check the event index with ``f!eventindex``.")
    elif eroll != []:
        esummon_pool = eur_pool + esr_pool + er_pool + em_pool
        urtotal = 0
        srtotal = 0
        rtotal = 0
        mtotal = 0
        urrateslist = []
        srrateslist = []
        rrateslist = []
        mrateslist = []
        for urfs in eur_pool:
            temp = 0
            for urcount in eroll:
                if urfs == urcount:
                    temp += 1
            urrateslist += [[urfs, temp/100]]
            urtotal += temp/100
        for srfs in esr_pool:
            temp = 0
            for srcount in eroll:
                if srfs == srcount:
                    temp += 1
            srrateslist += [[srfs, temp/100]]
            srtotal += temp/100
        for rfs in er_pool:
            temp = 0
            for rcount in eroll:
                if rfs == rcount:
                    temp += 1
            rrateslist += [[rfs, temp/100]]
            rtotal += temp/100
        for mfs in em_pool:
            temp = 0
            for mcount in eroll:
                if mfs == mcount:
                    temp += 1
            mrateslist += [[mfs, temp/100]]
            mtotal += temp/100
        embed = discord.Embed(title = "Feast of Creation:", color = 0xffb100)
        embed.add_field(name = "UR: " + str(round(urtotal, 2)) + "%", value = "\n".join([urc[0] + ": " + str(round(urc[1], 2)) + "%" for urc in urrateslist]), inline = False)
        embed.add_field(name = "SR: " + str(round(srtotal, 2)) + "%", value = "\n".join([src[0] + ": " + str(round(src[1], 2)) + "%" for src in srrateslist]), inline = False)
        embed.add_field(name = "R: " + str(round(rtotal, 2)) + "%", value = "\n".join([rrc[0] + ": " + str(round(rrc[1], 2)) + "%" for rrc in rrateslist]), inline = False)
        embed.add_field(name = "M: " + str(round(mtotal, 2)) + "%", value = "\n".join([mrc[0] + ": " + str(round(mrc[1], 2)) + "%" for mrc in mrateslist]), inline = False)
        await client.say(embed = embed)

@client.command(name = "eventindex")
@commands.cooldown(1, 30, commands.BucketType.user)
async def eventhelp():
    sadded = " has been added to the summoning pool"
    padded = " have been added to the summoning pool"
    srateup = " has an inceased summoning rate"
    prateup = " have increased summoning rates"
    eventlist = [["0", "Sweet Temptations", "Chocolate and Popcorn" + padded + " permanently; Gingerbread and Chocolate also" + prateup, "25th July to 30th July 2018", "Gingerbread: 0.23% -> 1.2%\nChocolate: 3.33%, drops to 0.83% after event\nPopcorn: 0.47%"],
                 ["1", "Promise of Youth", "Pineapple Cake and Eggette" + padded + " permanently", "August 8th 2018 onwards", "Pineapple Cake: 1.51%\nEggette: 1.50%"],
                 ["2", "Brewing Fine Wine", "Toso and Sweet Tofu" + padded, "13th August to 19th August 2018", "Toso: 1.50%\nSweet Tofu: 6.61%"],
                 ["3", "Sakura Falls", "Strawberry Daifuku and Raindrop Cake" + padded, "4th September to 17th September 2018", "Strawberry Daifuku: 1.20%\nRaindrop Cake: 0.31%"],
                 ["4a", "Autumn Memories", "Milt and Bonito Rice" + padded, "1st October to 14th October 2018", "Milt: 0.48%\nBonito Rice: 0.96%"],
                 ["4b", "Autumn Memories", "Milt and Bonito Rice" + padded, "17th December to 26th December 2018", "Milt: 1.21%\nBonito Rice: 4.99%"],
                 ["5a", "Come Have a Chat", "Peking Duck" + srateup, "15th October to 22nd October 2018", "Peking Duck: 0.61% -> 1.50%"],
                 ["5b", "Let's Chat", "Peking Duck" + srateup, "1st December to 9th December 2018.", "Peking Duck: 0.61 -> 1.50%"],
                 ["6", "Amusement Park Sign Up! I", "Cassata" + sadded + " and B-52" + srateup, "24th October to 26th October 2018", "Cassata: 3.32%\nB-52: 1.20%"],
                 ["7", "Amusement Park Sign Up! II", "Cassata" + sadded + " and Crab Long Bao" + srateup, "27th October to 29th October 2018", "Crab Long Bao: 0.36% -> 1.2%\n Cassata: 3.32%"],
                 ["8", "Amusement Park Sign Up! III", "Cassata" + sadded + " and Double Scoop" + srateup, "30th October to 1st November 2018", "Double Scoop: 0.05% -> 0.30%\n Cassata: 3.32%"],
                 ["9", "Amusement Park Sign Up! IV", "Cassata" + sadded + " and Bamboo Rice" + srateup, "2nd November to 4th November 2018", "Bamboo Rice: 0.52% -> 1.2%\n Cassata: 3.32%"],
                 ["10", "Amusement Park Sign Up! V", "Toso and Cassata" + padded, "5th November to 7th November 2018", "Toso: 1.20%\nCassata: 3.32%"],
                 ["11a", "Candy Strike!", "Gingerbread" + srateup, "8th November to 15th November 2018", "Gingerbread: 0.23%% -> 1.50%"],
                 ["11b", "Candy Strike!", "Gingerbread" + srateup, "27th December 2018 to 2nd January 2019", "Gingerbread: 0.23%% -> 1.50%"],
                 ["12", "Seaside Moon", "Caviar and Seaweed Soup" + padded, "16th November to 30th November 2018", "Caviar: 1.21%\nSeaweed Soup: 4.98%"],
                 ["13", "Breezy Snacks", "Raindrop Cake" + sadded + " and Sanma" + srateup, "16th November to 30th November 2018", "Raindrop: 1.21%\nSanma: 0.72% -> 4.98%"],
                 ["14", "No Spice No Dice", "Sichuan Hotpot and Beer" + padded, "17th December to 26th December 2018", "Sichuan Hotpot: 1.21%\nBeer: 4.99%"],
                 ["15", "Flavor Frenzy", "Bibimbap" + sadded + " permanently and" + srateup, "3rd January to 10th January 2019", "Bibimbap: 0.09% -> 1.21%"],
                 ["16", "Fragrant Garden: Champagne", "Champagne, Raindrop Cake, Bonito Rice and Beer" + padded + " and URs have an overall increased summoning rate", "11th January to 20 January 2019", "Champagne: 1.21%\nRaindrop Cake: 0.50%\nBonito Rice: 0.43%\nBeer: 0.43%\nURs: 3.01% -> 4.01%"],
                 ["17", "Fragrant Garden: Toso", "Toso, Milt, Strawberry Daifuku, Bonito Rice and Beer" + padded + " and URs have an overall increased summoning rate", "11th January to 20 January 2019", "Toso: 1.21%\nMilt: 0.50%\nStrawberry Daifuku: 0.47%\nBonito Rice: 0.43%\nBeer: 0.43%\nURs: 3.01% -> 4.01%"],
                 ["18", "Flame Storm", "B-52" + srateup, "25th January to 31st January 2019", "B-52: 0.60% -> 1.20%"]]
    embed = discord.Embed(title = "Event Index List", description = "Use the event index number to input what event you want to summon in! Remember that this is for events in the global server.", color = 0x2ecc71)
    for eventcount in range(len(eventlist)):
        embed.add_field(name = eventlist[eventcount][0] + ". " + eventlist[eventcount][1], value = eventlist[eventcount][2] + " from " + eventlist[eventcount][3] + ".\n" + eventlist[eventcount][4], inline = False)
    await client.say(embed = embed)

# Dish commands:

food_pool = ["Stir-Fried Potatoes", "Braised Pork", "Braised Eggplant", "Sauteed Lettuce", "Carrot Bread", "Cucumber Egg Stir-Fry", "Black Pepper Beef", "Sauteed Mushrooms", "Egg Fried Rice", "Salmon Fried Rice", "Onion Fried Rice", "Bacon Fried Rice", "Braised Octopus", "Risotto", "Butter Bread", "Emerald Roll", "Corn Pie", "Toffee Apple", "Pineapple Fried Rice", "Chicken Soup", "Mango Pudding", "Strawberry Ice Cream", "Red Bean Pudding", "Kung Pao Chicken", "Pumpkin Pie", "Sweet Yam Buns", "Steamed Cod", "Steamed Unagi", "Garlic Lobster", "Crab Hotpot", "French Fries", "Crispy Pork", "Salad", "Eggplant Roll", "Smoked Salmon", "Roast Beef", "Cheese Bread", "Mushroom Soup", "Fried Rice Cake", "Pork Burger", "Bacon Tofu Wrap", "Grilled Calamari", "Popcorn", "Shortbread", "Minestrone", "Pineapple Juice", "Apple Crisp", "Chicken Pizza", "Roast Chicken", "Mango Wrap", "Fruit Salad", "Peanut Pie", "Pumpkin Soup", "Hotteok", "Cheesy Yam", "Fried Cod", "Fried Unagi", "Baked Lobster", "Crab Salad", "Baked Potato", "Grilled Pork Belly", "Cucumber Salad", "Boiled Lettuce", "Mushroom Yaki", "Salmon Sashimi", "Beef Tartare", "Tamagoyaki", "Omurice", "Shogayki", "Bacon Bites", "Cold Tofu", "Grilled Corn", "Vegetable Tempura", "Takoyaki", "Creamed Spinach", "Baked Pineapple", "Apples & Cream", "Chicken Skewer", "Fried Chicken", "Mango Smoothie", "Strawberry Smoothie", "Peanut Crisp", "Cod Fillet", "Piglet Daifuku", "Pumpkin Muffin", "Yam Dumplings", "Unagi Don", "Lobster Sashimi", "Crab Sashimi"]
lostfood_pool = ["Calamari Skewer", "Garlic Oyster", "Grilled Prawns", "Pickled Salmon Head", "Tomato & Eggs", "Steamed Mushrooms", "Spaghetti", "Har Gow", "Gold Cake", "Mixed Greens", "Stir-Fried Mussels", "Mushroom Alfredo", "Cha Siu Bao", "Spinach Noodles", "Mint Pineapple", "Apple Sangria", "Braised Lamb", "Mushroom Chicken Stew", "Matcha Cake", "Cappuccino", "Fruit Tea", "Lemon Pie", "Meat Zongzi", "Stuffed Lotus Root", "Lotus Root Stir-Fry", "Black Fungus Congee", "Sanma Shioyaki", "Steamed Crab", "Crab Rice Cake", "Curry Crab", "Yam Pigeon Soup", "Bamboo & Meat Stir-Fry", "Braised Geese", "Roe Meat Ball", "Birds Nest", "Ginseng Stew Chicken"]
lfood_pool = [itemd.lower() for itemd in food_pool]
llostfood_pool = [iteml.lower() for iteml in lostfood_pool]

def output3(foodstats, dishname, colour, cuisine, ingredient1, ingredient2, ingredient3, level, quest, flavor, texture, aroma, appearence, season1, season2, attribute):
    if season1 == "Ginger":
        season3 = "Tender Ginger"
    if season2 == "Ginger":
        season4 = "Tender Ginger"

    if season1 == "Scallion":
        season3 = "Diced Scallions"
    if season2 == "Scallion":
        season4 = "Diced Scallions"

    if season1 == "Garlic":
        season3 = "Fresh Garlic"
    if season2 == "Garlic":
        season4 = "Fresh Garlic"

    if season1 == "Chili":
        season3 = "Royal Dressing"
    if season2 == "Chili":
        season4 = "Royal Dressing"

    if season1 == "Soy Sauce":
        season3 = "Premium Soy Sauce"
    if season2 == "Soy Sauce":
        season4 = "Premium Soy Sauce"

    if season1 == "Black Pepper":
        season3 = "Tellicherry Pepper"
    if season2 == "Black Pepper":
        season4 = "Tellicherry Pepper"

    if season1 == "Sugar":
        season3 = "Granulated Sugar"
    if season2 == "Sugar":
        season4 = "Granulated Sugar"

    if season1 == "Cooking Oil":
        season3 = "Sealed Oil"
    if season2 == "Cooking Oil":
        season4 = "Sealed Oil"

    if season1 == "Rock Sugar":
        season3 = "Pearl Sugar"
    if season2 == "Rock Sugar":
        season4 = "Pearl Sugar"

    if season1 == "Salt":
        season3 = "Sea Salt"
    if season2 == "Salt":
        season4 = "Sea Salt"

    if season1 == "Salad Dressing":
        season3 = "Thousand Island"
    if season2 == "Salad Dressing":
        season4 = "Thousand Island"

    if season1 == "Sago":
        season3 = "Crystal Sago"
    if season2 == "Sago":
        season4 = "Crystal Sago"

    if season1 == "Condensed Milk":
        season3 = "Premium Condensed Milk"
    if season2 == "Condensed Milk":
        season4 = "Premium Condensed Milk"

    if season1 == "Cooking Wine":
        season3 = "Sparkling Wine"
    if season2 == "Cooking Wine":
        season4 = "Sparkling Wine"

    if season1 == "Icing":
        season3 = "Mist Icing"
    if season2 == "Icing":
        season4 = "Mist Icing"

    foodoutput = discord.Embed(title = dishname, color = colour)
    foodoutput.add_field(name = "Cuisine", value = cuisine, inline = False)
    if ingredient1 != "" and ingredient2 == "" and ingredient3 == "":
        foodoutput.add_field(name = "Ingredients/Recipe", value = ingredient1, inline = False)
    if ingredient1 != "" and ingredient2 != "" and ingredient3 == "":
        foodoutput.add_field(name = "Ingredients/Recipe", value = ingredient1 + " and " + ingredient2, inline = False)
    if ingredient1 != "" and ingredient2 != "" and ingredient3 != "":
        foodoutput.add_field(name = "Ingredients/Recipe", value = ingredient1 + ", " + ingredient2 + " and " + ingredient3, inline = False)
    if level != "":
        foodoutput.add_field(name = "Level Requirement", value = level, inline = False)
    if quest != "":
        foodoutput.add_field(name = "Quest", value = quest, inline = False)
    foodoutput.add_field(name = "Max Food Stats", value = "Flavour: " + flavor + "\nTexture: " + texture + "\nAroma: " + aroma + "\nAppearence: " + appearence, inline = False)
    foodoutput.add_field(name = "Seasoning", value = "These seasonings add **" + attribute + "** to the dish\n" + season1 + " ^\n" + season2 + " ^^\n" + season3 + " ^^^\n" + season4 + " ^^^^", inline = False)
    foodoutput.add_field(name = "Selling Price", value = "D: " + foodstats[0] + " Gold" + "\nC: " + foodstats[1] + " Gold" +"\nB: " + foodstats [2] + " Gold" + "\nA: " + foodstats[3] + " Gold" + "\nS: " + foodstats[4] + " Gold", inline = False)
    foodoutput.add_field(name = "Maximum Production Quantity ", value = "D: " + foodstats[5] + " dishes" + "\nC: " + foodstats[6] + " dishes" +"\nB: " + foodstats [7] + " dishes" + "\nA: " + foodstats[8] + " dishes" + "\nS: " + foodstats[9] + " dishes", inline = False)
    foodoutput.add_field(name = "Time Per Dish", value = "D: " + foodstats[10] + " seconds" + "\nC: " + foodstats[11] + " seconds" +"\nB: " + foodstats [12] + " seconds" + "\nA: " + foodstats[13] + " seconds" + "\nS: " + foodstats[14] + " seconds", inline = False)
    foodoutput.add_field(name = "Meal Time", value = foodstats[15] + " seconds", inline = False)
    foodoutput.add_field(name = "Cost Per Dish", value = foodstats[16] + " Gold", inline = False)
    return foodoutput

@client.command(name = "food")
@commands.cooldown(1, 3, commands.BucketType.user)
async def foodinfo(dish):
    dish = dish.replace(".", " ")
    dish = dish.replace(" and ", " & ")
    dish = dish.replace("'", "")
    ldish = dish.lower()
    if ldish not in lfood_pool:
        if ldish not in llostfood_pool:
            await client.say("Error - Invalid input: Food does not exsist or improper spelling")
        elif ldish in llostfood_pool:
            if ldish == "calamari skewer":
                foodstats = ["72", "79", "87", "96", "106", "35", "49", "63", "77", "105", "9", "9", "9", "8", "8", "180", "24"]
                embed = output3(foodstats, "Calamari Skewer", 0xe67e22, "Lost", "Squid (1-7)", "", "", "5", "Make 5 dishes of any kind", "771", "910", "1500", "819", "Chili", "Black Pepper", "Texture")
                await client.say(embed = embed)
            elif ldish == "garlic oyster":
                foodstats = ["120", "132", "145", "160", "176", "45", "63", "81", "99", "135", "15", "14", "14", "13", "12", "300", "40"]
                embed = output3(foodstats, "Garlic Oyster", 0x979c9f, "Lost", "Oyster (2-8)", "", "", "8", "Submit 5 Calamari Skewers", "972", "1800", "506", "722", "Chili", "Garlic", "Aroma")
                await client.say(embed = embed)
            elif ldish == "grilled prawns":
                foodstats = ["84", "92", "101", "111", "122", "105", "147", "189", "231", "315", "11", "10", "10", "9", "9", "210", "28"]
                embed = output3(foodstats, "Grilled Prawns", 0xa84300, "Lost", "Shrimp (3-8)", "", "", "10", "Cook C rated dishes 8 times", "1500", "707", "992", "801", "Cooking Wine", "Salt", "Flavor")
                await client.say(embed = embed)
            elif ldish == "pickled salmon head":
                foodstats = ["79", "87", "96", "106", "117", "55", "77", "99", "121", "165", "12", "11", "11", "10", "10", "180", "26"]
                embed = output3(foodstats, "Pickled Salmon Head", 0x979c9f, "Lost", "Salmon (4-2)", "Pickled Peppers (4-8)", "", "12", "Challenge Parisel 1-1", "902", "754", "744", "1600", "Garlic",  "Chili", "Appearence")
                await client.say(embed = embed)
            elif ldish == "tomato & eggs":
                foodstats = ["119", "131", "144", "158", "174", "35", "49", "63", "77", "105", "18", "17", "17", "16", "15", "270", "40",]
                embed = output3(foodstats, "Tomato & Eggs", 0xe74c3c, "Lost", "Egg (5-2)", "Tomato (5-8)", "", "14", "Clear Rube's Mischief 3 times", "888", "1700", "705", "707", "Salt", "Sugar", "Aroma")
                await client.say(embed = embed)
            elif ldish == "steamed mushrooms":
                foodstats = ["119", "131", "144", "158", "174", "225", "315", "405", "495", "675", "18", "17", "17", "16", "15", "270", "40"]
                embed = output3(foodstats, "Steamed Mushrooms", 0xffee, "Lost", "Shrimp (3-8)", "Cheese (6-2)", "Shiitake (6-8)", "16", "Challenge Parisel 1-2", "1700", "750", "800", "750", "Cooking Wine", "Cooking Oil", "Flavor")
                await client.say(embed = embed)
            elif ldish == "spaghetti":
                foodstats = ["101", "111", "122", "134", "147", "43", "63", "81", "99", "135", "15", "14", "14", "13", "12", "210", "34"]
                embed = output3(foodstats, "Spaghetti", 0xf1c40f, "Lost", "Tomato (5-8)", "Pasta (7-10)", "", "18", "Complete 2 Take-out orders from Gloriville", "725", "813", "1500", "962", "Black Pepper", "Sugar", "Texture")
                await client.say(embed = embed)
            elif ldish == "har gow":
                foodstats = ["101", "111", "122", "134", "147", "85", "119", "153", "187", "255", "15", "14", "14", "13", "12", "210", "34"]
                embed = output3(foodstats, "Har Gow", 0xffffff, "Lost", "Pork Belly (1-6)", "Shrimp (3-8)", "Wheat Flour (8-4)", "20", "Develop the menu 2 times", "912", "692", "796", "1600", "Cooking Oil", "Ginger", "Appearence")
                await client.say(embed = embed)
            elif ldish == "gold cake":
                foodstats = ["86", "95", "105", "116", "128", "125", "175", "225", "275", "375", "12", "12", "12", "11", "10", "180", "29"]
                embed = output3(foodstats, "Gold Cake", 0xf1c40f, "Lost", "Egg (5-2)", "Butter (7-8)", "Tapioca (8-7)", "22", "Complete all daily missions", "680", "1900", "858", "565", "Salad Dressing", "Condensed Milk", "Aroma")
                await client.say(embed = embed)
            elif ldish == "mixed greens":
                foodstats = ["140", "154", "169", "186", "205", "125", "175", "225", "275", "375", "21", "20", "20", "19", "18", "270", "47"]
                embed = output3(foodstats, "Mixed Greens", 0x2ecc71, "Lost", "Cucumber (2-2)", "Egg (5-2)", "Enokitake (9-8)", "24", "Challenge Parisel 4-2", "1700", "717", "707", "876", "Garlic", "Chili", "Flavor")
                await client.say(embed = embed)
            elif ldish == "stir-fried mussels":
                foodstats = ["156", "172", "189", "208", "229", "225", "315", "405", "495", "675", "23", "22", "22", "21", "20", "300", "52"]
                embed = output3(foodstats, "Stir-Fried Mussels", 0x546e7a, "Lost", "Mussels (10-8)", "", "", "26", "Serve 100 regular customers in your restaurant", "607", "984", "1800", "609", "Scallion", "Cooking Wine", "Texture")
                await client.say(embed = embed)
            elif ldish == "mushroom alfredo":
                foodstats = ["94", "103", "113", "124", "136", "55", "77", "99", "121", "165", "14", "13", "13", "12", "11", "180", "31"]
                embed = output3(foodstats, "Mushroom Alfredo", 0xffeea9, "Lost", "Mushroom (7-3)", "Pasta (7-10)", "Cream (11-7)", "28", "Collect 15 Low-Grade Screws (Screws already in inventory are not counted)", "617", "687", "896", "1800", "Condensed Milk", "Black Pepper", "Appearence")
                await client.say(embed = embed)
            elif ldish == "cha siu bao":
                foodstats = ["101", "111", "122", "134", "147", "145", "203", "261", "319", "435", "15", "14", "14", "13", "12", "180", "34"]
                embed = output3(foodstats, "Cha Siu Bao", 0x95a5a6, "Lost", "Flour (12-2)", "BBQ Pork (12-8)", "", "30", "Make 10 dishes of any kind", "1600", "938", "756", "706", "Salad Dressing", "Cooking Wine", "Flavor")
                await client.say(embed = embed)
            elif ldish == "spinach noodles":
                foodstats = ["151", "166", "183", "201", "221", "125", "175", "225", "275", "375", "22", "21", "21", "20", "19", "270", "50"]
                embed = output3(foodstats, "Spinach Noodles", 0x2ecc71, "Lost", "Egg (5-2)", "Flour (12-2)", "Spinach (13-6)", "32", "Challenge Parisel stage 6-2", "556", "2000", "907", "537", "Soy Sauce", "Salad Dressing", "Aroma")
                await client.say(embed = embed)
            elif ldish == "mint pineapple":
                foodstats = ["118", "130", "143", "157", "173", "105", "147", "189", "231", "315", "17", "16", "16", "15", "14", "210", "39"]
                embed = output3(foodstats, "Mint Pineapple", 0xf1c40f, "Lost", "Pineapple (14-3)", "Mint (14-7)", "", "34", "Complete 5 Delivery orders in the Gloriville area", "508", "413", "2100", "979", "Icing", "Salad Dressing", "Texture")
                await client.say(embed = embed)
            elif ldish == "apple sangria":
                foodstats = ["126", "139", "153", "168", "185", "145", "203", "261", "319", "435", "18", "17", "17", "16", "15", "210", "41"]
                embed = output3(foodstats, "Apple Sangria", 0xe74c3c, "Lost", "Apple (15-1)", "Red Wine (15-6)", "", "36", "Collect and submit 10 Spinach", "578", "515", "898", "2000", "Icing", "Rock Sugar", "Appearence")
                await client.say(embed = embed)
            elif ldish == "brasied lamb":
                foodstats = ["126", "139", "153", "168", "185", "245", "343", "441", "539", "735", "18", "17", "17", "16", "15", "210", "42"]
                embed = output3(foodstats, "Braised Lamb", 0xe74c3c, "Lost", "Red Wine (15-6)", "Lamb Leg (15-9)", "", "38", "Bring a Control talent into battle", "397", "2200", "808", "595", "Sugar", "Garlic", "Aroma")
                await client.say(embed = embed)
            elif ldish == "mushroom chicken stew":
                foodstats = ["162", "178", "196", "216", "238", "75", "105", "135", "165", "225", "23", "22", "22" , "21", "20", "270", "54"]
                embed = output3(foodstats, "Mushroom Chicken Stew", 0x992d22, "Lost", "Shiitake (6-8)", "Diced Chicken (16-5)", "Glass Noodles (16-9)", "40", "Challenge Spirng Outskirts 9-2", "1900", "504", "938", "658", "Ginger", "Soy Sauce", "Flavor")
                await client.say(embed = embed)
            elif ldish == "matcha cake":
                foodstats = ["134", "147", "162", "178", "196", "85", "119", "153", "187", "255", "19", "18", "18", "17", "16", "210", "45"]
                embed = output3(foodstats, "Matcha Cake", 0x1f8b4c, "Lost", "Egg (5-2)", "Flour (12-2)", "Matcha Power (17-6)", "41", "Defeat 20 Dine and Dash customers in the restaurant", "875", "609", "316", "2200", "Sago", "Icing", "Appearence")
                await client.say(embed = embed)
            elif ldish == "cappuccino":
                foodstats = ["134", "147", "162", "178", "196", "205", "287", "369", "451", "615", "19", "18", "18", "17", "16", "210", "45"]
                embed = output3(foodstats, "Cappuccino", 0xc27c0e, "Lost", "Milk (12-5)", "Coffee Beans (17-7)", "", "42", "Collect 50 Mints (those already in inventory are not counted)", "354", "607", "2100", "939", "Sago", "Condensed Milk", "Texture")
                await client.say(embed = embed)
            elif ldish == "fruit tea":
                foodstats = ["173", "190", "209", "230", "253", "165", "231", "297", "363", "495", "25", "24", "24", "23", "22", "270", "58"]
                embed = output3(foodstats, "Fruit Tea", 0xe67e22, "Lost", "Strawberry (18-1)", "Lemon (18-6)", "Osmanthus (18-9)", "44", "Complete all daily missions", "1900", "988", "682", "430", "Rock Sugar", "Sago", "Flavor")
                await client.say(embed = embed)
            elif ldish == "lemon pie":
                foodstats = ["143", "157", "173", "190", "209", "185", "259", "333", "407", "555", "20", "19", "19", "18", "17", "210", "48"]
                embed = output3(foodstats, "Lemon Pie", 0xf1c40f, "Lost", "Egg (5-2)", "Flour (12-2)", "Lemon (18-6)", "45", "Develop the menu 3 times", "600", "2200", "600", "600", "Condensed Milk", "Sago", "Aroma")
                await client.say(embed = embed)
            elif ldish == "meat zongzi":
                foodstats = ["143", "157", "173", "190", "209", "165", "231", "297", "363", "495", "20", "19", "19", "18", "17", "210", "48"]
                embed = output3(foodstats, "Meat Zongzi", 0x1f8b4c, "Lost", "Pork Loin (9-2)", "Glutinous Rice (19-7)", "", "47", "Challenge Spring Outskirts 12-2", "683", "901", "2100", "416", "Soy Sauce", "Cooking Oil", "Texture")
                await client.say(embed = embed)
            elif ldish == "stuffed lotus root":
                foodstats = ["143", "157", "173", "190", "209", "245", "343", "441", "539", "735", "20", "19", "19", "18", "17", "210", "47"]
                embed = output3(foodstats, "Stuffed Lotus Root", 0xe67e22, "Lost", "Osmanthus (18-9)", "Glutinous Rice (19-7)", "Lotus Root (20-8)", "49", "Submit 20 Lemon Pies", "405", "307", "888", "2400", "Rock Sugar", "Icing", "Appearence")
                await client.say(embed = embed)
            elif ldish == "lotus root stir-fry":
                foodstats = ["173", "190", "209", "230", "253", "185", "259", "333", "407", "555", "24", "23", "23", "22", "21", "240", "58"]
                embed = output3(foodstats, "Lotus Root Stir-Fry", 0xe91e63, "Lost", "Onion (9-5)", "Lotus Root (20-8)", "Black Fungus (21-6)", "50", "Complete 10 Delivery orders in the Nevras are", "2000", "694", "888", "418", "Salt", "Rock Sugar", "Flavor")
                await client.say(embed = embed)
            elif ldish == "black fungus congee":
                foodstats = ["216", "238", "262", "288", "317", "245", "343", "441", "539", "735", "30", "29", "29", "28", "27", "300", "72"]
                embed = output3(foodstats, "Black Fungus Congee", 0x546e7a, "Lost", "Rice (8-2)", "Black Fungus (21-6)", "King Mushroom (21-7)", "52", "Collect and submit 10 Advanced Seasoning", "868", "2300", "422", "410", "Sugar", "Scallion", "Aroma")
                await client.say(embed = embed)
            elif ldish == "sanma shioyaki":
                foodstats = ["155", "166", "183", "201", "221", "205", "287", "369", "451", "615", "21", "20", "20", "19", "18", "210", "50"]
                embed = output3(foodstats, "Sanma Shioyaki", 0x546e7a, "Lost", "Sanma (22-7)", "", "", "54", "Collect and submit 10 Advanced Sesaoning", "493", "285", "822", "2400", "Cooking Oil", "Salt", "Appearence")
                await client.say(embed = embed)
            elif ldish == "steamed crab":
                foodstats = ["182", "200", "220", "242", "266", "245", "343", "441", "539", "735", "26", "25", "25", "24", "23", "240", "61"]
                embed = output3(foodstats, "Steamed Crab", 0xe74c3c, "Lost", "Mitten Crab (23-7)", "", "", "56", "Challenge Outskirts 16-3", "835", "388", "2300", "477", "Scallion", "Ginger", "Texture")
                await client.say(embed = embed)
            elif ldish == "crab rice cake":
                foodstats = ["182", "200", "220", "242", "266", "75", "105", "135", "165", "225", "26", "25", "25", "24", "23", "240", "61"]
                embed = output3(foodstats, "Crab Rice Cake", 0xe74c3c, "Lost", "Mitten Crab (23-7)", "Rice Cake (23-8)", "", "58", "Complete 15 Delivery orders in the Sakurajima area", "2300", "354", "514", "832", "Ginger", "Soy Sauce", "Flavor")
                await client.say(embed = embed)
            elif ldish == "curry crab":
                foodstats = ["228", "251", "276", "304", "334", "245", "343", "441", "539", "735", "32", "31", "31", "30", "29", "300", "76"]
                embed = output3(foodstats, "Curry Crab", 0xf1c40f, "Lost", "Blue Crab (24-6)", "Curry Cube (24-7)", "", "60", "Make 50 A grade dishes", "409", "2400", "227", "964", "Black Pepper", "Scallion", "Aroma")
                await client.say(embed = embed)
            elif ldish == "chinese yam and squab soup":
                foodstats = ["75", "83", "91", "100", "110", "200", "280", "360", "440", "600", "12", "12", "11", "11", "10", "120", "25"]
                embed = output3(foodstats, "Chinese Yam and Squab Soup", 0xf1c40f, "Lost", "Squab (25-1)", "Chinese Yam (25-4)", "Goji (25-7)", "60", "Serve 200 regular customers in your restaurant", "768", "410", "422", "2400", "Ginger", "Scallion", "Appearence")
                await client.say(embed = embed)
            elif ldish == "bamboo stir-fry":
                foodstats = ["68", "75", "83", "91", "100", "200", "280", "360", "440", "600", "10", "10", "10", "9", "9", "90", "23"]
                embed = output3(foodstats, "Bamboo Stir-Fry", 0xffeea9, "Lost", "Potherb Mustard (26-2)", "Bamboo Shoots (26-4)", "Shredded Meat (26-8)", "63", "Explore Sandstone Cave once", "2200", "556", "807", "437", "Garlic", "Chili", "Flavor")
                await client.say(embed = embed)
            elif ldish == "orange goose":
                foodstats = ["57", "63", "69", "76", "84", "200", "280", "360", "440", "600", "7", "7", "7", "6", "6", "60", "19"]
                embed = output3(foodstats, "Orange Goose", 0x2ecc71, "Lost", "Goose (27-2)", "Orange (27-4)", "Cellophane Noodles (27-8)", "66", "Defeat 20 Dine and Dash customers in the restaurant", "701", "494", "2400", "405", "Cooking Oil", "Soy Sauce", "Aroma")
                await client.say(embed = embed)
            elif ldish == "crab roe lion's head":
                foodstats = ["118", "130", "143", "157", "173", "200", "280", "360", "440", "600", "15", "14", "14", "13", "12", "180", "39"]
                embed = output3(foodstats, "Crab Roe Lion's Head", 0xffeea9, "Lost", "Crab Roe (28-2)", "Ground Meat (28-5)", "Greens (28-9)", "69", "Collect 50 Crab Roe (those already in inventory are not counted)", "594", "2400", "485", "520", "Scallion", "Ginger", "Texture")
                await client.say(embed = embed)
            elif ldish == "birds nest with white fungus":
                foodstats = ["230", "253", "278", "306", "337", "300", "420", "540", "660", "900", "32", "31", "31", "30", "29", "300", "77"]
                embed = output3(foodstats, "Bird's Nest With White Fungus", 0xfffee3, "Lost", "Bird's Nest (29-1)", "White Fungus (29-4)", "Lotus Seeds (29-8)", "72", "Cook 30 A grade dishes", "2300", "354", "514", "832", "Sugar", "Rock Sugar", "Flavor",)
                await client.say(embed = embed)
            elif ldish == "ginseng black chicken":
                foodstats = ["230", "253", "278", "306", "337", "300", "420", "540", "660", "900", "32", "31", "31", "30", "29", "300", "77"]
                embed = output3(foodstats, "Ginseng Black Chicken", 0x494949, "Lost", "American Ginseng (30-1)", "Black Chicken (30-4)", "Jujube (30-9)", "75", "Challenge Fallen Angel Remains 25-2", "768", "2300", "522", "410", "Salt", "Cooking Wine", "Texture")
                await client.say(embed = embed)          
    elif ldish in lfood_pool:
        if ldish == "stir-fried potatoes":
            foodstats = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
            embed = output3(foodstats, "Stir-Fried Potatoes", 0xf1c40f, "Potato (1-3)", "", "", "Light Kingdom", "Potato (1-3)", "", "", "", "", "801", "1500", "992", "707", "Chili", "Scallion", "Flavor")
            await client.say(embed = embed)
        elif ldish == "braised pork":
            foodstats = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
            embed = output3(foodstats, "Braised Pork", 0xa84300, "Light Kingdom", "Pork Belly (1-6)", "", "", "", "", "771", "910", "1500", "819", "Scallion", "Soy Sauce", "Texture")
            await client.say(embed = embed)
        elif ldish == "braised eggplant":
            foodstats = ["24", "26", "29", "32", "35", "125", "175", "225", "275", "375", "3", "3", "3", "2", "2", "", ""]
            embed = output3(foodstats, "Braised Eggplant", 0x71368a, "Light Kingdom", "Eggplant (2-7)", "", "", "", "", "717", "707", "876", "1700", "Garlic", "Cooking Oil", "Appearence")
            await client.say(embed = embed)
        elif ldish == "sauteed lettuce":
            foodstats = ["53", "58", "64", "70", "77", "105", "147", "189", "231", "315", "8", "8", "8", "7", "7", "120", "18"]
            embed = output3(foodstats, "Sauteed Lettuce", 0x2ecc71, "Light Kingdom", "Lettuce (3-1)", "", "", "", "", "725", "1500", "813", "962", "Soy Sauce", "Garlic", "Aroma")
            await client.say(embed = embed)
        elif ldish == "carrot bread":
            foodstats = ["31", "34", "37", "41", "45", "35", "49", "63", "77", "105", "5", "5", "5", "4", "4", "70", "10"]
            embed = output3(foodstats, "Carrot Bread", 0xe67e22, "Light Kingdom", "Carrot (3-5)", "Bread (4-4)", "", "", "", "888", "1700", "705", "707", "Icing", "Salad Dressing", "Aroma")
            await client.say(embed = embed)
        elif ldish == "cucumber egg stir-fry":
            foodstats = ["79", "87", "96", "106", "117", "225", "315", "405", "495", "675", "12", "11", "11", "10", "10", "180", "26"]
            embed = output3(foodstats, "Cucumber Egg Stir-Fry", 0x2ecc71, "Light Kingdom", "Cucumber (2-2)", "Egg (5-2)", "", "", "", "1700", "750", "800", "750", "Sugar", "Scallion", "Flavor")
            await client.say(embed = embed)
        elif ldish == "black pepper beef":
            foodstats = ["43", "47", "52", "57", "63", "45", "63", "81", "99", "135", "7", "7", "7", "6", "6", "90", "14"]
            embed = output3(foodstats, "Black Pepper Beef", 0xc27c0e, "Light Kingdom", "Beef Tenderloin (5-6)", "Green Pepper (6-6)", "", "", "", "587", "515", "898", "2000", "Salt", "Cooking Wine", "Appearence")
            await client.say(embed = embed)
        elif ldish == "sauteed mushrooms":
            foodstats = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
            embed = output3(foodstats, "Sauteed Mushrooms", 0xc27c0e, "Light Kingdom", "Shiitake (6-8)", "Mushroom (7-3)", "", "", "", "972", "506", "1800", "722", "Black Pepper", "Cooking Oil", "Texture")
            await client.say(embed = embed)
        elif ldish == "egg fried rice":
            foodstats = ["29", "32", "35", "39", "43", "75", "105", "135", "165", "225", "5", "5", "5", "4", "4", "60", "10"]
            embed = output3(foodstats, "Egg Fried Rice", 0xf1c40f, "Light Kingdom", "Egg (5-2)", "Rice (8-2)", "", "", "", "556", "2000", "907", "537", "Scallion", "Salt", "Aroma")
            await client.say(embed = embed)
        elif ldish == "salmon fried rice":
            foodstats = ["62", "68", "75", "83", "91", "55", "77", "99", "121", "165", "9", "9", "9", "8", "8", "120", "21"]
            embed = output3(foodstats, "Salmon Fried Rice", 0xe67e22, "Light Kingdom", "Salmon (4-2)", "Rice (8-2)", "Onion (9-5)", "", "", "1600", "754", "902", "744", "Cooking Oil", "Black Pepper", "Flavor")
            await client.say(embed = embed)
        elif ldish == "onion fried rice":
            foodstats = ["94", "103", "113", "124", "136", "55", "77", "99", "121", "165", "14", "13", "13", "12", "11", "180", "31"]
            embed = output3(foodstats, "Onion Fried Rice", 0x9b59b6, "Light Kingdom", "Rice (8-2)", "Pork Loin (9-2)", "Onion (9-5)", "", "", "405", "888", "2400", "307", "Salt", "Chili", "Texture")
            await client.say(embed = embed)
        elif ldish == "bacon fried rice":
            foodstats = ["62", "68", "75", "83", "91", "165", "231", "297", "363", "495", "9", "9", "9", "8", "8", "120", "21"]
            embed = output3(foodstats, "Bacon Fried Rice", 0x992d22, "Light Kingdom", "Carrot (3-5)", "Rice (8-2)", "Bacon (10-3)", "", "", "875", "609", "316", "2200", "Chili", "Black Pepper", "Appearence")
            await client.say(embed = embed)
        elif ldish == "braised octopus":
            foodstats = ["39", "43", "47", "52", "57", "165", "231", "297", "363", "495", "6", "6", "6", "5", "5", "70", "13"]
            embed = output3(foodstats, "Braised Octopus", 0x992d22, "Light Kingdom", "Green Pepper (6-6)", "Octopus (11-4)", "", "", "", "912", "692", "796", "1600", "Garlic", "Soy Sauce", "Appearence")
            await client.say(embed = embed)
        elif ldish == "risotto":
            foodstats = ["101", "111", "122", "134", "147", "145", "203", "261", "319", "435", "15", "14", "14", "13", "12", "180", "34"]
            embed = output3(foodstats, "Risotto", 0xf1c40f, "Light Kingdom", "Cheese (6-2)", "Rice (8-2)", "Cream (11-7)", "", "", "504", "938", "1900", "658", "Sago", "Sugar", "Texture")
            await client.say(embed = embed)
        elif ldish == "butter bread":
            foodstats = ["67", "74", "81", "89", "98", "125", "175", "225", "275", "375", "10", "10", "10", "9", "9", "70", "22"]
            embed = output3(foodstats, "Butter Bread", 0xe67e22, "Light Kingdom", "Egg (5-2)", "Butter (7-8)", "Flour (12-2)", "", "", "2000", "694", "888", "418", "Condensed Milk", "Icing", "Flavor")
            await client.say(embed = embed)
        elif ldish == "emerald roll":
            foodstats = ["36", "40", "44", "48", "53", "245", "343", "441", "539", "735", "6", "6", "6", "5", "5", "60", "12"]
            embed = output3(foodstats, "Emerald Roll", 0x2ecc71, "Light Kingdom", "Cabbage (13-5)", "Spinach (13-6)", "", "", "", "508", "413", "979", "2100", "Soy Sauce", "Icing", "Appearence")
            await client.say(embed = embed)
        elif ldish == "corn pie":
            foodstats = ["108", "119", "131", "144", "158", "75", "105", "135", "165", "225", "16", "15", "15", "14", "13", "180", "36"]
            embed = output3(foodstats, "Corn Pie", 0xf1c40f, "Light Kingdom", "Corn (11-5)", "Starch (13-9)", "", "", "", "617", "687", "896", "1800", "Cooking Oil", "Salad Dressing", "Appearence")
            await client.say(embed = embed)
        elif ldish == "toffee apple":
            foodstats = ["58", "64", "70", "77", "85", "85", "119", "153", "187", "255", "9", "9", "9", "8", "8", "90", "19"]
            embed = output3(foodstats, "Toffee Apple", 0xe67e22, "Light Kingdom", "Starch (13-9)", "Apple (15-1)", "", "", "", "600", "2200", "600", "600", "Sugar", "Rock Sugar", "Aroma")
            await client.say(embed = embed)
        elif ldish == "pineapple fried rice":
            foodstats = ["42", "46", "51", "56", "62", "125", "175", "225", "275", "375", "6", "6", "6", "5", "5", "70", "14"]
            embed = output3(foodstats, "Pineapple Fried Rice", 0xf1c40f, "Light Kingdom", "Rice (8-2)", "Pineapple (14-3)", "", "", "", "514", "354", "2300", "832", "Salad Dressing", "Rock Sugar", "Flavor")
            await client.say(embed = embed)
        elif ldish == "chicken soup":
            foodstats = ["96", "106", "117", "129", "142", "225", "315", "405", "495", "675", "14", "13", "13", "12", "11", "150", "32"]
            embed = output3(foodstats, "Chicken Soup", 0xc27c0e, "Light Kingdom", "Shiitake (6-8)", "Whole Chicken (16-6)", "", "", "", "354", "607", "2100", "939", "Ginger", "Salt", "Texture")
            await client.say(embed = embed)
        elif ldish == "mango pudding":
            foodstats = ["115", "127", "140", "154", "169", "185", "259", "333", "407", "555", "17", "16", "16", "15", "14", "180", "38"]
            embed = output3(foodstats, "Mango Pudding", 0xf1c40f, "Light Kingdom", "Egg (5-2)", "Milk (12-5)", "Mango (17-3)", "", "", "706", "938", "756", "1600", "Rock Sugar", "Sago", "Appearence")
            await client.say(embed = embed)
        elif ldish == "strawberry ice cream":
            foodstats = ["48", "53", "58", "64", "70", "205", "287", "369", "451", "615", "7", "7", "7", "6", "6", "70", "16"]
            embed = output3(foodstats, "Strawberry Ice Cream", 0xe91e63, "Light Kingdom", "Cream (11-7)", "Milk (12-5)", "Strawberry (18-1)", "", "", "808", "397", "2200", "595", "Sago", "Condensed Milk", "Flavor")
            await client.say(embed = embed)
        elif ldish == "red bean pudding":
            foodstats = ["122", "134", "147", "162", "178", "245", "343", "441", "539", "735", "18", "17", "17", "16", "15", "180", "41"]
            embed = output3(foodstats, "Red Bean Pudding", 0x992d22, "Light Kingdom", "Milk (12-5)", "Red Beans (19-5)", "", "", "", "683", "2100", "801", "416", "Rock Sugar", "Sago", "Aroma")
            await client.say(embed = embed)
        elif ldish == "kung pao chicken":
            foodstats = ["61", "67", "74", "81", "89", "185", "259", "333", "407", "555", "9", "9", "9", "8", "8", "90", "20"]
            embed = output3(foodstats, "Kung Pao Chicken", 0x992d22, "Light Kingdom", "Diced Chicken (16=5)", "Peanut (19-3)", "", "", "", "607", "984", "1800", "609", "Chili", "Cooking Wine", "Texture")
            await client.say(embed = embed)
        elif ldish == "pumpkin pie":
            foodstats = ["43", "47", "52", "57", "63", "85", "119", "153", "187", "255", "6", "6", "6", "5", "5", "60", "14"]
            embed = output3(foodstats, "Pumpkin Pie", 0xe67e22, "Light Kingdom", "Honey (14-6)", "Pumpkin (20-5)", "Rice Flour (20-7)", "", "", "680", "1900", "858", "562", "Icing", "Condensed Milk", "Aroma")
            await client.say(embed = embed)
        elif ldish == "sweet yam buns":
            foodstats = ["86", "95", "105", "116", "128", "245", "343", "441", "539", "735", "12", "11", "11", "10", "10", "120", "29"]
            embed = output3(foodstats, "Sweet Yam Buns", 0x71368a, "Light Kingdom", "Egg (5-2)", "Flour (12-2)", "Purple Yam (21-3)", "", "", "1900", "988", "682", "430", "Condensed Milk", "Sugar", "Flavor")
            await client.say(embed = embed)
        elif ldish == "steamed cod":
            foodstats = ["65", "72", "79", "87", "96", "205", "287", "369", "451", "615", "9", "9", "9", "8", "8", "90", "22"]
            embed = output3(foodstats, "Steamed Cod", 0xe67e22, "Light Kingdom", "Tofu (10-6)", "Cod (22-2)", "", "", "", "409", "2400", "227", "964", "Black Pepper", "Ginger", "Aroma")
            await client.say(embed = embed)
        elif ldish == "steamed unagi":
            foodstats = ["114", "125", "138", "152", "167", "245", "343", "441", "539", "735", "16", "15", "15", "14", "13", "105", "38"]
            embed = output3(foodstats, "Steamed Unagi", 0x979c9f, "Light Kingdom", "Shiitake (6-8)", "Eel (22-5)", "", "", "", "493", "285", "822", "2400", "Ginger", "Cooking Wine", "Appearence")
            await client.say(embed = embed)
        elif ldish == "garlic lobster":
            foodstats = ["137", "151", "166", "183", "201", "105", "147", "189", "231", "315", "19", "18", "18", "17", "16", "180", "46"]
            embed = output3(foodstats, "Garlic Lobster", 0xe74c3c, "Light Kingdom", "Rock Lobsters (23-5)", "", "", "", "", "835", "388", "2300", "477", "Salad Dressing", "Garlic", "Texture")
            await client.say(embed = embed)
        elif ldish == "crab hotpot":
            foodstats = ["53", "58", "64", "70", "77", "245", "343", "441", "539", "735", "8", "8", "8", "7", "7", "70", "18"]
            embed = output3(foodstats, "Crab Hotpot", 0xe74c3c, "Light Kingdom", "Shiitake (6-8)", "Tofu (10-6)", "King Crab (24-2)", "", "", "410", "422", "868", "2300", "Cooking Wine", "Ginger", "Flavor")
            await client.say(embed = embed)
        elif ldish == "french fries":
            foodstats = ["24", "26", "29", "32", "35", "35", "49", "63", "77", "105", "3", "3", "3", "2", "2", "60", "8"]
            embed = output3(foodstats, "French Fries", 0xf1c40f, "Gloriville", "Potato (1-3)", "", "", "", "", "972", "1800", "506", "722", "Black Pepper", "Cooking Oil", "Aroma")
            await client.say(embed = embed)
        elif ldish == "crispy pork":
            foodstats = ["24", "26", "29", "32", "35", "45", "63", "81", "99", "135", "3", "3", "3", "2", "2", "60", "8"]
            embed = output3(foodstats, "Crispy Pork", 0xa84300, "Gloriville", "Pork Belly (1-6)", "", "", "", "", "725", "813", "1500", "962", "Garlic", "Cooking Wine", "Texture")
            embed.set_image(url = "http://p6.qhimg.com/dr/250__/t0146bd30bf0c6bc70a.png")
            await client.say(embed = embed)
        elif ldish == "salad":
            foodstats = ["53", "58", "64", "70", "77", "55", "77", "99", "121", "165", "8", "8", "8", "7", "7", "120", "18"]
            embed = output3(foodstats, "Salad", 0x2ecc71, "Gloriville", "Cucumber (2-2)", "Lettuce (3-1)", "Carrot (3-5)", "", "", "1500", "707", "992", "801", "Salt", "Salad Dressing", "Flavor")
            await client.say(embed = embed)
        elif ldish == "eggplant roll":
            foodstats = ["24", "26", "29", "32", "35", "105", "147", "189", "231", "315", "3", "3", "3", "2", "2", "60", "8"]
            embed = output3(foodstats, "Eggplant Roll", 0xe67e22, "Gloriville", "Potato (1-3)", "Eggplant (2-7)", "", "", "", "912", "692", "796", "1600", "Chili", "Soy Sauce", "Appearence")
            await client.say(embed = embed)
        elif ldish == "smoked salmon":
            foodstats = ["31", "34", "37", "41", "45", "35", "49", "63", "77", "105", "5", "5", "5", "4", "4", "70", "10"]
            embed = output3(foodstats, "Smoked Salmon", 0xe67e22, "Gloriville", "Salmon (4-2)", "", "", "", "", "888", "1700", "705", "707", "Soy Sauce", "Salt", "Aroma")
            await client.say(embed = embed)
        elif ldish == "roast beef":
            foodstats = ["79", "87", "96", "106", "117", "225", "315", "405", "495", "675", "12", "11", "11", "10", "10", "180", "26"]
            embed = output3(foodstats, "Roast Beef", 0x992d22, "Gloriville", "Beef Tenderloin (5-6)", "", "", "", "", "607", "984", "1800", "609", "Garlic", "Cooking Wine", "Texture")
            await client.say(embed = embed)
        elif ldish == "cheese bread":
            foodstats = ["43", "47", "52", "57", "63", "45", "63", "81", "99", "135", "7", "7", "7", "6", "6", "90", "14"]
            embed = output3(foodstats, "Cheese Bread", 0xf1c40f, "Gloriville", "Bread (4-4)", "Cheese (6-2)", "", "", "", "1700", "717", "707", "876", "Scallion", "Garlic", "Flavor")
            await client.say(embed = embed)
        elif ldish == "mushroom soup":
            foodstats = ["72", "79", "87", "96", "106", "85", "119", "153", "187", "255", "11", "10", "10", "9", "9", "150", "24"]
            embed = output3(foodstats, "Mushroom Soup", 0xffeea9, "Gloriville", "Shiitake (6-8)", "Mushroom (7-3)", "Butter (7-8)", "", "", "1900", "504", "938", "658", "Ginger", "Scallion", "Flavor")
            await client.say(embed = embed)
        elif ldish == "fried rice cake":
            foodstats = ["29", "32", "35", "39", "43", "125", "175", "225", "275", "375", "5", "5", "5", "4", "4", "60", "10"]
            embed = output3(foodstats, "Fried Rice Cake", 0xffe6b0, "Gloriville", "Egg (5-2)", "Rice (8-2)", "", "", "", "680", "1900", "858", "451", "Black Pepper", "Cooking Oil", "Aroma")
            await client.say(embed = embed)
        elif ldish == "pork burger":
            foodstats = ["62", "68", "75", "83", "91", "125", "175", "225", "275", "375", "9", "9", "9", "8", "8", "120", "21"]
            embed = output3(foodstats, "Pork Burger", 0xe67e22, "Gloriville", "Lettuce (3-1)", "Bread (4-4)", "Pork Loin (9-2)", "", "", "493", "285", "822", "2400", "Salad Dressing", "Chili", "Appearence")
            await client.say(embed = embed)
        elif ldish == "bacon tofu wrap":
            foodstats = ["94", "103", "113", "124", "136", "225", "315", "405", "495", "675", "14", "13", "13", "12", "11", "180", "31"]
            embed = output3(foodstats, "Bacon Tofu Wrap", 0xeb7c7c, "Gloriville", "Bacon (10-3)", "Tofu (10-6)", "", "", "", "617", "687", "896", "1800", "Scallion", "Soy Sauce", "Appearence")
            await client.say(embed = embed)
        elif ldish == "grilled calamari":
            foodstats = ["39", "43", "47", "52", "57", "145", "203", "261", "319", "435", "6", "6", "6", "5", "5", "70", "13"]
            embed = output3(foodstats, "Grilled Calamari", 0xc27c0e, "Gloriville", "Green Pepper (6-6)", "Onion (9-5)", "Octopus (11-4)", "", "", "771", "910", "1500", "819", "Soy Sauce", "Chili", "Texture")
            await client.say(embed = embed)
        elif ldish == "popcorn":
            foodstats = ["62", "68", "75", "83", "91", "55", "77", "99", "121", "165", "9", "9", "9", "8", "8", "90", "21"]
            embed = output3(foodstats, "Popcorn", 0xf1c40f, "Gloriville", "Butter (7-8)", "Corn (11-2)", "", "", "", "409", "2400", "227", "964", "Cooking Oil", "Sugar", "Aroma")
            await client.say(embed = embed)
        elif ldish == "shortbread":
            foodstats = ["101", "111", "122", "134", "147", "125", "175", "225", "275", "375", "15", "14", "14", "13", "12", "180", "34"]
            embed = output3(foodstats, "Shortbread", 0xffeea9, "Gloriville", "Butter (7-8)", "Flour (12-2)", "Milk (12-5)", "", "", "875", "609", "316", "2200", "Icing", "Rock Sugar", "Appearence")
            await client.say(embed = embed)
        elif ldish == "minestrone":
            foodstats = ["64", "74", "81", "89", "98", "105", "147", "189", "231", "315", "10", "10", "10", "9", "9", "120", "22"]
            embed = output3(foodstats, "Minestrone", 0x2ecc71, "Gloriville", "Cabbage (13-5)", "Spinach (13-6)", "Starch (13-9)", "", "", "1600", "938", "756", "706", "Salt", "Ginger", "Flavor")
            await client.say(embed = embed)
        elif ldish == "pineapple juice":
            foodstats = ["36", "40", "44", "48", "53", "145", "203", "261", "319", "435", "6", "6", "6", "5", "5", "60", "12"]
            embed = output3(foodstats, "Pineapple Juice", 0xf1c40f, "Gloriville", "Pineapple (14-3)", "Honey (14-6)", "", "", "", "2000", "694", "888", "418", "Rock Sugar", "Sago", "Flavor")
            await client.say(embed = embed)
        elif ldish == "apple crisp":
            foodstats = ["108", "119", "131", "144", "158", "245", "343", "441", "539", "735", "16", "15", "15", "14", "13", "180", "36"]
            embed = output3(foodstats, "Apple Crisp", 0xffeea9, "Gloriville", "Flour (12-2)", "Apple (15-1)", "", "", "", "397", "2200", "808", "595", "Condensed Milk", "Icing", "Aroma")
            await client.say(embed = embed)
        elif ldish == "chicken pizza":
            foodstats = ["42", "46", "51", "56", "65", "75", "105", "135", "165", "225", "6", "6", "6", "5", "5", "70", "14"]
            embed = output3(foodstats, "Chicken Pizza", 0xe67e22, "Gloriville", "Cheese (6-2)", "Flour (12-2)", "Diced Chicken (16-5)", "", "", "354", "507", "2100", "939", "Chili", "Black Pepper", "Texture")
            await client.say(embed = embed)
        elif ldish == "roast chicken":
            foodstats = ["58", "64", "70", "77", "85", "85", "119", "153", "187", "255", "9", "9", "9", "8", "8", "90", "19"]
            embed = output3(foodstats, "Roast Chicken", 0xe67e22, "Gloriville", "Whole Chicken (16-6)", "", "", "", "", "683", "801", "2100", "416", "Cooking Oil", "Black Pepper", "Texture")
            await client.say(embed = embed)
        elif ldish == "mango wrap":
            foodstats = ["96", "106", "117", "129", "145", "205", "287", "369", "451", "615", "14", "13", "13", "12", "11", "150", "32"]
            embed = output3(foodstats, "Mango Wrap", 0xf1c40f, "Gloriville", "Cream (11-7)", "Flour (12-2)", "Mango (17-3)", "", "", "902", "754", "744", "1600", "Sugar", "Condensed Milk", "Appearence")
            await client.say(embed = embed)
        elif ldish == "strawberry mousse":
            foodstats = ["48", "53", "58", "64", "70", "185", "259", "333", "407", "555", "7", "7", "7", "6", "6", "70", "16"]
            embed = output3(foodstats, "Strawberry Mousse", 0xff91b6, "Gloriville", "Cream (11-7)", "Strawberry (18-1)", "", "", "", "888", "2300", "422", "410", "Sugar", "Icing", "Aroma")
            await client.say(embed = embed)
        elif ldish == "fruit salad":
            foodstats = ["115", "127", "140", "154", "169", "165", "231", "297", "363", "495", "17", "16", "16", "15", "14", "180", "38"]
            embed = output3(foodstats, "Fruit Salad", 0xe67e22, "Gloriville", "Pineapple (14-3)", "Apple (15-1)", "Mango (17-3)", "", "", "1700", "750", "800", "750", "Condensed Milk", "Salad Dressing", "Flavor")
            await client.say(embed = embed)
        elif ldish == "peanut pie":
            foodstats = ["61", "67", "74", "81", "89", "165", "231", "297", "363", "495", "9", "9", "9", "8", "8", "90", "20"]
            embed = output3(foodstats, "Peanut Pie", 0xc27c0e, "Gloriville", "Egg (5-2)", "Flour (12-2)", "Peanut (19-3)", "", "", "587", "515", "898", "2000", "Icing", "Sugar", "Appearence")
            await client.say(embed = embed)
        elif ldish == "pumpkin soup":
            foodstats = ["122", "134", "147", "162", "178", "245", "343", "441", "539", "735", "18", "17", "17", "16", "15", "180", "41"]
            embed = output3(foodstats, "Pumpkin Soup", 0xe67e22, "Gloriville", "Milk (12-5)", "Pumpkin (20-5)", "", "", "", "508", "413", "2100", "979", "Rock Sugar", "Sago", "Texture")
            await client.say(embed = embed)
        elif ldish == "hotteok":
            foodstats = ["43", "47", "52", "57", "63", "185", "259", "333", "407", "555", "6", "6", "6", "5", "5", "60", "14"]
            embed = output3(foodstats, "Hotteok", 0xffffff, "Gloriville", "Milk (12-5)", "Red Beans (19-5)", "Rice Flour (20-7)", "", "", "1900", "988", "682", "430", "Sago", "Condensed Milk", "Flavor")
            await client.say(embed = embed)
        elif ldish == "cheesy yam":
            foodstats = ["86", "95", "105", "116", "128", "245", "343", "441", "539", "735", "12", "11", "11", "10", "10", "120", "29"]
            embed = output3(foodstats, "Cheesy Yam", 0x71368a, "Gloriville", "Cheese (6-2)", "Purple Yam (21-3)", "", "", "", "556", "2000", "907", "537", "Sago", "Rock Sugar", "Aroma")
            await client.say(embed = embed)
        elif ldish == "fried cod":
            foodstats = ["65", "72", "79", "87", "96", "205", "287", "369", "451", "615", "9", "9", "9", "8", "8", "90", "22"]
            embed = output3(foodstats, "Fried Cod", 0xe67e22, "Gloriville", "Egg (5-2)", "Flour (12-2)", "Cod (22-2)", "", "", "2300", "354", "514", "832", "Ginger", "Scallion", "Flavor")
            await client.say(embed = embed)
        elif ldish == "fried unagi":
            foodstats = ["114", "125", "138", "152", "167", "245", "343", "441", "539", "735", "16", "15", "15", "14", "13", "150", "38"]
            embed = output3(foodstats, "Fried Unagi", 0xe67e22, "Gloriville", "Egg (5-2)", "Flour (12-2)", "Eel (22-5)", "", "", "405", "307", "888", "2400", "Cooking Wine", "Ginger", "Appearence")
            await client.say(embed = embed)
        elif ldish == "baked lobster":
            foodstats = ["137", "151", "166", "183", "201", "75", "105", "135", "165", "225", "19", "18", "18", "17", "16", "180", "46"]
            embed = output3(foodstats, "Baked Lobster", 0xe74c3c, "Gloriville", "Cheese (6-2)", "Rock Lobsters (23-5)", "", "", "", "835", "388", "2300", "477", "Cooking Wine", "Garlic", "Texture")
            await client.say(embed = embed)
        elif ldish == "crab salad":
            foodstats = ["53", "58", "64", "70", "77", "245", "343", "441", "539", "735", "8", "8", "8", "7", "7", "70", "18"]
            embed = output3(foodstats, "Crab Salad", 0xe74c3c, "Gloriville", "Lettuce (3-1)", "King Crab (24-2)", "", "", "", "600", "2200", "600", "600", "Salad Dressing", "Salt", "Aroma")
            await client.say(embed = embed)
        elif ldish == "baked potato":
            foodstats = ["24", "26", "29", "32", "35", "35", "49", "63", "77", "105", "3", "3", "3", "2", "2", "60", "8"]
            embed = output3(foodstats, "Baked Potato", 0xf1c40f, "Sakurajima", "Potato (1-3)", "", "", "", "", "725", "813", "1500", "962", "Scallion", "Cooking Oil", "Texture")
            await client.say(embed = embed)
        elif ldish == "grilled pork belly":
            foodstats = ["24", "26", "29", "32", "35", "45", "63", "81", "99", "135", "3", "3", "3", "2", "2", "60", "8"]
            embed = output3(foodstats, "Grilled Pork Belly", 0x9c5d15, "Sakurajima", "Pork Belly (1-6)", "", "", "", "", "912", "692", "796", "1600", "Sugar", "Cooking Wine", "Appearence")
            await client.say(embed = embed)
        elif ldish == "cucumber salad":
            foodstats = ["24", "26", "29", "32", "35", "165", "231", "297", "363", "495", "3", "3", "3", "2", "2", "60", "8"]
            embed = output3(foodstats, "Cucumber Salad", 0x2ecc71, "Sakurajima", "Cucumber (2-2)", "", "", "", "", "607", "1800", "984", "609", "Sugar", "Rock Sugar", "Aroma")
            await client.say(embed = embed)
        elif ldish == "boiled lettuce":
            foodstats = ["53", "58", "64", "70", "77", "55", "77", "99", "121", "165", "8", "8", "8", "7", "7", "120", "18"]
            embed = output3(foodstats, "Boiled Lettuce", 0x2ecc71, "Sakurajima", "Lettuce (3-1)", "", "", "", "", "1500", "707", "992", "801", "Chili", "Garlic", "Flavor")
            await client.say(embed = embed)
        elif ldish == "mushroom yaki":
            foodstats = ["72", "79", "87", "96", "106", "125", "175", "225", "275", "375", "11", "10", "10", "9", "9", "150", "24"]
            embed = output3(foodstats, "Mushroom Yaki", 0xffeea9, "Sakurajima", "Mushroom (7-3)", "Butter (7-8)", "", "", "", "717", "876", "1700", "707", "Black Pepper", "Ginger", "Texture")
            await client.say(embed = embed)
        elif ldish == "salmon sashimi":
            foodstats = ["31", "34", "37", "41", "45", "35", "49", "63", "77", "105", "7", "7", "7", "6", "6", "90", "14"]
            embed = output3(foodstats, "Salmon Sashimi", 0xe67e22, "Sakurajima", "Salmon (4-2)", "", "", "", "", "771", "1500", "910", "819", "Soy Sauce", "Salt", "Aroma")
            await client.say(embed = embed)
        elif ldish == "beef tartare":
            foodstats = ["79", "87", "96", "106", "117", "225", "315", "405", "495", "675", "12", "11", "11", "10", "10", "180", "26"]
            embed = output3(foodstats, "Beef Tartare", 0xe74c3c, "Sakurajima", "Egg (5-2)", "Beef Tenderloin (5-6)", "", "", "", "587", "515", "898", "2000", "Garlic", "Ginger", "Appearence")
            await client.say(embed = embed)
        elif ldish == "tamagoyaki":
            foodstats = ["43", "47", "52", "57", "63", "105", "147", "189", "231", "315", "7", "7", "7", "6", "6", "90", "14"]
            embed = output3(foodstats, "Tamagoyaki", 0xf1c40f, "Sakurajima", "Carrot (3-5)", "Egg (5-2)", "Shiitake (6-8)", "", "", "2000", "694", "888", "418", "Icing", "Scallion", "Flavor")
            await client.say(embed = embed)
        elif ldish == "omurice":
            foodstats = ["29", "32", "35", "39", "43", "75", "105", "135", "165", "225", "5", "5", "5", "4", "4", "60", "10"]
            embed = output3(foodstats, "Omurice", 0xf1c40f, "Sakurajima", "Egg (5-2)", "Rice (8-2)", "", "", "", "354", "2100", "607", "939", "Salad Dressing", "Salt", "Aroma")
            await client.say(embed = embed)
        elif ldish == "shogayaki":
            foodstats = ["62", "68", "75", "83", "91", "45", "63", "81", "99", "135", "14", "13", "13", "12", "11", "120", "21"]
            embed = output3(foodstats, "Shogayki", 0xc27c0e, "Sakurajima", "Pork Loin (9-2)", "Onion (9-5)", "", "", "", "835", "388", "2300", "477", "Scallion", "Chili", "Texture")
            await client.say(embed = embed)
        elif ldish == "bacon bites":
            foodstats = ["94", "103", "113", "124", "136", "45", "63", "81", "99", "135", "14", "13", "13", "12", "11", "180", "31"]
            embed = output3(foodstats, "Bacon Bites", 0xeb7c7c, "Sakurajima", "Bread (4-4)", "Cheese (6-2)", "Bacon (10-3)", "", "", "617", "687", "896", "1800", "Salad Dressing", "Black Pepper", "Appearence")
            await client.say(embed = embed)
        elif ldish == "cold tofu":
            foodstats = ["62", "68", "75", "83", "91", "145", "203", "261", "319", "435", "9", "9", "9", "8", "8", "90", "21"]
            embed = output3(foodstats, "Cold Tofu", 0xffffff, "Sakurajima", "Tofu (10-6)", "", "", "", "", "2300", "354", "514", "832", "Garlic", "Scallion", "Flavor")
            await client.say(embed = embed)
        elif ldish == "grilled corn":
            foodstats = ["39", "43", "47", "52", "57", "125", "175", "225", "275", "375", "6", "6", "6", "5", "5", "70", "13"]
            embed = output3(foodstats, "Grilled Corn", 0xf1c40f, "Sakurajima", "Corn (11-2)", "Cream (11-7)", "", "", "", "902", "1600", "754", "744", "Condensed Milk", "Salad Dressing", "Aroma")
            await client.say(embed = embed)
        elif ldish == "vegetable tempura":
            foodstats = ["101", "111", "122", "134", "147", "125", "175", "225", "275", "375", "15", "14", "14", "13", "12", "180", "34"]
            embed = output3(foodstats, "Vegetable Tempura", 0xffeea9, "Sakurajima", "Eggplant (2-7)", "Shiitake (6-8)", "Flour (12-2)", "", "", "1600", "938", "756", "706", "Salt", "Cooking Oil", "Flavor")
            await client.say(embed = embed)
        elif ldish == "takoyaki":
            foodstats = ["67", "74", "81", "89", "98", "245", "343", "441", "539", "735", "10", "10", "10", "9", "9", "120", "22"]
            embed = output3(foodstats, "Takoyaki", 0x9c5d15, "Sakurajima", "Octopus (11-4)", "Flour (12-2)", "Cabbage (13-5)", "", "", "888", "705", "1700", "707", "Soy Sauce", "Salad Dressing", "Texture")
            await client.say(embed = embed)
        elif ldish == "creamed spinach":
            foodstats = ["36", "40", "44", "48", "53", "145", "203", "261", "319", "435", "6", "6", "6", "5", "5", "60", "12"]
            embed = output3(foodstats, "Creamed Spinach", 0x1f8b4c, "Sakurajima", "Cream (11-7)", "Spinach (13-6)", "", "", "", "875", "2200", "609", "316", "Black Pepper", "Sugar", "Aroma")
            await client.say(embed = embed)
        elif ldish == "baked pineapple":
            foodstats = ["108", "119", "131", "144", "158", "55", "77", "99", "121", "165", "16", "15", "15", "14", "13", "180", "36"]
            embed = output3(foodstats, "Baked Pineapple", 0xf1c40f, "Sakurajima", "Pineapple (14-3)", "Honey (14-6)", "", "", "", "405", "888", "2400", "307", "Cooking Oil", "Rock Sugar", "Texture")
            await client.say(embed = embed)
        elif ldish == "apples & cream":
            foodstats = ["42", "46", "51", "56", "62", "75", "105", "135", "165", "225", "6", "6", "6", "5", "5", "70", "14"]
            embed = output3(foodstats, "Apples & Cream", 0xe74c3c, "Sakurajima", "Cream (11-7)", "Apple (15-1)", "", "", "", "508", "413", "979", "2100", "Rock Sugar", "Icing", "Appearence")
            await client.say(embed = embed)
        elif ldish == "chicken skewer":
            foodstats = ["58", "64", "70", "77", "85", "85", "119", "153", "187", "255", "9", "9", "9", "8", "8", "90", "19"]
            embed = output3(foodstats, "Chicken Skewer", 0x9c5d15, "Sakurajima", "Green Pepper (6-6)", "Diced Chicken (16-5)", "", "", "", "680", "1900", "858", "562", "Cooking Wine", "Chili", "Aroma")
            await client.say(embed = embed)
        elif ldish == "fried chicken":
            foodstats = ["96", "106", "117", "129", "142", "225", "315", "405", "495", "675", "14", "13", "13", "12", "11", "150", "32"]
            embed = output3(foodstats, "Fried Chicken", 0xffeea9, "Sakurajima", "Egg (5-2)", "Flour (12-2)", "Whole Chicken (16-6)", "", "", "808", "2200", "397", "595", "Chili", "Garlic", "Aroma")
            await client.say(embed = embed)
        elif ldish == "mango smoothie":
            foodstats = ["115", "127", "140", "154", "169", "185", "259", "333", "407", "555", "17", "16", "16", "15", "14", "180", "38"]
            embed = output3(foodstats, "Mango Smoothie", 0xe67e22, "Sakurajima", "Cream (11-7)", "Mango (17-3)", "", "", "", "1700", "750", "800", "750", "Condensed Milk", "Sago", "Flavor")
            await client.say(embed = embed)
        elif ldish == "strawberry smoothie":
            foodstats = ["48", "53", "58", "64", "70", "185", "259", "333", "407", "555", "7", "7", "7", "6", "6", "70", "16"]
            embed = output3(foodstats, "Strawberry Smoothie", 0xff91b6, "Sakurajima", "Cream (11-7)", "Milk (12-5)", "Strawberry (18-1)", "", "", "683", "801", "416", "2100", "Rock Sugar", "Sago", "Appearence")
            await client.say(embed = embed)
        elif ldish == "peanut crisp":
            foodstats = ["61", "67", "74", "81", "89", "165", "231", "297", "363", "495", "9", "9", "9", "8", "8", "90", "20"]
            embed = output3(foodstats, "Peanut Crisp", 0xffeea9, "Sakurajima", "Flour (12-2)", "Milk (12-5)", "Peanut (19-3)", "", "", "556", "537", "907", "2000", "Salt", "Sugar", "Appearence")
            await client.say(embed = embed)
        elif ldish == "cod fillet":
            foodstats = ["65", "72", "79", "87", "96", "205", "287", "369", "451", "615", "9", "9", "9", "8", "8", "90", "22"]
            embed = output3(foodstats, "Cod Fillet", 0xffeea9, "Sakurajima", "Butter (7-8)", "Starch (13-9)", "Cod (22-2)", "", "", "600", "600", "2200", "600", "Cooking Wine", "Black Pepper", "Texture")
            await client.say(embed = embed)
        elif ldish == "piglet daifuku":
            foodstats = ["122", "134", "147", "162", "178", "245", "343", "441", "537", "735", "18", "17", "17", "16", "15", "180", "41"]
            embed = output3(foodstats, "Piglet Daifuku", 0xffeea9, "Sakurajima", "Egg (5-2)", "Flour (12-2)", "Red Beans (19-5)", "", "", "504", "658", "938", "1900", "Icing", "Condensed Milk", "Appearence")
            await client.say(embed = embed)
        elif ldish == "pumpkin muffin":
            foodstats = ["43", "47", "52", "57", "63", "205", "287", "369", "451", "615", "6", "6", "6", "5", "5", "60", "14"]
            embed = output3(foodstats, "Pumpkin Muffin", 0xe67e22, "Sakurajima", "Honey (14-6)", "(Red Beans (19-5)", "Pumpkin (20-5)", "", "", "972", "506", "1800", "722", "Sago", "Condensed Milk", "Texture")
            await client.say(embed = embed)
        elif ldish == "yam dumplings":
            foodstats = ["86", "95", "105", "116", "128", "245", "343", "441", "539", "735", "12", "11", "11", "10", "10", "120", "29"]
            embed = output3(foodstats, "Yam Dumplings", 0x9b59b6, "Sakurajima", "Rice Flour (20-7)", "Purple Yam (21-3)", "", "", "", "1900", "988", "682", "430", "Sago", "Icing", "Flavor")
            await client.say(embed = embed)
        elif ldish == "unagi don":
            foodstats = ["114", "125", "138", "152", "167", "245", "343", "441", "539", "735", "16", "15", "15", "14", "13", "150", "38"]
            embed = output3(foodstats, "Unagi Don", 0x992d22, "Sakurajima", "Rice (8-2)", "Eel (22-5)", "", "", "", "2300", "422", "868", "410", "Cooking Oil", "Cooking Wine", "Flavor")
            await client.say(embed = embed)
        elif ldish == "lobster sashimi":
            foodstats = ["137", "151", "166", "183", "201", "105", "147", "189", "231", "315", "19", "18", "18", "17", "16", "180", "46"]
            embed = output3(foodstats, "Lobster Sashimi", 0x607d8b, "Sakurajima", "Rock Lobsters (23-5)", "", "", "", "", "493", "285", "822", "2400", "Ginger", "Soy Sauce", "Appearence")
            await client.say(embed = embed)
        elif ldish == "crab sashimi":
            foodstats = ["53", "58", "64", "70", "77", "245", "343", "441", "539", "735", "8", "8", "8", "7", "7", "70", "18"]
            embed = output3(foodstats, "Crab Sashimi", 0xe74c3c, "Sakurajima", "King Crab (24-2)", "", "", "", "", "409", "2400", "227", "964", "Ginger", "Soy Sauce", "Aroma")
            await client.say(embed = embed)

# Food soul's info commands:

##
##@client.command(name = "soulinfo")
##@commands.cooldown(1, 3, commands.BucketType.user)
##async def soulinfo(food_soul):
##    lfood_soul = food_soul.lower()
##    if lsoul in lsummon_pool or lsoul in lnone_pool or lsoul in levent_pool or lsoul in lunre_pool:
##        pass

# Non-summoning commands:

client.remove_command('help')

@client.command(name = "help")
@commands.cooldown(1, 20, commands.BucketType.user)
async def help():
    helplist = [["f!summon <amount>", "Summons a desired amount of food souls from the current summoning pool.\\nExample: f!summon 100 will summon 100 food souls from the current summoning pool."],
                ["f!foodsoul <food_soul> <amount>", 'Summons endlessly until a specific food soul of a specified amount has been summoned. Use "." instead of spaces.\nExample: f!foodsoul Bamboo.Rice 2 will summon endlessly until two Bamboo Rice have been summoned.'],
                ["f!rates", "Checks the probability rates of the food souls in the current summoning pool."],
                ["f!eventindex", "Shows the event index number to key into f!summonevent or f!event."],
                ["f!esummon <event_index> <amount>", 'Summons a desired amount of food souls from an event. Use f!eventindex to check the event index number\nExample: f!summonevent 2 100 will summon 100 times during the "Brewing Fine Wine" event.'],
                ["f!efoodsoul <event_index> <food_soul> <amount>", 'Summon endlessly from an event until a specific food soul of a specified amount has been summoned. Use f!eventindex to check the event index.\nExample: f!event 2 foodsoul sweet.tofu 2 will summon endlessly during the "Brewing Fine Wine" event until it summons 2 Sweet Tofu.'],
                ["f!erates <event_index>", "Checks the probability rates of the food souls in any summoning event. Check the event index using f!eventindex"],
                ["f!food <dish>", 'Shows the stats and information of a dish. Use "." instead of space.\nExample: f!food buuter.bread will show the stats and information of Butter Bread.'],
                ["f!soulinfo <food_soul>", 'Shows the information about a food soul. Use "." instead of space.\nNOTE: This feature is UNRELEASED.'],
                ["f!update", "Checks the latest version of the bot and most recent updates"],
                ["f!credits", "Reveals the people behind the bot."]]
    embed = discord.Embed(title = "Foie Gras", description = 'Hello. My name is Foie Gras. How may I help you today? I will await your command. My prefix is "f!" or "F!"', color = 0x3498db)
    for helpcount in range(len(helplist)):
        embed.add_field(name = helplist[helpcount][0], value = helplist[helpcount][1], inline = False)
    await client.say(embed = embed)

@client.command(name = "update")
@commands.cooldown(1, 30, commands.BucketType.user)
async def update():
    updatelist = [["Event summoning: Flame Storm added", "You can summon from the summon event: Flame Storm now!"],
                  ["Probability rates can be checked", "You can use f!rates or f!erates to check the rates of the current summoning pull and the event summoning pools"]]
    embed = discord.Embed(title = "Bot Update (v2.12)", description = "If there are any problems with the bot, please ping @「Pengu Pout」ディラン (Dylan) and state the problem.", color = 0x3498db)
    for updatecount in range(len(updatelist)):
        embed.add_field(name = updatelist[updatecount][0], value = updatelist[updatecount][1], inline = False)
    await client.say(embed = embed)

@client.command(name = "credits")
@commands.cooldown(1, 30, commands.BucketType.user)
async def credit():
    await client.say("\
**All nicknames are from the Food Fantasy Discord Server.**\n\
Developer: Monokhorome#2353 AKA 「Pengu Pout」ディラン (Dylan)\n\
Speical thanks to cyn#1598 AKA Just Marisa and Madara#0483 AKA [Thirsty] MadaraKeehl for assisting me with the base programming of the bot!")

@client.event
async def on_command_error(error, context):
    if isinstance(error, commands.CommandOnCooldown):
        await client.send_message(context.message.channel, "Please do not spam. There is only so much I can handle")

@client.event
async def on_ready():
    await client.change_presence(game=Game(name = "with Master Attendant"))
    print(client.user.name + " is online.")

client.run(TOKEN)
