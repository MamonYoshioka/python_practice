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