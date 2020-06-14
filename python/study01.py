

# def number():

#     try:
#         n=eval(input('입력 : '))

#         for i in range(2,n):

#             if num % i == 0:a
#                 print('정수')
#             else :
#                 print('소수')
#     except:
#         print('math error')

# number()

# 소수는 1과 자기 자신 외의 약수를 가지지 않는 1보다 큰 자연수
# 2,3,5,7,11,13,17,19,23,29 ....

#print(num.isdigit())

def prime_number(num):
    if num == 1:
        print('math_error')
        exit(-1)
    if num !=1 :
        for n in range(2, num):
            if num % n == 0:
                return False

    return True

num = input('숫자를 입력하세요')
if False == num.isdigit():
    print('math_error')
    exit(-1)

if prime_number(int(num)):
    print('True :  입력한 수' + num + '는 소수이다')

else:
    print('False :  입력한 수' + num + '는 소수가 아니다')
