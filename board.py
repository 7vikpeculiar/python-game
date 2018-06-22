import os
import random
from bomberman import Bomberman
from enemy import Enemy
from getch import getch

def bricks(arr): 
    count = 0
    while(count < 55):
        y = range(1,76,4)
        x = range(2,38,2)
        i = random.choice(x)
        j = random.choice(y)
        if (i < 5 and j < 6):
            continue
        if (i%4 == 0 and j%8 == 5):
            continue
        if (arr[i][j]=='/'):
            continue
        for a in [0,1,2,3]:
            for b in [0,1]:
                arr[i+b][j+a] = '/'  
        count+=1

'''def bricks(final_array):
    y = range(1,76,4)
    x = range(2,38,2)
    for i in x:
        for j in y:
            if (i%4 == 0 and j%8 == 5):
                continue
            for a in [0,1,2,3]:
                for b in [0,1]:
                    final_array[i+b][j+a] = '/'
    return final_array
'''

def empty():
    a = ['X']*80
    b = ['X']+[' ']*78 + ['X']
    c = ['X']+['    XXXX']*(78//8) +['     X']
    final_array = []
    final_array.append(['X']*80)
    final_array.append(['X']*80)
    for ele in range(38//4):
        final_array.append(['X']+[' ']*76 + ['X']*3)
        final_array.append(['X']+[' ']*76 + ['X']*3)
        final_array.append(['X']+([' ']*4+['X']*4)* 9+ [' ']*4 +['X']*3)
        final_array.append(['X']+([' ']*4+['X']*4)* 9+ [' ']*4 +['X']*3)
    final_array.append(['X']*80)
    final_array.append(['X']*80)
    bricks(final_array)
    return final_array

def printer(final_array):
    for arr in final_array:
        print("".join(arr))


a = empty()
player = Bomberman()
e1  = Enemy()
e2  = Enemy()
e3  = Enemy()
#printer(a)
(player.insert(a))
e1.place(a)
e2.place(a)
e3.place(a)
#printer(a)
print("Press z to start the game")
new = getch()
count = 0
while new != 'q': 
    
    if player.check_wall(new,a):
        player.delete(a)
        player.move(new,a)
        if new == 'b':
            count = 4
        printer(a)
    else:
        printer(a)
    if count > 0:
        player.bomb.insert(a)
        if count == 2:
            player.bomb.explode(player.bomb.check_wall(a),a)
        if count == 1:
            player.bomb.clear(a)
        count-=1
    e1.delete(a)
    ls1 = e1.check_wall(a)
    e1.move(ls1,a) 
    e2.delete(a)
    ls2 = e2.check_wall(a)
    e2.move(ls2,a) 
    e3.delete(a)
    ls3 = e3.check_wall(a)
    e3.move(ls3,a) 
    if(e1.x == player.x and e1.y == player.y):
        break
    new = getch()
    os.system('cls' if os.name=='nt' else 'clear')
if new == 'q':
    print('You have quit the game')
'''
'''


