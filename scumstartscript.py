
from nethackdefinitions import *
reroll = False
print("This is python checking invintory")

invin = open('nethackinvi.txt', 'r')
text = invin.read()
start = text.index('Weapons')
end = text.index('(end)')
all_items = text[start:end]

buffer = []
game_items = []
game_items2 = []

bad_scraping = ['\n', 'Weapons', 'Armor', 'Scrolls', 'Potions', 'Rings', 'Wands','Spellbooks','Tools',
                ' b ',' c ',' d ',' e ',' f ',' g ',' h ',' i ',' j ',' k ',' l ', ' m ',' n ', ' o ', ' p ', ' q ']

for item in all_items:
    if item != "-":        
        buffer.append(item)
    elif item == "-":
        items = "".join(buffer)
        game_items.append(items)
        buffer.clear()

for i in game_items:
    for j in bad_scraping:
        i = i.replace (j,"")
    i = i.replace (' an ','1 ')
    i = i.replace (' a ','1 ')
    i = i.lstrip()
    i = i.rstrip()
    game_items2.append(i)
    junk = game_items2[0]
game_items2.remove(junk)


ugly_hack = []             #PLEASE HELP   (used in  def specificitems() )
for items in game_items2:
    if len(ugly_hack) == 0:
        ugly_hack.append(items)
    elif len(ugly_hack) > 0:
        ugly_hack[0] = ugly_hack[0] + items
    
###  EXAMPLES (for specific charges)
  ###FORMAT: game_list2, ITEMNAME, NUMBER

#reroll = specifycharge(game_items2,'wand of create monster',11)
reroll = specifycharge(game_items2,'magic marker',60)

### EXAMPLES   (for specific enchantments)    

#reroll = specifyenchantment(game_items2,'ring of protection',1)
#reroll = specifyenchantment(game_items2,'increase damage',2)



### EXAPLES individual items, or dont care about charges/enchanments  
    #(dont add so many that you will never get them all (read: technically not a infinite loop (read: the sun will one day stop))

# ADD ITEMS TO itemlist
itemlist = ['slow di']
reroll = specificitems(ugly_hack,itemlist)


# stop script if only one of these items is found  #dosnt superceede privious stops
one_or_two = [
    'spellbook of identify', 'spellbook of detect monsters',
    'spellbook of light','spellbook of detect food',
    ]
reroll = oneortwo(one_or_two,ugly_hack)



if 'true' in reroll:
    rerolling = 'True'
else:
    rerolling = 'False'


with open("true_or.txt", "w") as true_or:
    true_or.write(rerolling)



