from person import Person
import random
class Enemy(Person):
    def __repr__(self):
        return 'EEEE\nEEEE'

    def insert(self,array):
        a = self.get_x()
        b = self.get_y()
        for i in range(2):
            for j in range(4):
                array[a+i][b+j]='E' 
        return array

    def delete(self,array):
        a = self.get_x()
        b = self.get_y()
        for i in range(2):
            for j in range(4):
                array[a+i][b+j]=' ' 
        return array
    def place(self,arr):
        got = False
        while not got:
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
            got = True
            self.x = i 
            self.y = j
        
    def check_wall(self,array):
        a = self.get_x()
        b = self.get_y()
        lis =[]
        if not('X' in array[a-1][b:b+4] or '/' in array[a-1][b:b+4]):
                lis.append('w')
        if not('X' in array[a+2][b:b+4] or '/' in array[a+2][b:b+4]):
                lis.append('s')
        if not(b < 1 or 'X' == array[a][b-1] or 'X' == array[a+1][b-1] or '/' == array[a][b-1] or '/' == array[a+1][b-1]):
                lis.append('a')
        if not(b >= 73 or 'X' == array[a][b+4] or '/' == array[a][b+4] or 'X' == array[a+1][b+4] or '/' == array[a+1][b+4]):
                lis.append('d')
        return lis
   
    def move(self,lis,array):
        inp = random.choice(lis)
        if inp == 'w':
            self.set_x(-2)
        elif inp == 's':
            self.set_x(2)
        elif inp == 'a':
            self.set_y(-4)
        elif inp == 'd':
            self.set_y(4)
        self.insert(array)


