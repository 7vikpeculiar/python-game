class Person:
    
    def __init__(self):
        self.__alive = True
        self.x = 2
        self.y = 1 

    def is_alive(self):
        print(self.__alive)

    def killed(self):
        self.__alive = False
        print(self.__alive)
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y

    def set_x(self,i):
        self.x+=i
    
    def set_y(self,i):
        self.y+=i
    
         
