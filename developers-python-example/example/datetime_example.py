#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
from datetime import datetime, timedelta

# 문자열 시간
str_time = 'Wed, 17 Jun 2015 08:25:34 GMT'

# time 객체를 이용한 문자열 to timestruct
obj_time_struct = time.strptime(str_time, '%a, %d %b %Y %H:%M:%S %Z')
print obj_time_struct
# time 객체를 이용한 timestruct 객체를 문자로 표현
print time.strftime('%Y-%m-%d %H:%M:%S', obj_time_struct)

# datetime 객체를 이용한 문자열 to datetime
obj_datetime = datetime.strptime(str_time, '%a, %d %b %Y %H:%M:%S %Z')
print obj_datetime
# datetime 객체를 문자료 표현
print obj_datetime.strftime('%Y-%m-%d %H:%M:%S')


# 날짜간 기간 계산
now = datetime.now()
one_day_prev = now - timedelta(1)
minus_timedelta = now - one_day_prev
print now
print one_day_prev
print minus_timedelta.total_seconds()