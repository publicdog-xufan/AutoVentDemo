import pytest
import os
import time
import datetime

def setup_function():
    print("setup_function 巴拉巴拉巴拉巴")


class Test_Case():
    print("test_class")

    def setup(self):
        print("setup: 每个用例开始前执行")

    def teardown(self):
        print("teardown: 每个用例结束后执行")

    def setup_class(self):
        print("setup_class：所有用例执行之前")

    def teardown_class(self):
        print("teardown_class：所有用例执行之前")

    def setup_method(self):
        print("setup_method:  每个用例开始前执行")

    def teardown_method(self):
        print("teardown_method:  每个用例结束后执行")

    def test_fun(self):
        print("test_fun")

    def test_one(self):
        print("正在执行----test_one")
        x = "this"
        assert 'h' in x

    # def test_two(self):
    #     print("正在执行----test_two")
    #     x = "hello"
    #     assert hasattr(x, 'check')

    def test_three(self):
        print("正在执行----test_three")
        a = "hello"
        b = "hello world"
        assert a in b


if __name__ == "__main__":
    # 获取当前时间戳
    timestamp = time.time()
    os.system(f'pytest --alluredir ./report/allure_raw/{timestamp}')


