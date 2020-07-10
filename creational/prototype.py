"""

Desc:               原型模式（应用：在对象初始化操作比较复杂的情况下，
                             优点：它能大大降低耗时，提高性能，
                             不用重新初始化对象，而是动态地获得对象运行时的状态）
CreatedOn:          2020/6/17 10:34
Author:             wut
"""

import copy


class Cloneable:
    def deep_copy(self):
        return copy.deepcopy(self)

    def copy(self):
        return copy.copy(self)


class Test(Cloneable):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def update(self, a, b):
        self.a = a
        self.b = b

    def show(self):
        print(id(self), self.a, self.b)


if __name__ == "__main__":
    t = Test(1, 2)
    t.show()
    t.update(3, 4)
    ts = t.deep_copy()
    ts.show()
