import discord

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
