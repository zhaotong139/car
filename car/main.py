from owner import Owner
from order import Order
from stopTxt import StopTxt
from stopCar import StopCar
from parking import Parking
import time
'''使用面向对象的思路实现『停车收费』场景：
1. 车主开车进入停车场，产生停车记录，
2. 车主开车继续向前，将车停到车位上，修改前面的停车记录，
3. 车主停车完成，
一段时间(购物、吃饭...)之后，车主驾车准备离开停车场，
4. 车主开车离开车位，修改停车记录，
5. 车主开车到达出口，系统根据停车的时间生成订单，
6. 车主缴纳停车费，
7. 车主离开停车场。
至此，整个停车收费的场景完成。
'''
while True:
    chose = input(
        '''
        您好,欢迎光临!
        请选择功能：
        1.停车
        2.出车
        3.退出系统 
        '''
        )
    if chose == '3':
        print('谢谢光临')
        break
    elif chose == '1':
        owner = Owner('zs')
        owner.drive()
        stopCar = StopCar('1')
        stopCar.in_car()
        time.sleep(5)
        owner.stop() 
        parking = Parking('2')
        parking.in_parking()
       
    elif chose == '2':
        owner = Owner('zs')  
        owner.drive_parking()
        owner.stop_car() 
        owner.pay()
        owner.leave()  
    time.sleep(3)
    continue

