# 関数定義
def say_something():
  s = 'hi'
  return s

result = say_something()

print(result)

def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'green papper'
    else:
        return "I don't know"

result = what_is_this('red')
result = what_is_this('green')

print(result)


# 関数の引数と返り値
def add_num(a, b):
    return a + b

"""
基本的には上記の書き方をするが、下記のような書き方をする場合もある。
def add_num(a:int, b:int) -> int:
    return a + b
"""

r = add_num(10, 20)
print(r)


# 位置引数とキーワード引数

def menu(entree='beef', drink='wine', desert= 'ice'):
    print('entree=',entree)
    print('drink=',drink)
    print('desert=',desert)

menu('chiken', drink='beer')

def test_func(x, l=[]):
    l.append(x)
    return l

# y = [1,2,3]
# r = test_func(100, y)
# print(r)

# r = test_func(200, y)
# print(r)

r = test_func(100)
print(r)

r = test_func(100)
print(r)

"""
リストは参照渡しになるので、空の状態でデフォルト引数には置かないのが
暗黙のルールとなっている。

じゃあ、どうするか？
以下のようにNoneを入れる。
"""

def test_f(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l

r = test_f(200)
print(r)

r = test_f(300)
print(r)

# 位置引数のタプル化

def say_greeting(word, *args):
    print('word=', word)
    for arg in  args:
        print(arg)

say_greeting('Hi.','Mike','Nancy')

# t = ('Jhon', 'Nancy')
# say_greeting('Hi!!', *t)