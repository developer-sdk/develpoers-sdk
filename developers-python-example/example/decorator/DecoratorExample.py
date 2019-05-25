#!/usr/bin/env python
# -*- coding: utf-8 -*-

_LIST1_ = [ "json", "txt", "csv" ]
_LIST2_ = [ "1", "2", "3" ]
_LIST3_ = [ "a", "b", "c" ]

def check_param_values(param_index, check_list):
    ''' param_index로 전달된 데이터가, check_list에 있는 데이터 인지 확인하고 오류를 발생하는 데코레이터  '''
    
    def wrapper(func):
        def decorator(*args, **kwargs):
            print("%s %s" % (func.__name__, "before"))
            
            if args[param_index] not in check_list:
                raise ValueError("args error {0} not in [{1}]".format(args[param_index], ",".join(check_list)))
            
            print(args)
            print(kwargs)
            
            result = func(*args, **kwargs)
            print("%s %s" % (func.__name__ , "after"))
            return result
        return decorator
    return wrapper

@check_param_values(0, _LIST1_)
@check_param_values(1, _LIST2_)
@check_param_values(2, _LIST3_)
def func(param1, param2, param3):
    return "{0}, {1}, {2}".format(param1, param2, param3)

print func("json", "2", "c")