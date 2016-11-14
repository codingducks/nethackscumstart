print('python changeing window id')

with open('windownumber.txt','r') as windownumber:
    windowid = windownumber.read()
    windowid = windowid.lstrip()
    windowid = windowid.rstrip()


#read data
with open("template_for_loop.txt", 'r') as template_for_loop:
    scripttext = template_for_loop.read()

#modify data
scripttext = scripttext.replace("WINDOWID",windowid) #reassign variable


#overwrite file with new data
with open("the_loop.txt", "w") as the_loop:
    the_loop.write(scripttext)


print('python done changeing window id')
