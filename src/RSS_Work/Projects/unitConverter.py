# Author : Sebastiano Giannelli Viscardi
# Date: 24-04-2022
# Version: 1.0
# Description: Unit converter, convert between different units in both metric and imperial.

weight = {
    "kg": 1000,
    "g": 1,
    "mg": 0.001,
    "lb": 453.5924,
    "oz": 28.34952,
    "t": 907185.07,
}

distance = {
    "km": 1000,
    "m": 1,
    "cm": 0.01,
    'mile': 1609.34,
    'yard': 0.9144,
    'foot': 0.3048,
    'inch': 0.0254,
}

inp1 = input('Enter the unit to convert from, out of: \nkg, g, mg, lb, oz, t, km, m, cm, mile, yard, foot, inch \n')
if inp1 in weight:
    inp2=input('Enter the unit to convert to, out of: \nkg, g, mg, lb, oz, t\n')
elif inp1 in distance:
    inp2=input('Enter the unit to convert to, out of: \nkm, m, cm, mile, yard, foot, inch\n')
num = input('Enter the number to convert: \n')


if inp1 in weight:
    if inp2 in weight:
        print(num + inp1 + ' is ' + str(float(num) * weight[inp1] / weight[inp2]) + inp2)
    else:
        print('Invalid unit')
elif inp1 in distance:
    if inp2 in distance:
        print(num + inp1 + ' is ' + str(float(num) * distance[inp1] / distance[inp2]) + ' ' + inp2)
    else:
        print('Invalid unit')
else:
    print('Invalid unit')
