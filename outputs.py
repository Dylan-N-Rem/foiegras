import discord

from pools import *

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

def output3(foodstats, dishname, colour, cuisine, recipe, dishunlock, maxstats, seasoning):
    if seasoning[0] == "Ginger":
        season3 = "Tender Ginger"
    if seasoning[1] == "Ginger":
        season4 = "Tender Ginger"

    if seasoning[0] == "Scallion":
        season3 = "Diced Scallions"
    if seasoning[1] == "Scallion":
        season4 = "Diced Scallions"

    if seasoning[0] == "Garlic":
        season3 = "Fresh Garlic"
    if seasoning[1] == "Garlic":
        season4 = "Fresh Garlic"

    if seasoning[0] == "Chili":
        season3 = "Royal Dressing"
    if seasoning[1] == "Chili":
        season4 = "Royal Dressing"

    if seasoning[0] == "Soy Sauce":
        season3 = "Premium Soy Sauce"
    if seasoning[1] == "Soy Sauce":
        season4 = "Premium Soy Sauce"

    if seasoning[0] == "Black Pepper":
        season3 = "Tellicherry Pepper"
    if seasoning[1] == "Black Pepper":
        season4 = "Tellicherry Pepper"

    if seasoning[0] == "Sugar":
        season3 = "Granulated Sugar"
    if seasoning[1] == "Sugar":
        season4 = "Granulated Sugar"

    if seasoning[0] == "Cooking Oil":
        season3 = "Sealed Oil"
    if seasoning[1] == "Cooking Oil":
        season4 = "Sealed Oil"

    if seasoning[0] == "Rock Sugar":
        season3 = "Pearl Sugar"
    if seasoning[1] == "Rock Sugar":
        season4 = "Pearl Sugar"

    if seasoning[0] == "Salt":
        season3 = "Sea Salt"
    if seasoning[1] == "Salt":
        season4 = "Sea Salt"

    if seasoning[0] == "Salad Dressing":
        season3 = "Thousand Island"
    if seasoning[1] == "Salad Dressing":
        season4 = "Thousand Island"

    if seasoning[0] == "Sago":
        season3 = "Crystal Sago"
    if seasoning[1] == "Sago":
        season4 = "Crystal Sago"

    if seasoning[0] == "Condensed Milk":
        season3 = "Premium Condensed Milk"
    if seasoning[1] == "Condensed Milk":
        season4 = "Premium Condensed Milk"

    if seasoning[0] == "Cooking Wine":
        season3 = "Sparkling Wine"
    if seasoning[1] == "Cooking Wine":
        season4 = "Sparkling Wine"

    if seasoning[0] == "Icing":
        season3 = "Mist Icing"
    if seasoning[1] == "Icing":
        season4 = "Mist Icing"

    foodoutput = discord.Embed(title = dishname, color = colour)
    foodoutput.add_field(name = "Cuisine", value = cuisine, inline = False)
    if recipe[0] != "" and recipe[1] == "" and recipe[2] == "":
        foodoutput.add_field(name = "Ingredients/Recipe", value = recipe[0], inline = False)
    if recipe[0] != "" and recipe[1] != "" and recipe[2] == "":
        foodoutput.add_field(name = "Ingredients/Recipe", value = recipe[0] + " and " + recipe[1], inline = False)
    if recipe[0] != "" and recipe[1] != "" and recipe[2] != "":
        foodoutput.add_field(name = "Ingredients/Recipe", value = recipe[0] + ", " + recipe[1] + " and " + recipe[2], inline = False)
    if dishunlock != []:
        foodoutput.add_field(name = "Level Requirement", value = dishunlock[0], inline = False)
        foodoutput.add_field(name = "Quest", value = dishunlock[1], inline = False)
    foodoutput.add_field(name = "Max Food Stats", value = "Flavour: " + maxstats[0] + "\nTexture: " + maxstats[1] + "\nAroma: " + maxstats[2] + "\nAppearence: " + maxstats[3], inline = False)
    foodoutput.add_field(name = "Seasoning", value = "These seasonings add **" + seasoning[2] + "** to the dish\n" + seasoning[0] + " ^\n" + seasoning[1] + " ^^\n" + season3 + " ^^^\n" + season4 + " ^^^^", inline = False)
    foodoutput.add_field(name = "Selling Price", value = "D: " + foodstats[0] + " Gold" + "\nC: " + foodstats[1] + " Gold" +"\nB: " + foodstats [2] + " Gold" + "\nA: " + foodstats[3] + " Gold" + "\nS: " + foodstats[4] + " Gold", inline = False)
    foodoutput.add_field(name = "Maximum Production Quantity ", value = "D: " + foodstats[5] + " dishes" + "\nC: " + foodstats[6] + " dishes" +"\nB: " + foodstats [7] + " dishes" + "\nA: " + foodstats[8] + " dishes" + "\nS: " + foodstats[9] + " dishes", inline = False)
    foodoutput.add_field(name = "Time Per Dish", value = "D: " + foodstats[10] + " seconds" + "\nC: " + foodstats[11] + " seconds" +"\nB: " + foodstats [12] + " seconds" + "\nA: " + foodstats[13] + " seconds" + "\nS: " + foodstats[14] + " seconds", inline = False)
    foodoutput.add_field(name = "Meal Time", value = foodstats[15] + " seconds", inline = False)
    foodoutput.add_field(name = "Cost Per Dish", value = foodstats[16] + " Gold", inline = False)
    return foodoutput
