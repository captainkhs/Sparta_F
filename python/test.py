import random # rnadom 모듈을 가져옴.

# n = int(input())

# for i in range(1,10):
#     print("%d * %d = %d" %(n, i, n*i))
#     print(n, '*', i, '=', n * i)

# a = random.randint(1, 6)  
# random.randint(a, b)

# a=[]
# for i in range(1,46):
#     a.append(i)
# # print(a)
# b=[]
# for s in a:
#     x = random.choice(a)
#     print(x)
#     b.append(x)
#     if 6 == len(b):
#         print(b)
#         break

# i = 2
# j = 5

# while i <= 32 or j >= 1:
#     print(i, j)
#     i *= 2
#     j -= 1

# num = int(input())

# charge = 1350

# charges = num

# while charges > 0:
#     charges = charges - charge
#     print(charges)
#     if charges < charge :
#         break


#표준 입력으로 정수 두 개가 입력됩니다
#(첫 번째 입력 값의 범위는 1~200, 두 번째 입력 값의 범위는 10~200이며 첫 번째 입력 값은 두 번째 입력 값보다 항상 작습니다). 
# 다음 소스 코드를 완성하여 첫 번째 정수와 두 번째 정수 사이의 숫자 중 3으로 끝나지 않는 숫자가 출력되게 만드세요. 

# start, stop = map(int, input('두 수를 입력하세요').split())
# i = start

# while True:
#     if i > stop :
#         break 
#     if i % 10 != 3 :
#         print(i, end= ' ') 
#     i += 1

# for i in range(5):          # 5번 반복. 바깥쪽 루프는 세로 방향
#     for j in range(5):      # 5번 반복. 안쪽 루프는 가로 방향
#         print('j:', j, sep='', end=' ')    # j값 출력. end에 ' '를 지정하여 줄바꿈 대신 한 칸 띄움
#     print('i:', i, '\\n', sep='')    # i값 출력, 개행 문자 모양도 출력
#                                      # 가로 방향으로 숫자를 모두 출력한 뒤 다음 줄로 넘어감
#                                      # (print는 기본적으로 출력 후 다음 줄로 넘어감)

# for i in range(5):            # 5번 반복. 바깥쪽 루프는 세로 방향
#     for j in range(5):        # 5번 반복. 안쪽 루프는 가로 방향
#         print('*', end='')    # 별 출력. end에 ''를 지정하여 줄바꿈을 하지 않음
#     print()    # 가로 방향으로 별을 다 그린 뒤 다음 줄로 넘어감
#                # (print는 출력 후 기본적으로 다음 줄로 넘어감)

# 여기서는 바깥쪽 루프가 세로 방향, 안쪽 루프가 가로 방향을 처리한다는 점만 기억하면 됩니다.
# for i in range(5):        # 0부터 4까지 5번 반복. 세로 방향
#     for j in range(5):    # 0부터 4까지 5번 반복. 가로 방향
#         if j == i:                # 세로 방향 변수와 같을 때
#             print('*', end='')    # 별 출력. end에 ''를 지정하여 줄바꿈을 하지 않음
#         else:                     # 세로 방향 변수와 다를 때
#             print(' ', end='')    # 공백 출력. end에 ''를 지정하여 줄바꿈을 하지 않음
#     print()    

# height = int(input())
# for i in range(height):
#     for j in reversed(range(height)):
#         if j > i:
#             print(' ', end='')
#         else:
#             print('*', end='')
#     for j in range(height):
#         if j < i:
#             print('*', end='')
#     print()


# for num in range(101):
#     if num % 3 ==0 and num % 5 ==0 :
#         print('FizzBuzz')
#     elif num %3 == 0:
#         print('Fizz')
#     elif num %5 == 0:
#         print('Buzz')
#     else :
#         print(num)

# a, b = map(int, input().split())

# for num in range(a, b+1):
#     if num % 5 ==0 and num % 7 ==0 :
#         print('FizzBuzz')
#     elif num %5 == 0:
#         print('Fizz')
#     elif num %7 == 0:
#         print('Buzz')
#     else :
#         print(num)
 
# n = 6    # 육각형
# t.shape('turtle')
# t.color('#FF69B4')           # 펜의 색을 빨간색으로 설정
# t.begin_fill()          # 색칠할 영역 시작
# for i in range(n):      # n번 반복
#     t.forward(100)
#     t.right(360 / n)    # 360을 n으로 나누어서 외각을 구함
# t.end_fill() 


import turtle as t
 
# n = 500    # 원을 60번 그림
# t.shape('turtle')
# t.speed('fastest')      # 거북이 속도를 가장 빠르게 설정
# for i in range(n):
#     t.circle(120)       # 반지름이 120인 원을 그림
#     t.right(360 / n)    # 오른쪽으로 6도 회전

n, line = map(int, input().split())

t.shape('turtle')
t.speed('slow')

for i in range(n):
    t.forward(line)
    t.right((360 / n) * 2)
    t.forward(line)
    t.left(360 / n)

t.mainloop()

