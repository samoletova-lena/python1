# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    number=number*(10**ndigits)+0.5
    number = number//1
    return number/(10**ndigits)
print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))
print(my_round(1.1275, 3)) 





# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить



'''import random
random.seed(a=None, version=2)
ticket_number=[]
a=0
while len(ticket_number)<6:
    a=random.randint(0,9)
    ticket_number.append(a)
print(ticket_number)'''

'''def lucky_ticket(ticket_number):
    sum1=0
    sum2=0
    sum1=ticket_number[i]+ticket_number[0]
    for i in range(len(ticket_number[3:])):
        sum2=ticket_number[i]+ticket_number[0]        
    if sum1==sum2:
        return true
if lucky_ticket:
    print("Счастливый билет!")'''


def lucky_ticket(ticket_number):
    ticket_number = str(ticket_number)
    list1 = ticket_number.split()
    print(list1)

    z=0
    sum1=0
    sum2=0
    z1=list1[0]
    z2=list1[1]
    z3=list1[2]
    sum1=z1+z2+z3
    z4=list1[3]
    z5=list1[4]
    z6=list1[5]
    sum2=z4+z5+z6
    if sum1==sum2:
        return True

ticket_number =123006
if lucky_ticket(ticket_number) == True:
    print("Счастливый билет!")

print(lucky_ticket(123006))
#print(lucky_ticket(12321))
#print(lucky_ticket(436751))
