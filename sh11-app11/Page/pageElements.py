from selenium.webdriver.common.by import By


class PageElements:
    """首页"""
    # 我
    home_my_btn_id = (By.ID, "com.yunmall.lc:id/tab_me")

    """登录选择页面"""
    # 已有账号去登录
    choice_login_exits_account_id = (By.ID, "com.yunmall.lc:id/textView1")

    """登录页面"""
    # 账号
    login_account_id = (By.ID, "com.yunmall.lc:id/logon_account_textview")
    # 密码
    login_passwd_id = (By.ID, "com.yunmall.lc:id/logon_password_textview")
    # 登录按钮
    login_logon_btn_id = (By.ID, "com.yunmall.lc:id/logon_button")
    # 关闭登录页面按钮
    login_close_btn_id = (By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image")

    """个人中心页面"""
    # 我的收藏
    person_shoppingcart_id = (By.ID, "com.yunmall.lc:id/txt_my_shoppingcart")
    # 设置按钮
    person_setting_btn_id = (By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image")

    """设置页面"""
    # 退出按钮
    setting_logout_btn_id = (By.ID, "com.yunmall.lc:id/setting_logout")
    # 确认退出按钮
    setting_logout_acc_btn_id = (By.ID, "com.yunmall.lc:id/ymdialog_right_button")
    # 取消退出按钮
    setting_logout_dis_btn_id = (By.ID, "com.yunmall.lc:id/ymdialog_left_button")
