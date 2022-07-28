class Car:
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year,):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 40

    def get_descriptive_name(self):
        """返回整洁的描述信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息
        """
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self,mileage):     # b. 通过方法修改属性的值
        """将里程表读数设置为指定的数
           禁止将里程表读数往回调
        """
        if mileage >=self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Your can't roll back an odometer!")

    def increment_odometer(self,miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles


class Battery:           # 将实例用作属性
    """一次模拟电动汽车电瓶的简单尝试"""
    def __init__(self,battery_size=100):
        """初始化电瓶的属性"""
        self.battery_size=battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息。"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 75:
            range1 = 260
        elif self.battery_size == 100:
            range1 = 315
        print(f"This car can go about {range1} miles on full charge")


class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """初始化父类的属性
           再初始化电动汽车特有的属性
        """
        super().__init__(make,model,year)
        # self.battery_size = 75
        self.battery = Battery()

    # def describe_battery(self):
    #     """打印一条描述电瓶容量的消息"""
    #     print(f"This car has a {self.battery_size}-kwh battery")

    def fill_gas_tank(self):    # 重写父类的方法，假设car类有同名方法，这样，python将不会考虑此个父类方法
        """电动车没有油箱"""
        print("This car doesn't need a gas tank!")

my_tesla = ElectricCar("tesla", "model s","2021")
print(my_tesla.get_descriptive_name())
my_tesla.battery.battery_size = 75
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()