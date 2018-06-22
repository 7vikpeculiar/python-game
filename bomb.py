class Bomb():

    def __init__(self,x,y):
        self.__alive = True
        self.x = x
        self.y = y 
        self.time = 3
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_time(self):
        return self.time

    def set_x(self,i):
        self.x+=i
    
    def set_y(self,i):
        self.y+=i
    
    def set_time(self,i):
        self.time+=i

    def __repr__(self):
        return 'OOOO\nOOOO'

    def insert(self,array):
        a = self.get_x()
        b = self.get_y()
        for i in range(2):
            for j in range(4):
                array[a+i][b+j]='O'
        return array

    def delete(self,array):
        a = self.get_x()
        b = self.get_y()
        for i in range(2):
            for j in range(4):
                array[a+i][b+j]=' '
        return array
	
    def check_wall(self,array):
        a = self.get_x()
        b = self.get_y()
        ls = ['c']
        if not('X' in array[a-1][b:b+4]):
            ls.append('w') 
        if not('X' in array[a+2][b:b+4]):
            ls.append('s') 
        if not(b < 1 or 'X' == array[a][b-1] or 'X' == array[a+1][b-1]):
            ls.append('a') 
        if not(b >= 73 or 'X' == array[a][b+4] or 'X' == array[a+1][b+4]):
            ls.append('d')
        self.ls = ls
        return ls

    def explode_block(arr,x,y):
        for i in range(2):
            for j in range(4):
                arr[x+i][y+j] = 'e'
    
    def clear_block(arr,x,y):
        for i in range(2):
            for j in range(4):
                arr[x+i][y+j] = ' '
    
    def explode(self,ls,array):
        x = self.get_x()
        y = self.get_y()
        if 'w' in ls:
            Bomb.explode_block(array,x-2,y)
        if 's' in ls:
            Bomb.explode_block(array,x+2,y)
        if 'a' in ls:
            Bomb.explode_block(array,x,y-4)
        if 'd' in ls:
            Bomb.explode_block(array,x,y+4)
        if 'c' in ls:
            Bomb.explode_block(array,x,y)
    
    def clear(self,array):
        ls = self.ls
        x = self.get_x()
        y = self.get_y()
        if 'w' in ls:
            Bomb.clear_block(array,x-2,y)
        if 's' in ls:
            Bomb.clear_block(array,x+2,y)
        if 'a' in ls:
            Bomb.clear_block(array,x,y-4)
        if 'd' in ls:
            Bomb.clear_block(array,x,y+4)
        if 'c' in ls:
            Bomb.clear_block(array,x,y)

 
