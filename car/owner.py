from stopTxt import StopTxt
from order import Order
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
#车主
class Owner():
    #drive方法用到的变量
    #得到Owner对象
    owner_car = ''
    #stop
    time_start = ''
    #drive_parking 方法用到的变量
    parking_car = ''
    #stop_car 方法用到的变量
    order_number = ''
    order_list = []
    txt_list = []
    owner_car_list = []
    def __init__ (self,_owner):
        self.owner = _owner
    # 1. 车主开车进入停车场，产生停车记录
    def drive(self):
        owner = ''
        car = ''
        state = ''
        txt = ''
        order_car = ''
        owner = input('输入您的姓名:')
        Owner.owner_car= Owner(owner)
        Owner.owner_car_list.append(Owner.owner_car)
        car = input('输入您的车牌号:')
        state = '进入停车场'
        Owner.time_start = time.time() 
        txt = StopTxt(owner,car,Owner.time_start,state)
        order_car = Order(owner,car,Owner.time_start,state)
        Owner.txt_list.append(txt)
        Owner.order_list.append(order_car)
        print('停车记录:车主:'+txt.owner+'车牌号:'+txt.car+'计时时间:'+time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(Owner.time_start))+'车辆状态:'+txt.state+':停车场编号:'+txt.stop_car)
    #2. 车主开车继续向前，将车停到车位上，修改前面的停车记录，
    #3. 车主停车完成，
    def stop(self):
        for i in Owner.txt_list:
            i.state = '停入车位' 
    #4.车主开车离开车位，修改停车记录，
    def drive_parking(self):
        Owner.parking_car = input('输入驶出车牌号:')
        for i in Owner.txt_list :
            if i.car == Owner.parking_car:
                i.state = '离开车位'
                print(i.__dict__)    
    #5. 车主开车到达出口，系统根据停车的时间生成订单，
    def stop_car(self):
        tt = ''
        Owner.order_number = input('输入驶出车牌号确认是否出库:')
        for i in Owner.order_list:
            if i.car == Owner.order_number:
                i.state = '确认离开'
                i.time_end = time.time()
                tt = float((i.time_end - i.time_start) / 3600)
                print('停车时间%f小时,停车费用%f元.' % (tt, float(tt / 5)))
    #6. 车主缴纳停车费，
    def pay(self):
        print('支付费用')
    #7. 车主离开停车场。
    def leave(self):
        print('车主已离开')   


