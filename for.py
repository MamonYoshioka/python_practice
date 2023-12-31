some_list = [1,2,3,4,5]

# i = 0
# while i < len (some_list):
#     print(some_list[i])
#     i += 1

for i in some_list:
    print(i)


for i in 'abcde':
    print(i)

for word in ['my','name','is','mike']:
    if word == 'name':
        continue
    print(word)


# for else
for fruit in ['apple','banana','orange']:
    if fruit == 'banana':
        print('stop eating')
        break
    print(fruit)
else:
    print('I ate all!')

# range関数

# num_list = [0,1,2,3,4,5,6,7,8,9]

# for i in num_list:
#     print(i)

for i in range(10):
    print(i)

for x in range(2, 10, 3):
    print(f'x is {x}')


# 変数に格納した数値を使わない場合は「_(アンダースコア)」を用いる
for _ in range(5):
    print('hello')

# enumerate関数 => index番号も一緒に表示してくれる

for i, fruit in enumerate(['apple','banana','orange']):
    print(i, fruit)

# zip関数
days = ['mon','tue','wed']
fruits = ['apple','banana','orange']
drinks = ['coffee','tea','beer']

# for i in range(len(days)):
#     print(days[i], fruits[i], drinks[i])

for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)


# for文で辞書の内容を処理する
d = {'x':100, 'y':200}

for k, v in d.items():
    print(k, v)

# 頻出頻度【高】
print(d.items())

"""
d.itemsをすることで、辞書の中身をタプルでアンパッキングし、
その後ｋとｖにその値を格納している
"""