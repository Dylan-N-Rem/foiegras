from discord.ext.commands import Bot
from discord import Game
from discord.ext import commands
import random
import time
import traceback
import sys
import os

TOKEN = os.getenv("TOKEN")
summon_pool = ["Crab Long Bao", "Foie Gras", "Peking Duck", "B-52", "Bamboo Rice", "Gingerbread", "Boston Lobster", "Double Scoop", "Tiraumisu", "Escargot", "Hotdog", "Mango Pudding", "Hamburger", "Steak", "Tangyuan", "Sanma", "Napoleon Cake", "Salad", "Pastel de nata", "Yuxiang", "Sukiyaki", "Brownie", "Red Wine", "Gyoza", "Chocolate", "Eggette", "Pineapple Cake", "Skewer", "Jello", "Pancake", "Popcorn", "Long Bao", "Coffee", "Sashimi", "Macaron", "Zongzi", "Sakuramochi", "Tom Yum", "Taiyaki", "Milk", "Dorayaki", "Sake", "Tempura", "Spicy Gluten", "Jiuniang", "Omurice", "Orange Juice", "Ume Ochazuke", "Miso Soup", "Yellow Wine"]
ur_pool = ["Crab Long Bao", "Foie Gras", "Peking Duck", "B-52", "Bamboo Rice", "Gingerbread", "Boston Lobster", "Double Scoop"]
sr_pool = ["Tiraumisu", "Escargot", "Hotdog", "Mango Pudding", "Hamburger", "Steak", "Tangyuan", "Sanma", "Napoleon Cake", "Salad", "Pastel de nata", "Yuxiang", "Sukiyaki", "Brownie", "Red Wine", "Gyoza", "Chocolate", "Eggette", "Pineapple Cake"]
r_pool = ["Long Bao", "Coffee", "Sashimi", "Macaron", "Zongzi", "Sakuramochi", "Tom Yum", "Taiyaki", "Milk", "Dorayaki", "Sake", "Tempura", "Spicy Gluten", "Jiuniang", "Omurice", "Orange Juice", "Ume Ochazuke", "Miso Soup", "Yellow Wine"]
m_pool = ["Skewer", "Jello", "Pancake", "Popcorn"]
rarity_pool = ["M", "R", "SR", "UR"]
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
prefix = ("f!")
client = Bot(command_prefix = prefix)

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
                description = "Summons a desired amount of food souls.",
                brief = "Summon food souls for FREE!",
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
                description = 'Summons endlessly until a specific food soul of a specified amount has been summoned. Use "-" instead of spaces (eg. f!summonsoul Bamboo-Rice 5)',
                brief = 'Summons continuously until a specified food soul has been summoned.',
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
            if lfood_soul == lfoodsoul:
                count_foodsoul += 1
            elif foodsoul in sr_pool:
                sr += 1
                number += 1
            elif foodsoul in r_pool:
                r += 1
                number += 1
            elif foodsoul in m_pool:
                m += 1
                number += 1
    bigline = output(summoned, valid, ur, sr, r, m, number, context)
    await client.say(bigline)

@client.command(name = 'rarity',
               description = 'Summons continuously until a specified amount of foods souls with a specified rarity has been summoned.',
               brief = 'Summons until a food soul of specified rarity has been summoned',
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

@client.command(name = 'dialogue',
                description = "Says a random quote from Foie Gras.",
                brief = "Words of wisdom from Foie Gras.",
                pass_context = True)
@commands.cooldown(1, 7, commands.BucketType.user)
async def say(context):
    possible_responses = [
        'For me, for you, destiny is inescapable.',
        'What exactly is different about you? Why does Heaven alwats show a special concern for you',
        "If... there really is a way to change fate... No... it's impossible...",
        "I feel a warmth in my heart. I've never felt this before",
    ]
    await client.say(random.choice(possible_responses))

@client.command(name = "info",
                description = "Gives a paragraph of information about Foie Gras",
                brief = "All about Foie Gras")
@commands.cooldown(1, 60, commands.BucketType.user)
async def infocard(context):
    await client.say("\
Nice to meet you. I am Foie Gras, a delicacy and rare dish in France, born in the 18th century.\
 You may not find me in your local restaurant, but do have a try if you enjoy exotic tastes.\
 Being here for more than 300 years, I grew a very indifferent personality, although, I would say I have a few exceptions.\
 I enjoy the company of Escargot, although his attention span is very low and loves sleeping, he's been with me since 1892.\
 Although all fallen angels are evil, I must say I really like the Sakura Spirit and Inugami. They avoid conflict and only attack when necessary.\
 I treat myself to an occasional Mango Wrap once in a while. As a food soul, we don't really have to eat to stay alive. But it's a treat once in a while that I can't resist.\
 I hope to see you fellow Master Attendants in the future.")

@client.command(name = "credits",
                description = "Reveals three amazing people behind the bot.",
                brief = "Show the creators and contributors of the bot.",
                pass_context = True)
@commands.cooldown(1, 30, commands.BucketType.user)
async def credits(context):
    await client.say("\
**All nicknames are from the Food Fantasy Discord Server.**\n\
Developer: Dylanime#2353 AKA ディラン\n\
Subdeveloper: cyn#1598 AKA Just Marisa\n\
IBeta Tester: Madara#0483")

@client.event
async def on_command_error(error, context):
    if isinstance(error, commands.CommandOnCooldown):
        await client.send_message(context.message.channel, "Please do not spam. There is only so much I can handle")

@client.event
async def on_ready():
    await client.change_presence(game=Game(name = "with Master Attendant"))
    print(client.user.name + " is online.")

client.run(TOKEN)
