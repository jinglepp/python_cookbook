# -*- coding: utf-8 -*-


def avg(middle):
    return sum(middle) / len(middle)


def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)


record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print(name, email, phone_numbers)
# Dave dave@example.com ['773-555-1212', '847-555-1212']

sales_record = [11, 22, 33, 44]
*trailing_qtrs, current_qtr = sales_record
trailing_avg = sum(trailing_qtrs) / len(trailing_qtrs)


def avg_comparison(trailing_avg, current_qtr):
    return current_qtr - trailing_avg


print(avg_comparison(trailing_avg, current_qtr))
