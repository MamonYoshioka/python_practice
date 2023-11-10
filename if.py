print("XXXXX")
"""
Test
Test
Test
Test
"""
print("XXXXX")

# apple price
some_value = 100

# コード途中での改行
"""
80文字以上になる場合は改行する
pythonの暗黙のルール
"""
s = "aaaaaaaaa" \
+ "bbbbbbbb"
print(s)

# if文
"""
python暗黙ルール：インテンドは４つ開ける
※rubyは２つ。

ifのブロックはインテンドで認識する。
"""
x = 10

if x < 0:
    print("negative")
elif x == 0:
    print("zero")
else:
    print("positive")

a = 5
b = 10

if a > 0:
    print("a is positive")
    if b > 0:
      print("b is positive")

# 論理演算子
a = 1
b = 1

a == b
a != b
# aがｂよりも小さい
a < b
# aがｂよりも大きい
a > b
# aがｂ以下
a <= b
# aがｂ以上
a >= b

# 論理演算子
# aもｂも真であれば真
if a > 0 and b > 0:
    print("a and b is positive")

# a または bが真であれば真
a = -1
b = 1

if a > 0 or b > 0:
    print("a or b is positive")

# in notの使用方法
y = [1,2,3]
x = 1

if x in y:
    print("in")

if 100 not in y:
    print("not in")

a = 1
b = 2

if not a==b:
    print("Not equal")

# 数値比較の場合は以下のような記述が推奨されている
if a != b:
    print("Not equal")




# is_ok = True
is_ok = 1

if not is_ok:
    print("No")
else:
    print("OK")

arr = [1,2,3,4]

if arr:
    print("Ok")
else:
    print("Ng")


# is
# 基本、isはNoneかどうかを確認する際によく用いられるもの
is_empty = None
# print(is_empty)

if is_empty is None:
    print("None!!!!")

# 1はTrueと等しいので、Trueになる
print(1 == True)
# 1はTrueではないので、Falseになる
print(1 is True)