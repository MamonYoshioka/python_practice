# count = 0
# while count < 5:
#     print(count)
#     # +=は累算代入文
#     count += 1


count = 0
while True:
    if count >= 5:
        break

    if count == 2:
        count += 1
        continue

    print(count)
    count += 1


c = 1
while c < 5:
    if c == 1:
        break
    print(c)
    c += 1
else:
    print('done')

# input関数（対話型になる）
while True:
    word = input('Enter:')
    if word == 'ok':
        break
    print('next')
