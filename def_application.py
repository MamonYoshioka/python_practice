# 関数内関数
# def outer(a, b):
#     def plus(c, d):
#         return c + d

#     r1 = plus(a, b)
#     r2 = plus(b, a)
#     print(r1 + r2)

# outer(1, 2)

# クロージャ
# def outer(a, b):
#     def inner():
#         return a + b

#     return inner

# f = outer(1,2)
# # ここで初めてinnerが実行される
# r = f()
# print(r)

def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius

    return circle_area

ca1 = circle_area_func(3.14)
ca2 = circle_area_func(3.141592)

print(ca1(10))
print(ca2(10))


# デコレータ
# 似たような言葉でイテレーターという言葉があるが、これは『反復可能処理可能なデータ』を意味する。

def print_more(func):
    def wrapper(*args, **kwargs):
        print('func', func.__name__)
        print('args',args)
        print('kwargs',kwargs)
        result = func(*args, **kwargs)
        print('result', result)
        return result
    return wrapper

def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

@print_info
@print_more
def add_num(a, b):
    return a + b

r = add_num(10,20)
print(r)

# f = print_info(add_num)
# r = f(10, 20)
# print(r)

# print('start')
# r = add_num(10, 20)
# print('end')

# print(r)



# ラムダ
l = ['Mon','tue','Wed','Thu','fri','sat','Sun']

def change_words(words, func):
    for word in words:
        print(func(word))

# def sample_func(word):
#     return word.capitalize()
# sample_func = lambda word: word.capitalize()

change_words(l, lambda word: word.capitalize())
change_words(l, lambda word: word.lower())


# ジェネレーター
l = ['Good morning','Good afaternoon','Good night']

for i in l :
    print(i)

print("###############")
def counter(num=10):
    for _ in range(num):
        yield 'run'



def greeting():
    yield 'Good morning'
    yield 'Good afternoot'
    yield 'Good night'

for g in greeting():
    print(g)

g = greeting()
c = counter()


print(next(g))
print(next(c))
print(next(g))
print(next(c))
print(next(g))