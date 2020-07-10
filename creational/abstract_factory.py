"""

Desc:               抽象工厂方法(应用:多适用于创建产品簇,相互依赖 相互关联的产品族群.
                                优点:符合开闭原则,对产品的管理方便
                                缺点:扩展修改会涉及多类)
CreatedOn:          2020/6/17 10:34
Author:             wut
"""

from abc import abstractmethod


class KeyBoard:
    def __init__(self, size, color, kb_type):
        self.size = size
        self.color = color
        self.type = kb_type


class Mouse:
    def __init__(self, color, size):
        self.size = size
        self.color = color


class CPU:
    def __init__(self, freq, version):
        self.freq = freq
        self.version = version


class DellKB(KeyBoard):
    def __init__(self, size, color, kb_type):
        super(DellKB, self).__init__(size, color, kb_type)


class LenovoKB(KeyBoard):
    def __init__(self, size, color, kb_type):
        super(LenovoKB, self).__init__(size, color, kb_type)


class DellMouse(Mouse):
    def __init__(self, color, size):
        super(DellMouse, self).__init__(color, size)


class LenovoMouse(Mouse):
    def __init__(self, color, size):
        super(LenovoMouse, self).__init__(color, size)


class DellCPU(CPU):
    def __init__(self, freq, version):
        super(DellCPU, self).__init__(freq, version)


class LenovoCPU(CPU):
    def __init__(self, freq, version):
        super(LenovoCPU, self).__init__(freq, version)


class AbstractFactory:

    @abstractmethod
    def create_product(self):
        raise Exception("no product")


class DellFactory(AbstractFactory):
    def create_product(self):
        cpu = DellCPU('1.5Ghz', '1.0')
        kb = DellKB('small', 'red', 'black')
        mouse = DellMouse('black', 'small')
        return "get dell cpu, kb, mouse", cpu, kb, mouse


class Factory:
    def __init__(self, factory):
        self.factory = factory

    def create(self):
        return self.factory().create_product()


if __name__ == "__main__":
    dell_product = Factory(DellFactory).create()
    print(dell_product)
