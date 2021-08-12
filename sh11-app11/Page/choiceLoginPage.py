from Base.Base import Base
from Page.pageElements import PageElements


class ChoiceLoginPage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_exits_account(self):
        """登录选择页点击已有账号去登录"""
        self.click_element(PageElements.choice_login_exits_account_id)
