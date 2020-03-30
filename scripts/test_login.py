import os, sys, time
import allure
import pytest
sys.path.append(os.getcwd())
from page.login_page import LoginPage
from base.base_driver import init_driver
from base.base_yml import yml_data_with_filename_and_key


def data_with_key(key):
    return yml_data_with_filename_and_key("login_data", key)


class Test_Login:

    def setup(self):
        self.driver = init_driver()
        self.loginpage = LoginPage(self.driver)

    @allure.step(title='测试登录界面')
    @pytest.mark.parametrize("args", data_with_key("test_login"))
    def test_login(self, args):
        username = args['username']
        password = args['password']
        self.loginpage.jump_login_page()

        self.loginpage.login_qq()

        self.loginpage.click_password_login()
        time.sleep(2)

        allure.attach('输入用户名' + username, "")
        self.loginpage.send_phone(username)
        allure.attach('输入密码', password)
        self.loginpage.password_send(password)
        self.loginpage.test_login()