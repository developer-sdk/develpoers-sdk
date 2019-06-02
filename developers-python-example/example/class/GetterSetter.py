#!/usr/bin/python
# -*- coding:utf-8 -*-

class God():
    def __init__(self):
        self.race = "God"
        self.age = 1000
        self.name = 'Zeus'

class Person():
    def __init__(self):
        self.race = 'human'
        self.age = 30
        self.name = 'Edward'

class DemiGod(God):
    def __init__(self):
        self.name = "heraclues"

    def __getattr__(self, attr):
        # __getattr__ 를 재정의 하여 __dict__의 값을 반환하도록 수정 
        if attr in self.__dict__:
            return self.__dict__[attr]
        return None

# 신 
g = God()
print(g.race)

# 사람 
p = Person()
print(p.race)

# 반인반신 
d = DemiGod()
print(d.name)
print(d.race)

# 속성 추가 
d.power = "thunder"
print(d.power)

# Person 객체는 __getattr__ 를 오버라이딩 하지 않았기 때문에 속성으로 데이터를 가져가는 것은 불가 
# __dict__ 를 이용하여 데이터 출력 
p.power = "run"
print(p.__dict__)
print(p.__dict__['power'])