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

# Global server summoning:

summon_pool = ["Crab Long Bao", "Foie Gras", "Peking Duck", "B-52", "Bamboo Rice", "Gingerbread", "Boston Lobster", "Double Scoop", "Udon", "Tiraumisu", "Escargot", "Hotdog", "Mango Pudding", "Hamburger", "Steak", "Tangyuan", "Sanma", "Napoleon Cake", "Salad", "Pastel de nata", "Yuxiang", "Sukiyaki", "Brownie", "Red Wine", "Gyoza", "Chocolate", "Eggette", "Pineapple Cake", "Skewer", "Jello", "Pancake", "Popcorn", "Long Bao", "Coffee", "Sashimi", "Macaron", "Zongzi", "Sakuramochi", "Tom Yum", "Taiyaki", "Milk", "Dorayaki", "Sake", "Tempura", "Spicy Gluten", "Jiuniang", "Omurice", "Orange Juice", "Ume Ochazuke", "Miso Soup", "Yellow Wine"]
ur_pool = ["Crab Long Bao", "Foie Gras", "Peking Duck", "B-52", "Bamboo Rice", "Gingerbread", "Boston Lobster", "Double Scoop"]
sr_pool = ["Tiraumisu", "Escargot", "Hotdog", "Mango Pudding", "Hamburger", "Steak", "Tangyuan", "Sanma", "Napoleon Cake", "Salad", "Pastel de nata", "Yuxiang", "Sukiyaki", "Brownie", "Red Wine", "Gyoza", "Chocolate", "Eggette", "Pineapple Cake"]
r_pool = ["Long Bao", "Coffee", "Sashimi", "Macaron", "Zongzi", "Sakuramochi", "Tom Yum", "Taiyaki", "Milk", "Dorayaki", "Sake", "Tempura", "Spicy Gluten", "Jiuniang", "Omurice", "Orange Juice", "Ume Ochazuke", "Miso Soup", "Yellow Wine"]
m_pool = ["Skewer", "Jello", "Pancake", "Popcorn"]
none_pool = ["Cloud Tea", "Canele", "Pizza", "Black Tea", "Mooncake", "Salty Tofu", "Spaghetti", "Sushi", "Tortoise Jelly", "Sweet & Sour Fish", "Beggar's Chicken", "Matcha Rice", "Green Curry", "Mung Bean Soup", "Milk Tea", "Katsudon", "Vodka", "Wonton", "Yogurt", "Cola", "Cold Rice Shrimp", "Plum Juice", "Cheese", "Toast"]
event_pool = ["Toso", "Raindrop Cake", "Strawberry Daifuku", "Sweet Tofu"]
unre_pool = ["Laba Congee", "Yunnan Noodles"]
cevent_pool = ["Bonito Rice", "Cassata", "Spicy Hot Pot", "Beer", "Caviar", "Seaweed Soup", "Pufferfish"]
rarity_pool = ["M", "R", "SR", "UR"]
food_pool = ["Stir-Fried Potatoes", "Braised Pork", "Braised Eggplant", "Sauteed Lettuce", "Carrot Bread", "Cucumber Egg Stir-Fry", "Black Pepper Beef", "Sauteed Mushrooms", "Egg Fried Rice", "Salmon Fried Rice", "Onion Fried Rice", "Bacon Fried Rice", "Braised Octopus", "Risotto", "Butter Bread", "Emerald Roll", "Corn Pie", "Toffee Apple", "Pineapple Fried Rice", "Chicken Soup", "Mango Pudding", "Strawberry Ice Cream", "Red Bean Pudding", "Kung Pao Chicken", "Pumpkin Pie", "Sweet Yam Buns", "Steamed Cod", "Steamed Unagi", "Garlic Lobster", "Crab Hotpot", "French Fries", "Crispy Pork", "Salad", "Eggplant Roll", "Smoked Salmon", "Roast Beef", "Cheese Bread", "Mushroom Soup", "Fried Rice Cake", "Pork Burger", "Bacon Tofu Wrap", "Grilled Calamari", "Popcorn", "Shortbread", "Minestrone", "Pineapple Juice", "Apple Crisp", "Chicken Pizza", "Roast Chicken", "Mango Wrap", "Fruit Salad", "Peanut Pie", "Pumpkin Soup", "Hotteok", "Cheesy Yam", "Fried Cod", "Fried Unagi", "Baked Lobster", "Crab Salad", "Baked Potato", "Grilled Pork Belly", "Cucumber Salad", "Boiled Lettuce", "Mushroom Yaki", "Salmon Sashimi", "Beef Tartare", "Tamagoyaki", "Omurice", "Shogayki", "Bacon Bites", "Cold Tofu", "Grilled Corn", "Vegetable Tempura", "Takoyaki", "Creamed Spinach", "Baked Pineapple", "Apples & Cream", "Chicken Skewer", "Fried Chicken", "Mango Smoothie", "Strawberry Smoothie", "Peanut Crisp", "Cod Fillet", "Piglet Daifuku", "Pumpkin Muffin", "Yam Dumplings", "Unagi Don", "Lobster Sashimi", "Crab Sashimi"]
lostfood_pool = ["Calamari Skewer", "Garlic Oyster", "Grilled Prawns", "Pickled Salmon Head", "Tomato & Eggs", "Steamed Mushrooms", "Spaghetti", "Har Gow", "Gold Cake", "Mixed Greens", "Stir-Fried Mussels", "Mushroom Alfredo", "Cha Siu Bao", "Spinach Noodles", "Mint Pineapple", "Apple Sangria", "Braised Lamb", "Mushroom Chicken Stew", "Matcha Cake", "Cappuccino", "Fruit Tea", "Lemon Pie", "Meat Zongzi", "Stuffed Lotus Root", "Lotus Root Stir-Fry", "Black Fungus Congee", "Sanma Shioyaki", "Steamed Crab", "Crab Rice Cake", "Curry Crab", "Yam Pigeon Soup", "Bamboo & Meat Stir-Fry", "Braised Geese", "Roe Meat Ball", "Birds Nest", "Ginseng Stew Chicken"]
roll = []
roll2 = []
for u1 in range(23):
    roll += ["Crab Long Bao", ]
    roll += ["Gingerbread", ]
for u2 in range(61):
    roll += ["Foie Gras", ]
    roll += ["Peking Duck", ]
    roll += ["B-52", ]
for u3 in range(62):
    roll += ["Bamboo Rice", ]
for u4 in range(5):
    roll += ["Boston Lobster", ]
    roll += ["Double Scoop", ]
for s1 in range(80):
    roll += ["Tiramisu", ]
    roll += ["Escargot", ]
    roll += ["Hotdog", ]
    roll += ["Mango Pudding", ]
    roll += ["Hamburger",]
    roll += ["Steak", ]
    roll += ["Tangyuan", ]
    roll += ["Sanma", ]
    roll += ["Napoleon Cake", ]
    roll += ["Salad", ]
    roll += ["Pastel de nata", ]
    roll += ["Yuxiang", ]
    roll += ["Sukiyaki", ]
    roll += ["Brownie", ]
    roll += ["Red Wine", ]
    roll += ["Gyoza", ]
    roll += ["Chocolate", ]
for s2 in range(150):
    roll += ["Eggette", ]
for s3 in range(151):
    roll += ["Pineapple Cake", ]
for r1 in range(413):
    roll += ["Long Bao", ]
    roll += ["Coffee", ]
    roll += ["Sashimi", ]
    roll += ["Macaron", ]
    roll += ["Zongzi", ]
    roll += ["Sakuramochi", ]
    roll += ["Tom Yum", ]
    roll += ["Taiyaki", ]
    roll += ["Milk", ]
    roll += ["Dorayaki", ]
    roll += ["Sake", ]
    roll += ["Tempura", ]
    roll += ["Spicy Gluten", ]
for r2 in range(414):
    roll += ["Jiuniang", ]
    roll += ["Omurice", ]
    roll += ["Orange Juice", ]
    roll += ["Ume Ochazuke" ,]
    roll += ["Miso Soup" ,]
    roll += ["Yellow Wine", ]
for m1 in range(46):
    roll += ["Skewer", ]
    roll += ["Jello", ]
    roll += ["Pancake", ]
for m2 in range(47):
    roll += ["Popcorn", ]

for u21 in range(23):
    roll2 += ["Crab Long Bao", ]
    roll2 += ["Gingerbread", ]
for u22 in range(61):
    roll2 += ["Foie Gras", ]
    roll2 += ["Peking Duck", ]
    roll2 += ["B-52", ]
for u23 in range(62):
    roll2 += ["Bamboo Rice", ]
for u24 in range(5):
    roll2 += ["Boston Lobster", ]
    roll2 += ["Double Scoop", ]
for s21 in range(76):
    roll2 += ["Tiramisu", ]
    roll2 += ["Escargot", ]
    roll2 += ["Hotdog", ]
    roll2 += ["Mango Pudding", ]
    roll2 += ["Hamburger",]
    roll2 += ["Steak", ]
    roll2 += ["Tangyuan", ]
    roll2 += ["Sanma", ]
    roll2 += ["Napoleon Cake", ]
    roll2 += ["Salad", ]
    roll2 += ["Pastel de nata", ]
    roll2 += ["Yuxiang", ]
    roll2 += ["Sukiyaki", ]
    roll2 += ["Brownie", ]
    roll2 += ["Red Wine", ]
    roll2 += ["Gyoza", ]
    roll2 += ["Chocolate", ]
    roll2 += ["Udon", ]
for s22 in range(146):
    roll2 += ["Eggette", ]
for s23 in range(147):
    roll2 += ["Pineapple Cake", ]
for r21 in range(413):
    roll2 += ["Long Bao", ]
    roll2 += ["Coffee", ]
    roll2 += ["Sashimi", ]
    roll2 += ["Macaron", ]
    roll2 += ["Zongzi", ]
    roll2 += ["Sakuramochi", ]
    roll2 += ["Tom Yum", ]
    roll2 += ["Taiyaki", ]
    roll2 += ["Milk", ]
    roll2 += ["Dorayaki", ]
    roll2 += ["Sake", ]
    roll2 += ["Tempura", ]
    roll2 += ["Spicy Gluten", ]
for r22 in range(414):
    roll2 += ["Jiuniang", ]
    roll2 += ["Omurice", ]
    roll2 += ["Orange Juice", ]
    roll2 += ["Ume Ochazuke" ,]
    roll2 += ["Miso Soup" ,]
    roll2 += ["Yellow Wine", ]
for m21 in range(46):
    roll2 += ["Skewer", ]
    roll2 += ["Jello", ]
    roll2 += ["Pancake", ]
for m22 in range(47):
    roll2 += ["Popcorn", ]
lsummon_pool = [items.lower() for items in summon_pool]
lrarity_pool = [itemr.lower() for itemr in rarity_pool]
lnone_pool = [itemn.lower() for itemn in none_pool]
levent_pool = [itemv.lower() for itemv in event_pool]
lunre_pool = [itemu.lower() for itemu in unre_pool]
lcevent_pool = [itemce.lower() for itemce in cevent_pool]
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

def output2(foodstats, dishname, colour, cuisine, ingredient1, ingredient2, ingredient3, level, quest, flavor, texture, aroma, appearence, season1, season2, attribute):
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
    elif int(number) > 1000000:
        await client.say ("Error - Invalid number: Must be less than 1000000")
    elif int(number) >= 1 and int(number) < 1000000:
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

@commands.check(restriction)
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
            await client.say("Error - Invalid food soul: " + lfood_soul.title() + " is from an event; use ``f!event`` instead")
        if lfood_soul in lunre_pool:
            ivalid = True
            await client.say("Error - Invalid food soul: " + lfood_soul.title() + " is not in the global server yet; use ``f!cfoodsoul`` instead")
        if lfood_soul in lcevent_pool:
            ivalid = True
            await client.say("Error - Invalid food soul: " + lfood_soul.title() + " is from an event in the Chinese server; use ``f!cevent`` instead")
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

@commands.check(restriction)
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
    elif int(amount) > 1000:
        await client.say("Error - Invalid number: Must be less than 1000")
    elif lrarity in lrarity_pool and int(amount) >= 1 and int(amount) < 1000:
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

# China server summoning:

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
for cs5 in range(60):
    croll += ["Hamburger", ]
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
    elif int(number) > 1000000:
        await client.say("Error - Invalid number: Must be less than 1000000")
    elif int(number) >= 1 and int(number) < 1000000:
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
    ivalid = False
    food_soul = food_soul.replace(".", " ")
    lfood_soul = food_soul.lower()
    if not(amount.isdigit()):
        await client.say('Error - Invalid 1st input: Use "." instead of space')
    if int(amount) <= 0:
        await client.say("Error - Invalid 2nd input: Number must be more than 0")
    elif lfood_soul not in lcsummon_pool:
        if lfood_soul in lnone_pool:
            ivalid = True
            await client.say("Error - Invalid food soul: " + lfood_soul.title() + " cannot be summoned")
        if lfood_soul in levent_pool:
            ivalid = True
            await client.say("Error - Invalid food soul: " + lfood_soul.title() + " is from an event; use ``f!cevent`` instead")
        if lfood_soul in lcevent_pool:
            ivalid = True
            await client.say("Error - Invalid food soul: " + lfood_soul.title() + " is from an event; use ``f!cevent`` instead")
        elif ivalid == False:
            await client.say("Error - Invalid 1st input: Food Soul does not exsist or improper spelling")
    elif int(amount) > 1000:
        await client.say("Error - Invalid number: Must be less than 1000")
    elif lfood_soul in lcsummon_pool and int(amount) >= 1 and int(amount) < 1000:
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
        await client.say("Error - Invalid number: Must be more than 0")
    elif int(amount) > 1000:
        await client.say("Error - Invalid number: Must be less than 1000")
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

# Global server event summoning:

def index0entry(eroll, eevent_pool, esummon_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool):
    esummon_pool.remove("Pineapple Cake")
    esummon_pool.remove("Eggette")
    esummon_pool.remove("Udon")
    unav_pool += ["Udon", "Pineapple Cake", "Eggette"]
    for e1 in range(151):
        eroll.remove("Pineapple Cake")
    for e2 in range(150):
        eroll.remove("Eggette")
    for e3 in range(10):
        eroll.remove("Crab Long Bao")
    for e4 in range(22):
        eroll.remove("Bamboo Rice")
    for e5 in range(21):
        eroll.remove("Foie Gras")
    for e6 in range(23):
        eroll.remove("B-52")
    for e7 in range(21):
        eroll.remove("Peking Duck")
    for e8 in range(97):
        eroll += ["Gingerbread", ]
    for e9 in range(253):
        eroll += ["Chocolate", ]
    for e10 in range(3):
        eroll += ["Tiramisu", ]
        eroll += ["Escargot", ]
        eroll += ["Hotdog", ]
        eroll += ["Mango Pudding", ]
        eroll += ["Hamburger", ]
        eroll += ["Steak", ]
        eroll += ["Tangyuan", ]
        eroll += ["Sanma", ]
        eroll += ["Napoleon Cake", ]
        eroll += ["Salad", ]
        eroll += ["Pastel de nata", ]
        eroll += ["Yuxiang", ]
        eroll += ["Sukiyaki", ]
        eroll += ["Brownie", ]
        eroll += ["Red Wine", ]
        eroll += ["Gyoza", ]

def index1entry(eroll, eevent_pool, esummon_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool):
    esummon_pool += ["Toso", "Sweet Tofu", ]
    eur_pool += ["Toso", ]
    esr_pool += ["Sweet Tofu", ]
    esummon_pool.remove("Udon")
    unav_pool += ["Udon"]
    for e0 in range(12):
        eroll.remove("Gingerbread")
    for e1 in range(150):
        eroll += ["Toso", ]
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
        eroll += ["Sweet Tofu", ]
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

def index2entry(eroll, eevent_pool, esummon_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool):
    eevent_pool.remove("Strawberry Daifuku")
    eevent_pool.remove("Raindrop Cake")
    esummon_pool += ["Raindrop Cake", "Strawberry Daifuku", ]
    eur_pool += ["Raindrop Cake", ]
    em_pool += ["Strawberry Daifuku", ]
    esummon_pool.remove("Udon")
    unav_pool += ["Udon"]
    for e1 in range(120):
        eroll += ["Raindrop Cake", ]
    for e2 in range(31):
        eroll += ["Strawberry Daifuku", ]
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
    print(esummon_pool)
    return eroll

def index3entry(eroll, eevent_pool, esummon_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool):
    pass

def index4entry(eroll, eevent_pool, esummon_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool):
    pass

def index5entry(eroll, eevent_pool, esummon_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool):
    pass

def index6entry(eroll, eevent_pool, esummon_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool):
    pass

def index7entry(eroll, eevent_pool, esummon_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool):
    pass

def index8entry(eroll, eevent_pool, esummon_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool):
    pass

def index9entry(eroll, eevent_pool, esummon_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool):
    pass

def index10entry(eroll, eevent_pool, esummon_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool):
    pass

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
    eevent_pool = []
    eevent_pool += event_pool
    unav_pool = []
    if event_index == "0":
        vaalid = True
        eroll = index0entry(eroll, eevent_pool, esummon_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    if event_index == "1":
        vaalid = True
        eroll = index1entry(eroll, eevent_pool, esummon_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    elif event_index == "2":
        vaalid = True
        eroll = index2entry(eroll, eevent_pool, esummon_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    if vaalid == True:
        if mode != "rarity" and mode != "foodsoul":
            await client.say('Error - Invalid mode: Must be "foodsoul" or "rarity"')
        elif mode == "foodsoul":
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
            food_soul = foodsoul_or_rarity
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
                    await client.say("Error - Invalid food soul: " + lfood_soul.title() + " is not in the global server yet; use ``f!cfoodsoul`` instead")
                if lfood_soul in lcevent_pool:
                    ivalid = True
                    await client.say("Error - Invalid food soul: " + lfood_soul.title() + " is from an event in the Chinese server; use ``f!cevent`` instead")
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
            if not(event_index.isdigit()):
                await client.say("Error - Invalid 1st input: Event index must be 2-10")
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
    eevent_pool = []
    eevent_pool += event_pool
    unav_pool = []
    if event_index == "0":
        vaalid = True
        eroll = index0entry(eroll, eevent_pool, esummon_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    elif event_index == "1":
        vaalid = True
        eroll = index1entry(eroll, eevent_pool, esummon_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    elif event_index == "2":
        vaalid = True
        eroll = index2entry(eroll, eevent_pool, esummon_pool, eur_pool, esr_pool, er_pool, em_pool, unav_pool)
    if vaalid == True:
        summoned = []
        eachsummoned = []
        ur = 0
        sr = 0
        r = 0
        m = 0
        valid = False
        if not(event_index.isdigit()):
            await client.say("Error - Invalid 1st input: Event index must be 0-2")
        if int(event_index) > 9 or int(event_index) < 0:
            await client.say("Error - Invalid event index: Must be 0-2")
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

# China server event summoning:

def cindex2entry(ceroll, ceevent_pool, cceevent_pool, cesummon_pool, ceur_pool, cesr_pool, cer_pool, cem_pool, unav_pool):
    ceroll += croll
    ceevent_pool.remove("Raindrop Cake")
    ceevent_pool.remove("Strawberry Daifuku")
    cesummon_pool += ["Raindrop Cake", "Strawberry Daifuku", ]
    cesummon_pool.remove("B-52")
    ceur_pool.remove("B-52")
    cesummon_pool.remove("Udon")
    cesr_pool.remove("Udon")
    cesummon_pool.remove("Yunnan Noodles")
    cesr_pool.remove("Yunnan Noodles")
    cesummon_pool.remove("Gyoza")
    cesr_pool.remove("Gyoza")
    ceur_pool += ["Raindrop Cake", ]
    cem_pool += ["Strawberry Daifuku", ]
    unav_pool += ["B-52", "Yunnan Noodles", "Udon", "Gyoza", ]
    ceroll += ["Boston Lobster", ]
    for ce1 in range(120):
        ceroll += ["Raindrop Cake", ]
    for ce2 in range(61):
        ceroll.remove("B-52")
    for ce3 in range(35):
        ceroll.remove("Foie Gras")
    for ce4 in range(10):
        ceroll.remove("Crab Long Bao")
    for ce5 in range(35):
        ceroll.remove("Bamboo Rice")
    for ce6 in range(35):
        ceroll.remove("Peking Duck")
    for ce7 in range(5):
        ceroll.remove("Gingerbread")
    for ce8 in range(9):
        ceroll.remove("Pancake")
    for ce9 in range(8):
        ceroll.remove("Popcorn")
    for ce10 in range(7):
        ceroll.remove("Jello")
    for ce11 in range(7):
        ceroll.remove("Skewer")
    for ce12 in range(31):
        ceroll += ["Strawberry Daifuku", ]
    for ce13 in range(61):
        ceroll.remove("Udon")
    for ce14 in range(61):
        ceroll.remove("Yunnan Noodles")
    for ce15 in range(60):
        ceroll.remove("Gyoza")
    for ce16 in range(10):
        ceroll += ["Tiramisu", ]
    for ce17 in range(10):
        ceroll += ["Escargot", ]
    for ce18 in range(10):
        ceroll += ["Hotdog", ]
    for ce19 in range(10):
        ceroll += ["Mango Pudding", ]
    for ce20 in range(10):
        ceroll += ["Hamburger", ]
    for ce21 in range(10):
        ceroll += ["Steak", ]
    for ce22 in range(10):
        ceroll += ["Tangyuan", ]
    for ce23 in range(10):
        ceroll += ["Sanma", ]
    for ce24 in range(10):
        ceroll += ["Napoleon Cake", ]
    for ce25 in range(10):
        ceroll += ["Salad", ]
    for ce26 in range(10):
        ceroll += ["Pastel de nata", ]
    for ce27 in range(10):
        ceroll += ["Yuxiang", ]
    for ce28 in range(10):
        ceroll += ["Sukiyaki", ]
    for ce29 in range(10):
        ceroll += ["Brownie", ]
    for ce30 in range(10):
        ceroll += ["Red Wine", ]
    for ce31 in range(10):
        ceroll += ["Chocolate", ]
    for ce32 in range(4):
        ceroll += ["Eggette", ]
    for ce33 in range(4):
        ceroll += ["Pineapple Cake", ]
    for ce34 in range(10):
        ceroll += ["Sweet Tofu", ]
    for ce35 in range(4):
        ceroll += ["Laba Congee", ]
    return ceroll

def cindex3entry(ceroll, ceevent_pool, cceevent_pool, cesummon_pool, ceur_pool, cesr_pool, cer_pool, cem_pool, unav_pool):
    cceevent_pool.remove("Pufferfish")
    cceevent_pool.remove("Bonito Rice")
    cesummon_pool.remove("B-52")
    ceur_pool.remove("B-52")
    cesummon_pool.remove("Udon")
    cesr_pool.remove("Udon")
    cesummon_pool.remove("Yunnan Noodles")
    cesr_pool.remove("Yunnan Noodles")
    cesummon_pool.remove("Gyoza")
    cesr_pool.remove("Gyoza")
    cesummon_pool += ["Pufferfish", "Bonito Rice", ]
    ceur_pool += ["Pufferfish", ]
    cesr_pool += ["Bonito Rice", ]
    unav_pool += ["B-52", "Udon", "Yunnan Noodles", "Gyoza", ]
    for ce1 in range(48):
        ceroll += ["Pufferfish", ]
    for ce2 in range(4):
        ceroll += ["Double Scoop"]
    for ce3 in range(5):
        ceroll += ["Boston Lobster", ]
    for ce4 in range(60):
        ceroll += ["Peking Duck", ]
    for ce5 in range(60):
        ceroll += ["Foie Gras", ]
    for ce6 in range(32):
        ceroll += ["Crab Long Bao", ]
    for ce7 in range(31):
        ceroll += ["Gingerbread", ]
    for ce8 in range(61):
        ceroll += ["Bamboo Rice", ]
    for ce9 in range(96):
        ceroll += ["Bonito Rice", ]
    for ce10 in range(159):
        ceroll += ["Laba Congee", ]
    for ce11 in range(69):
        ceroll += ["Brownie", ]
    for ce12 in range(59):
        ceroll += ["Chocolate", ]
    for ce13 in range(63):
        ceroll += ["Sukiyaki", ]
    for ce14 in range(155):
        ceroll += ["Eggette", ]
    for ce15 in range(68):
        ceroll += ["Tiramisu", ]
    for ce16 in range(60):
        ceroll += ["Sweet Tofu", ]
    for ce17 in range(64):
        ceroll += ["Yuxiang", ]
    for ce18 in range(63):
        ceroll += ["Pastel de nata", ]
    for ce19 in range(65):
        ceroll += ["Red Wine"]
    for ce20 in range(70):
        ceroll += ["Napoleon Cake", ]
    for ce21 in range(64):
        ceroll += ["Salad", ]
    for ce22 in range(69):
        ceroll += ["Sanma"]
    for ce23 in range(64):
        ceroll += ["Steak"]
    for ce24 in range(66):
        ceroll += ["Hamburger", ]
    for ce25 in range(64):
        ceroll += ["Hotdog", ]
    for ce26 in range(64):
        ceroll += ["Mango Pudding", ]
    for ce27 in range(64):
        ceroll += ["Escargot", ]
    for ce28 in range(396):
        ceroll += ["Sakuramochi", ]
    for ce29 in range(387):
        ceroll += ["Cold Rice Shrimp"]
    for ce30 in range(396):
        ceroll += ["Miso Soup", ]
    for ce31 in range(396):
        ceroll += ["Orange Juice", ]
    for ce32 in range(389):
        ceroll += ["Jiuniang", ]
    for ce33 in range(390):
        ceroll += ["Tempura", ]
    for ce34 in range(395):
        ceroll += ["Dorayaki", ]
    for ce35 in range(392):
        ceroll += ["Taiyaki", ]
    for ce36 in range(395):
        ceroll += ["Macaron", ]
    for ce37 in range(392):
        ceroll += ["Coffee", ]
    for ce38 in range(396):
        ceroll += ["Zongzi", ]
    for ce39 in range(394):
        ceroll += ["Yellow Wine", ]
    for ce40 in range(396):
        ceroll += ["Ume Ochazuke", ]
    for ce41 in range(393):
        ceroll += ["Omurice", ]
    for ce42 in range(392):
        ceroll += ["Spicy Gluten", ]
    for ce43 in range(382):
        ceroll += ["Milk", ]
    for ce44 in range(393):
        ceroll += ["Tom Yum", ]
    for ce45 in range(391):
        ceroll += ["Sashimi", ]
    for ce46 in range(396):
        ceroll += ["Long Bao", ]
    for ce47 in range(44):
        ceroll += ["Pancake", ]
    for ce48 in range(49):
        ceroll += ["Popcorn", ]
    for ce49 in range(48):
        ceroll += ["Jello", ]
    for ce50 in range(44):
        ceroll += ["Skewer", ]
    return ceroll

def cindex4entry(ceroll, ceevent_pool, cceevent_pool, cesummon_pool, ceur_pool, cesr_pool, cer_pool, cem_pool, unav_pool):
    cceevent_pool.remove("Caviar")
    cceevent_pool.remove("Seaweed Soup")
    ceevent_pool.remove("Toso")
    cesummon_pool += ["Caviar", "Toso", "Seaweed Soup", ]
    ceur_pool += ["Caviar", "Toso", ]
    cesr_pool += ["Seaweed Soup", ]
    for ce1 in range(50):
        ceroll += ["Caviar", ]
    for ce2 in range(50):
        ceroll += ["Toso", ]
    for ce3 in range(5):
        ceroll += ["Double Scoop",]
    for ce4 in range(5):
        ceroll += ["Boston Lobster", ]
    for ce5 in range(40):
        ceroll += ["Peking Duck", ]
    for ce6 in range(40):
        ceroll += ["B-52", ]
    for ce7 in range(40):
        ceroll += ["Foie Gras", ]
    for ce8 in range(16):
        ceroll += ["Crab Long Bao", ]
    for ce9 in range(16):
        ceroll += ["Gingerbread", ]
    for ce10 in range(40):
        ceroll += ["Bamboo Rice", ]
    for ce11 in range(341):
        ceroll += ["Seaweed Soup", ]
    for ce12 in range(48):
        ceroll += ["Chocolate", ]
    for ce13 in range(49):
        ceroll += ["Sukiyaki"]
    for ce14 in range(52):
        ceroll += ["Yunnan Noodles", ]
    for ce15 in range(110):
        ceroll += ["Pineapple Cake", ]
    for ce16 in range(50):
        ceroll += ["Tiramisu", ]
    for ce17 in range(47):
        ceroll += ["Sweet Tofu", ]
    for ce18 in range(52):
        ceroll += ["Red Wine", ]
    for ce19 in range(52):
        ceroll += ["Napoleon Cake", ]
    for ce20 in range(47):
        ceroll += ["Tangyuan", ]
    for ce21 in range(52):
        ceroll += ["Hamburger", ]
    for ce22 in range(46):
        ceroll += ["Hotdog", ]
    for ce23 in range(116):
        ceroll += ["Laba Comgee", ]
    for ce24 in range(48):
        ceroll += ["Brownie", ]
    for ce25 in range(47):
        ceroll += ["Udon", ]
    for ce26 in range(114):
        ceroll += ["Eggette", ]
    for ce27 in range(51):
        ceroll += ["Gyoza", ]
    for ce28 in range(50):
        ceroll += ["Yuxiang", ]
    for ce29 in range(52):
        ceroll += ["Pastel de nata", ]
    for ce30 in range(47):
        ceroll += ["Salad", ]
    for ce31 in range(46):
        ceroll += ["Sanma", ]
    for ce32 in range(49):
        ceroll += ["Steak", ]
    for ce33 in range(47):
        ceroll += ["Mango Pudding", ]
    for ce34 in range(50):
        ceroll += ["Escargot", ]
    for ce35 in range(403):
        ceroll += ["Sakuramochi", ]
    for ce36 in range(407):
        ceroll += ["Cold Rice Shrimp", ]
    for ce37 in range(397):
        ceroll += ["Miso Soup", ]
    for ce38 in range(391):
        ceroll += ["Orange Juice", ]
    for ce39 in range(388):
        ceroll += ["Jiuniang", ]
    for ce40 in range(390):
        ceroll += ["Tempura", ]
    for ce41 in range(382):
        ceroll += ["Dorayaki", ]
    for ce42 in range(390):
        ceroll += ["Taiyaki", ]
    for ce43 in range(392):
        ceroll += ["Macaron", ]
    for ce44 in range(394):
        ceroll += ["Coffee", ]
    for ce45 in range(393):
        ceroll += ["Zongzi", ]
    for ce46 in range(390):
        ceroll += ["Yellow Wine", ]
    for ce47 in range(393):
        ceroll += ["Ume Ochazuke", ]
    for ce48 in range(379):
        ceroll += ["Omurice", ]
    for ce49 in range(388):
        ceroll += ["Spicy Gluten", ]
    for ce50 in range(402):
        ceroll += ["Sake", ]
    for ce51 in range(395):
        ceroll += ["Milk", ]
    for ce52 in range(391):
        ceroll += ["Tom Yum", ]
    for ce52 in range(397):
        ceroll += ["Sashimi", ]
    for ce53 in range(394):
        ceroll += ["Long Bao", ]
    for ce54 in range(49):
        ceroll += ["Pancake", ]
    for ce55 in range(45):
        ceroll += ["Popcorn", ]
    for ce56 in range(47):
        ceroll += ["Jello", ]
    for ce57 in range(46):
        ceroll += ["Skewer", ]
    return ceroll

def cindex5entry(ceroll, ceevent_pool, cceevent_pool, cesummon_pool, ceur_pool, cesr_pool, cer_pool, cem_pool, unav_pool):
    cceevent_pool.remove("Spicy Hot Pot")
    cceevent_pool.remove("Beer")
    cesummon_pool += ["Spicy Hot Pot", "Beer", ]
    ceur_pool += ["Spicy Hot Pot", ]
    cesr_pool += ["Beer", ]
    for ce1 in range(120):
        ceroll += ["Spicy Hot Pot", ]
    for ce2 in range(5):
        ceroll += ["Boston Lobster", ]
        ceroll += ["Double Scoop", ]
    for ce3 in range(35):
        ceroll += ["Bamboo Rice", ]
        ceroll += ["B-52", ]
        ceroll += ["Peking Duck", ]
        ceroll += ["Foie Gras", ]
    for ce4 in range(16):
        ceroll += ["Gingerbread", ]
    for ce5 in range(15):
        ceroll += ["Crab Long Bao", ]
    for ce6 in range(332):
        ceroll += ["Beer", ]
    for ce7 in range(48):
        ceroll += ["Chocolate", ]
        ceroll += ["Brownie", ]
        ceroll += ["Sukiyaki" ,]
        ceroll += ["Udon", ]
        ceroll += ["Yunnan Noodles", ]
        ceroll += ["Gyoza", ]
        ceroll += ["Tiramisu", ]
        ceroll += ["Yuxiang", ]
        ceroll += ["Sweet Tofu", ]
        ceroll += ["Pastel de nata"]
        ceroll += ["Red Wine", ]
        ceroll += ["Salad", ]
        ceroll += ["Napoleon Cake", ]
        ceroll += ["Sanma", ]
        ceroll += ["Tangyuan", ]
        ceroll += ["Steak", ]
        ceroll += ["Hamburger", ]
        ceroll += ["Mango Pudding", ]
        ceroll += ["Hotdog", ]
        ceroll += ["Escargot", ]
    for ce8 in range(123):
        ceroll += ["Laba Congee", ]
        ceroll += ["Pineapple Cake", ]
        ceroll += ["Eggette", ]
    for ce9 in range(393):
        ceroll += ["Sakuramochi", ]
        ceroll += ["Zongzi",]
        ceroll += ["Spicy Gluten", ]
        ceroll += ["Tempura", ]
        ceroll += ["Sake", ]
        ceroll += ["Dorayaki", ]
        ceroll += ["Milk", ]
        ceroll += ["Taiyaki", ]
        ceroll += ["Tom Yum", ]
        ceroll += ["Macaron", ]
        ceroll += ["Sashimi", ]
        ceroll += ["Coffee", ]
        ceroll += ["Long Bao", ]
    for ce10 in range(392):
        ceroll += ["Cold Rice Shrimp", ]
        ceroll += ["Yellow Wine", ]
        ceroll += ["Miso Soup", ]
        ceroll += ["Orange Juice", ]
        ceroll += ["Omurice", ]
        ceroll += ["Jiuniang", ]
        ceroll += ["Ume Ochazuke", ]
    for ce11 in range(47):
        ceroll += ["Pancake", ]
    for ce12 in range(46):
        ceroll += ["Popcorn", ]
        ceroll += ["Jello", ]
        ceroll += ["Skewer", ]
    return ceroll

def cindex6entry(ceroll, ceevent_pool, cceevent_pool, cesummon_pool, ceur_pool, cesr_pool, cer_pool, cem_pool, unav_pool):
    ceevent_pool.remove("Raindrop Cake")
    cceevent_pool.remove("Cassata")
    cesummon_pool += ["Raindrop Cake", "Cassta", ]
    ceur_pool += ["Raindrop Cake", ]
    cesr_pool += ["Cassata", ]
    for ce1 in range(120):
        ceroll += ["Raindrop Cake", ]
    for ce2 in range(5):
        ceroll += ["Boston Lobster", ]
        ceroll += ["Double Scoop", ]
    for ce3 in range(35):
        ceroll += ["Bamboo Rice", ]
        ceroll += ["B-52", ]
        ceroll += ["Peking Duck", ]
        ceroll += ["Foie Gras", ]
    for ce4 in range(16):
        ceroll += ["Gingerbread", ]
    for ce5 in range(15):
        ceroll += ["Crab Long Bao", ]
    for ce6 in range(332):
        ceroll += ["Cassata", ]
    for ce7 in range(48):
        ceroll += ["Chocolate", ]
        ceroll += ["Brownie", ]
        ceroll += ["Sukiyaki" ,]
        ceroll += ["Udon", ]
        ceroll += ["Yunnan Noodles", ]
        ceroll += ["Gyoza", ]
        ceroll += ["Tiramisu", ]
        ceroll += ["Yuxiang", ]
        ceroll += ["Sweet Tofu", ]
        ceroll += ["Pastel de nata"]
        ceroll += ["Red Wine", ]
        ceroll += ["Salad", ]
        ceroll += ["Napoleon Cake", ]
        ceroll += ["Sanma", ]
        ceroll += ["Tangyuan", ]
        ceroll += ["Steak", ]
        ceroll += ["Hamburger", ]
        ceroll += ["Mango Pudding", ]
        ceroll += ["Hotdog", ]
        ceroll += ["Escargot", ]
    for ce8 in range(123):
        ceroll += ["Laba Congee", ]
        ceroll += ["Pineapple Cake", ]
        ceroll += ["Eggette", ]
    for ce9 in range(393):
        ceroll += ["Sakuramochi", ]
        ceroll += ["Zongzi",]
        ceroll += ["Spicy Gluten", ]
        ceroll += ["Tempura", ]
        ceroll += ["Sake", ]
        ceroll += ["Dorayaki", ]
        ceroll += ["Milk", ]
        ceroll += ["Taiyaki", ]
        ceroll += ["Tom Yum", ]
        ceroll += ["Macaron", ]
        ceroll += ["Sashimi", ]
        ceroll += ["Coffee", ]
        ceroll += ["Long Bao", ]
    for ce10 in range(392):
        ceroll += ["Cold Rice Shrimp", ]
        ceroll += ["Yellow Wine", ]
        ceroll += ["Miso Soup", ]
        ceroll += ["Orange Juice", ]
        ceroll += ["Omurice", ]
        ceroll += ["Jiuniang", ]
        ceroll += ["Ume Ochazuke", ]
    for ce11 in range(47):
        ceroll += ["Pancake", ]
    for ce12 in range(46):
        ceroll += ["Popcorn", ]
        ceroll += ["Jello", ]
        ceroll += ["Skewer", ]
    return ceroll

def cindex7entry(ceroll, ceevent_pool, cceevent_pool, cesummon_pool, ceur_pool, cesr_pool, cer_pool, cem_pool, unav_pool):
    cceevent_pool.remove("Cassata")
    cesummon_pool += ["Cassta", ]
    cesr_pool += ["Cassata", ]
    for ce1 in range(5):
        ceroll += ["Boston Lobster", ]
        ceroll += ["Double Scoop", ]
    for ce2 in range(38):
        ceroll += ["Bamboo Rice", ]
        ceroll += ["B-52", ]
        ceroll += ["Peking Duck", ]
        ceroll += ["Foie Gras", ]
    for ce3 in range(19):
        ceroll += ["Gingerbread", ]
    for ce4 in range(120):
        ceroll += ["Crab Long Bao", ]
    for ce5 in range(332):
        ceroll += ["Cassata", ]
    for ce6 in range(48):
        ceroll += ["Chocolate", ]
        ceroll += ["Brownie", ]
        ceroll += ["Sukiyaki" ,]
        ceroll += ["Udon", ]
        ceroll += ["Yunnan Noodles", ]
        ceroll += ["Gyoza", ]
        ceroll += ["Tiramisu", ]
        ceroll += ["Yuxiang", ]
        ceroll += ["Sweet Tofu", ]
        ceroll += ["Pastel de nata"]
        ceroll += ["Red Wine", ]
        ceroll += ["Salad", ]
        ceroll += ["Napoleon Cake", ]
        ceroll += ["Sanma", ]
        ceroll += ["Tangyuan", ]
        ceroll += ["Steak", ]
        ceroll += ["Hamburger", ]
        ceroll += ["Mango Pudding", ]
        ceroll += ["Hotdog", ]
        ceroll += ["Escargot", ]
    for ce7 in range(123):
        ceroll += ["Laba Congee", ]
        ceroll += ["Pineapple Cake", ]
        ceroll += ["Eggette", ]
    for ce8 in range(393):
        ceroll += ["Sakuramochi", ]
        ceroll += ["Zongzi",]
        ceroll += ["Spicy Gluten", ]
        ceroll += ["Tempura", ]
        ceroll += ["Sake", ]
        ceroll += ["Dorayaki", ]
        ceroll += ["Milk", ]
        ceroll += ["Taiyaki", ]
        ceroll += ["Tom Yum", ]
        ceroll += ["Macaron", ]
        ceroll += ["Sashimi", ]
        ceroll += ["Coffee", ]
        ceroll += ["Long Bao", ]
    for ce9 in range(392):
        ceroll += ["Cold Rice Shrimp", ]
        ceroll += ["Yellow Wine", ]
        ceroll += ["Miso Soup", ]
        ceroll += ["Orange Juice", ]
        ceroll += ["Omurice", ]
        ceroll += ["Jiuniang", ]
        ceroll += ["Ume Ochazuke", ]
    for ce10 in range(47):
        ceroll += ["Pancake", ]
    for ce11 in range(46):
        ceroll += ["Popcorn", ]
        ceroll += ["Jello", ]
        ceroll += ["Skewer", ]
    return ceroll

def cindex8entry(ceroll, ceevent_pool, cceevent_pool, cesummon_pool, ceur_pool, cesr_pool, cer_pool, cem_pool, unav_pool):
    cceevent_pool.remove("Cassata")
    cesummon_pool += ["Cassta", ]
    cesr_pool += ["Cassata", ]
    for ce1 in range(30):
        ceroll += ["Double Scoop", ]
    for ce2 in range(5):
        ceroll += ["Boston Lobster", ]
    for ce3 in range(56):
        ceroll += ["Bamboo Rice", ]
        ceroll += ["B-52", ]
        ceroll += ["Peking Duck", ]
        ceroll += ["Foie Gras", ]
    for ce4 in range(21):
        ceroll += ["Gingerbread", ]
        ceroll += ["Crab Long Bao", ]
    for ce5 in range(332):
        ceroll += ["Cassata", ]
    for ce6 in range(48):
        ceroll += ["Chocolate", ]
        ceroll += ["Brownie", ]
        ceroll += ["Sukiyaki" ,]
        ceroll += ["Udon", ]
        ceroll += ["Yunnan Noodles", ]
        ceroll += ["Gyoza", ]
        ceroll += ["Tiramisu", ]
        ceroll += ["Yuxiang", ]
        ceroll += ["Sweet Tofu", ]
        ceroll += ["Pastel de nata"]
        ceroll += ["Red Wine", ]
        ceroll += ["Salad", ]
        ceroll += ["Napoleon Cake", ]
        ceroll += ["Sanma", ]
        ceroll += ["Tangyuan", ]
        ceroll += ["Steak", ]
        ceroll += ["Hamburger", ]
        ceroll += ["Mango Pudding", ]
        ceroll += ["Hotdog", ]
        ceroll += ["Escargot", ]
    for ce7 in range(123):
        ceroll += ["Laba Congee", ]
        ceroll += ["Pineapple Cake", ]
        ceroll += ["Eggette", ]
    for ce8 in range(393):
        ceroll += ["Sakuramochi", ]
        ceroll += ["Zongzi",]
        ceroll += ["Spicy Gluten", ]
        ceroll += ["Tempura", ]
        ceroll += ["Sake", ]
        ceroll += ["Dorayaki", ]
        ceroll += ["Milk", ]
        ceroll += ["Taiyaki", ]
        ceroll += ["Tom Yum", ]
        ceroll += ["Macaron", ]
        ceroll += ["Sashimi", ]
        ceroll += ["Coffee", ]
        ceroll += ["Long Bao", ]
    for ce9 in range(392):
        ceroll += ["Cold Rice Shrimp", ]
        ceroll += ["Yellow Wine", ]
        ceroll += ["Miso Soup", ]
        ceroll += ["Orange Juice", ]
        ceroll += ["Omurice", ]
        ceroll += ["Jiuniang", ]
        ceroll += ["Ume Ochazuke", ]
    for ce10 in range(47):
        ceroll += ["Pancake", ]
    for ce11 in range(46):
        ceroll += ["Popcorn", ]
        ceroll += ["Jello", ]
        ceroll += ["Skewer", ]
    return ceroll

def cindex9entry(ceroll, ceevent_pool, cceevent_pool, cesummon_pool, ceur_pool, cesr_pool, cer_pool, cem_pool, unav_pool):
    cceevent_pool.remove("Cassata")
    cesummon_pool += ["Cassta", ]
    cesr_pool += ["Cassata", ]
    for ce1 in range(120):
        ceroll += ["Bamboo Rice", ]
    for ce2 in range(5):
        ceroll += ["Boston Lobster", ]
        ceroll += ["Double Scoop", ]
    for ce3 in range(42):
        ceroll += ["B-52", ]
        ceroll += ["Peking Duck", ]
        ceroll += ["Foie Gras", ]
    for ce4 in range(23):
        ceroll += ["Gingerbread", ]
    for ce5 in range(22):
        ceroll += ["Crab Long Bao", ]
    for ce6 in range(332):
        ceroll += ["Cassata", ]
    for ce7 in range(48):
        ceroll += ["Chocolate", ]
        ceroll += ["Brownie", ]
        ceroll += ["Sukiyaki" ,]
        ceroll += ["Udon", ]
        ceroll += ["Yunnan Noodles", ]
        ceroll += ["Gyoza", ]
        ceroll += ["Tiramisu", ]
        ceroll += ["Yuxiang", ]
        ceroll += ["Sweet Tofu", ]
        ceroll += ["Pastel de nata"]
        ceroll += ["Red Wine", ]
        ceroll += ["Salad", ]
        ceroll += ["Napoleon Cake", ]
        ceroll += ["Sanma", ]
        ceroll += ["Tangyuan", ]
        ceroll += ["Steak", ]
        ceroll += ["Hamburger", ]
        ceroll += ["Mango Pudding", ]
        ceroll += ["Hotdog", ]
        ceroll += ["Escargot", ]
    for ce8 in range(123):
        ceroll += ["Laba Congee", ]
        ceroll += ["Pineapple Cake", ]
        ceroll += ["Eggette", ]
    for ce9 in range(393):
        ceroll += ["Sakuramochi", ]
        ceroll += ["Zongzi",]
        ceroll += ["Spicy Gluten", ]
        ceroll += ["Tempura", ]
        ceroll += ["Sake", ]
        ceroll += ["Dorayaki", ]
        ceroll += ["Milk", ]
        ceroll += ["Taiyaki", ]
        ceroll += ["Tom Yum", ]
        ceroll += ["Macaron", ]
        ceroll += ["Sashimi", ]
        ceroll += ["Coffee", ]
        ceroll += ["Long Bao", ]
    for ce10 in range(392):
        ceroll += ["Cold Rice Shrimp", ]
        ceroll += ["Yellow Wine", ]
        ceroll += ["Miso Soup", ]
        ceroll += ["Orange Juice", ]
        ceroll += ["Omurice", ]
        ceroll += ["Jiuniang", ]
        ceroll += ["Ume Ochazuke", ]
    for ce11 in range(47):
        ceroll += ["Pancake", ]
    for ce12 in range(46):
        ceroll += ["Popcorn", ]
        ceroll += ["Jello", ]
        ceroll += ["Skewer", ]
    return ceroll

def cindex10entry(ceroll, ceevent_pool, cceevent_pool, cesummon_pool, ceur_pool, cesr_pool, cer_pool, cem_pool, unav_pool):
    ceevent_pool.remove("Toso")
    cceevent_pool.remove("Cassata")
    cesummon_pool += ["Toso", "Cassta", ]
    ceur_pool += ["Toso", ]
    cesr_pool += ["Cassata", ]
    for ce1 in range(120):
        ceroll += ["Toso", ]
    for ce2 in range(5):
        ceroll += ["Boston Lobster", ]
        ceroll += ["Double Scoop", ]
    for ce3 in range(35):
        ceroll += ["Bamboo Rice", ]
        ceroll += ["B-52", ]
        ceroll += ["Peking Duck", ]
        ceroll += ["Foie Gras", ]
    for ce4 in range(16):
        ceroll += ["Gingerbread", ]
    for ce5 in range(15):
        ceroll += ["Crab Long Bao", ]
    for ce6 in range(332):
        ceroll += ["Cassata", ]
    for ce7 in range(48):
        ceroll += ["Chocolate", ]
        ceroll += ["Brownie", ]
        ceroll += ["Sukiyaki" ,]
        ceroll += ["Udon", ]
        ceroll += ["Yunnan Noodles", ]
        ceroll += ["Gyoza", ]
        ceroll += ["Tiramisu", ]
        ceroll += ["Yuxiang", ]
        ceroll += ["Sweet Tofu", ]
        ceroll += ["Pastel de nata"]
        ceroll += ["Red Wine", ]
        ceroll += ["Salad", ]
        ceroll += ["Napoleon Cake", ]
        ceroll += ["Sanma", ]
        ceroll += ["Tangyuan", ]
        ceroll += ["Steak", ]
        ceroll += ["Hamburger", ]
        ceroll += ["Mango Pudding", ]
        ceroll += ["Hotdog", ]
        ceroll += ["Escargot", ]
    for ce8 in range(123):
        ceroll += ["Laba Congee", ]
        ceroll += ["Pineapple Cake", ]
        ceroll += ["Eggette", ]
    for ce9 in range(393):
        ceroll += ["Sakuramochi", ]
        ceroll += ["Zongzi",]
        ceroll += ["Spicy Gluten", ]
        ceroll += ["Tempura", ]
        ceroll += ["Sake", ]
        ceroll += ["Dorayaki", ]
        ceroll += ["Milk", ]
        ceroll += ["Taiyaki", ]
        ceroll += ["Tom Yum", ]
        ceroll += ["Macaron", ]
        ceroll += ["Sashimi", ]
        ceroll += ["Coffee", ]
        ceroll += ["Long Bao", ]
    for ce10 in range(392):
        ceroll += ["Cold Rice Shrimp", ]
        ceroll += ["Yellow Wine", ]
        ceroll += ["Miso Soup", ]
        ceroll += ["Orange Juice", ]
        ceroll += ["Omurice", ]
        ceroll += ["Jiuniang", ]
        ceroll += ["Ume Ochazuke", ]
    for ce11 in range(47):
        ceroll += ["Pancake", ]
    for ce12 in range(46):
        ceroll += ["Popcorn", ]
        ceroll += ["Jello", ]
        ceroll += ["Skewer", ]
    return ceroll

@commands.check(restriction)
@client.command(name = "cevent",
                pass_context = True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def event3(context, event_index, mode, foodsoul_or_rarity, amount):
    vaalid = False
    ceroll = []
    cesummon_pool = []
    cesummon_pool += csummon_pool
    ceur_pool = []
    ceur_pool += cur_pool
    cesr_pool = []
    cesr_pool += csr_pool
    cer_pool = []
    cer_pool += cr_pool
    cem_pool = []
    cem_pool += cm_pool
    ceevent_pool = []
    ceevent_pool += event_pool
    cceevent_pool = []
    cceevent_pool += cevent_pool
    unav_pool = []
    if event_index == "0" or event_index == "1":
        await client.say("Error - Invalid event index - Unavailable in the Chinese server")
    elif event_index == "2":
        vaalid = True
        ceroll = cindex2entry(ceroll, ceevent_pool, cceevent_pool, cesummon_pool, ceur_pool, cesr_pool, cer_pool, cem_pool, unav_pool)
    elif event_index == "3":
        vaalid = True
        ceroll = cindex3entry(ceroll, ceevent_pool, cceevent_pool, cesummon_pool, ceur_pool, cesr_pool, cer_pool, cem_pool, unav_pool)
    elif event_index == "4":
        vaalid = True
        ceroll = cindex4entry(ceroll, ceevent_pool, cceevent_pool, cesummon_pool, ceur_pool, cesr_pool, cer_pool, cem_pool, unav_pool)
    elif event_index == "5":
        vaalid = True
        ceroll = cindex5entry(ceroll, ceevent_pool, cceevent_pool, cesummon_pool, ceur_pool, cesr_pool, cer_pool, cem_pool, unav_pool)
    elif event_index == "6":
        vaalid = True
        ceroll = cindex6entry(ceroll, ceevent_pool, cceevent_pool, cesummon_pool, ceur_pool, cesr_pool, cer_pool, cem_pool, unav_pool)
    elif event_index == "7":
        vaalid = True
        ceroll = cindex7entry(ceroll, ceevent_pool, cceevent_pool, cesummon_pool, ceur_pool, cesr_pool, cer_pool, cem_pool, unav_pool)
    elif event_index == "8":
        vaalid = True
        ceroll = cindex8entry(ceroll, ceevent_pool, cceevent_pool, cesummon_pool, ceur_pool, cesr_pool, cer_pool, cem_pool, unav_pool)
    elif event_index == "9":
        vaalid = True
        ceroll = cindex9entry(ceroll, ceevent_pool, cceevent_pool, cesummon_pool, ceur_pool, cesr_pool, cer_pool, cem_pool, unav_pool)
    elif event_index == "10":
        vaalid = True
        ceroll = cindex10entry(ceroll, ceevent_pool, cceevent_pool, cesummon_pool, ceur_pool, cesr_pool, cer_pool, cem_pool, unav_pool)    
    if vaalid == True:
        if mode != "rarity" and mode != "foodsoul":
            await client.say('Error - Invalid mode: Must be "foodsoul" or "rarity"')
        elif mode == "foodsoul":
            lcesummon_pool = [iteme.lower() for iteme in cesummon_pool]
            lcceevent_pool = [itemccc.lower() for itemccc in cceevent_pool]
            lceevent_pool = [eventitem.lower() for eventitem in ceevent_pool]
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
            food_soul = foodsoul_or_rarity
            food_soul = food_soul.replace(".", " ")
            lfood_soul = food_soul.lower()
            if not(amount.isdigit()):
                await client.say('Error - Invalid 3rd input: Use "." instead of space')
            if int(amount) <= 0:
                await client.say("Error - Invalid 4th input: Number must be more than 0")
            elif lfood_soul not in lcesummon_pool:
                if lfood_soul in lnone_pool:
                    ivalid = True
                    await client.say("Error - Invalid food soul: " + lfood_soul.title() + " cannot be summoned")
                if lfood_soul in leevent_pool or lfood_soul in lcevent_pool:
                    ivalid = True
                    await client.say("Error - Invalid food soul: " + lfood_soul.title() + " is from another event; check your event index number with ``f!eventindex``")
                if lfood_soul in lunav_pool:
                    await client.say("Error - Invalid food soul: " + lfood_soul.title() + " is not in the summoning pool during this event")
                elif ivalid == False:
                    await client.say("Error - Invalid 3rd input: Food Soul does not exsist or improper spelling")
            elif int(amount) > 1000:
                await client.say("Error - Invalid 4th input: Number must be less than 1000")
            elif lfood_soul in lcesummon_pool and int(amount) >= 1 and int(amount) < 1000:
                await client.say("Summoning food souls...\n")
                time.sleep(2)
                count_foodsoul = 0
                while int(amount) != count_foodsoul:
                    foodsoul = random.choice(ceroll)
                    valid = True
                    lfoodsoul = foodsoul.lower()
                    summoned += [foodsoul, ]
                    if foodsoul in ceur_pool:
                        ur += 1
                        number += 1
                    if foodsoul in cesr_pool:
                        sr += 1
                        number += 1
                    if foodsoul in cer_pool:
                        r += 1
                        number += 1
                    if foodsoul in cem_pool:
                        m += 1
                        number += 1
                    if lfood_soul == lfoodsoul:
                        count_foodsoul += 1
            bigline = output4(summoned, valid, ur, sr, r, m, number, context, cesummon_pool, ceur_pool, cesr_pool, cer_pool, cem_pool)
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
            if not(event_index.isdigit()):
                await client.say("Error - Invalid 1st input: Event index must be 2-10")
            if lrarity not in lrarity_pool:
                await client.say("Error - Invalid 3rd input: Rarity does not exsist or improper spelling")
            if not(amount.isdigit()):
                await client.say("Error - Invalid 4th input: Must be a positive integer")
            elif int(amount) <= 0:
                await client.say("Error - Invalid 4th input: Number must be more than 0")
            elif int(amount) > 1000:
                await client.say("Error - Invalid 4th input: Number must be less than 1000")
            elif lrarity in lrarity_pool and int(amount) >= 1 and int(amount) < 1000:
                valid = True
                await client.say("Summoning food souls...\n")
                time.sleep(2)
                count_foodsoul = 0
                while int(amount) != count_foodsoul:
                    foodsoul = random.choice(eroll)
                    summoned += [foodsoul, ]
                    if foodsoul in ceur_pool:
                        ur += 1
                        number += 1
                        if lrarity == "ur":
                            count_foodsoul += 1
                    elif foodsoul in cesr_pool:
                        sr += 1
                        number += 1
                        if lrarity == "sr":
                            count_foodsoul += 1
                    elif foodsoul in cer_pool:
                        r += 1
                        number += 1
                        if lrarity == "r":
                            count_foodsoul += 1
                    elif foodsoul in cem_pool:
                        m += 1
                        number += 1
                        if lrarity == "m":
                            count_foodsoul += 1
            bigline = output4(summoned, valid, ur, sr, r, m, number, context, cesummon_pool, ceur_pool, cesr_pool, cer_pool, cem_pool)
            await client.say(bigline)

@commands.check(restriction)
@client.command(name = "csummonevent",
                pass_context = True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def event4(context, event_index, number):
    vaalid = False
    ceroll = []
    cesummon_pool = []
    cesummon_pool += csummon_pool
    ceur_pool = []
    ceur_pool += cur_pool
    cesr_pool = []
    cesr_pool += csr_pool
    cer_pool = []
    cer_pool += cr_pool
    cem_pool = []
    cem_pool += cm_pool
    ceevent_pool = []
    ceevent_pool += event_pool
    cceevent_pool = []
    cceevent_pool += cevent_pool
    unav_pool = []
    if event_index == "0" or event_index == "1":
        await client.say("Error - Invalid event index - Unavailable in the Chinese server")
    elif event_index == "2":
        vaalid = True
        ceroll = cindex2entry(ceroll, ceevent_pool, cceevent_pool, cesummon_pool, ceur_pool, cesr_pool, cer_pool, cem_pool, unav_pool)
    elif event_index == "3":
        vaalid = True
        ceroll = cindex3entry(ceroll, ceevent_pool, cceevent_pool, cesummon_pool, ceur_pool, cesr_pool, cer_pool, cem_pool, unav_pool)
    elif event_index == "4":
        vaalid = True
        ceroll = cindex4entry(ceroll, ceevent_pool, cceevent_pool, cesummon_pool, ceur_pool, cesr_pool, cer_pool, cem_pool, unav_pool)
    elif event_index == "5":
        vaalid = True
        ceroll = cindex5entry(ceroll, ceevent_pool, cceevent_pool, cesummon_pool, ceur_pool, cesr_pool, cer_pool, cem_pool, unav_pool)
    elif event_index == "6":
        vaalid = True
        ceroll = cindex6entry(ceroll, ceevent_pool, cceevent_pool, cesummon_pool, ceur_pool, cesr_pool, cer_pool, cem_pool, unav_pool)
    elif event_index == "7":
        vaalid = True
        ceroll = cindex7entry(ceroll, ceevent_pool, cceevent_pool, cesummon_pool, ceur_pool, cesr_pool, cer_pool, cem_pool, unav_pool)
    elif event_index == "8":
        vaalid = True
        ceroll = cindex8entry(ceroll, ceevent_pool, cceevent_pool, cesummon_pool, ceur_pool, cesr_pool, cer_pool, cem_pool, unav_pool)
    elif event_index == "9":
        vaalid = True
        ceroll = cindex9entry(ceroll, ceevent_pool, cceevent_pool, cesummon_pool, ceur_pool, cesr_pool, cer_pool, cem_pool, unav_pool)
    elif event_index == "10":
        vaalid = True
        ceroll = cindex10entry(ceroll, ceevent_pool, cceevent_pool, cesummon_pool, ceur_pool, cesr_pool, cer_pool, cem_pool, unav_pool)    
    if vaalid == True:
        summoned = []
        eachsummoned = []
        ur = 0
        sr = 0
        r = 0
        m = 0
        valid = False
        if not(event_index.isdigit()):
            await client.say("Error - Invalid 1st input: Event index must be 2-10")
        if int(event_index) > 10 or int(event_index) <= 1:
            await client.say("Error - Invalid event index: Must be 2-10")
        if not(number.isdigit()):
            await client.say("Error - Invalid 2nd input: Must be a positive integer")
        elif int(number) <= 0:
            await client.say("Error - Invalid number: Must be more than 0")
        elif int(number) > 1000:
            await client.say("Error - Invalid number: Must be less than 1000000")
        elif int(number) >= 1 and int(number) < 1000000:
            await client.say("Summoning food souls...")
            time.sleep(2)
            number = int(number)
            valid = True
            for x1 in range(number):
                foodsoul = random.choice(ceroll)
                summoned += [foodsoul, ]
                if foodsoul in ceur_pool:
                    ur += 1
                elif foodsoul in cesr_pool:
                    sr += 1
                elif foodsoul in cer_pool:
                    r += 1
                elif foodsoul in cem_pool:
                    m += 1
            bigline = output4(summoned, valid, ur, sr, r, m, number, context, cesummon_pool, ceur_pool, cesr_pool, cer_pool, cem_pool)
            await client.say(bigline)

@commands.check(restriction)
@client.command(name = "eventindex")
@commands.cooldown(1, 30, commands.BucketType.user)
async def eventhelp():
    embed = discord.Embed(title = "Event Index List", description = "Use the event index number to input what event you want to summon in!\nThe global server has only event index numbers 0 to 2 available while the Chinese sever has 2 to 10 available. Note that 2. Sakura Falls have different rates in the global server and Chinese server\nIn event index number 2 and 3 for the Chinese server, Gyoza, Yunnan Noodles, Udon and B-52 are NOT in the pool during the event. They are added into the pool afterwards.", color = 0x2ecc71)
    embed.add_field(name = "0. Sweet Temptations", value = "Chocolate has been addded to the summoning pool permamently; Gingerbread and Chocolate have an increased summoning rate for a limited time.\nGingerbread: 0.23% > 1.2%\nChocolate: 3.33%, drops to 0.8% after event", inline = False)
    embed.add_field(name = "1. Brewing Fine Wine", value = "Toso and Sweet Tofu have been added to the summoning pool for a limited time.\nToso: 1.5%\nSweet Tofu: 6.61%", inline = False)
    embed.add_field(name = "2. Sakura Falls (樱落水月)", value = "Strawberry Daifuku and Raindrop Cake have been added to the summoning pool for a limited time.\nStrawberry Daifuku: 1.2%\nRaindrop Cake: 0.31%", inline = False)
    embed.add_field(name = "3. 盛夏沁凉", value = "Pufferfish and Bonito Rice have been added to the summoning pool for a limited time.\nPufferfish: 0.48%\nBonito Rice: 0.96%", inline = False)
    embed.add_field(name = "4. 月华倾泻", value = "Toso, Caviar and Seaweed Soup have been added to the summoning pool for a limited time.\nToso: 0.5%\nCaviar: 0.5%\nSeaweed Soup: 3.41%", inline = False)
    embed.add_field(name = "5. 冰与火之夏", value = "Spicy Hot Pot and Beer have been added to the summoning pool for a limited time.\nSpicy Hot Pot: 1.2%\nBeer: 3.32%", inline = False)
    embed.add_field(name = "6. 水映夏花", value = "Cassata and Raindrop Cake have been added to the summoning pool for a limited time.\nCassata: 3.32%\nRaindrop Cake: 1.2%", inline = False)
    embed.add_field(name = "7. 安夏回忆", value = "Cassata has been added to the summoning pool and Crab Long Bao has an increased summoning rate for a limited time.\nCrab Long Bao: 0.36% > 1.2%\n Cassata: 3.32%", inline = False)
    embed.add_field(name = "8. 夏季甜点", value = "Cassata has been added to the summoning pool and Double Scoop has an increased summoning rate for a limited time.\nDouble Scoop: 0.05% > 0.3%\n Cassata: 3.32%", inline = False)
    embed.add_field(name = "9. 绿荫之夏", value = "Cassata has been added to the summoning pool and Bamboo Rice has an increased summoning rate for a limited time.\nBamboo Rice: 0.52% > 1.2%\n Cassata: 3.32%", inline = False)
    embed.add_field(name = "10. 流浪夏日", value = "Toso and Cassata has been added to summoning pool for a limited time.\nToso: 1.2%\n Cassata: 3.32%", inline = False)
    await client.say(embed = embed)

# Non summoning commands:

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
    embed.add_field(name = "f!food <dish>", value = 'Shows the recipe, cuisine, seasoning and type of food. Use "." instead of space.', inline = False)
    embed.add_field(name = "f!soulinfo <food_soul>", value = 'Shows the information about a food soul. Use "." instead of space.\nNOTE: This feature is UNRELEASED.', inline = False)
    embed.add_field(name = "f!info", value = "Gives a paragraph of information about Foie Gras", inline = False)
    embed.add_field(name = "f!dialogue", value = "Words of wisdom from Foie Gras.", inline = False)
    embed.add_field(name = "f!credit", value = "Reveals the people behind the bot.", inline = False)
    await client.say(embed = embed)

@commands.check(restriction)
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

@commands.check(restriction)
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
    dish = dish.replace(".", " ")
    dish = dish.replace(" and ", " & ")
    ldish = dish.lower()
    if ldish not in lfood_pool:
        if ldish not in llostfood_pool:
            await client.say("Error - Invalid input: Food does not exsist or improper spelling")
        elif ldish in llostfood_pool:
            if ldish == "calamari skewer":
                foodstats = ["72", "79", "87", "96", "106", "35", "49", "63", "77", "105", "9", "9", "9", "8", "8", "180", "24"]
                embed = output2(foodstats, "Calamari Skewer", 0xe67e22, "Lost", "Squid (1-7)", "", "", "5", "Make 5 dishes of any kind", "771", "910", "1500", "819", "Chili", "Black Pepper", "Texture")
                await client.say(embed = embed)
            elif ldish == "garlic oyster":
                foodstats = ["120", "132", "145", "160", "176", "45", "63", "81", "99", "135", "15", "14", "14", "13", "12", "300", "40"]
                embed = output2(foodstats, "Garlic Oyster", 0x979c9f, "Lost", "Oyster (2-8)", "", "", "8", "Submit 5 Calamari Skewers", "972", "1800", "506", "722", "Chili", "Garlic", "Aroma")
                await client.say(embed = embed)
            elif ldish == "grilled prawns":
                foodstats = ["84", "92", "101", "111", "122", "105", "147", "189", "231", "315", "11", "10", "10", "9", "9", "210", "28"]
                embed = output2(foodstats, "Grilled Prawns", 0xa84300, "Lost", "Shrimp (3-8)", "", "", "10", "Cook C rated dishes 8 times", "1500", "707", "992", "801", "Cooking Wine", "Salt", "Flavor")
                await client.say(embed = embed)
            elif ldish == "pickled salmon head":
                foodstats = ["79", "87", "96", "106", "117", "55", "77", "99", "121", "165", "12", "11", "11", "10", "10", "180", "26"]
                embed = output2(foodstats, "Pickled Salmon Head", 0x979c9f, "Lost", "Salmon (4-2)", "Pickled Peppers (4-8)", "", "12", "Challenge Parisel 1-1", "902", "754", "744", "1600", "Garlic",  "Chili", "Appearence")
                await client.say(embed = embed)
            elif ldish == "tomato & eggs":
                foodstats = ["119", "131", "144", "158", "174", "35", "49", "63", "77", "105", "18", "17", "17", "16", "15", "270", "40",]
                embed = output2(foodstats, "Tomato & Eggs", 0xe74c3c, "Lost", "Egg (5-2)", "Tomato (5-8)", "", "14", "Clear Rube's Mischief 3 times", "888", "1700", "705", "707", "Salt", "Sugar", "Aroma")
                await client.say(embed = embed)
            elif ldish == "steamed mushrooms":
                foodstats = ["119", "131", "144", "158", "174", "225", "315", "405", "495", "675", "18", "17", "17", "16", "15", "270", "40"]
                embed = output2(foodstats, "Steamed Mushrooms", 0xffee, "Lost", "Shrimp (3-8)", "Cheese (6-2)", "Shiitake (6-8)", "16", "Challenge Parisel 1-2", "1700", "750", "800", "750", "Cooking Wine", "Cooking Oil", "Flavor")
                await client.say(embed = embed)
            elif ldish == "spaghetti":
                foodstats = ["101", "111", "122", "134", "147", "43", "63", "81", "99", "135", "15", "14", "14", "13", "12", "210", "34"]
                embed = output2(foodstats, "Spaghetti", 0xf1c40f, "Lost", "Tomato (5-8)", "Pasta (7-10)", "", "18", "Complete 2 Take-out orders from Gloriville", "725", "813", "1500", "962", "Black Pepper", "Sugar", "Texture")
                await client.say(embed = embed)
            elif ldish == "har gow":
                foodstats = ["101", "111", "122", "134", "147", "85", "119", "153", "187", "255", "15", "14", "14", "13", "12", "210", "34"]
                embed = output2(foodstats, "Har Gow", 0xffffff, "Lost", "Pork Belly (1-6)", "Shrimp (3-8)", "Wheat Flour (8-4)", "20", "Develop the menu 2 times", "912", "692", "796", "1600", "Cooking Oil", "Ginger", "Appearence")
                await client.say(embed = embed)
            elif ldish == "gold cake":
                foodstats = ["86", "95", "105", "116", "128", "125", "175", "225", "275", "375", "12", "12", "12", "11", "10", "180", "29"]
                embed = output2(foodstats, "Gold Cake", 0xf1c40f, "Lost", "Egg (5-2)", "Butter (7-8)", "Tapioca (8-7)", "22", "Complete all daily missions", "680", "1900", "858", "565", "Salad Dressing", "Condensed Milk", "Aroma")
                await client.say(embed = embed)
            elif ldish == "mixed greens":
                foodstats = ["140", "154", "169", "186", "205", "125", "175", "225", "275", "375", "21", "20", "20", "19", "18", "270", "47"]
                embed = output2(foodstats, "Mixed Greens", 0x2ecc71, "Lost", "Cucumber (2-2)", "Egg (5-2)", "Enokitake (9-8)", "24", "Challenge Parisel 4-2", "1700", "717", "707", "876", "Garlic", "Chili", "Flavor")
                await client.say(embed = embed)
            elif ldish == "stir-fried mussels":
                foodstats = ["156", "172", "189", "208", "229", "225", "315", "405", "495", "675", "23", "22", "22", "21", "20", "300", "52"]
                embed = output2(foodstats, "Stir-Fried Mussels", 0x546e7a, "Lost", "Mussels (10-8)", "", "", "26", "Serve 100 regular customers in your restaurant", "607", "984", "1800", "609", "Scallion", "Cooking Wine", "Texture")
                await client.say(embed = embed)
            elif ldish == "mushroom alfredo":
                foodstats = ["94", "103", "113", "124", "136", "55", "77", "99", "121", "165", "14", "13", "13", "12", "11", "180", "31"]
                embed = output2(foodstats, "Mushroom Alfredo", 0xffeea9, "Lost", "Mushroom (7-3)", "Pasta (7-10)", "Cream (11-7)", "28", "Collect 15 Low-Grade Screws (Screws already in inventory are not counted)", "617", "687", "896", "1800", "Condensed Milk", "Black Pepper", "Appearence")
                await client.say(embed = embed)
            elif ldish == "cha siu bao":
                foodstats = ["101", "111", "122", "134", "147", "145", "203", "261", "319", "435", "15", "14", "14", "13", "12", "180", "34"]
                embed = output2(foodstats, "Cha Siu Bao", 0x95a5a6, "Lost", "Flour (12-2)", "BBQ Pork (12-8)", "", "30", "Make 10 dishes of any kind", "1600", "938", "756", "706", "Salad Dressing", "Cooking Wine", "Flavor")
                await client.say(embed = embed)
            elif ldish == "spinach noodles":
                foodstats = ["151", "166", "183", "201", "221", "125", "175", "225", "275", "375", "22", "21", "21", "20", "19", "270", "50"]
                embed = output2(foodstats, "Spinach Noodles", 0x2ecc71, "Lost", "Egg (5-2)", "Flour (12-2)", "Spinach (13-6)", "32", "Challenge Parisel stage 6-2", "556", "2000", "907", "537", "Soy Sauce", "Salad Dressing", "Aroma")
                await client.say(embed = embed)
            elif ldish == "mint pineapple":
                foodstats = ["118", "130", "143", "157", "173", "105", "147", "189", "231", "315", "17", "16", "16", "15", "14", "210", "39"]
                embed = output2(foodstats, "Mint Pineapple", 0xf1c40f, "Lost", "Pineapple (14-3)", "Mint (14-7)", "", "34", "Complete 5 Delivery orders in the Gloriville area", "508", "413", "2100", "979", "Icing", "Salad Dressing", "Texture")
                await client.say(embed = embed)
            elif ldish == "apple sangria":
                foodstats = ["126", "139", "153", "168", "185", "145", "203", "261", "319", "435", "18", "17", "17", "16", "15", "210", "41"]
                embed = output2(foodstats, "Apple Sangria", 0xe74c3c, "Lost", "Apple (15-1)", "Red Wine (15-6)", "", "36", "Collect and submit 10 Spinach", "578", "515", "898", "2000", "Icing", "Rock Sugar", "Appearence")
                await client.say(embed = embed)
            elif ldish == "brasied lamb":
                foodstats = ["126", "139", "153", "168", "185", "245", "343", "441", "539", "735", "18", "17", "17", "16", "15", "210", "42"]
                embed = output2(foodstats, "Braised Lamb", 0xe74c3c, "Lost", "Red Wine (15-6)", "Lamb Leg (15-9)", "", "38", "Bring a Control talent into battle", "397", "2200", "808", "595", "Sugar", "Garlic", "Aroma")
                await client.say(embed = embed)
            elif ldish == "mushroom chicken stew":
                foodstats = ["162", "178", "196", "216", "238", "75", "105", "135", "165", "225", "23", "22", "22" , "21", "20", "270", "54"]
                embed = output2(foodstats, "Mushroom Chicken Stew", 0x992d22, "Lost", "Shiitake (6-8)", "Diced Chicken (16-5)", "Glass Noodles (16-9)", "40", "Challenge Spirng Outskirts 9-2", "1900", "504", "938", "658", "Ginger", "Soy Sauce", "Flavor")
                await client.say(embed = embed)
            elif ldish == "matcha cake":
                foodstats = ["134", "147", "162", "178", "196", "85", "119", "153", "187", "255", "19", "18", "18", "17", "16", "210", "45"]
                embed = output2(foodstats, "Matcha Cake", 0x1f8b4c, "Lost", "Egg (5-2)", "Flour (12-2)", "Matcha Power (17-6)", "41", "Defeat 20 Dine and Dash customers in the restaurant", "875", "609", "316", "2200", "Sago", "Icing", "Appearence")
                await client.say(embed = embed)
            elif ldish == "cappuccino":
                foodstats = ["134", "147", "162", "178", "196", "205", "287", "369", "451", "615", "19", "18", "18", "17", "16", "210", "45"]
                embed = output2(foodstats, "Cappuccino", 0xc27c0e, "Lost", "Milk (12-5)", "Coffee Beans (17-7)", "", "42", "Collect 50 Mints (those already in inventory are not counted)", "354", "607", "2100", "939", "Sago", "Condensed Milk", "Texture")
                await client.say(embed = embed)
            elif ldish == "fruit tea":
                foodstats = ["173", "190", "209", "230", "253", "165", "231", "297", "363", "495", "25", "24", "24", "23", "22", "270", "58"]
                embed = output2(foodstats, "Fruit Tea", 0xe67e22, "Lost", "Strawberry (18-1)", "Lemon (18-6)", "Osmanthus (18-9)", "44", "Complete all daily missions", "1900", "988", "682", "430", "Rock Sugar", "Sago", "Flavor")
                await client.say(embed = embed)
            elif ldish == "lemon pie":
                foodstats = ["143", "157", "173", "190", "209", "185", "259", "333", "407", "555", "20", "19", "19", "18", "17", "210", "48"]
                embed = output2(foodstats, "Lemon Pie", 0xf1c40f, "Lost", "Egg (5-2)", "Flour (12-2)", "Lemon (18-6)", "45", "Develop the menu 3 times", "600", "2200", "600", "600", "Condensed Milk", "Sago", "Aroma")
                await client.say(embed = embed)
            elif ldish == "meat zongzi":
                foodstats = ["143", "157", "173", "190", "209", "165", "231", "297", "363", "495", "20", "19", "19", "18", "17", "210", "48"]
                embed = output2(foodstats, "Meat Zongzi", 0x1f8b4c, "Lost", "Pork Loin (9-2)", "Glutinous Rice (19-7)", "", "47", "Challenge Spring Outskirts 12-2", "683", "901", "2100", "416", "Soy Sauce", "Cooking Oil", "Texture")
                await client.say(embed = embed)
            elif ldish == "stuffed lotus root":
                foodstats = ["143", "157", "173", "190", "209", "245", "343", "441", "539", "735", "20", "19", "19", "18", "17", "210", "47"]
                embed = output2(foodstats, "Stuffed Lotus Root", 0xe67e22, "Lost", "Osmanthus (18-9)", "Glutinous Rice (19-7)", "Lotus Root (20-8)", "49", "Submit 20 Lemon Pies", "405", "307", "888", "2400", "Rock Sugar", "Icing", "Appearence")
                await client.say(embed = embed)
            elif ldish == "lotus root stir-fry":
                foodstats = ["173", "190", "209", "230", "253", "185", "259", "333", "407", "555", "24", "23", "23", "22", "21", "240", "58"]
                embed = output2(foodstats, "Lotus Root Stir-Fry", 0xe91e63, "Lost", "Onion (9-5)", "Lotus Root (20-8)", "Black Fungus (21-6)", "50", "Complete 10 Delivery orders in the Nevras are", "2000", "694", "888", "418", "Salt", "Rock Sugar", "Flavor")
                await client.say(embed = embed)
            elif ldish == "black fungus congee":
                foodstats = ["216", "238", "262", "288", "317", "245", "343", "441", "539", "735", "30", "29", "29", "28", "27", "300", "72"]
                embed = output2(foodstats, "Black Fungus Congee", 0x546e7a, "Lost", "Rice (8-2)", "Black Fungus (21-6)", "King Mushroom (21-7)", "52", "Collect and submit 10 Advanced Seasoning", "868", "2300", "422", "410", "Sugar", "Scallion", "Aroma")
                await client.say(embed = embed)
            elif ldish == "sanma shioyaki":
                foodstats = ["155", "166", "183", "201", "221", "205", "287", "369", "451", "615", "21", "20", "20", "19", "18", "210", "50"]
                embed = output2(foodstats, "Sanma Shioyaki", 0x546e7a, "Lost", "Sanma (22-7)", "", "", "54", "Collect and submit 10 Advanced Sesaoning", "493", "285", "822", "2400", "Cooking Oil", "Salt", "Appearence")
                await client.say(embed = embed)
            elif ldish == "steamed crab":
                foodstats = ["182", "200", "220", "242", "266", "245", "343", "441", "539", "735", "26", "25", "25", "24", "23", "240", "61"]
                embed = output2(foodstats, "Steamed Crab", 0xe74c3c, "Lost", "Mitten Crab (23-7)", "", "", "56", "Challenge Outskirts 16-3", "835", "388", "2300", "477", "Scallion", "Ginger", "Texture")
                await client.say(embed = embed)
            elif ldish == "crab rice cake":
                foodstats = ["182", "200", "220", "242", "266", "75", "105", "135", "165", "225", "26", "25", "25", "24", "23", "240", "61"]
                embed = output2(foodstats, "Crab Rice Cake", 0xe74c3c, "Lost", "Mitten Crab (23-7)", "Rice Cake (23-8)", "", "58", "Complete 15 Delivery orders in the Sakurajima area", "2300", "354", "514", "832", "Ginger", "Soy Sauce", "Flavor")
                await client.say(embed = embed)
            elif ldish == "curry crab":
                foodstats = ["228", "251", "276", "304", "334", "245", "343", "441", "539", "735", "32", "31", "31", "30", "29", "300", "76"]
                embed = output2(foodstats, "Curry Crab", 0xf1c40f, "Lost", "Blue Crab (24-6)", "Curry Cube (24-7)", "", "60", "Make 50 A grade dishes", "409", "2400", "227", "964", "Black Pepper", "Scallion", "Aroma")
                await client.say(embed = embed)
##            elif ldish == "yam pigeon soup":
##                foodstats = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
##                embed = output2(foodstats, "Yam Pigeon Soup", , "Lost", "", "", "", "60", "Serve 200 regular customers in your restaurant", "", "", "", "", "Ginger", "Scallion", "Appearence")
##                await client.say(embed = embed)
##            elif ldish == "bamboo & meat stir-fry":
##                foodstats = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
##                embed = output2(foodstats, "Bamboo & Meat Stir-Fry", , "Lost", "", "", "", "63", "Explore Sandstone Cave once", "", "", "", "", "", "Garlic", "Chili", "Flavor")
##                await client.say(embed = embed)
##            elif ldish == "braised geese":
##                foodstats = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
##                embed = output2(foodstats, "Braised Geese", , "Lost", "", "", "", "66", "Defeat 20 Dine and Dash customers in the restaurant", "", "", "", "", "", "Cooking Oil", "Soy Sauce", "Aroma")
##                await client.say(embed = embed)
##            elif ldish == "roe meat ball":
##                foodstats = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
##                embed = output2(foodstats, "Roe Meat Ball", , "Lost", "", "", "", "69", "Collect 50 Crab Roe (those already in inventory are not counted)", "", "", "", "", "Scallion", "Ginger", "Texture")
##                await client.say(embed = embed)
##            elif ldish == "birds nest":
##                foodstats = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
##                embed = output2(foodstats, "Birds Nest", , "Lost", "", "", "", "72", "Cook 30 A grade dishes", "", "", "", "", "Sugar", "Rock Sugar", "Flavor",)
##                await client.say(embed = embed)
##            elif ldish == "ginseng stew chicken":
##                foodstats = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
##                embed = output2(foodstats, "Ginseng Chicken Stew", , "Lost", "", "", "", "75", "Challenge Fallen Angel Remains 25-2", "", "", "", "", "Ginger", "Garlic", "Texture")
##                await client.say(embed = embed)            
    elif ldish in lfood_pool:
        if ldish == "stir-fried potatoes":
            foodstats = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
            embed = output2(foodstats, "Stir-Fried Potatoes", 0xf1c40f, "Potato (1-3)", "", "", "Light Kingdom", "Potato (1-3)", "", "", "", "", "801", "1500", "992", "707", "Chili", "Scallion", "Flavor")
            await client.say(embed = embed)
        elif ldish == "braised pork":
            foodstats = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
            embed = output2(foodstats, "Braised Pork", 0xa84300, "Light Kingdom", "Pork Belly (1-6)", "", "", "", "", "771", "910", "1500", "819", "Scallion", "Soy Sauce", "Texture")
            await client.say(embed = embed)
        elif ldish == "braised eggplant":
            foodstats = ["24", "26", "29", "32", "35", "125", "175", "225", "275", "375", "3", "3", "3", "2", "2", "", ""]
            embed = output2(foodstats, "Braised Eggplant", 0x71368a, "Light Kingdom", "Eggplant (2-7)", "", "", "", "", "717", "707", "876", "1700", "Garlic", "Cooking Oil", "Appearence")
            await client.say(embed = embed)
        elif ldish == "sauteed lettuce":
            foodstats = ["53", "58", "64", "70", "77", "105", "147", "189", "231", "315", "8", "8", "8", "7", "7", "120", "18"]
            embed = output2(foodstats, "Sauteed Lettuce", 0x2ecc71, "Light Kingdom", "Lettuce (3-1)", "", "", "", "", "725", "1500", "813", "962", "Soy Sauce", "Garlic", "Aroma")
            await client.say(embed = embed)
        elif ldish == "carrot bread":
            foodstats = ["31", "34", "37", "41", "45", "35", "49", "63", "77", "105", "5", "5", "5", "4", "4", "70", "10"]
            embed = output2(foodstats, "Carrot Bread", 0xe67e22, "Light Kingdom", "Carrot (3-5)", "Bread (4-4)", "", "", "", "888", "1700", "705", "707", "Icing", "Salad Dressing", "Aroma")
            await client.say(embed = embed)
        elif ldish == "cucumber egg stir-fry":
            foodstats = ["79", "87", "96", "106", "117", "225", "315", "405", "495", "675", "12", "11", "11", "10", "10", "180", "26"]
            embed = output2(foodstats, "Cucumber Egg Stir-Fry", 0x2ecc71, "Light Kingdom", "Cucumber (2-2)", "Egg (5-2)", "", "", "", "1700", "750", "800", "750", "Sugar", "Scallion", "Flavor")
            await client.say(embed = embed)
        elif ldish == "black pepper beef":
            foodstats = ["43", "47", "52", "57", "63", "45", "63", "81", "99", "135", "7", "7", "7", "6", "6", "90", "14"]
            embed = output2(foodstats, "Black Pepper Beef", 0xc27c0e, "Light Kingdom", "Beef Tenderloin (5-6)", "Green Pepper (6-6)", "", "", "", "587", "515", "898", "2000", "Salt", "Cooking Wine", "Appearence")
            await client.say(embed = embed)
        elif ldish == "sauteed mushrooms":
            foodstats = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
            embed = output2(foodstats, "Sauteed Mushrooms", 0xc27c0e, "Light Kingdom", "Shiitake (6-8)", "Mushroom (7-3)", "", "", "", "972", "506", "1800", "722", "Black Pepper", "Cooking Oil", "Texture")
            await client.say(embed = embed)
        elif ldish == "egg fried rice":
            foodstats = ["29", "32", "35", "39", "43", "75", "105", "135", "165", "225", "5", "5", "5", "4", "4", "60", "10"]
            embed = output2(foodstats, "Egg Fried Rice", 0xf1c40f, "Light Kingdom", "Egg (5-2)", "Rice (8-2)", "", "", "", "556", "2000", "907", "537", "Scallion", "Salt", "Aroma")
            await client.say(embed = embed)
        elif ldish == "salmon fried rice":
            foodstats = ["62", "68", "75", "83", "91", "55", "77", "99", "121", "165", "9", "9", "9", "8", "8", "120", "21"]
            embed = output2(foodstats, "Salmon Fried Rice", 0xe67e22, "Light Kingdom", "Salmon (4-2)", "Rice (8-2)", "Onion (9-5)", "", "", "1600", "754", "902", "744", "Cooking Oil", "Black Pepper", "Flavor")
            await client.say(embed = embed)
        elif ldish == "onion fried rice":
            foodstats = ["94", "103", "113", "124", "136", "55", "77", "99", "121", "165", "14", "13", "13", "12", "11", "180", "31"]
            embed = output2(foodstats, "Onion Fried Rice", 0x9b59b6, "Light Kingdom", "Rice (8-2)", "Pork Loin (9-2)", "Onion (9-5)", "", "", "405", "888", "2400", "307", "Salt", "Chili", "Texture")
            await client.say(embed = embed)
        elif ldish == "bacon fried rice":
            foodstats = ["62", "68", "75", "83", "91", "165", "231", "297", "363", "495", "9", "9", "9", "8", "8", "120", "21"]
            embed = output2(foodstats, "Bacon Fried Rice", 0x992d22, "Light Kingdom", "Carrot (3-5)", "Rice (8-2)", "Bacon (10-3)", "", "", "875", "609", "316", "2200", "Chili", "Black Pepper", "Appearence")
            await client.say(embed = embed)
        elif ldish == "braised octopus":
            foodstats = ["39", "43", "47", "52", "57", "165", "231", "297", "363", "495", "6", "6", "6", "5", "5", "70", "13"]
            embed = output2(foodstats, "Braised Octopus", 0x992d22, "Light Kingdom", "Green Pepper (6-6)", "Octopus (11-4)", "", "", "", "912", "692", "796", "1600", "Garlic", "Soy Sauce", "Appearence")
            await client.say(embed = embed)
        elif ldish == "risotto":
            foodstats = ["101", "111", "122", "134", "147", "145", "203", "261", "319", "435", "15", "14", "14", "13", "12", "180", "34"]
            embed = output2(foodstats, "Risotto", 0xf1c40f, "Light Kingdom", "Cheese (6-2)", "Rice (8-2)", "Cream (11-7)", "", "", "504", "938", "1900", "658", "Sago", "Sugar", "Texture")
            await client.say(embed = embed)
        elif ldish == "butter bread":
            foodstats = ["67", "74", "81", "89", "98", "125", "175", "225", "275", "375", "10", "10", "10", "9", "9", "70", "22"]
            embed = output2(foodstats, "Butter Bread", 0xe67e22, "Light Kingdom", "Egg (5-2)", "Butter (7-8)", "Flour (12-2)", "", "", "2000", "694", "888", "418", "Condensed Milk", "Icing", "Flavor")
            await client.say(embed = embed)
        elif ldish == "emerald roll":
            foodstats = ["36", "40", "44", "48", "53", "245", "343", "441", "539", "735", "6", "6", "6", "5", "5", "60", "12"]
            embed = output2(foodstats, "Emerald Roll", 0x2ecc71, "Light Kingdom", "Cabbage (13-5)", "Spinach (13-6)", "", "", "", "508", "413", "979", "2100", "Soy Sauce", "Icing", "Appearence")
            await client.say(embed = embed)
        elif ldish == "corn pie":
            foodstats = ["108", "119", "131", "144", "158", "75", "105", "135", "165", "225", "16", "15", "15", "14", "13", "180", "36"]
            embed = output2(foodstats, "Corn Pie", 0xf1c40f, "Light Kingdom", "Corn (11-5)", "Starch (13-9)", "", "", "", "617", "687", "896", "1800", "Cooking Oil", "Salad Dressing", "Appearence")
            await client.say(embed = embed)
        elif ldish == "toffee apple":
            foodstats = ["58", "64", "70", "77", "85", "85", "119", "153", "187", "255", "9", "9", "9", "8", "8", "90", "19"]
            embed = output2(foodstats, "Toffee Apple", 0xe67e22, "Light Kingdom", "Starch (13-9)", "Apple (15-1)", "", "", "", "600", "2200", "600", "600", "Sugar", "Rock Sugar", "Aroma")
            await client.say(embed = embed)
        elif ldish == "pineapple fried rice":
            foodstats = ["42", "46", "51", "56", "62", "125", "175", "225", "275", "375", "6", "6", "6", "5", "5", "70", "14"]
            embed = output2(foodstats, "Pineapple Fried Rice", 0xf1c40f, "Light Kingdom", "Rice (8-2)", "Pineapple (14-3)", "", "", "", "514", "354", "2300", "832", "Salad Dressing", "Rock Sugar", "Flavor")
            await client.say(embed = embed)
        elif ldish == "chicken soup":
            foodstats = ["96", "106", "117", "129", "142", "225", "315", "405", "495", "675", "14", "13", "13", "12", "11", "150", "32"]
            embed = output2(foodstats, "Chicken Soup", 0xc27c0e, "Light Kingdom", "Shiitake (6-8)", "Whole Chicken (16-6)", "", "", "", "354", "607", "2100", "939", "Ginger", "Salt", "Texture")
            await client.say(embed = embed)
        elif ldish == "mango pudding":
            foodstats = ["115", "127", "140", "154", "169", "185", "259", "333", "407", "555", "17", "16", "16", "15", "14", "180", "38"]
            embed = output2(foodstats, "Mango Pudding", 0xf1c40f, "Light Kingdom", "Egg (5-2)", "Milk (12-5)", "Mango (17-3)", "", "", "706", "938", "756", "1600", "Rock Sugar", "Sago", "Appearence")
            await client.say(embed = embed)
        elif ldish == "strawberry ice cream":
            foodstats = ["48", "53", "58", "64", "70", "205", "287", "369", "451", "615", "7", "7", "7", "6", "6", "70", "16"]
            embed = output2(foodstats, "Strawberry Ice Cream", 0xe91e63, "Light Kingdom", "Cream (11-7)", "Milk (12-5)", "Strawberry (18-1)", "", "", "808", "397", "2200", "595", "Sago", "Condensed Milk", "Flavor")
            await client.say(embed = embed)
        elif ldish == "red bean pudding":
            foodstats = ["122", "134", "147", "162", "178", "245", "343", "441", "539", "735", "18", "17", "17", "16", "15", "180", "41"]
            embed = output2(foodstats, "Red Bean Pudding", 0x992d22, "Light Kingdom", "Milk (12-5)", "Red Beans (19-5)", "", "", "", "683", "2100", "801", "416", "Rock Sugar", "Sago", "Aroma")
            await client.say(embed = embed)
        elif ldish == "kung pao chicken":
            foodstats = ["61", "67", "74", "81", "89", "185", "259", "333", "407", "555", "9", "9", "9", "8", "8", "90", "20"]
            embed = output2(foodstats, "Kung Pao Chicken", 0x992d22, "Light Kingdom", "Diced Chicken (16=5)", "Peanut (19-3)", "", "", "", "607", "984", "1800", "609", "Chili", "Cooking Wine", "Texture")
            await client.say(embed = embed)
        elif ldish == "pumpkin pie":
            foodstats = ["43", "47", "52", "57", "63", "85", "119", "153", "187", "255", "6", "6", "6", "5", "5", "60", "14"]
            embed = output2(foodstats, "Pumpkin Pie", 0xe67e22, "Light Kingdom", "Honey (14-6)", "Pumpkin (20-5)", "Rice Flour (20-7)", "", "", "680", "1900", "858", "562", "Icing", "Condensed Milk", "Aroma")
            await client.say(embed = embed)
        elif ldish == "sweet yam buns":
            foodstats = ["86", "95", "105", "116", "128", "245", "343", "441", "539", "735", "12", "11", "11", "10", "10", "120", "29"]
            embed = output2(foodstats, "Sweet Yam Buns", 0x71368a, "Light Kingdom", "Egg (5-2)", "Flour (12-2)", "Purple Yam (21-3)", "", "", "1900", "988", "682", "430", "Condensed Milk", "Sugar", "Flavor")
            await client.say(embed = embed)
        elif ldish == "steamed cod":
            foodstats = ["65", "72", "79", "87", "96", "205", "287", "369", "451", "615", "9", "9", "9", "8", "8", "90", "22"]
            embed = output2(foodstats, "Steamed Cod", 0xe67e22, "Light Kingdom", "Tofu (10-6)", "Cod (22-2)", "", "", "", "409", "2400", "227", "964", "Black Pepper", "Ginger", "Aroma")
            await client.say(embed = embed)
        elif ldish == "steamed unagi":
            foodstats = ["114", "125", "138", "152", "167", "245", "343", "441", "539", "735", "16", "15", "15", "14", "13", "105", "38"]
            embed = output2(foodstats, "Steamed Unagi", 0x979c9f, "Light Kingdom", "Shiitake (6-8)", "Eel (22-5)", "", "", "", "493", "285", "822", "2400", "Ginger", "Cooking Wine", "Appearence")
            await client.say(embed = embed)
        elif ldish == "garlic lobster":
            foodstats = ["137", "151", "166", "183", "201", "105", "147", "189", "231", "315", "19", "18", "18", "17", "16", "180", "46"]
            embed = output2(foodstats, "Garlic Lobster", 0xe74c3c, "Light Kingdom", "Rock Lobsters (23-5)", "", "", "", "", "835", "388", "2300", "477", "Salad Dressing", "Garlic", "Texture")
            await client.say(embed = embed)
        elif ldish == "crab hotpot":
            foodstats = ["53", "58", "64", "70", "77", "245", "343", "441", "539", "735", "8", "8", "8", "7", "7", "70", "18"]
            embed = output2(foodstats, "Crab Hotpot", 0xe74c3c, "Light Kingdom", "Shiitake (6-8)", "Tofu (10-6)", "King Crab (24-2)", "", "", "410", "422", "868", "2300", "Cooking Wine", "Ginger", "Flavor")
            await client.say(embed = embed)
        elif ldish == "french fries":
            foodstats = ["24", "26", "29", "32", "35", "35", "49", "63", "77", "105", "3", "3", "3", "2", "2", "60", "8"]
            embed = output2(foodstats, "French Fries", 0xf1c40f, "Gloriville", "Potato (1-3)", "", "", "", "", "972", "1800", "506", "722", "Black Pepper", "Cooking Oil", "Aroma")
            await client.say(embed = embed)
        elif ldish == "crispy pork":
            foodstats = ["24", "26", "29", "32", "35", "45", "63", "81", "99", "135", "3", "3", "3", "2", "2", "60", "8"]
            embed = output2(foodstats, "Crispy Pork", 0xa84300, "Gloriville", "Pork Belly (1-6)", "", "", "", "", "725", "813", "1500", "962", "Garlic", "Cooking Wine", "Texture")
            embed.set_image(url = "http://p6.qhimg.com/dr/250__/t0146bd30bf0c6bc70a.png")
            await client.say(embed = embed)
        elif ldish == "salad":
            foodstats = ["53", "58", "64", "70", "77", "55", "77", "99", "121", "165", "8", "8", "8", "7", "7", "120", "18"]
            embed = output2(foodstats, "Salad", 0x2ecc71, "Gloriville", "Cucumber (2-2)", "Lettuce (3-1)", "Carrot (3-5)", "", "", "1500", "707", "992", "801", "Salt", "Salad Dressing", "Flavor")
            await client.say(embed = embed)
        elif ldish == "eggplant roll":
            foodstats = ["24", "26", "29", "32", "35", "105", "147", "189", "231", "315", "3", "3", "3", "2", "2", "60", "8"]
            embed = output2(foodstats, "Eggplant Roll", 0xe67e22, "Gloriville", "Potato (1-3)", "Eggplant (2-7)", "", "", "", "912", "692", "796", "1600", "Chili", "Soy Sauce", "Appearence")
            await client.say(embed = embed)
        elif ldish == "smoked salmon":
            foodstats = ["31", "34", "37", "41", "45", "35", "49", "63", "77", "105", "5", "5", "5", "4", "4", "70", "10"]
            embed = output2(foodstats, "Smoked Salmon", 0xe67e22, "Gloriville", "Salmon (4-2)", "", "", "", "", "888", "1700", "705", "707", "Soy Sauce", "Salt", "Aroma")
            await client.say(embed = embed)
        elif ldish == "roast beef":
            foodstats = ["79", "87", "96", "106", "117", "225", "315", "405", "495", "675", "12", "11", "11", "10", "10", "180", "26"]
            embed = output2(foodstats, "Roast Beef", 0x992d22, "Gloriville", "Beef Tenderloin (5-6)", "", "", "", "", "607", "984", "1800", "609", "Garlic", "Cooking Wine", "Texture")
            await client.say(embed = embed)
        elif ldish == "cheese bread":
            foodstats = ["43", "47", "52", "57", "63", "45", "63", "81", "99", "135", "7", "7", "7", "6", "6", "90", "14"]
            embed = output2(foodstats, "Cheese Bread", 0xf1c40f, "Gloriville", "Bread (4-4)", "Cheese (6-2)", "", "", "", "1700", "717", "707", "876", "Scallion", "Garlic", "Flavor")
            await client.say(embed = embed)
        elif ldish == "mushroom soup":
            foodstats = ["72", "79", "87", "96", "106", "85", "119", "153", "187", "255", "11", "10", "10", "9", "9", "150", "24"]
            embed = output2(foodstats, "Mushroom Soup", 0xffeea9, "Gloriville", "Shiitake (6-8)", "Mushroom (7-3)", "Butter (7-8)", "", "", "1900", "504", "938", "658", "Ginger", "Scallion", "Flavor")
            await client.say(embed = embed)
        elif ldish == "fried rice cake":
            foodstats = ["29", "32", "35", "39", "43", "125", "175", "225", "275", "375", "5", "5", "5", "4", "4", "60", "10"]
            embed = output2(foodstats, "Fried Rice Cake", 0xffe6b0, "Gloriville", "Egg (5-2)", "Rice (8-2)", "", "", "", "680", "1900", "858", "451", "Black Pepper", "Cooking Oil", "Aroma")
            await client.say(embed = embed)
        elif ldish == "pork burger":
            foodstats = ["62", "68", "75", "83", "91", "125", "175", "225", "275", "375", "9", "9", "9", "8", "8", "120", "21"]
            embed = output2(foodstats, "Pork Burger", 0xe67e22, "Gloriville", "Lettuce (3-1)", "Bread (4-4)", "Pork Loin (9-2)", "", "", "493", "285", "822", "2400", "Salad Dressing", "Chili", "Appearence")
            await client.say(embed = embed)
        elif ldish == "bacon tofu wrap":
            foodstats = ["94", "103", "113", "124", "136", "225", "315", "405", "495", "675", "14", "13", "13", "12", "11", "180", "31"]
            embed = output2(foodstats, "Bacon Tofu Wrap", 0xeb7c7c, "Gloriville", "Bacon (10-3)", "Tofu (10-6)", "", "", "", "617", "687", "896", "1800", "Scallion", "Soy Sauce", "Appearence")
            await client.say(embed = embed)
        elif ldish == "grilled calamari":
            foodstats = ["39", "43", "47", "52", "57", "145", "203", "261", "319", "435", "6", "6", "6", "5", "5", "70", "13"]
            embed = output2(foodstats, "Grilled Calamari", 0xc27c0e, "Gloriville", "Green Pepper (6-6)", "Onion (9-5)", "Octopus (11-4)", "", "", "771", "910", "1500", "819", "Soy Sauce", "Chili", "Texture")
            await client.say(embed = embed)
        elif ldish == "popcorn":
            foodstats = ["62", "68", "75", "83", "91", "55", "77", "99", "121", "165", "9", "9", "9", "8", "8", "90", "21"]
            embed = output2(foodstats, "Popcorn", 0xf1c40f, "Gloriville", "Butter (7-8)", "Corn (11-2)", "", "", "", "409", "2400", "227", "964", "Cooking Oil", "Sugar", "Aroma")
            await client.say(embed = embed)
        elif ldish == "shortbread":
            foodstats = ["101", "111", "122", "134", "147", "125", "175", "225", "275", "375", "15", "14", "14", "13", "12", "180", "34"]
            embed = output2(foodstats, "Shortbread", 0xffeea9, "Gloriville", "Butter (7-8)", "Flour (12-2)", "Milk (12-5)", "", "", "875", "609", "316", "2200", "Icing", "Rock Sugar", "Appearence")
            await client.say(embed = embed)
        elif ldish == "minestrone":
            foodstats = ["64", "74", "81", "89", "98", "105", "147", "189", "231", "315", "10", "10", "10", "9", "9", "120", "22"]
            embed = output2(foodstats, "Minestrone", 0x2ecc71, "Gloriville", "Cabbage (13-5)", "Spinach (13-6)", "Starch (13-9)", "", "", "1600", "938", "756", "706", "Salt", "Ginger", "Flavor")
            await client.say(embed = embed)
        elif ldish == "pineapple juice":
            foodstats = ["36", "40", "44", "48", "53", "145", "203", "261", "319", "435", "6", "6", "6", "5", "5", "60", "12"]
            embed = output2(foodstats, "Pineapple Juice", 0xf1c40f, "Gloriville", "Pineapple (14-3)", "Honey (14-6)", "", "", "", "2000", "694", "888", "418", "Rock Sugar", "Sago", "Flavor")
            await client.say(embed = embed)
        elif ldish == "apple crisp":
            foodstats = ["108", "119", "131", "144", "158", "245", "343", "441", "539", "735", "16", "15", "15", "14", "13", "180", "36"]
            embed = output2(foodstats, "Apple Crisp", 0xffeea9, "Gloriville", "Flour (12-2)", "Apple (15-1)", "", "", "", "397", "2200", "808", "595", "Condensed Milk", "Icing", "Aroma")
            await client.say(embed = embed)
        elif ldish == "chicken pizza":
            foodstats = ["42", "46", "51", "56", "65", "75", "105", "135", "165", "225", "6", "6", "6", "5", "5", "70", "14"]
            embed = output2(foodstats, "Chicken Pizza", 0xe67e22, "Gloriville", "Cheese (6-2)", "Flour (12-2)", "Diced Chicken (16-5)", "", "", "354", "507", "2100", "939", "Chili", "Black Pepper", "Texture")
            await client.say(embed = embed)
        elif ldish == "roast chicken":
            foodstats = ["58", "64", "70", "77", "85", "85", "119", "153", "187", "255", "9", "9", "9", "8", "8", "90", "19"]
            embed = output2(foodstats, "Roast Chicken", 0xe67e22, "Gloriville", "Whole Chicken (16-6)", "", "", "", "", "683", "801", "2100", "416", "Cooking Oil", "Black Pepper", "Texture")
            await client.say(embed = embed)
        elif ldish == "mango wrap":
            foodstats = ["96", "106", "117", "129", "145", "205", "287", "369", "451", "615", "14", "13", "13", "12", "11", "150", "32"]
            embed = output2(foodstats, "Mango Wrap", 0xf1c40f, "Gloriville", "Cream (11-7)", "Flour (12-2)", "Mango (17-3)", "", "", "902", "754", "744", "1600", "Sugar", "Condensed Milk", "Appearence")
            await client.say(embed = embed)
        elif ldish == "strawberry mousse":
            foodstats = ["48", "53", "58", "64", "70", "185", "259", "333", "407", "555", "7", "7", "7", "6", "6", "70", "16"]
            embed = output2(foodstats, "Strawberry Mousse", 0xff91b6, "Gloriville", "Cream (11-7)", "Strawberry (18-1)", "", "", "", "888", "2300", "422", "410", "Sugar", "Icing", "Aroma")
            await client.say(embed = embed)
        elif ldish == "fruit salad":
            foodstats = ["115", "127", "140", "154", "169", "165", "231", "297", "363", "495", "17", "16", "16", "15", "14", "180", "38"]
            embed = output2(foodstats, "Fruit Salad", 0xe67e22, "Gloriville", "Pineapple (14-3)", "Apple (15-1)", "Mango (17-3)", "", "", "1700", "750", "800", "750", "Condensed Milk", "Salad Dressing", "Flavor")
            await client.say(embed = embed)
        elif ldish == "peanut pie":
            foodstats = ["61", "67", "74", "81", "89", "165", "231", "297", "363", "495", "9", "9", "9", "8", "8", "90", "20"]
            embed = output2(foodstats, "Peanut Pie", 0xc27c0e, "Gloriville", "Egg (5-2)", "Flour (12-2)", "Peanut (19-3)", "", "", "587", "515", "898", "2000", "Icing", "Sugar", "Appearence")
            await client.say(embed = embed)
        elif ldish == "pumpkin soup":
            foodstats = ["122", "134", "147", "162", "178", "245", "343", "441", "539", "735", "18", "17", "17", "16", "15", "180", "41"]
            embed = output2(foodstats, "Pumpkin Soup", 0xe67e22, "Gloriville", "Milk (12-5)", "Pumpkin (20-5)", "", "", "", "508", "413", "2100", "979", "Rock Sugar", "Sago", "Texture")
            await client.say(embed = embed)
        elif ldish == "hotteok":
            foodstats = ["43", "47", "52", "57", "63", "185", "259", "333", "407", "555", "6", "6", "6", "5", "5", "60", "14"]
            embed = output2(foodstats, "Hotteok", 0xffffff, "Gloriville", "Milk (12-5)", "Red Beans (19-5)", "Rice Flour (20-7)", "", "", "1900", "988", "682", "430", "Sago", "Condensed Milk", "Flavor")
            await client.say(embed = embed)
        elif ldish == "cheesy yam":
            foodstats = ["86", "95", "105", "116", "128", "245", "343", "441", "539", "735", "12", "11", "11", "10", "10", "120", "29"]
            embed = output2(foodstats, "Cheesy Yam", 0x71368a, "Gloriville", "Cheese (6-2)", "Purple Yam (21-3)", "", "", "", "556", "2000", "907", "537", "Sago", "Rock Sugar", "Aroma")
            await client.say(embed = embed)
        elif ldish == "fried cod":
            foodstats = ["65", "72", "79", "87", "96", "205", "287", "369", "451", "615", "9", "9", "9", "8", "8", "90", "22"]
            embed = output2(foodstats, "Fried Cod", 0xe67e22, "Gloriville", "Egg (5-2)", "Flour (12-2)", "Cod (22-2)", "", "", "2300", "354", "514", "832", "Ginger", "Scallion", "Flavor")
            await client.say(embed = embed)
        elif ldish == "fried unagi":
            foodstats = ["114", "125", "138", "152", "167", "245", "343", "441", "539", "735", "16", "15", "15", "14", "13", "150", "38"]
            embed = output2(foodstats, "Fried Unagi", 0xe67e22, "Gloriville", "Egg (5-2)", "Flour (12-2)", "Eel (22-5)", "", "", "405", "307", "888", "2400", "Cooking Wine", "Ginger", "Appearence")
            await client.say(embed = embed)
        elif ldish == "baked lobster":
            foodstats = ["137", "151", "166", "183", "201", "75", "105", "135", "165", "225", "19", "18", "18", "17", "16", "180", "46"]
            embed = output2(foodstats, "Baked Lobster", 0xe74c3c, "Gloriville", "Cheese (6-2)", "Rock Lobsters (23-5)", "", "", "", "835", "388", "2300", "477", "Cooking Wine", "Garlic", "Texture")
            await client.say(embed = embed)
        elif ldish == "crab salad":
            foodstats = ["53", "58", "64", "70", "77", "245", "343", "441", "539", "735", "8", "8", "8", "7", "7", "70", "18"]
            embed = output2(foodstats, "Crab Salad", 0xe74c3c, "Gloriville", "Lettuce (3-1)", "King Crab (24-2)", "", "", "", "600", "2200", "600", "600", "Salad Dressing", "Salt", "Aroma")
            await client.say(embed = embed)
        elif ldish == "baked potato":
            foodstats = ["24", "26", "29", "32", "35", "35", "49", "63", "77", "105", "3", "3", "3", "2", "2", "60", "8"]
            embed = output2(foodstats, "Baked Potato", 0xf1c40f, "Sakurajima", "Potato (1-3)", "", "", "", "", "725", "813", "1500", "962", "Scallion", "Cooking Oil", "Texture")
            await client.say(embed = embed)
        elif ldish == "grilled pork belly":
            foodstats = ["24", "26", "29", "32", "35", "45", "63", "81", "99", "135", "3", "3", "3", "2", "2", "60", "8"]
            embed = output2(foodstats, "Grilled Pork Belly", 0x9c5d15, "Sakurajima", "Pork Belly (1-6)", "", "", "", "", "912", "692", "796", "1600", "Sugar", "Cooking Wine", "Appearence")
            await client.say(embed = embed)
        elif ldish == "cucumber salad":
            foodstats = ["24", "26", "29", "32", "35", "165", "231", "297", "363", "495", "3", "3", "3", "2", "2", "60", "8"]
            embed = output2(foodstats, "Cucumber Salad", 0x2ecc71, "Sakurajima", "Cucumber (2-2)", "", "", "", "", "607", "1800", "984", "609", "Sugar", "Rock Sugar", "Aroma")
            await client.say(embed = embed)
        elif ldish == "boiled lettuce":
            foodstats = ["53", "58", "64", "70", "77", "55", "77", "99", "121", "165", "8", "8", "8", "7", "7", "120", "18"]
            embed = output2(foodstats, "Boiled Lettuce", 0x2ecc71, "Sakurajima", "Lettuce (3-1)", "", "", "", "", "1500", "707", "992", "801", "Chili", "Garlic", "Flavor")
            await client.say(embed = embed)
        elif ldish == "mushroom yaki":
            foodstats = ["72", "79", "87", "96", "106", "125", "175", "225", "275", "375", "11", "10", "10", "9", "9", "150", "24"]
            embed = output2(foodstats, "Mushroom Yaki", 0xffeea9, "Sakurajima", "Mushroom (7-3)", "Butter (7-8)", "", "", "", "717", "876", "1700", "707", "Black Pepper", "Ginger", "Texture")
            await client.say(embed = embed)
        elif ldish == "salmon sashimi":
            foodstats = ["31", "34", "37", "41", "45", "35", "49", "63", "77", "105", "7", "7", "7", "6", "6", "90", "14"]
            embed = output2(foodstats, "Salmon Sashimi", 0xe67e22, "Sakurajima", "Salmon (4-2)", "", "", "", "", "771", "1500", "910", "819", "Soy Sauce", "Salt", "Aroma")
            await client.say(embed = embed)
        elif ldish == "beef tartare":
            foodstats = ["79", "87", "96", "106", "117", "225", "315", "405", "495", "675", "12", "11", "11", "10", "10", "180", "26"]
            embed = output2(foodstats, "Beef Tartare", 0xe74c3c, "Sakurajima", "Egg (5-2)", "Beef Tenderloin (5-6)", "", "", "", "587", "515", "898", "2000", "Garlic", "Ginger", "Appearence")
            await client.say(embed = embed)
        elif ldish == "tamagoyaki":
            foodstats = ["43", "47", "52", "57", "63", "105", "147", "189", "231", "315", "7", "7", "7", "6", "6", "90", "14"]
            embed = output2(foodstats, "Tamagoyaki", 0xf1c40f, "Sakurajima", "Carrot (3-5)", "Egg (5-2)", "Shiitake (6-8)", "", "", "2000", "694", "888", "418", "Icing", "Scallion", "Flavor")
            await client.say(embed = embed)
        elif ldish == "omurice":
            foodstats = ["29", "32", "35", "39", "43", "75", "105", "135", "165", "225", "5", "5", "5", "4", "4", "60", "10"]
            embed = output2(foodstats, "Omurice", 0xf1c40f, "Sakurajima", "Egg (5-2)", "Rice (8-2)", "", "", "", "354", "2100", "607", "939", "Salad Dressing", "Salt", "Aroma")
            await client.say(embed = embed)
        elif ldish == "shogayaki":
            foodstats = ["62", "68", "75", "83", "91", "45", "63", "81", "99", "135", "14", "13", "13", "12", "11", "120", "21"]
            embed = output2(foodstats, "Shogayki", 0xc27c0e, "Sakurajima", "Pork Loin (9-2)", "Onion (9-5)", "", "", "", "835", "388", "2300", "477", "Scallion", "Chili", "Texture")
            await client.say(embed = embed)
        elif ldish == "bacon bites":
            foodstats = ["94", "103", "113", "124", "136", "45", "63", "81", "99", "135", "14", "13", "13", "12", "11", "180", "31"]
            embed = output2(foodstats, "Bacon Bites", 0xeb7c7c, "Sakurajima", "Bread (4-4)", "Cheese (6-2)", "Bacon (10-3)", "", "", "617", "687", "896", "1800", "Salad Dressing", "Black Pepper", "Appearence")
            await client.say(embed = embed)
        elif ldish == "cold tofu":
            foodstats = ["62", "68", "75", "83", "91", "145", "203", "261", "319", "435", "9", "9", "9", "8", "8", "90", "21"]
            embed = output2(foodstats, "Cold Tofu", 0xffffff, "Sakurajima", "Tofu (10-6)", "", "", "", "", "2300", "354", "514", "832", "Garlic", "Scallion", "Flavor")
            await client.say(embed = embed)
        elif ldish == "grilled corn":
            foodstats = ["39", "43", "47", "52", "57", "125", "175", "225", "275", "375", "6", "6", "6", "5", "5", "70", "13"]
            embed = output2(foodstats, "Grilled Corn", 0xf1c40f, "Sakurajima", "Corn (11-2)", "Cream (11-7)", "", "", "", "902", "1600", "754", "744", "Condensed Milk", "Salad Dressing", "Aroma")
            await client.say(embed = embed)
        elif ldish == "vegetable tempura":
            foodstats = ["101", "111", "122", "134", "147", "125", "175", "225", "275", "375", "15", "14", "14", "13", "12", "180", "34"]
            embed = output2(foodstats, "Vegetable Tempura", 0xffeea9, "Sakurajima", "Eggplant (2-7)", "Shiitake (6-8)", "Flour (12-2)", "", "", "1600", "938", "756", "706", "Salt", "Cooking Oil", "Flavor")
            await client.say(embed = embed)
        elif ldish == "takoyaki":
            foodstats = ["67", "74", "81", "89", "98", "245", "343", "441", "539", "735", "10", "10", "10", "9", "9", "120", "22"]
            embed = output2(foodstats, "Takoyaki", 0x9c5d15, "Sakurajima", "Octopus (11-4)", "Flour (12-2)", "Cabbage (13-5)", "", "", "888", "705", "1700", "707", "Soy Sauce", "Salad Dressing", "Texture")
            await client.say(embed = embed)
        elif ldish == "creamed spinach":
            foodstats = ["36", "40", "44", "48", "53", "145", "203", "261", "319", "435", "6", "6", "6", "5", "5", "60", "12"]
            embed = output2(foodstats, "Creamed Spinach", 0x1f8b4c, "Sakurajima", "Cream (11-7)", "Spinach (13-6)", "", "", "", "875", "2200", "609", "316", "Black Pepper", "Sugar", "Aroma")
            await client.say(embed = embed)
        elif ldish == "baked pineapple":
            foodstats = ["108", "119", "131", "144", "158", "55", "77", "99", "121", "165", "16", "15", "15", "14", "13", "180", "36"]
            embed = output2(foodstats, "Baked Pineapple", 0xf1c40f, "Sakurajima", "Pineapple (14-3)", "Honey (14-6)", "", "", "", "405", "888", "2400", "307", "Cooking Oil", "Rock Sugar", "Texture")
            await client.say(embed = embed)
        elif ldish == "apples & cream":
            foodstats = ["42", "46", "51", "56", "62", "75", "105", "135", "165", "225", "6", "6", "6", "5", "5", "70", "14"]
            embed = output2(foodstats, "Apples & Cream", 0xe74c3c, "Sakurajima", "Cream (11-7)", "Apple (15-1)", "", "", "", "508", "413", "979", "2100", "Rock Sugar", "Icing", "Appearence")
            await client.say(embed = embed)
        elif ldish == "chicken skewer":
            foodstats = ["58", "64", "70", "77", "85", "85", "119", "153", "187", "255", "9", "9", "9", "8", "8", "90", "19"]
            embed = output2(foodstats, "Chicken Skewer", 0x9c5d15, "Sakurajima", "Green Pepper (6-6)", "Diced Chicken (16-5)", "", "", "", "680", "1900", "858", "562", "Cooking Wine", "Chili", "Aroma")
            await client.say(embed = embed)
        elif ldish == "fried chicken":
            foodstats = ["96", "106", "117", "129", "142", "225", "315", "405", "495", "675", "14", "13", "13", "12", "11", "150", "32"]
            embed = output2(foodstats, "Fried Chicken", 0xffeea9, "Sakurajima", "Egg (5-2)", "Flour (12-2)", "Whole Chicken (16-6)", "", "", "808", "2200", "397", "595", "Chili", "Garlic", "Aroma")
            await client.say(embed = embed)
        elif ldish == "mango smoothie":
            foodstats = ["115", "127", "140", "154", "169", "185", "259", "333", "407", "555", "17", "16", "16", "15", "14", "180", "38"]
            embed = output2(foodstats, "Mango Smoothie", 0xe67e22, "Sakurajima", "Cream (11-7)", "Mango (17-3)", "", "", "", "1700", "750", "800", "750", "Condensed Milk", "Sago", "Flavor")
            await client.say(embed = embed)
        elif ldish == "strawberry smoothie":
            foodstats = ["48", "53", "58", "64", "70", "185", "259", "333", "407", "555", "7", "7", "7", "6", "6", "70", "16"]
            embed = output2(foodstats, "Strawberry Smoothie", 0xff91b6, "Sakurajima", "Cream (11-7)", "Milk (12-5)", "Strawberry (18-1)", "", "", "683", "801", "416", "2100", "Rock Sugar", "Sago", "Appearence")
            await client.say(embed = embed)
        elif ldish == "peanut crisp":
            foodstats = ["61", "67", "74", "81", "89", "165", "231", "297", "363", "495", "9", "9", "9", "8", "8", "90", "20"]
            embed = output2(foodstats, "Peanut Crisp", 0xffeea9, "Sakurajima", "Flour (12-2)", "Milk (12-5)", "Peanut (19-3)", "", "", "556", "537", "907", "2000", "Salt", "Sugar", "Appearence")
            await client.say(embed = embed)
        elif ldish == "cod fillet":
            foodstats = ["65", "72", "79", "87", "96", "205", "287", "369", "451", "615", "9", "9", "9", "8", "8", "90", "22"]
            embed = output2(foodstats, "Cod Fillet", 0xffeea9, "Sakurajima", "Butter (7-8)", "Starch (13-9)", "Cod (22-2)", "", "", "600", "600", "2200", "600", "Cooking Wine", "Black Pepper", "Texture")
            await client.say(embed = embed)
        elif ldish == "piglet daifuku":
            foodstats = ["122", "134", "147", "162", "178", "245", "343", "441", "537", "735", "18", "17", "17", "16", "15", "180", "41"]
            embed = output2(foodstats, "Piglet Daifuku", 0xffeea9, "Sakurajima", "Egg (5-2)", "Flour (12-2)", "Red Beans (19-5)", "", "", "504", "658", "938", "1900", "Icing", "Condensed Milk", "Appearence")
            await client.say(embed = embed)
        elif ldish == "pumpkin muffin":
            foodstats = ["43", "47", "52", "57", "63", "205", "287", "369", "451", "615", "6", "6", "6", "5", "5", "60", "14"]
            embed = output2(foodstats, "Pumpkin Muffin", 0xe67e22, "Sakurajima", "Honey (14-6)", "(Red Beans (19-5)", "Pumpkin (20-5)", "", "", "972", "506", "1800", "722", "Sago", "Condensed Milk", "Texture")
            await client.say(embed = embed)
        elif ldish == "yam dumplings":
            foodstats = ["86", "95", "105", "116", "128", "245", "343", "441", "539", "735", "12", "11", "11", "10", "10", "120", "29"]
            embed = output2(foodstats, "Yam Dumplings", 0x9b59b6, "Sakurajima", "Rice Flour (20-7)", "Purple Yam (21-3)", "", "", "", "1900", "988", "682", "430", "Sago", "Icing", "Flavor")
            await client.say(embed = embed)
        elif ldish == "unagi don":
            foodstats = ["114", "125", "138", "152", "167", "245", "343", "441", "539", "735", "16", "15", "15", "14", "13", "150", "38"]
            embed = output2(foodstats, "Unagi Don", 0x992d22, "Sakurajima", "Rice (8-2)", "Eel (22-5)", "", "", "", "2300", "422", "868", "410", "Cooking Oil", "Cooking Wine", "Flavor")
            await client.say(embed = embed)
        elif ldish == "lobster sashimi":
            foodstats = ["137", "151", "166", "183", "201", "105", "147", "189", "231", "315", "19", "18", "18", "17", "16", "180", "46"]
            embed = output2(foodstats, "Lobster Sashimi", 0x607d8b, "Sakurajima", "Rock Lobsters (23-5)", "", "", "", "", "493", "285", "822", "2400", "Ginger", "Soy Sauce", "Appearence")
            await client.say(embed = embed)
        elif ldish == "crab sashimi":
            foodstats = ["53", "58", "64", "70", "77", "245", "343", "441", "539", "735", "8", "8", "8", "7", "7", "70", "18"]
            embed = output2(foodstats, "Crab Sashimi", 0xe74c3c, "Sakurajima", "King Crab (24-2)", "", "", "", "", "409", "2400", "227", "964", "Ginger", "Soy Sauce", "Aroma")
            await client.say(embed = embed)

@client.event
async def on_command_error(error, context):
    if isinstance(error, commands.CommandOnCooldown):
        await client.send_message(context.message.channel, "Please do not spam. There is only so much I can handle")

@client.event
async def on_ready():
    await client.change_presence(game=Game(name = "with Master Attendant"))
    print(client.user.name + " is online.")

client.run(TOKEN)
