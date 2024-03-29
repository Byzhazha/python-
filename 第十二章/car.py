class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year, ):
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

    def update_odometer(self, mileage):  # b. 通过方法修改属性的值
        """将里程表读数设置为指定的数
           禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Your can't roll back an odometer!")

    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles


my_new_car = Car("audi", "a4", 2019)
print(my_new_car.get_descriptive_name())

# 修改属性的值
# a.直接改
# my_new_car.odometer_reading = 23
my_new_car.update_odometer(23_500)
my_new_car.read_odometer()
my_new_car.increment_odometer(100)
my_new_car.read_odometer()
