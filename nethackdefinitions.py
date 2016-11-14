reroll = []
buffer2 = []
buffer3 = []
def specifycharge(game_list,thing,number):
    for item in game_list:
        if thing in item:
            charge = (item[-3:-1])
            if int(charge) >= number:
                reroll.append('false')
                return reroll
            else:
                reroll.append('true')
                return reroll

def specifyenchantment(game_list,thing,number):
    for item in game_list:
        if thing in item:
            if '+' in item:
                operate = item.index('+')
                enchantment =  int(item[operate+1:operate+2])
                if enchantment >= number:
                    reroll.append('false')
                    return reroll
                else:
                    reroll.append('true')
                    return reroll

def specificitems(ugly_hack,item_list):
    for i in item_list:
        for j in ugly_hack:
            if i in j:
                buffer2.append('true')
            elif i not in j:
                buffer2.append('false')
    if 'false' in buffer2:
        reroll.append('true')
        buffer2.clear()
        return reroll
    else:
        reroll.append('false')
        return reroll


def oneortwo(one_or_two,ugly_hack):
    for item in one_or_two:
        for  j in ugly_hack:
            if item in j:
                buffer3.append('true')
    if 'true' in buffer3:
        reroll.append('false')
        return reroll
    else:
        reroll.append('true')
        return reroll
