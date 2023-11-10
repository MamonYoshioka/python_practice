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
