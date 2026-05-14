# 입력 - input

###

# print를 이용해서 컴퓨터로부터 정보를 받았다면,
# 정보를 컴퓨터에게 전달도 가능
# 전달 받은 값은 어딘가에 보관해야 함 = 변수 !

var = input()

# input 함수는 무조건 String 자료형으로 값을 전달
# 숫자형으로 전달 받고 싶다면, int() 함수를 이용해서 변환 필요

var = int(input())

# type() 함수를 이용해서 자료형 확인 가능
type(var) # -> int 자료형으로 변환된 것을 확인할 수 있음

# 자료형 변환 함수
# int() : 숫자형으로 변환
# str() : 문자열로 변환
# float() : 실수형으로 변환
# list() : 리스트로 변환
# tuple() : 튜플로 변환
# set() : 집합으로 변환
# dict() : 딕셔너리로 변환
# bool() : 불리언으로 변환

# [실습]
# input()을 이용해서 입력을 넣고, 이를 변수 var에 담아봅시다.
# input의 괄호 안에 내용을 넣으면 채점이 정상적으로 동작하지 않습니다. 
# ex. input("입력하세요") → 채점 동작 안 됨
var = input()

# 앵무새야 안녕 ?

# 앵무새가 말을 따라합니다!
print("앵무새 :", var)

# 앵무새 : 앵무새야 안녕 ? 출력됨

# 입력한 값이 어떤 자료형인지 확인해 봅시다.
print(type(var))

# <class 'str'> 출력됨

# [실습]
#변수 money에 input을 이용해서 입력을 받아봅시다.
money = input()

# money를 int형으로 변환해서, 다시 money에 넣어줍시다.
money = int(money)

# money를 2배 불려서 print로 출력해 봅시다.

print(money * 2)

###

# 논리형 자료와 비교연산

# True, False는 논리형 자료의 값
# 논리형 자료는 참과 거짓을 나타내는 자료형

# 비교연산자 : > , < , >= , <= , == , !=
3 > 2 # True 
3 < 2 # False
3 >= 3 # True
3 <= 2 # False
3 == 3 # 같다 True
3 != 3 # 다르다 False

# 논리 자료형은 True와 False로만 이루어져 있지만, 
# 숫자형 자료와도 연산이 가능
# True는 1로, False는 0으로 취급

True + 1 # 2
False + 1 # 1   

# AND 연산자 : and
# A and B : A와 B가 모두 참일 때 참, 나머지는 거짓
# 각 논리 모두 True일 때만 결과가 True, 나머지는 False
True and True # True
True and False # False
False and True # False
False and False # False

# OR 연산자 : or
# A or B : A와 B 중 하나라도 참이면 참, 둘 다 거짓이면 거짓
# 논리들 중 하나라도 True이면 결과가 True, 
# 둘 다 False일 때만 False
True or True # True 
True or False # True
False or True # True
False or False # False

# NOT 연산자 : not
# not A : A가 참이면 거짓, A가 거짓이면 참
not True # False
not False # True

not 3==4 # 3은 4가 아니다 → True
not 3==3 # 3은 3이다 → False    

# [실습]
# Q1. == 혹은 != 연산자를 이용해서 True인 명제를 ans1에 넣어봅시다.
ans1 = 3 == 3

# Q2. > 혹은 < 연산자를 이용해서 False인 명제를 ans2에 넣어봅시다.
ans2 = 3 < 2

# Q3. >= 혹은 <= 연산자를 이용해서 True인 명제를 ans3에 넣어봅시다.
ans3 = 3 >= 3

# 위의 세 변수를 출력해서 True, False 여부를 확인해 봅시다.
print(ans1, ans2, ans3)

# [실습]
# 괄호 안에 적절한 명제를 채워 stat1이 True가 되게 해봅시다.
stat1 = 3==3 and 2<4 and 5>1

# 괄호 안에 적절한 명제를 채워 stat2이 False가 되게 해봅시다.
stat2 = 4>=6 or "apple"=="Apple" or 5!=5

# 괄호 안에 적절한 명제를 채워 stat3이 True가 되게 해봅시다.
stat3 = not 5!=5

# 위의 세 변수를 한 문장으로 출력해서 True, False 여부를 확인해 봅시다.
print(stat1, stat2, stat3)

###

# 조건문

# 회원가입정보==로그인정보 -> 로그인 성공
# 회원가입정보!=로그인정보 -> 로그인 실패


# if 조건문 :
# if 조건문은 조건이 참(True)일 때 명령 실행

# 만약 변수 i가 1이라면 변수 i를 출력해라.
# if i == 1 : 
#     print(i)

# if 문에 들어갈 명령어들은 같은 들여쓰기로 구분

i = int(input())
if i == 1 :
    print(i)

# 조건이 맞지 않는다면?
# if 조건문은 조건이 참일 때만 명령 실행

# 만약 변수 i가 1이라면 변수 i를 출력해라.
# if : 
# 아니라면, i+1 을 출력해라. 
# else :
i = int(input())

if i == 1 :
    print(i)
else : 
    print(i+1)

 # 조건이 여러 개라면?
# if 조건문은 조건이 참일 때 명령 실행
# 만약 변수 i가 1이라면 변수 i를 출력해라.
# if : 
# 만약 변수 i가 2라면 변수 i+1을 출력해라.
# elif : 
# 둘 다 아니라면, i+2 를 출력해라.
# else : 
i = int(input())

if i == 1 :
    print(i)
elif i == 2 :
    print(i+1)
else :
    print(i+2)

# [실습]
# input()을 이용해서 숫자(정수) 입력을 받고, 변수 num에 이를 넣어봅시다.
num = int(input())

# if-else문을 이용해서 만약 입력받은 수가 홀수면 "(입력받은 수) 홀수입니다."
# 짝수면 "(입력받은 수) 짝수입니다."를 출력해 봅시다.
# 괄호는 출력하지 않습니다.
if num % 2 == 1 :
    print(num, "홀수입니다.")
else :
    print(num, "짝수입니다.")

# [실습]
# 변수 answer에 수 1~50 중 하나를 넣어봅시다.
answer = 33

# input을 통해 숫자형으로 입력을 받아서 변수 submit에 저장해 봅시다.
submit = int(input())

# if-elif-else문으로 Up-Down Game을 구현해 봅시다.
# 만약 answer보다 submit이 더 크면 "정답보다 더 큰 수를 입력했습니다."
# 만약 answer보다 submit이 더 작으면 "정답보다 더 작은 수를 입력했습니다."
# 만약 answer와 submit이 같으면 "정답!" 를 출력합니다.

if answer < submit : 
    print("정답보다 더 큰 수를 입력했습니다.")
elif answer > submit :
    print("정답보다 더 작은 수를 입력했습니다.")
else :
    print("정답!")