# 전국 도서관 표준데이터 정보
# 1. 열람좌석수가 가장 많은 상위 TOP5 도서관은?
# 2. 자료수(독서+연속간행물+비도서)가 가장 많은 상위 Top5 도서관

import csv
from collections import  Counter

seat_counter = Counter()
data_counter = Counter()


for line in reader:
