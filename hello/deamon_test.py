import time

try:
    while True:

       time.sleep(60 * 10)
except KeyboardInterrupt as key:
    print('프로그램 종료')