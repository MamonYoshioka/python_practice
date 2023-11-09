# データ構造
list = [1,2,3]
print(list)
print(list[0])
print(list[1])
print(list[2])

print(list[1:3])

n = [1,2,3,4,5,6,7,8,9,10]
print(n)
print(n[::2])

s = ['a','b','c','d','e','f','g']
print(s)

s[0] = 'X'
print(s)

s[2:5] = ['C','D','E']
print(s)


# メソッド
n = [1,2,3,4,5,6,7,8,9,10]
print(n)

n.append(100)
print(n)

n.insert(0, 200)
print(n)

n.pop()
print(n)

del n[0]
print(n)

del n
# print(n)

m = [1,1,2,3,4]
print(m)

m.remove(1)
print(m)

r = [1,2,3,4,5,1,2,3]
print(r.index(3))

print(r.index(3,3))
print(r.count(3))

if 5 in r:
  print("5 is exist!!!")


r.sort()
print(r)

r.sort(reverse=True)
print(r)

name = 'My name is Potter.'
print(name)

to_split = name.split(' ')
print(to_split)

# リストのコピーについて => （値渡しと参照渡し）

i = [1,2,3,4,5]
j = i
j[0] = 100
print('j=', j)
print('i=', i)

x = [1,2,3,4,5]
y = x.copy()
y[0] = 100

print('y=', y)
print('x=', x)

print(id(x))
print(id(y))


# タプル
t = (1,2,3,1,2)
print(t)

print(t[0])
print(t[-3])

# errorになる処理
# t[0] = 100
# print(t)


# タプルのアンパッキング
num_touple = (10, 20)
print(num_touple)

x ,y = num_touple
print(x ,y)

x, y = 20, 30
print(x ,y)

i = 30
j = 40

tmp = i
i = j
j = tmp

print(i, j)


a = 100
b = 200
print(a, b)

a, b = b, a
print(a,b)



# タプルの使い方
choose_from_two = ('Apple','Ornge','Banana')
answer = []

# choose_from_two.append('Apple')
# choose_from_two.append('Banana')

"""
上記の135,136行目を実行しようとすると、タプルにで宣言しているので以下のようなメッセージになる
(タプルにはappendなどはできないため)
【Error masseage】
Traceback (most recent call last):
  File "data_structure.py", line 135, in <module>
    choose_from_two.append('Apple')
AttributeError: 'tuple' object has no attribute 'append'
"""

answer.append('Apple')
answer.append('Banana')


print(choose_from_two)
print(answer)

# 辞書型
d = {'x':10, 'y':20}
print(d)

print(type(d))


d['x'] = 100 # xの値の変更
print(d)


# 辞書型のメソッド
d1 = {'z': 100, 'w': 300}
print(d1)

print(d1.keys())
print(d1.values())

d2 = {'x':100, 'y':400}

print(d2)
print(d2.values())

d1.update(d2)
print(d1)

print(d2.get('x'))
d2['y'] = 200
print(d2.get('y'))
print(d1)

d1.pop('x')
print(d1)

del d1['y']
print(d1)

print('z' in d1)

# 辞書型のコピー
x = {'a' : 1}
y = x
y['a'] = 1000
print(x)
print(y)

x = {'a' : 1}
y = x.copy()
y['a'] = 2000
print(x)
print(y)

# 辞書型の使い方
fruits = {
  'apple':100,
  'orange':200,
  'banana':300,
}

print('apple is', fruits['apple'], 'yen!!')

"""
辞書型はハッシュテーブルという検索に強い仕組みを持ってる。
なので、なにかkeyを元に検索をかけるような仕組みを作りたい場合は辞書型を使うのがベター。
"""