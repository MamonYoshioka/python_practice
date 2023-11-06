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