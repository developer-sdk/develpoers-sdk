#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Parent(object):

    def __init__(self, name):
        self.name = name
        print('My name is {0}'.format(name))

    def show(self):
        print('Parent show, {0}'.format(self.name))

class Child(Parent):
    
    def __init__(self, name):
        super(Child, self).__init__(name)

    def show(self):
        print('Child show, {0}'.format(self.name))

def main():
    p = Parent('P')
    p.show()

    c = Child('C')
    c.show()

if __name__ == '__main__':
    main()
