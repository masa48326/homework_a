# A-11: BMIアプリ
height = float(input("Height(m)? > "))
weight = float(input("Weight(kg) > "))
print(f'Your BMI is {weight / height ** 2 : .2f}')
