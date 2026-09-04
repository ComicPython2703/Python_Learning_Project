# vim: set fileencoding=utf-8 :
class Car:
    def __init__(self, brand, model, mile):
        self.brand = brand
        self.model = model
        self.mile = mile

    def get_deta(self):
        data = "品牌：%s  ; 型号：%s  ; 里程：%d KM" % self.brand, self.mile, self.mile
        print(data)


# noinspection PyPep8Naming
class Electric_car(Car):
    def __init__(self, brand, model, mile):
        super().__init__(brand, model, mile)
        self.electrics = 70

    def car(self):
        print(f"品牌：{self.brand} ; 型号：{self.model} ; 里程：{self.mile}")
        print(f"里程：{self.electrics}")


# =====================================
c1 = Car("QWE", "SSR", 114)
c2 = Electric_car("QWE", "SSR", 114)
c2.car()
