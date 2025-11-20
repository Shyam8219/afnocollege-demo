#This is Amazon fullfillment warehouse  stow department
pod = input('enter the item in ther pod:')
if pod =='half':
    print('enter the 1 to 100 item pod space available now or continoue stow')
elif pod =='full or little space':
     print('thats ok no problem')
else:
     print('not possible fillup unable release pod')
     

#This an Amazon fullfillment warehouse shipdock work time think idea.
catogery = ('A','B','c','D')
print(f'the catogery is{catogery}')
name = input('enter the item name:')

if name== 'vpcd':
     print('vpcd name item is in catogery press buttom  A')
elif name == 'vtdx':
      print('vtdx name item is in catogery press buttom c')
elif name == 'cpdt':
      print('cpdt name item is in catogery press press buttom B')
else:
      print ('all other item name is in catogery press buttom D')
