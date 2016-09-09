s = "abcdef가나다"

# a b c d e f 가 나 다

for x in s:
    print(x, end=' ')

print(" ".join(s))

# 숫자를 반복해서 쓸 경우 range() 함수 사용
for x in range(10):     # 0 ~ 9
    print(x, end=' ')

# 1부터 10까지의 합
tot = 0
for x in range(1,11):
    tot += x

print(tot)

# sum 내장함수 사용
print(sum(range(1,11)))

# 2 ~ 9단 까지 구구단 출력
for x in range(2,10):
    for y in range(2,10):
        print("%d*%d=%d\t" % (x, y, x*y), end = ' ')
    print()
else:
    print('구구단 출력 끝!!')

