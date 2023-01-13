"""
4-1 문제
1~10 사이의 숫자를 선택해서 secret 변수에 할당한다.
그리고 1~10 사이의 다른 숫자를 선택해서 guess 변수에 할당한다.
if, elif, else 문을 사용하여 guess 변수가 secret 변수보다 작으면
'too low', 크면 'too high', 일치하면 'just right'을 출력한다.
"""

import random

secret = random.randint(1, 10)
print(secret)
guess = random.randint(1, 10)
print(guess)

if guess < secret:
    print('too low')

elif guess > secret:
    print('too high')

else:
    'just right'