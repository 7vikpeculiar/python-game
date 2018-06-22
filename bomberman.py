from person import Person
from bomb import Bomb

def printer(final_array):
    for arr in final_array:
        print("".join(arr))

class Bomberman(Person):

    #def __init__(self):
    #    __pass_wall = False
    def setBomb(self):
        pass

    #def __repr__(self):
    #    return 'BBBB\nBBBB'

    def insert(self,array):
        a = self.get_x()
        b = self.get_y()
        for i in range(2):
            for j in range(4):
                array[a+i][b+j]='B' 
        return array

    def delete(self,array):
        a = self.get_x()
        b = self.get_y()
        for i in range(2):
            for j in range(4):
                array[a+i][b+j]=' ' 
        return array 
    
    def check_wall(self,inp,array):
        a = self.get_x()
        b = self.get_y()
        if inp == 'w':
            if 'X' in array[a-1][b:b+4] or '/' in array[a-1][b:b+4]:
                return False
        elif inp == 's':
            if 'X' in array[a+2][b:b+4] or '/' in array[a+2][b:b+4]:
                return False
        elif inp == 'a':
            if b < 1 or 'X' == array[a][b-1] or 'X' == array[a+1][b-1] or '/' == array[a][b-1] or '/' == array[a+1][b-1]:
                return False
        elif inp == 'd':
            if b >= 73 or 'X' == array[a][b+4] or '/' == array[a][b+4] or 'X' == array[a+1][b+4] or '/' == array[a+1][b+4]:
                return False
        return True
    
    def paired(self,array):
        a = self.get_x()
        b = self.get_y()
        self.bomb = Bomb(a,b)
        self.bomb.insert(array) 

    def move(self,inp,array):
        if inp == 'w':
            self.set_x(-2)
        elif inp == 's':
            self.set_x(2)
        elif inp == 'a':
            self.set_y(-4)
        elif inp == 'd':
            self.set_y(4)
        elif inp == 'b':
            self.paired(array)
            return 
        self.insert(array)


