import random

# 1부터 10까지 출력
count = 1

while count <= 10:
    print("count : " + str(count))
    count += 1
    if count ==5:
        break
    count += 1
else:
    print('ent')

# 숫자 맞추기 게임
print(random.random())
print(random.random())
print(random.random())

# 0.0xx ~ 0.9xx
# 0.XX ~ 9.xx
print(random.random() *10)

# 1 ~ 10
print(int(random.random()*10)+1)

# 숫자를 입력받고  3번만에 숫자 맞추기 게임
# 3번만에 못맞추면 다음 기회에!

#!!!숙제!!!