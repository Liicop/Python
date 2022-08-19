class Television:
    
    def __init__(self,size,color):  #inches
        self.size = size        #public
        self.color = color      #public
        self.__volts = 110     #private

    def TV_data(self):
        print(f"""TV characteristics are: 
size: {self.size} 
color: {self.color}
volts: {self.__volts}
""")
        
    def Turn_on(self):
        print(f'T.V turn on with {self.__volts} volts')  #public
    
    def Turn_off(self):
        print('T.V turn off, no power')    #public
        
    def _Add_chanels(self):   #protected
        pass
    
    def __Change_volts(self):   #private
        self.__volts = 220
        print(f'Volts change to {self.__volts}')
        
Samsung = Television(45,'black')
#Samsung.volts = 120   # volts es diferente de la variable __volts, es una nueva
#print(Samsung.volts)
Samsung.TV_data()
Samsung.Turn_on()