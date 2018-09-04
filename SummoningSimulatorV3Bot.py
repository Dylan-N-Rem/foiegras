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
prefix = ("f!")
client = Bot(command_prefix = prefix)

# v3:

summon_pool = ["Crab Long Bao", "Foie Gras", "Peking Duck", "B-52", "Bamboo Rice", "Gingerbread", "Boston Lobster", "Double Scoop", "Tiraumisu", "Escargot", "Hotdog", "Mango Pudding", "Hamburger", "Steak", "Tangyuan", "Sanma", "Napoleon Cake", "Salad", "Pastel de nata", "Yuxiang", "Sukiyaki", "Brownie", "Red Wine", "Gyoza", "Chocolate", "Eggette", "Pineapple Cake", "Skewer", "Jello", "Pancake", "Popcorn", "Long Bao", "Coffee", "Sashimi", "Macaron", "Zongzi", "Sakuramochi", "Tom Yum", "Taiyaki", "Milk", "Dorayaki", "Sake", "Tempura", "Spicy Gluten", "Jiuniang", "Omurice", "Orange Juice", "Ume Ochazuke", "Miso Soup", "Yellow Wine"]
ur_pool = ["Crab Long Bao", "Foie Gras", "Peking Duck", "B-52", "Bamboo Rice", "Gingerbread", "Boston Lobster", "Double Scoop"]
sr_pool = ["Tiraumisu", "Escargot", "Hotdog", "Mango Pudding", "Hamburger", "Steak", "Tangyuan", "Sanma", "Napoleon Cake", "Salad", "Pastel de nata", "Yuxiang", "Sukiyaki", "Brownie", "Red Wine", "Gyoza", "Chocolate", "Eggette", "Pineapple Cake"]
r_pool = ["Long Bao", "Coffee", "Sashimi", "Macaron", "Zongzi", "Sakuramochi", "Tom Yum", "Taiyaki", "Milk", "Dorayaki", "Sake", "Tempura", "Spicy Gluten", "Jiuniang", "Omurice", "Orange Juice", "Ume Ochazuke", "Miso Soup", "Yellow Wine"]
m_pool = ["Skewer", "Jello", "Pancake", "Popcorn"]
rarity_pool = ["M", "R", "SR", "UR"]
food_pool = ["Stir-Fried Potatoes", "Braised Pork", "Braised Eggplant", "Sauteed Lettuce", "Carrot Bread", "Cucumber Egg Stir-Fry", "Black Pepper Beef", "Sauteed Mushrooms", "Egg Fried Rice", "Salmon Fried Rice", "Onion Fried Rice", "Bacon Fried Rice", "Braised Octopus", "Risotto", "Butter Bread", "Emerald Roll", "Corn Pie", "Toffee Apple", "Pineapple Fried Rice", "Chicken Soup", "Mango Pudding", "Strawberry Ice Cream", "Red Bean Pudding", "Kung Pao Chicken", "Pumpkin Pie", "Sweet Yam Buns", "Steamed Cod", "Steamed Unagi", "Garlic Lobster", "Crab Hotpot", "French Fries", "Crispy Pork", "Salad", "Eggplant Roll", "Smoked Salmon", "Roast Beef", "Cheese Bread", "Mushroom Soup", "Fried Rice Cake", "Pork Burger", "Bacon Tofu Wrap", "Grilled Calamari", "Popcorn", "Shortbread", "Minestrone", "Pineapple Juice", "Apple Crisp", "Chicken Pizza", "Roast Chicken", "Mango Wrap", "Fruit Salad", "Peanut Pie", "Pumpkin Soup", "Hotteok", "Cheesy Yam", "Fried Cod", "Fried Unagi", "Baked Lobster", "Crab Salad", "Baked Potato", "Grilled Pork Belly", "Cucumber Salad", "Boiled Lettuce", "Mushroom Yaki", "Salmon Sashimi", "Beef Tartare", "Tamagoyaki", "Omurice", "Shogayki", "Bacon Bites", "Cold Tofu", "Grilled Corn", "Vegetable Tempura", "Takoyaki", "Creamed Spinach", "Baked Pineapple", "Apples & Cream", "Chicken Skewer", "Fried Chicken", "Mango Smoothie", "Strawberry Smoothie", "Peanut Crisp", "Cod Fillet", "Piglet Daifuku", "Pumpkin Muffin", "Yam Dumplings", "Unagi Don", "Lobster Sashimi", "Crab Sashimi"]
lostfood_pool = ["Calamari Skewer", "Garlic Oyster", "Grilled Prawns", "Pickled Salmon Head", "Tomato & Eggs", "Steamed Mushrooms", "Spaghetti", "Har Gow", "Gold Cake", "Mixed Greens", "Stir-Fried Mussels", "Mushroom Alfredo", "Cha Siu Bao", "Spinach Noodles", "Mint Pineapple", "Apple Sangria", "Braised Lamb", "Mushroom Chicken Stew", "Matcha Cake", "Cappuccino", "Fruit Tea", "Lemon Pie", "Meat Zongzi", "Stuffed Lotus Root", "Lotus Root Stir-Fry", "Black Fungus Congee", "Sanma Shioyaki", "Steamed Crab", "Crab Rice Cake", "Curry Crab", "Yam Pigeon Soup", "Bamboo & Meat Stir-Fry", "Braised Geese", "Roe Meat Ball", "Birds Nest", "Ginseng Stew Chicken"]
roll = []
for u1 in range(23):
    roll += ["Crab Long Bao", ]
for u2 in range(61):
    roll += ["Foie Gras", ]
for u3 in range(61):
    roll += ["Peking Duck", ]
for u4 in range(61):
    roll += ["B-52", ]
for u5 in range(62):
    roll += ["Bamboo Rice", ]
for u6 in range(23):
    roll += ["Gingerbread", ]
for u7 in range(5):
    roll += ["Boston Lobster", ]
for u8 in range(5):
    roll += ["Double Scoop", ]
for s1 in range(80):
    roll += ["Tiramisu", ]
for s2 in range(80):
    roll += ["Escargot", ]
for s3 in range(80):
    roll += ["Hotdog", ]
for s4 in range(80):
    roll += ["Mango Pudding", ]
for s5 in range(80):
    roll += ["Hamburger",]
for s6 in range(80):
    roll += ["Steak", ]
for s7 in range(80):
    roll += ["Tangyuan", ]
for s8 in range(80):
    roll += ["Sanma", ]
for s9 in range(80):
    roll += ["Napoleon Cake", ]
for s10 in range(80):
    roll += ["Salad", ]
for s11 in range(80):
    roll += ["Pastel de nata", ]
for s12 in range(80):
    roll += ["Yuxiang", ]
for s13 in range(80):
    roll += ["Sukiyaki", ]
for s14 in range(80):
    roll += ["Brownie", ]
for s15 in range(80):
    roll += ["Red Wine", ]
for s16 in range(80):
    roll += ["Gyoza", ]
for s17 in range(80):
    roll += ["Chocolate", ]
for s18 in range(150):
    roll += ["Eggette", ]
for s19 in range(151):
    roll += ["Pineapple Cake", ]
for r1 in range(413):
    roll += ["Long Bao", ]
for r2 in range(413):
    roll += ["Coffee", ]
for r3 in range(413):
    roll += ["Sashimi", ]
for r4 in range(413):
    roll += ["Macaron", ]
for r5 in range(413):
    roll += ["Zongzi", ]
for r6 in range(413):
    roll += ["Sakuramochi", ]
for r7 in range(413):
    roll += ["Tom Yum", ]
for r8 in range(413):
    roll += ["Taiyaki", ]
for r9 in range(413):
    roll += ["Milk", ]
for r10 in range(413):
    roll += ["Dorayaki", ]
for r11 in range(413):
    roll += ["Sake", ]
for r12 in range(413):
    roll += ["Tempura", ]
for r13 in range(413):
    roll += ["Spicy Gluten", ]
for r14 in range(414):
    roll += ["Jiuniang", ]
for r15 in range(414):
    roll += ["Omurice", ]
for r16 in range(414):
    roll += ["Orange Juice", ]
for r17 in range(414):
    roll += ["Ume Ochazuke" ,]
for r18 in range(414):
    roll += ["Miso Soup" ,]
for r19 in range(414):
    roll += ["Yellow Wine", ]
for m1 in range(46):
    roll += ["Skewer", ]
for m2 in range(46):
    roll += ["Jello", ]
for m3 in range(46):
    roll += ["Pancake", ]
for m4 in range(47):
    roll += ["Popcorn", ]
lsummon_pool = [items.lower() for items in summon_pool]
lrarity_pool = [itemr.lower() for itemr in rarity_pool]
lfood_pool = [itemd.lower() for itemd in food_pool]
llostfood_pool = [iteml.lower() for iteml in lostfood_pool]

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

def output2(dishname, colour, cuisine, ingredient1, ingredient2, ingredient3, level, quest, flavor, texture, aroma, appearence, season1, season2, attribute):
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
    return foodoutput

@client.command(name = "channel",
                pass_context = True)
async def channel(ctx):
    global onlychannel
    if ctx.message.author.server_permissions.administrator:
        onlychannel = ctx.message.channel.id
        with open("channelfile.txt", "w") as xfile:
            json.dump(onlychannel, xfile)
        await client.say("Very well. Commands should only be used here.")

def restriction(context):
    with open("channelfile.txt") as file:
        onlychannel = json.load(file)
    if context.message.channel.id != onlychannel:
        return False
    elif context.message.channel.id == onlychannel:
        return True

@commands.check(restriction)
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
    elif int(number) >= 1:
        await client.say("Summoning food souls...")
        time.sleep(2)
        number = int(number)
        valid = True
        for x in range(number):
            foodsoul = random.choice(roll)
            summoned += [foodsoul, ]
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
async def afoodsoul(context, food_soul, amount):
    summoned = []
    eachsummoned = []
    ur = 0
    sr = 0
    r = 0
    m = 0
    number = 0
    valid = False
    food_soul = food_soul.replace(".", " ")
    lfood_soul = food_soul.lower()
    if not(amount.isdigit()):
        await client.say('Error - Invalid 1st input: Use "." instead of space')
    if int(amount) <= 0:
        await client.say("Error - Invalid 2nd input: Number must be more than 0")
    elif lfood_soul not in lsummon_pool:
        await client.say("Error - Invalid 1st input: Food Soul does not exsist or improper spelling")
    elif lfood_soul in lsummon_pool and int(amount) >= 1:
        await client.say("Summoning food souls...\n")
        time.sleep(2)
        count_foodsoul = 0
        while int(amount) != count_foodsoul:
            foodsoul = random.choice(roll)
            valid = True
            lfoodsoul = foodsoul.lower()
            summoned += [foodsoul, ]
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

@client.command(name = 'rarity',
               pass_context = True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def rarity(context, rarity, amount):
    summoned = []
    eachsummoned = []
    ur = 0
    sr = 0
    r = 0
    m = 0
    number = 0
    valid = False
    lrarity = rarity.lower()
    if lrarity not in lrarity_pool:
        await client.say("Error - Invalid 1st input: Rarity does not exsist or improper spelling")
    if not(amount.isdigit()):
        await client.say("Error - Invalid 2nd input: Must be a positive integer")
    elif int(amount) <= 0:
        await client.say("Error - Invalid 2nd input: Number must be more than 0")
    elif lrarity in lrarity_pool and int(amount) >= 1:
        valid = True
        await client.say("Summoning food souls...\n")
        time.sleep(2)
        count_foodsoul = 0
        while int(amount) != count_foodsoul:
            foodsoul = random.choice(roll)
            summoned += [foodsoul, ]
            if foodsoul in ur_pool:
                ur += 1
                number += 1
                if lrarity == "ur":
                    count_foodsoul += 1
            elif foodsoul in sr_pool:
                sr += 1
                number += 1
                if lrarity == "sr":
                    count_foodsoul += 1
            elif foodsoul in r_pool:
                r += 1
                number += 1
                if lrarity == "r":
                    count_foodsoul += 1
            elif foodsoul in m_pool:
                m += 1
                number += 1
                if lrarity == "m":
                    count_foodsoul += 1
    bigline = output(summoned, valid, ur, sr, r, m, number, context)
    await client.say(bigline)

# v4:

csummon_pool = ["Crab Long Bao", "Foie Gras", "Peking Duck", "B-52", "Bamboo Rice", "Gingerbread", "Boston Lobster", "Double Scoop", "Sweet Tofu", "Laba Congee", "Yunnan Noodles", "Udon", "Tiraumisu", "Escargot", "Hotdog", "Mango Pudding", "Hamburger", "Steak", "Tangyuan", "Sanma", "Napoleon Cake", "Salad", "Pastel de nata", "Yuxiang", "Sukiyaki", "Brownie", "Red Wine", "Gyoza", "Chocolate", "Eggette", "Pineapple Cake", "Skewer", "Jello", "Pancake", "Popcorn", "Cold Rice Shrimp", "Long Bao", "Coffee", "Sashimi", "Macaron", "Zongzi", "Sakuramochi", "Tom Yum", "Taiyaki", "Milk", "Dorayaki", "Sake", "Tempura", "Spicy Gluten", "Jiuniang", "Omurice", "Orange Juice", "Ume Ochazuke", "Miso Soup", "Yellow Wine"]
cur_pool = ["Crab Long Bao", "Foie Gras", "Peking Duck", "B-52", "Bamboo Rice", "Gingerbread", "Boston Lobster", "Double Scoop"]
csr_pool = ["Sweet Tofu", "Laba Congee", "Yunnan Noodles", "Udon", "Tiraumisu", "Escargot", "Hotdog", "Mango Pudding", "Hamburger", "Steak", "Tangyuan", "Sanma", "Napoleon Cake", "Salad", "Pastel de nata", "Yuxiang", "Sukiyaki", "Brownie", "Red Wine", "Gyoza", "Chocolate", "Eggette", "Pineapple Cake"]
cr_pool = ["Cold Rice Shrimp", "Long Bao", "Coffee", "Sashimi", "Macaron", "Zongzi", "Sakuramochi", "Tom Yum", "Taiyaki", "Milk", "Dorayaki", "Sake", "Tempura", "Spicy Gluten", "Jiuniang", "Omurice", "Orange Juice", "Ume Ochazuke", "Miso Soup", "Yellow Wine"]
cm_pool = ["Skewer", "Jello", "Pancake", "Popcorn"]
rarity_pool = ["M", "R", "SR", "UR"]
croll = []
for cu1 in range(36):
    croll += ["Crab Long Bao", ]
for cu2 in range(57):
    croll += ["Foie Gras", ]
for cu3 in range(61):
    croll += ["Peking Duck", ]
for cu4 in range(61):
    croll += ["B-52", ]
for cu5 in range(52):
    croll += ["Bamboo Rice", ]
for cu6 in range(25):
    croll += ["Gingerbread", ]
for cu7 in range(4):
    croll += ["Boston Lobster", ]
for cu8 in range(5):
    croll += ["Double Scoop", ]
for cs1 in range(60):
    croll += ["Tiramisu", ]
for cs2 in range(65):
    croll += ["Escargot", ]
for cs3 in range(63):
    croll += ["Hotdog", ]
for cs4 in range(61):
    croll += ["Mango Pudding", ]
for cs5 in range(59):
    croll += ["Hamburger",]
for cs6 in range(61):
    croll += ["Steak", ]
for cs7 in range(62):
    croll += ["Tangyuan", ]
for cs8 in range(61):
    croll += ["Sanma", ]
for cs9 in range(62):
    croll += ["Napoleon Cake", ]
for cs10 in range(62):
    croll += ["Salad", ]
for cs11 in range(60):
    croll += ["Pastel de nata", ]
for cs12 in range(63):
    croll += ["Yuxiang", ]
for cs13 in range(60):
    croll += ["Sukiyaki", ]
for cs14 in range(61):
    croll += ["Brownie", ]
for cs15 in range(58):
    croll += ["Red Wine", ]
for cs16 in range(60):
    croll += ["Gyoza", ]
for cs17 in range(58):
    croll += ["Chocolate", ]
for cs18 in range(155):
    croll += ["Eggette", ]
for cs19 in range(141):
    croll += ["Pineapple Cake", ]
for cs20 in range(150):
    croll += ["Laba Congee", ]
for cs21 in range(61):
    croll += ["Yunnan Noodles", ]
for cs22 in range(61):
    croll += ["Udon", ]
for cs23 in range(56):
    croll += ["Sweet Tofu", ]
for cr1 in range(400):
    croll += ["Long Bao", ]
for cr2 in range(398):
    croll += ["Coffee", ]
for cr3 in range(388):
    croll += ["Sashimi", ]
for cr4 in range(388):
    croll += ["Macaron", ]
for cr5 in range(394):
    croll += ["Zongzi", ]
for cr6 in range(394):
    croll += ["Sakuramochi", ]
for cr7 in range(394):
    croll += ["Tom Yum", ]
for cr8 in range(394):
    croll += ["Taiyaki", ]
for cr9 in range(388):
    croll += ["Milk", ]
for cr10 in range(390):
    croll += ["Dorayaki", ]
for cr11 in range(389):
    croll += ["Sake", ]
for cr12 in range(399):
    croll += ["Tempura", ]
for cr13 in range(388):
    croll += ["Spicy Gluten", ]
for cr14 in range(400):
    croll += ["Jiuniang", ]
for cr15 in range(401):
    croll += ["Omurice", ]
for cr16 in range(381):
    croll += ["Orange Juice", ]
for cr17 in range(390):
    croll += ["Ume Ochazuke" ,]
for cr18 in range(388):
    croll += ["Miso Soup" ,]
for cr19 in range(394):
    croll += ["Yellow Wine", ]
for cr20 in range(396):
    croll += ["Cold Rice Shrimp", ]
for cm1 in range(46):
    croll += ["Skewer", ]
for cm2 in range(46):
    croll += ["Jello", ]
for cm3 in range(49):
    croll += ["Pancake", ]
for cm4 in range(44):
    croll += ["Popcorn", ]
lcsummon_pool = [items.lower() for items in csummon_pool]

def output3(summoned, valid, ur, sr, r, m, number, context):
    eachsummoned = set(summoned) & set(csummon_pool)
    eachsummoned = list(eachsummoned)
    ursummoned = set(eachsummoned) & set(cur_pool)
    ursummoned = list(ursummoned)
    ursummoned.sort()
    srsummoned = set(eachsummoned) & set(csr_pool)
    srsummoned = list(srsummoned)
    srsummoned.sort()
    rsummoned = set(eachsummoned) & set(cr_pool)
    rsummoned = list(rsummoned)
    rsummoned.sort()
    msummoned = set(eachsummoned) & set(cm_pool)
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

def output4(summoned, valid, ur, sr, r, m, number, context, esummon_pool, eur_pool, esr_pool, er_pool, em_pool):
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

@commands.check(restriction)
@client.command(name = 'csummon',
                pass_context = True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def csummon(context, number):
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
    elif int(number) >= 1:
        await client.say("Summoning food souls...")
        time.sleep(2)
        number = int(number)
        valid = True
        for x in range(number):
            foodsoul = random.choice(croll)
            summoned += [foodsoul, ]
            if foodsoul in cur_pool:
                ur += 1
            elif foodsoul in csr_pool:
                sr += 1
            elif foodsoul in cr_pool:
                r += 1
            elif foodsoul in cm_pool:
                m += 1
        bigline = output3(summoned, valid, ur, sr, r, m, number, context)
        await client.say(bigline)

@commands.check(restriction)
@client.command(name = 'cfoodsoul',
                pass_context = True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def cafoodsoul(context, food_soul, amount):
    summoned = []
    eachsummoned = []
    ur = 0
    sr = 0
    r = 0
    m = 0
    number = 0
    valid = False
    food_soul = food_soul.replace(".", " ")
    lfood_soul = food_soul.lower()
    if not(amount.isdigit()):
        await client.say('Error - Invalid 1st input: Use "." instead of space')
    if int(amount) <= 0:
        await client.say("Error - Invalid 2nd input: Number must be more than 0")
    elif lfood_soul not in lcsummon_pool:
        await client.say("Error - Invalid 1st input: Food Soul does not exsist or improper spelling")
    elif lfood_soul in lcsummon_pool and int(amount) >= 1:
        await client.say("Summoning food souls...\n")
        time.sleep(2)
        count_foodsoul = 0
        while int(amount) != count_foodsoul:
            foodsoul = random.choice(croll)
            valid = True
            lfoodsoul = foodsoul.lower()
            summoned += [foodsoul, ]
            if foodsoul in cur_pool:
                ur += 1
                number += 1
            if foodsoul in csr_pool:
                sr += 1
                number += 1
            if foodsoul in cr_pool:
                r += 1
                number += 1
            if foodsoul in cm_pool:
                m += 1
                number += 1
            if lfood_soul == lfoodsoul:
                count_foodsoul += 1
    bigline = output3(summoned, valid, ur, sr, r, m, number, context)
    await client.say(bigline)

@commands.check(restriction)
@client.command(name = 'crarity',
                pass_context = True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def crarity(context, rarity, amount):
    summoned = []
    eachsummoned = []
    ur = 0
    sr = 0
    r = 0
    m = 0
    number = 0
    valid = False
    lrarity = rarity.lower()
    if lrarity not in lrarity_pool:
        await client.say("Error - Invalid 1st input: Rarity does not exsist or improper spelling")
    if not(amount.isdigit()):
        await client.say("Error - Invalid 2nd input: Must be a positive integer")
    elif int(amount) <= 0:
        await client.say("Error - Invalid 2nd input: Number must be more than 0")
    elif lrarity in lrarity_pool and int(amount) >= 1:
        valid = True
        await client.say("Summoning food souls...\n")
        time.sleep(2)
        count_foodsoul = 0
        while int(amount) != count_foodsoul:
            foodsoul = random.choice(croll)
            summoned += [foodsoul, ]
            if foodsoul in cur_pool:
                ur += 1
                number += 1
                if lrarity == "ur":
                    count_foodsoul += 1
            elif foodsoul in csr_pool:
                sr += 1
                number += 1
                if lrarity == "sr":
                    count_foodsoul += 1
            elif foodsoul in cr_pool:
                r += 1
                number += 1
                if lrarity == "r":
                    count_foodsoul += 1
            elif foodsoul in cm_pool:
                m += 1
                number += 1
                if lrarity == "m":
                    count_foodsoul += 1
    bigline = output3(summoned, valid, ur, sr, r, m, number, context)
    await client.say(bigline)

@commands.check(restriction)
@client.command(name = "event",
                pass_context = True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def event1(context, event_index, mode, foodsoul_or_rarity, amount):
    vaalid = False
    eroll = []
    eroll += roll
    esummon_pool = []
    esummon_pool += summon_pool
    eur_pool = []
    eur_pool += ur_pool
    esr_pool = []
    esr_pool += sr_pool
    er_pool = []
    er_pool += r_pool
    em_pool = []
    em_pool += m_pool
    if event_index == "0":
        vaalid = True
        esummon_pool += ["Toso", "Sweet Tofu", ]
        eur_pool += ["Toso", ]
        esr_pool += ["Sweet Tofu", ]
        for e1 in range(15):
            eroll += ["Toso", ]
        for e2 in range(3):
            eroll.remove("B-52")
        for e3 in range(3):
            eroll.remove("Foie Gras")
        for e4 in range(3):
            eroll.remove("Crab Long Bao")
        for e5 in range(3):
            eroll.remove("Bamboo Rice")
        for e6 in range(3):
            eroll.remove("Peking Duck")
        for e7 in range(641):
            eroll += ["Sweet Tofu", ]
        for e8 in range(65):
            eroll.remove("Pineapple Cake")
        for e9 in range(66):
            eroll.remove("Eggette")
        for e10 in range(3):
            eroll.remove("Tiramisu")
        for e11 in range(3):
            eroll.remove("Escargot")
        for e12 in range(3):
            eroll.remove("Hotdog")
        for e13 in range(3):
            eroll.remove("Mango Pudding")
        for e14 in range(3):
            eroll.remove("Hamburger")
        for e15 in range(3):
            eroll.remove("Steak")
        for e16 in range(3):
            eroll.remove("Tangyuan")
        for e17 in range(3):
            eroll.remove("Sanma")
        for e18 in range(3):
            eroll.remove("Napoleon Cake")
        for e19 in range(3):
            eroll.remove("Salad")
        for e20 in range(3):
            eroll.remove("Pastel de nata")
        for e21 in range(3):
            eroll.remove("Yuxiang")
        for e22 in range(3):
            eroll.remove("Sukiyaki")
        for e23 in range(3):
            eroll.remove("Brownie")
        for e24 in range(3):
            eroll.remove("Red Wine")
        for e25 in range(3):
            eroll.remove("Gyoza")
        for e26 in range(3):
            eroll.remove("Chocolate")
    elif event_index == "1":
        vaalid = True
        esummon_pool += ["Raindrop Cake", "Strawberry Daifuku", ]
        eur_pool += ["Raindrop Cake", ]
        em_pool += ["Strawberry Daifuku", ]
        for e1 in range(120):
            eroll += ["Raindrop Cake", ]
        for e2 in range(25):
            eroll.remove("B-52")
        for e3 in range(25):
            eroll.remove("Foie Gras")
        for e4 in range(8):
            eroll.remove("Crab Long Bao")
        for e5 in range(26):
            eroll.remove("Bamboo Rice")
        for e6 in range(25):
            eroll.remove("Peking Duck")
        for e7 in range(8):
            eroll.remove("Gingerbread")
        for e8 in range(7):
            eroll.remove("Pancake")
        for e9 in range(8):
            eroll.remove("Popcorn")
        for e10 in range(8):
            eroll.remove("Jello")
        for e11 in range(8):
            eroll.remove("Skewer")
        for e12 in range(31):
            eroll += ["Strawberry Daifuku", ]
    if vaalid == True:
        if mode != "rarity" and mode != "foodsoul":
            await client.say('Error - Invalid mode: Must be "foodsoul" or "rarity"')
        elif mode == "foodsoul":
            lesummon_pool = [iteme.lower() for iteme in esummon_pool]
            summoned = []
            eachsummoned = []
            ur = 0
            sr = 0
            r = 0
            m = 0
            number = 0
            valid = False
            food_soul = foodsoul_or_rarity
            food_soul = food_soul.replace(".", " ")
            lfood_soul = food_soul.lower()
            if not(amount.isdigit()):
                await client.say('Error - Invalid 3rd input: Use "." instead of space')
            if int(amount) <= 0:
                await client.say("Error - Invalid 4th input: Number must be more than 0")
            elif lfood_soul not in lesummon_pool:
                await client.say("Error - Invalid 3rd input: Food Soul does not exsist or improper spelling")
            elif lfood_soul in lesummon_pool and int(amount) >= 1:
                await client.say("Summoning food souls...\n")
                time.sleep(2)
                count_foodsoul = 0
                while int(amount) != count_foodsoul:
                    foodsoul = random.choice(eroll)
                    valid = True
                    lfoodsoul = foodsoul.lower()
                    summoned += [foodsoul, ]
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
            bigline = output4(summoned, valid, ur, sr, r, m, number, context, esummon_pool, eur_pool, esr_pool, er_pool, em_pool)
            await client.say(bigline)
        elif mode == "rarity":
            summoned = []
            eachsummoned = []
            ur = 0
            sr = 0
            r = 0
            m = 0
            number = 0
            valid = False
            rarity = foodsoul_or_rarity
            lrarity = rarity.lower()
            if lrarity not in lrarity_pool:
                await client.say("Error - Invalid 3rd input: Rarity does not exsist or improper spelling")
            if not(amount.isdigit()):
                await client.say("Error - Invalid 4th input: Must be a positive integer")
            elif int(amount) <= 0:
                await client.say("Error - Invalid 4th input: Number must be more than 0")
            elif lrarity in lrarity_pool and int(amount) >= 1:
                valid = True
                await client.say("Summoning food souls...\n")
                time.sleep(2)
                count_foodsoul = 0
                while int(amount) != count_foodsoul:
                    foodsoul = random.choice(eroll)
                    summoned += [foodsoul, ]
                    if foodsoul in eur_pool:
                        ur += 1
                        number += 1
                        if lrarity == "ur":
                            count_foodsoul += 1
                    elif foodsoul in esr_pool:
                        sr += 1
                        number += 1
                        if lrarity == "sr":
                            count_foodsoul += 1
                    elif foodsoul in er_pool:
                        r += 1
                        number += 1
                        if lrarity == "r":
                            count_foodsoul += 1
                    elif foodsoul in em_pool:
                        m += 1
                        number += 1
                        if lrarity == "m":
                            count_foodsoul += 1
            bigline = output4(summoned, valid, ur, sr, r, m, number, context, esummon_pool, eur_pool, esr_pool, er_pool, em_pool)
            await client.say(bigline)

@commands.check(restriction)
@client.command(name = "summonevent",
                pass_context = True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def event2(context, event_index, number):
    vaalid = False
    event_toggle = 0
    eroll = []
    eroll += roll
    esummon_pool = []
    esummon_pool += summon_pool
    eur_pool = []
    eur_pool += ur_pool
    esr_pool = []
    esr_pool += sr_pool
    er_pool = []
    er_pool += r_pool
    em_pool = []
    em_pool += m_pool
    if event_index == "0":
        vaalid = True
        esummon_pool += ["Toso", "Sweet Tofu", ]
        eur_pool += ["Toso", ]
        esr_pool += ["Sweet Tofu", ]
        for e1 in range(15):
            eroll += ["Toso", ]
        for e2 in range(3):
            eroll.remove("B-52")
        for e3 in range(3):
            eroll.remove("Foie Gras")
        for e4 in range(3):
            eroll.remove("Crab Long Bao")
        for e5 in range(3):
            eroll.remove("Bamboo Rice")
        for e6 in range(3):
            eroll.remove("Peking Duck")
        for e7 in range(641):
            eroll += ["Sweet Tofu", ]
        for e8 in range(65):
            eroll.remove("Pineapple Cake")
        for e9 in range(66):
            eroll.remove("Eggette")
        for e10 in range(3):
            eroll.remove("Tiramisu")
        for e11 in range(3):
            eroll.remove("Escargot")
        for e12 in range(3):
            eroll.remove("Hotdog")
        for e13 in range(3):
            eroll.remove("Mango Pudding")
        for e14 in range(3):
            eroll.remove("Hamburger")
        for e15 in range(3):
            eroll.remove("Steak")
        for e16 in range(3):
            eroll.remove("Tangyuan")
        for e17 in range(3):
            eroll.remove("Sanma")
        for e18 in range(3):
            eroll.remove("Napoleon Cake")
        for e19 in range(3):
            eroll.remove("Salad")
        for e20 in range(3):
            eroll.remove("Pastel de nata")
        for e21 in range(3):
            eroll.remove("Yuxiang")
        for e22 in range(3):
            eroll.remove("Sukiyaki")
        for e23 in range(3):
            eroll.remove("Brownie")
        for e24 in range(3):
            eroll.remove("Red Wine")
        for e25 in range(3):
            eroll.remove("Gyoza")
        for e26 in range(3):
            eroll.remove("Chocolate")
    elif event_index == "1":
        vaalid = True
        esummon_pool += ["Raindrop Cake", "Strawberry Daifuku", ]
        eur_pool += ["Raindrop Cake", ]
        em_pool += ["Strawberry Daifuku", ]
        for e1 in range(120):
            eroll += ["Raindrop Cake", ]
        for e2 in range(25):
            eroll.remove("B-52")
        for e3 in range(25):
            eroll.remove("Foie Gras")
        for e4 in range(8):
            eroll.remove("Crab Long Bao")
        for e5 in range(26):
            eroll.remove("Bamboo Rice")
        for e6 in range(25):
            eroll.remove("Peking Duck")
        for e7 in range(8):
            eroll.remove("Gingerbread")
        for e8 in range(7):
            eroll.remove("Pancake")
        for e9 in range(8):
            eroll.remove("Popcorn")
        for e10 in range(8):
            eroll.remove("Jello")
        for e11 in range(8):
            eroll.remove("Skewer")
        for e12 in range(31):
            eroll += ["Strawberry Daifuku", ]
    if vaalid == True:
        summoned = []
        eachsummoned = []
        ur = 0
        sr = 0
        r = 0
        m = 0
        valid = False
        if not(event_index.isdigit()):
            await client.say("Error - Invalid 1st input: Event index must be 0-9")
        if int(event_index) > 9 or int(event_index) < 0:
            await client.say("Error - Invalid event index: Must be 0-9")
        if not(number.isdigit()):
            await client.say("Error - Invalid 2nd input: Must be a positive integer")
        elif event_toggle == 1 or event_index == "2" or event_index == "3" or event_index == "4" or event_index == "5" or event_index == "6" or event_index == "7" or event_index == "8" or event_index == "9":
            await client.say("Coming soon!")
        elif int(number) <= 0:
            await client.say("Error - Invalid number: Must be more than 0")
        elif int(number) >= 1:
            await client.say("Summoning food souls...")
            time.sleep(2)
            number = int(number)
            valid = True
            for x1 in range(number):
                foodsoul = random.choice(eroll)
                summoned += [foodsoul, ]
                if foodsoul in eur_pool:
                    ur += 1
                elif foodsoul in esr_pool:
                    sr += 1
                elif foodsoul in er_pool:
                    r += 1
                elif foodsoul in em_pool:
                    m += 1
            bigline = output4(summoned, valid, ur, sr, r, m, number, context, esummon_pool, eur_pool, esr_pool, er_pool, em_pool)
            await client.say(bigline)

@commands.check(restriction)
@client.command(name = "eventindex")
@commands.cooldown(1, 30, commands.BucketType.user)
async def eventhelp():
    embed = discord.Embed(title = "Event Index List", description = "Use the event index number to input what event you want to summon in!", color = 0x2ecc71)
    embed.add_field(name = "0. Brewing Fine Wine", value = "Toso and Sweet Tofu have been added to the summoning pool for a limited time.\nToso: 1.5%\nSweet Tofu: 6.41%", inline = False)
    embed.add_field(name = "1. Sakura Falls (樱落水月)", value = "Strawberry Daifuku and Raindrop Cake have been added to the summoning pool for a limited time.\nStrawberry Daifuku: 1.2%\nRaindrop Cake: 0.31%", inline = False)
    embed.add_field(name = "2. 盛夏沁凉", value = "Pufferfish and Bonito Rice have been added to the summoning pool for a limited time.\nPufferfish: 0.48%\nBonito Rice: 0.96%", inline = False)
    embed.add_field(name = "3. 月华倾泻", value = "Toso, Caviar and Seaweed Soup have been added to the summoning pool for a limited time.\nToso: 0.5%\nCaviar: 0.5%\nSeaweed Soup: 3.41%", inline = False)
    embed.add_field(name = "4. 冰与火之夏", value = "Spicy Hot Pot and Beer have been added to the summoning pool for a limited time.\nSpicy Hot Pot: 1.2%\nBeer: 3.32%", inline = False)
    embed.add_field(name = "5. 水映夏花", value = "Cassata and Raindrop Cake have been added to the summoning pool for a limited time.\nCassata: 3.32%\nRaindrop Cake: 1.2%", inline = False)
    embed.add_field(name = "6. 安夏回忆", value = "Cassata has been added to the summoning pool and Crab Long Bao has an increased summoning rate for a limited time.\nCrab Long Bao: 0.36% > 1.2%\n Cassata: 3.32%", inline = False)
    embed.add_field(name = "7. 夏季甜点", value = "Cassata has been added to the summoning pool and Double Scoop has an increased summoning rate for a limited time.\nDouble Scoop: 0.05% > 0.3%\n Cassata: 3.32%", inline = False)
    embed.add_field(name = "8. 绿荫之夏", value = "Cassata has been added to the summoning pool and Bamboo Rice has an increased summoning rate for a limited time.\nBamboo Rice: 0.52% > 1.2%\n Cassata: 3.32%", inline = False)
    embed.add_field(name = "9. 流浪夏日", value = "Toso and Cassata has been added to summoning pool for a limited time.\nToso: 1.2%\n Cassata: 3.32%", inline = False)
    await client.say(embed = embed)

# v5:

client.remove_command('help')

@commands.check(restriction)
@client.command(name = "help")
@commands.cooldown(1, 20, commands.BucketType.user)
async def help():
    embed = discord.Embed(title = "Foie Gras", description = "Hello. My name is Foie Gras. How may I help you today? I will await your command", color = 0x3498db)
    embed.add_field(name = "f!summon <amount>", value = "Summons a desired amount of food souls", inline = False)
    embed.add_field(name = "f!foodsoul <food_soul> <amount>", value = 'Summons endlessly until a specific food soul of a specified amount has been summoned. Use "." instead of spaces. Example, f!foodsoul Bamboo.Rice 2 will summon endlessly until two Bamboo Rice have been summoned.', inline = False)
    embed.add_field(name = "f!rarity <rarity> <amount>", value = "Summons continuously until a specified amount of foods souls with a specified rarity has been summoned.", inline = False)
    embed.add_field(name = "f!csummon <amount>", value = "Summons a desired amount of food souls from the China version.", inline = False)
    embed.add_field(name = "f!cfoodsoul <food_soul> <amount>", value = 'Summons endlessly until a specific food soul of a specified amount has been summoned from the China version. Use "." instead of spaces. Example, f!cfoodsoul Laba.Congee 2 will summon endlessly until two Laba Congee have been summoned.', inline = False)
    embed.add_field(name = "f!crarity", value = 'Summons continuously until a specified amount of foods souls with a specified rarity has been summoned.', inline = False)
    embed.add_field(name = "f!eventindex", value = "Shows the event index number to key into f!summonevent or f!event", inline = False)
    embed.add_field(name = "f!summonevent <event_index> <amount>", value = 'Event summoning! Use f!eventindex to check the event index number. Example, f!summonevent 0 100 will summon 100 times during the "Brewing Fine Wine" event.', inline = False)
    embed.add_field(name = "f!event <event_index> <mode> <foodsoul_or_rarity> <amount>", value = 'Event summoning! You can use "foodsoul" and "rarity" just like the regular f!foodsoul or f!rarity. Use f!eventindex to check the event index. Example, f!event 1 foodsoul sweet.tofu 2 will summon endlessly during the "Brewing Fine Wine" event until it summons 2 Sweet Tofu.', inline = False)
    embed.add_field(name = "f!food <dish>", value = 'Shows the recipe, cuisine, seasoning and stats. Use "." instead of space.\nNOTE: This feature is NOT OUT YET, it is currently developing as we speak. Please be patient!', inline = False)
    embed.add_field(name = "f!info", value = "Gives a paragraph of information about Foie Gras", inline = False)
    embed.add_field(name = "f!dialogue", value = "Words of wisdom from Foie Gras.", inline = False)
    embed.add_field(name = "f!credit", value = "Reveals the people behind the bot.", inline = False)
    await client.say(embed = embed)

@client.command(name = 'dialogue',
                pass_context = True)
@commands.cooldown(1, 7, commands.BucketType.user)
async def say(context):
    possible_responses = [
        'For me, for you, destiny is inescapable.',
        'What exactly is different about you? Why does Heaven always show a special concern for you?',
        "If... there really is a way to change fate... No... it's impossible...",
        "I feel a warmth in my heart. I've never felt this before",
    ]
    await client.say(random.choice(possible_responses))

@client.command(name = "info")
@commands.cooldown(1, 60, commands.BucketType.user)
async def infocard():
    await client.say("\
Nice to meet you. I am Foie Gras, a delicacy and rare dish in France, born in the 18th century.\
 You may not find me in your local restaurant, but do have a try if you enjoy exotic tastes.\
 Being here for more than 300 years, I grew a very indifferent personality, although, I would say I have a few exceptions.\
 I enjoy the company of Escargot, although his attention span is very low and loves sleeping, he's been with me since 1892.\
 Although all fallen angels are evil, I must say I really like the Sakura Spirit and Inugami. They avoid conflict and only attack when necessary.\
 I treat myself to an occasional Mango Wrap once in a while. As a food soul, we don't really have to eat to stay alive. But it's a treat once in a while that I can't resist.\
 I hope to see you fellow Master Attendants in the future.")

@client.command(name = "credits")
@commands.cooldown(1, 30, commands.BucketType.user)
async def credit():
    await client.say("\
**All nicknames are from the Food Fantasy Discord Server.**\n\
Developer: Dylanime#2353 AKA ディラン\n\
Subdeveloper: cyn#1598 AKA Just Marisa\n\
Beta Tester: Madara#0483")

@commands.check(restriction)
@client.command(name = "food")
@commands.cooldown(1, 3, commands.BucketType.user)
async def foodinfo(dish):
    await client.say("Coming Soon!")

@client.event
async def on_command_error(error, context):
    if isinstance(error, commands.CommandOnCooldown):
        await client.send_message(context.message.channel, "Please do not spam. There is only so much I can handle")

@client.event
async def on_ready():
    await client.change_presence(game=Game(name = "with Master Attendant"))
    print(client.user.name + " is online.")

client.run(TOKEN)
