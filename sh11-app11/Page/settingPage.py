from Base.Base import Base
from Page.pageElements import PageElements


class SettingPage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def logout(self, tag=1):
        """
        退出
        :param tag: 1:退出 0:取消
        :return:
        """
        # 向上滑动页面
        self.swipe_screen()

        # 点击退出
        self.click_element(PageElements.setting_logout_btn_id)

        if tag:
            # 退出
            self.click_element(PageElements.setting_logout_acc_btn_id)
        else:
            # 取消
            self.click_element(PageElements.setting_logout_dis_btn_id)

