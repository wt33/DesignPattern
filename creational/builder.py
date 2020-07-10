"""

Desc:               建造者模式(应用：适合创建一个复杂的对象，
                              创建的流程稳定，但是创建细节需要频繁变动。)
CreatedOn:          2020/6/17 10:34
Author:             wut
"""

from abc import abstractmethod


class Director:
    def __init__(self):
        self.builder = None  # 持有一个建造者对象

    def build_produce(self):
        self.builder.build_floor()
        self.builder.build_desk()

    def get_building(self):
        return self.builder.building


class Builder:
    def __init__(self):
        self.building = None

    @abstractmethod
    def build_floor(self):
        raise Exception

    @abstractmethod
    def build_desk(self):
        raise Exception


class HouseBuilder(Builder):
    def __init__(self):
        super(HouseBuilder, self).__init__()
        self.building = House()

    def build_desk(self):
        self.building.desk = "nice desk"

    def build_floor(self):
        self.building.floor = "nice floor"


class House:
    def __init__(self):
        self.desk = None
        self.floor = None


if __name__ == "__main__":
    d = Director()
    d.builder = HouseBuilder()
    d.build_produce()
    print(d.get_building().floor, d.get_building().desk)
