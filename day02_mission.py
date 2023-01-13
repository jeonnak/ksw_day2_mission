"""
True나 False를 small과 green 변수에 할당한다.
if, else 문을 사용하여 작은 것(small)과 녹색(green)을
기준으로 체리, 완두콩, 수박, 호박(cherry, pea, watermelon, pumpkin)을
출력해보자
(예: 체리는 작고 녹색이 아니다, 완두콩은 작고 녹색이다, 수박은 크고 녹색이다,
호박은 크고 녹색이 아니다).
"""

import random

small = random.choice([True, False])
green = random.choice([True, False])

if small:
    if green:
        print("This is a pea.")
    else:
        print("This is a cherry.")

else:
    if green:
        print("This is a watermelon")
    else:
        print("This is a pumpkin")