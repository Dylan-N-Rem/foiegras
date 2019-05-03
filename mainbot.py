from discord.ext.commands import Bot
from discord import Game
from discord.ext import commands
import discord
import random
import time
import traceback
import sys
import os

TOKEN = os.environ.get("TOKEN")
prefix = ("f!", "F!")
client = Bot(command_prefix = prefix)

# Normal summoning:

from pools import *
from rolls import *

roll = roll10

lsummon_pool = [items.lower() for items in summon_pool]
lnone_pool = [itemx.lower() for itemx in none_pool]
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
            await client.say("Error - Invalid 1st input: Food Soul does not exist or improper spelling")
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

from erolls import *

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
                await client.say("Error - Invalid 3rd input: Food Soul does not exist or improper spelling")
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

from outputs import output3

from dishes import *
from dishstats import *

all_dishes = lost_dishes + glori_dishes + light_dishes + sakura_dishes
tempdishes = [dishes.lower() for dishes in all_dishes]
alldishes = [ldish.replace(" and ", " & ") for ldish in tempdishes]

@client.command(name = "food")
@commands.cooldown(1, 3, commands.BucketType.user)
async def foodinfo(dish):
    dish = dish.lower()
    dish = dish.replace(".", " ")
    dish = dish.replace(" & ", " and ")
    dish = dish.replace(" and ", " & ")
    dishindex = -1
    for dishcount in range(len(alldishes)):
        if dish == alldishes[dishcount]:
            dishindex = dishcount
    if dishindex == -1:
        await client.say("Error - Invalid input: Dish does not exist or improper spelling")
    else:
        if all_dishes[dishindex] in lost_dishes:
            embed = output3(foodstats[dishindex], all_dishes[dishindex], embedcolour[dishindex], "Lost", recipe[dishindex], dishunlock[dishindex], maxstats[dishindex], seasoning[dishindex])
        elif all_dishes[dishindex] in glori_dishes:
            embed = output3(foodstats[dishindex], all_dishes[dishindex], embedcolour[dishindex], "Gloriville", recipe[dishindex], [], maxstats[dishindex], seasoning[dishindex])
        elif all_dishes[dishindex] in light_dishes:
            embed = output3(foodstats[dishindex], all_dishes[dishindex], embedcolour[dishindex], "Light Kingdom", recipe[dishindex], [], maxstats[dishindex], seasoning[dishindex])
        elif all_dishes[dishindex] in sakura_dishes:
            embed = output3(foodstats[dishindex], all_dishes[dishindex], embedcolour[dishindex], "Sakurajima", recipe[dishindex], [], maxstats[dishindex], seasoning[dishindex])
        await client.say(embed = embed)

# Food soul's info commands:

##
##@client.command(name = "info")
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
                ["f!info <food_soul>", 'Shows the information about a food soul. Use "." instead of space.\nNOTE: This feature is UNRELEASED.'],
                ["f!update", "Checks the latest version of the bot and most recent updates"],
                ["f!credits", "Reveals the people behind the bot."]]
    embed = discord.Embed(title = "Foie Gras", description = 'Hello. My name is Foie Gras. How may I help you today? I will await your command. My prefix is "f!" or "F!"', color = 0x3498db)
    for helpcount in range(len(helplist)):
        embed.add_field(name = helplist[helpcount][0], value = helplist[helpcount][1], inline = False)
    await client.say(embed = embed)

@client.command(name = "update")
@commands.cooldown(1, 30, commands.BucketType.user)
async def update():
    updatelist = [["Event summoning: Crimson Gem added", "In this event, you can only summon Magic Food Souls, including Sichuan Hotpot, Beer, Sandwich and Pudding for a limited time!"]]
    embed = discord.Embed(title = "Bot Update (v2.27)", description = "If there are any problems with the bot, please ping @ディラン (Dylan) and state the problem.", color = 0x3498db)
    for updatecount in range(len(updatelist)):
        embed.add_field(name = updatelist[updatecount][0], value = updatelist[updatecount][1], inline = False)
    await client.say(embed = embed)

@client.command(name = "credits")
@commands.cooldown(1, 30, commands.BucketType.user)
async def credit():
    await client.say("\
**All nicknames are from the Food Fantasy Discord Server.**\n\
Developer: Monokhorome#3439 AKA ディラン (Dylan)\n\
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
