# 문자열 : "", ''

print("Hello", 'world!!')

print('I Love "KISUM"')

# 여러줄 문자열 출력

s = """
최유정
김소현
키썸
"""

print(s)

# 문자열 연결
a = "I" + " Love" + " KISUM"
print(a)

# 주의사항
#print(10 + "KISUM")

print("=" * 50)

# 문자열 길이 : len()
print(len(a))

# 문자열 포맷팅
# 1. 서식문자 사용 (%d, %f, %s)
print("ID : %d, NAME : %s" % (2619, "신성휘"))

# 2. format() 사용
print("키 : ", format(185.34, ".1f"))
print("재산 : ", format(10000000000000, ",d"))

s = "I ate {} {}".format(5, "apples")
print(s)

s = "I ate {0} {1} and {0} {2}".format(5, "apples", "bananas")
print(s)

s = "I ate {num} {what}".format(num=5, what="kiwi")
print(s)
