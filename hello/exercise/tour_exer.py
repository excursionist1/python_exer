# -*-coding:utf-8-*-
# 항공 요금 계산 프로그램
flight_fee = 953200

#성인 요금
adult_fee = flight_fee * 3

#유아 요금은 성인 요금의 10%
infant_fee = 953200 * 0.1

total_fee = adult_fee + infant_fee

# round로 결과 값 소수점 자리 없앰
print(round(total_fee))