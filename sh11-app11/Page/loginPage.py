from Base.Base import Base
from Page.pageElements import PageElements


class LoginPage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def login(self, account, passwd):
        """
        登录
        :param account: 账号
        :param passwd: 密码
        :return:
        """

        # 输入账号
        self.send_element(PageElements.login_account_id, account)
        # 输入密码
        self.send_element(PageElements.login_passwd_id, passwd)
        # 点击登录按钮
        self.click_element(PageElements.login_logon_btn_id)

    def if_login_btn(self):
        """
        判断登录按钮是否存在
        :return: 存在返回True 不存在返回False
        """
        try:
            # 登录按钮
            self.get_element(PageElements.login_logon_btn_id)
            return True
        except:
            print("登录按钮不存在")
            return False

    def close_login_page(self):
        """关闭登录页面"""
        self.click_element(PageElements.login_close_btn_id)
