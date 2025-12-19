
from random import randint

secret = randint(100, 9999)

topildi = False
urinish = 0
while not topildi :
        if urinish == 7:
            print(f'urinishlar soni tugadi men oylagan son {secret} edi ')
            topildi = True
        else :

            num = int(input('son :')) 
            urinish += 1

            if secret == num :
                print('topdingiz ')

                topildi = True
            elif num < secret :
                 print('men kattaroq son oylaganman ')
            else :
                 print('kichikroq son oylaganman')
