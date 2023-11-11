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

for _ in range(5):
    print('hello')