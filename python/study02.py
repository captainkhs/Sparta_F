#10미만의 자연수에서 3과 5의 배수를 구하면 3,5,6,9이다. 이들의 총합은 23이다.
#1000미만의 자연수에서 3,5의 배수의 총합을 구하라.

# num = int(input('1000미만의 수를 입력하세요'))
# sum = 0
# for i in range(num):
#     if i % 3 == 0 or i % 5 == 0:
#         print(i)
#         sum += i
# print(sum)

# m = int(input('총건수'))
# n = int(input('한페이지에 보여줄 게시물'))

# c = m // n  # 나누기 연산 후 소수 이하는 버리고 몫만 구함
# if m % n != 0 :
#     c += 1

# print(c)

# name = input('이름을 입력하세요').split(',')
# print(name)
# count = 0
# count1 = 0
# for i in name: 
# # print(i[-3])
#     if i[-3] == '김':
#         count += 1
#     if i[-3] == '이':
#         count1 += 1
# # 김 = name.count('김')
# # 이 = name.count('이')
# # print(count, count1)
# print('김씨는 : %s명 , 이씨는 : %s명' % (count, count1))

# 이재영 = name.count('이재영')
# print('이재영씨는 : %s번 반복됩니다.' %(이재영))

# ex_name = list(set(name))

# print('중복을 제거한 이름 : ')
# print(ex_name)


# ex_name.sort()
# ex_name.reverse()
# print('중복을 제거한 이름을 오름차순으로 정렬하면: ')
# print(ex_name)

# 0~9까지의 문자로 된 숫자를 입력 받았을 때, 이 입력 값이 0~9까지의 숫자가 각각 한 번 씩만 사용된 것인지 확인하는 함수를 구하시오.

# num = input('10자리 수를 입력하세요')
# numlen = len(str(num))
# num2 = list(num)
# result = True

# if numlen != 10:
#     print('입력한 수가 10자리가 아닙니다.')

# else:
#     for i in num2:
#         num2.remove(str(i))
#         if i in num2:
#             result = False
#             print(result)
#             break

# print (result, num2)
# num = input('뭐든지 입력하세요')
# num_list = list(num)
# ex_num_list = list(set(num_list))
# num_list.sort()
# ex_num_list.sort()

# print(num_list)
# print(ex_num_list)

# if num_list == ex_num_list:
#     print('True')

# else:
#     print('False')


a = str(input())
b = list(a)
for i in b:
    if b.count(i) == 1 :
        print(True)
        break
    else :
        print(False)
        break


    