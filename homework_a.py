# A-1: 文字列のリスト
users = ["Bob", "Tom", "Ken"]

# A-2: 整数のリスト
int_numbers = [1, 2, 3, 4, 5]

# A-3: 要素のデータ型が異なるリスト
kazuma_info = ["Kazuma", "Takahashi", 35]

# A-4: 要素へのアクセス
members = ["Kazuma", "Makoto", "Ohira"]
print(members[1])
print(members[0])

# A-5:  要素へのアクセスとフォーマット
kazuma_info = ["Kazuma", "Takahashi", 35]
print(f'Name: {kazuma_info[1]} {kazuma_info[0]},Age: {kazuma_info[2]}')

# A-6: forによるループその1
odd_numbers = [1, 3, 5, 7, 9]
for odd_number in odd_numbers:
    print(odd_number)
# A-7: forによるループその2
even_numbers = [2, 4, 6, 8]
for even_number in even_numbers:
    print(even_number * 2)

# A-8: リストを要素に持つリスト
users_info = {"Kazuma": 35, "Tom": 57, "Bob": 77}
for user_info in users_info:
    print(f'Name: {user_info}, Age: {users_info[user_info]}')

# A-9: 辞書
kazuma_info = {"first_name": "Kazuma", "family_name": "Takahashi", "age": 35}
print(kazuma_info["first_name"])  # "Kazuma"
print(kazuma_info["family_name"])  # "Takahashi"
print(kazuma_info["age"])  # 35

# A-10: サイコロ
import random


def dice():
    print(random.randint(1, 6))


# dice()
# dice()

# A-11: BMIアプリ
height = float(input("Height(m)? > "))
weight = float(input("Weight(kg) > "))
print(f'Your BMI is {weight / height ** 2 : .2f}')
