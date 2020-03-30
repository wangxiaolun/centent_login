import os, sys
sys.path.append(os.getcwd())

from base.base_action import BaseAction

from selenium.webdriver.common.by import By


class LoginPage(BaseAction):

    # 登录
    login1 = By.ID, "com.tencent.wemeet.app:id/cc"
    # QQ
    qq_input = By.ID, "com.tencent.wemeet.app:id/by"
    # 密码
    password_login = By.XPATH, "text,使用账号密码登录"

    phone_number = By.XPATH, ["text,请输入手机号码"]
    # phone_number = By.XPATH, ["text,请输入手机号码", "resource-id,com.tencent.wemeet.app:id/fd"]
    send_password = By.ID, "com.tencent.wemeet.app:id/fb"

    # 登录
    login_data = By.ID, "com.tencent.wemeet.app:id/br"

    def __init__(self, driver):
        BaseAction.__init__(self, driver)

    def jump_login_page(self):
        self.click(self.login1)

    def login_qq(self):
        self.click(self.qq_input)

    def click_password_login(self):
        self.click(self.password_login)

    def send_phone(self, text):
        self.input_text(self.phone_number, text)

    def test_login(self):
        self.click(self.login_data)

    def password_send(self, text):
        try:
            self.input_text(self.send_password, text)
            return True
        except Exception:
            return False
