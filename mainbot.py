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

from pools import ur_pool
ur_pool = ur_pool()
from pools import sr_pool
sr_pool = sr_pool()
from pools import r_pool
r_pool = r_pool()
from pools import m_pool
m_pool = m_pool()
from pools import summon_pool
summon_pool = summon_pool()
from pools import none_pool
none_pool = none_pool()
from pools import event_pool
event_pool = event_pool()
from pools import unre_pool
unre_pool = unre_pool()

from rolls import roll0
roll0 = roll0()
from rolls import roll1
roll1 = roll1()
from rolls import roll2
roll2 = roll2()
from rolls import roll3
roll3 = roll3()
from rolls import roll4
roll4 = roll4()
from rolls import roll5
roll5 = roll5()
from rolls import roll6
roll6 = roll6()
from rolls import roll7
roll7 = roll7()
from rolls import roll8
roll8 = roll8()
from rolls import roll9
roll9 = roll9()

roll = roll9

lsummon_pool = [items.lower() for items in summon_pool]
lnone_pool = [itemn.lower() for itemn in none_pool]
levent_pool = [itemv.lower() for itemv in event_pool]
lunre_pool = [itemu.lower() for itemu in unre_pool]

from outputs import output

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

from outputs import output2

from erolls import autounav
from erolls import eventfs
from erolls import removefs
from erolls import autoroll

from erolls import index0entry
from erolls import index1entry
from erolls import index2entry
from erolls import index3entry
from erolls import index4aentry
from erolls import index4bentry
from erolls import index5aentry
from erolls import index6entry
from erolls import index7entry
from erolls import index8entry
from erolls import index9entry
from erolls import index10entry
from erolls import index11aentry
from erolls import index11bentry
from erolls import index12entry
from erolls import index13entry
from erolls import index14entry
from erolls import index15entry
from erolls import index16entry
from erolls import index17entry
from erolls import index18entry
from erolls import index19entry
from erolls import index20entry

from erolls import eventindexcheck

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
    from erolls import eventlist
    eventlist, eventlist2 = eventlist()
    embed = discord.Embed(title = "Event Index List", description = "Use the event index number to input what event you want to summon in!", color = 0x2ecc71)
    for eventcount in range(len(eventlist)):
        embed.add_field(name = eventlist[eventcount][0] + ". " + eventlist[eventcount][1], value = eventlist[eventcount][2] + " from " + eventlist[eventcount][3] + ".\n" + eventlist[eventcount][4], inline = False)
    await client.say(embed = embed)
    embed = discord.Embed(color = 0x2ecc71)
    for eventcount2 in range(len(eventlist2)):
        embed.add_field(name = eventlist2[eventcount2][0] + ". " + eventlist2[eventcount2][1], value = eventlist2[eventcount2][2] + " from " + eventlist2[eventcount2][3] + ".\n" + eventlist2[eventcount2][4], inline = False)
    await client.say(embed = embed)

# Dish commands:

food_pool = ["Stir-Fried Potatoes", "Braised Pork", "Braised Eggplant", "Sauteed Lettuce", "Carrot Bread", "Cucumber Egg Stir-Fry", "Black Pepper Beef", "Sauteed Mushrooms", "Egg Fried Rice", "Salmon Fried Rice", "Onion Fried Rice", "Bacon Fried Rice", "Braised Octopus", "Risotto", "Butter Bread", "Emerald Roll", "Corn Pie", "Toffee Apple", "Pineapple Fried Rice", "Chicken Soup", "Mango Pudding", "Strawberry Ice Cream", "Red Bean Pudding", "Kung Pao Chicken", "Pumpkin Pie", "Sweet Yam Buns", "Steamed Cod", "Steamed Unagi", "Garlic Lobster", "Crab Hotpot", "French Fries", "Crispy Pork", "Salad", "Eggplant Roll", "Smoked Salmon", "Roast Beef", "Cheese Bread", "Mushroom Soup", "Fried Rice Cake", "Pork Burger", "Bacon Tofu Wrap", "Grilled Calamari", "Popcorn", "Shortbread", "Minestrone", "Pineapple Juice", "Apple Crisp", "Chicken Pizza", "Roast Chicken", "Mango Wrap", "Fruit Salad", "Peanut Pie", "Pumpkin Soup", "Hotteok", "Cheesy Yam", "Fried Cod", "Fried Unagi", "Baked Lobster", "Crab Salad", "Baked Potato", "Grilled Pork Belly", "Cucumber Salad", "Boiled Lettuce", "Mushroom Yaki", "Salmon Sashimi", "Beef Tartare", "Tamagoyaki", "Omurice", "Shogayki", "Bacon Bites", "Cold Tofu", "Grilled Corn", "Vegetable Tempura", "Takoyaki", "Creamed Spinach", "Baked Pineapple", "Apples & Cream", "Chicken Skewer", "Fried Chicken", "Mango Smoothie", "Strawberry Smoothie", "Peanut Crisp", "Cod Fillet", "Piglet Daifuku", "Pumpkin Muffin", "Yam Dumplings", "Unagi Don", "Lobster Sashimi", "Crab Sashimi"]
lostfood_pool = ["Calamari Skewer", "Garlic Oyster", "Grilled Prawns", "Pickled Salmon Head", "Tomato & Eggs", "Steamed Mushrooms", "Spaghetti", "Har Gow", "Gold Cake", "Mixed Greens", "Stir-Fried Mussels", "Mushroom Alfredo", "Cha Siu Bao", "Spinach Noodles", "Mint Pineapple", "Apple Sangria", "Braised Lamb", "Mushroom Chicken Stew", "Matcha Cake", "Cappuccino", "Fruit Tea", "Lemon Pie", "Meat Zongzi", "Stuffed Lotus Root", "Lotus Root Stir-Fry", "Black Fungus Congee", "Sanma Shioyaki", "Steamed Crab", "Crab Rice Cake", "Curry Crab", "Yam Pigeon Soup", "Bamboo & Meat Stir-Fry", "Braised Geese", "Roe Meat Ball", "Birds Nest", "Ginseng Stew Chicken"]
lfood_pool = [itemd.lower() for itemd in food_pool]
llostfood_pool = [iteml.lower() for iteml in lostfood_pool]

from outputs import output3

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
            foodstats = ["24", "26", "29", "32", "35", "35", "49", "63", "77", "105", "3", "3", "3", "2", "2", "60", "8"]
            embed = output3(foodstats, "Stir-Fried Potatoes", 0xf1c40f, "Potato (1-3)", "", "", "Light Kingdom", "Potato (1-3)", "", "", "", "", "801", "1500", "992", "707", "Chili", "Scallion", "Flavor")
            await client.say(embed = embed)
        elif ldish == "braised pork":
            foodstats = ["24", "26", "29", "32", "35", "45", "63", "81", "99", "1355", "3", "3", "3", "2", "2", "60", "8"]
            embed = output3(foodstats, "Braised Pork", 0xa84300, "Light Kingdom", "Pork Belly (1-6)", "", "", "", "", "771", "910", "1500", "819", "Scallion", "Soy Sauce", "Texture")
            await client.say(embed = embed)
        elif ldish == "braised eggplant":
            foodstats = ["24", "26", "29", "32", "35", "125", "175", "225", "275", "375", "3", "3", "3", "2", "2", "60", "8"]
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
    updatelist = [["Added summoning event: Savory Feast", "You can now summon Ddeokbokki and Kimchi from the new event!"],
                  ["Event index list split", "The event index list has been split into two embeds due to it being too long."]]
    embed = discord.Embed(title = "Bot Update (v2.15)", description = "If there are any problems with the bot, please ping @「Pengu Pout」ディラン (Dylan) and state the problem.", color = 0x3498db)
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
