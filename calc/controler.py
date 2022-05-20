import In
import Prog
import Out

def sum():
   a1 = In.get_value()  # запросили
   b1 = In.get_value()
   In.number(a1, b1)    #записали в базу данных
   num = In.get_data()
   #Prog.plus1(num[0], num[1])
   Out.view_data(Prog.plus1(num[0], num[1]))

