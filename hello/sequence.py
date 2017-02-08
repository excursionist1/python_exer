# -*-coding:utf-8-*-

days = ['monday', 'tuesday', 'friday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie']

for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day, ": drink", drink, "-eat", fruit, "-enjoy", dessert)