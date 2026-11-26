##num1 = int(input('첫 번째 숫자 입력 : '))
##num2 = int(input('두 번째 숫자 입력 : '))
##print(f'num1 // num2 = {num1 // num2}')
##print(f'num1 % num2 = {num1 % num2}')
##print(f'num1 ** num2 = {num1 ** num2}')
##num1 = int(input('숫자를 입력하세요 : '))
##print(f'num1 // 4 = {num1 // 4}')
##print(f'num1 % 4 = {num1 % 4}')
##print(f'num1 ** 4 = {num1 ** 4}')
##num1 = int(input('몸무게(kg)를 입력하세요 : '))
##num2 = float(input('키(m)를 입력하세요 : '))
##print(f'BMI 지수는 : {(num1 / num2 ** 2):.2f}' )
##sec = int(input('초 입력 : '))
##min = sec // 60
##sec = sec % 60
##hour = min // 60
##min = min % 60
##day = hour // 24
##hour = hour % 24
##print(f'{day}일{hour}시간{min}분{sec}초')
price = int(input('물건의 가격을 입력합니다 : '))#400
result = 1000 - price 
obaeg = result // 500 #나눈 몫

print(result)
print(obaeg)


result = result % 500 #나머지
baegcheon = obaeg // 100
obaeg = obaeg % 100
osib = baegcheon // 50
baegcheon = baegcheon % 50
won = osib % 10
osib = osib // 10
print(baegcheon)
print(osib)
print(won)
