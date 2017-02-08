# -*-coding:utf-8-*-

def tax(bill):
    # adds 8% tax to a restaurant bill
    bill *= 1.08
    print("with tax: %f" % bill)
    return bill

def tip(bill):
    bill *= 1.15
    print('with tip: %f' % bill)
    return bill

meal_cost= 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)
