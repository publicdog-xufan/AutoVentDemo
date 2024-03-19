import os
import time
# 获取当前时间戳
def start():
    timestamp = time.time()
    os.system(f'pytest --alluredir ../report/allure_raw/{timestamp}')
    os.system(f'allure generate ../report/allure_raw/{timestamp} -o ../report/HTML/{timestamp}')

start()