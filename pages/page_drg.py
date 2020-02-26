from selenium import webdriver
from common.base import Base
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from pages.merchantfuc import Merchant
from common.sf_xm import SF









class drg_pages(Base):

    # 001-003 登录元素
    username = ('id', 'login_name')
    password = ('id', 'password')
    buttom = ('xpath', '/html/body/div[1]/div[1]/div/div/div/form/div[5]/a')
    login_sucess_name = ('xpath','//*[@id="headerR"]/em')
    username_null = ('xpath','/html/body/div[1]/div[1]/div/div/div/form/div[3]')
    password_null = ('xpath','/html/body/div[1]/div[1]/div/div/div/form/div[3]')
    # 004 发包方管理页面
    user_control = ('xpath','//*[text()="用户管理"]')
    FBF_control = ('xpath','//li[text()="发包方管理"]')
    add_FBF = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/button')
    # 005 新增发包方(基础信息)
    short_name = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[2]/td[2]/div/input')
    link_name = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[3]/td[2]/div/input')
    email = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[4]/td[2]/div/input')
    address = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[5]/td[2]/div/input')
    phone_number = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[6]/td[2]/div/input')
    business_man = ('xpath','//table/tr[7]/td[2]/div')
    next = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/button')#下一步按钮通用
    #执照信息：
    upload_license = ('xpath','//*[@class="upload-file"]')
    business_license = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[3]/td[2]/div/input')
    registered_money = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[7]/td[2]/div/input')
    live = ('xpath','//label/span[1]/span')
    #结算账户
    open_province = ('xpath','//*[@placeholder="省份"]')
    province = ('xpath','/html/body/div[3]/div/div[1]/ul/li[13]/span')
    open_city = ('xpath','//*[@placeholder="城市"]')
    city = ('xpath','/html/body/div[4]/div/div[1]/ul/li[1]/span')
    open_bank = ('xpath','//*[@placeholder="请先选择开户城市"]')
    bank = ('xpath','/html/body/div[5]/div/div[1]/ul/li[4]/span')
    open_bank1 = ('xpath','//*[@placeholder="请先选择开户银行"]')
    bank1 = ('xpath','/html/body/div[6]/div/div[1]/ul/li[5]/span')
    open_name = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[6]/td[2]/div/input')
    bank_number = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[7]/td[2]/div/input')
    #开票信息
    ratepayer_number = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[3]/td[2]/div/input')
    work_telphone = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[5]/td[2]/div/input')
    invoice_content = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[6]/td[2]/div/input')
    work_business = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[7]/td[2]/div/input')
    platform = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[8]/td[2]/div/input')
    service = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[9]/td[2]/div/input')
    #新增商户成功检查点：纳税人识别号
    add_fbf_sucess = ('xpath','//*[@id="app"]/section/div[2]/section/div[3]/div[3]/table/tbody/tr[1]/td[3]/div')
    # 006 发包方简称查询
    check_shortname = ('xpath','//*[@placeholder="发包方简称"]')
    #查询按钮，查询栏通用
    check_button = ('xpath','//*[@id="app"]/section/div[2]/section/div[1]/form/div[8]/div/button')
    #验证查询成功
    check_shortname_sucess = ('xpath','//*[@id="app"]/section/div[2]/section/div[3]/div[3]/table/tbody/tr/td[2]/div')
    # 007 纳税人识别号查询
    check_ratepayer_number = ('xpath','//input[@placeholder=" 纳税人识别号"]')
    #验证点
    check_ratepayer_sucess = ('xpath','//*[@id="app"]/section/div[2]/section/div[3]/div[3]/table/tbody/tr/td[3]/div')
    # 008 跳转商户详情页面
    merchant_details = ('xpath','//*[@id="app"]/section/div[2]/section/div[3]/div[3]/table/tbody/tr[1]/td[9]/div/div/button[1]/span')
    #验证点
    merchant_details_sucess = ('xpath','//*[@id="app"]/section/div[2]/section/h2')
    # 009 跳转归属用户页面
    audit_status = ('xpath','//*[@placeholder="审核状态"]')
    the_audit_pass = ('xpath','/html/body/div[3]/div/div[1]/ul/li[3]/span')
    affiliation_user = ('xpath','//*[@id="app"]/section/div[2]/section/div[3]/div[3]/table/tbody/tr[4]/td[9]/div/div/button[3]')
    #验证点
    affiliation_user_sucess = ('xpath','//*[@id="app"]/section/nav/div/span[3]/span[1]/a')
    # 010 正常打开承揽方管理页面
    user_pages = ('xpath','//li[text()="承揽方管理"]')
    #验证点,承揽方管理
    user_pages_sucess = ('xpath','//*[@id="app"]/section/nav/div/span[2]/span[1]/a')
    # 011 打开承揽方详情页面
    user_details = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/div[3]/table/tbody/tr[1]/td[9]/div/button/span')
    user_details_sucess = ('xpath','//*[@id="app"]/section/div[2]/section/h2')
    # 012 新增任务
    add_task_1 = ('xpath','//span[text()="任务管理"]')
    add_task_2 = ('xpath','//li[text()="新增任务"]')
    add_task_3 = ('xpath','//table/tr[2]/td[2]/span/div[1]/div/div/div[1]/input')
    add_task_4 = ('xpath','//*[@placeholder="发包方简称"]')
    add_task_5 = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[2]/td[2]/span/div[2]/div/div[2]/div[1]/form/div[3]/div/button')
    add_task_5_1 = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[2]/td[2]/span/div[2]/div/div[2]/div[2]/div[3]/table/tbody/tr/td[1]/div/label/span/span')
    add_task_6 = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[2]/td[2]/span/div[2]/div/div[3]/div/button[2]')
    add_task_7 = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[3]/td[2]/div/input')
    add_task_8 = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[4]/td[2]/div[1]/label[6]/span[1]/span')
    add_task_9 = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[5]/td[2]/div[1]/label[5]/span[1]/span')
    add_task_10 = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[6]/td[2]/div/input')
    add_task_11 = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[7]/td[2]/div[1]/label[3]/span[1]/span')
    add_task_12 = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[8]/td[2]/div/input')
    add_task_13 = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[9]/td[2]/div/input')
    add_task_14 = ('xpath','//*[@id="app"]/section/div[2]/section/form/table/tr[15]/td[2]/div/textarea')
    add_task_15 = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/button')
    add_task_16 = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/div[3]/table/tbody/tr[1]/td[3]/div')
    # 013 跳转任务详情页面
    task_countorl = ('xpath','//li[text()="任务管理"]')
    task_details = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/div[3]/table/tbody/tr[1]/td[9]/div/button[1]/span')
    task_details_sucess = ('xpath','//*[@id="app"]/section/div[2]/section/h2')
    # 014 跳转报名信息
    task_information = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/div[3]/table/tbody/tr[1]/td[9]/div/button[2]/span')
    task_information_sucess = ('xpath','//*[@id="app"]/section/nav/div/span[3]/span[1]/a')
    # 015 关闭任务
    task_close3 = ('xpath','//*[@id="app"]/section/div[2]/section/div[1]/form/div[4]/div/div/div[1]/input')
    task_close4 = ('xpath','/html/body/div[3]/div/div[1]/ul/li[1]/span')
    task_close5 = ('xpath','//*[@id="app"]/section/div[2]/section/div[1]/form/div[6]/div/button')
    task_close6 = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/div[3]/table/tbody/tr[1]/td[3]/div')
    task_close7 = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/div[3]/table/tbody/tr[1]/td[9]/div/button[3]/span')
    task_close8 = ('xpath','/html/body/div[4]/div/div[3]/button[2]')
    task_close9 = ('xpath','//li[text()="新增任务"]')
    task_close10 = ('xpath','//li[text()="任务管理"]')

    task_close11 = ('xpath','//*[@id="app"]/section/div[2]/section/div[1]/form/div[3]/div/div/input')
    task_close12 = ('xpath','//*[@id="app"]/section/div[2]/section/div[1]/form/div[6]/div/button')
    task_state = ('xpath', '//*[@id="app"]/section/div[2]/section/div[2]/div[3]/table/tbody/tr[1]/td[7]/div/span')
    task_close_sucess = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/div[3]/table/tbody/tr/td[7]/div/span')
    # 016 跳转付款记录页面
    pay1 = ('xpath','//*[text()="发包方付款管理"]')
    pay2 = ('xpath','//*[@id="menu"]/li[3]/ul/li')
    pay_sucess = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/ul/li[1]/span')

    # 017 跳转充值详情页面
    pay_details1 = ('xpath','//*[@placeholder="选择开始时间"]')
    pay_details2 = ('xpath','//*[@id="app"]/section/div[2]/section/div[1]/form/div[8]/div/button')
    pay_details3 = ('xpath','//*[@id="app"]/section/div[2]/section/div[3]/div[3]/table/tbody/tr[1]/td[10]/div/button/span')
    pay_details_sucess = ('xpath','//*[@id="app"]/section/div[2]/section/h2')

    # 018  确认充值申请
    add_pay1 = ('xpath','//*[@placeholder="选择开始时间"]')
    add_pay2 = ('xpath','//*[@placeholder="付款状态"]')
    add_pay3 = ('xpath','//*[@class="el-select-dropdown__item hover"]/span')
    add_pay4 = ('xpath','//*[@id="app"]/section/div[2]/section/div[1]/form/div[8]/div/button')
    #判断是否详情，有执行后面操作，没有提示：暂无充值记录
    no_add_pay1 = ('xpath','//*[@id="app"]/section/div[2]/section/div[3]/div[3]/div/span')
    add_pay5 = ('xpath','//*[@id="app"]/section/div[2]/section/div[3]/div[3]/table/tbody/tr[1]/td[10]/div/button/span')
    add_pay6 = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/button[1]')
    add_pay7 = ('xpath','//*[@placeholder="选择日期时间"]')
    add_pay8 = ('xpath','//*[text()="此刻"]')
    add_pay9 = ('xpath','//*[@id="app"]/section/div[2]/section/div[5]/div/div[3]/div/button')
    add_pay_sucess = ('xpath','//*[@id="app"]/section/div[2]/section/table/tr[2]/td[2]')
    # 019 充值订单驳回
    add_payfail1 = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/button[2]')
    add_payfail2 = ('xpath','//*[@id="app"]/section/div[2]/section/div[4]/div/div[3]/div/button[2]')
    add_payfail_sucess = ('xpath','//*[@id="app"]/section/div[2]/section/table/tr[2]/td[2]')

    # 020 付款记录页面
    loan_manage = ('xpath','//*[@id="menu"]/li[4]/div/span')
    loan_record = ('xpath','//*[@id="menu"]/li[4]/ul/li[1]')
    loan_record_sucess = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/ul/li[1]/span')
    # 021 放款记录详情页面
    loan_details1 = ('xpath','//*[@id="menu"]/li[4]/div/span')
    loan_details2 = ('xpath','//*[@id="menu"]/li[4]/ul/li[1]')
    loan_details3 = ('xpath','//*[@id="app"]/section/div[2]/section/div[1]/form/div[2]/div/div/input')
    loan_details4 = ('xpath','//*[text()="查询"]')
    loan_details5 = ('xpath','//*[@id="app"]/section/div[2]/section/div[3]/div[3]/table/tbody/tr[1]/td[12]/div/button[1]')
    loan_details_sucess = ('xpath','//*[@id="app"]/section/div[2]/section/h2')
    # 022 上传完税证明
    upload_prove4 = ('xpath','//*[@placeholder="放款状态"]')
    upload_prove5 = ('xpath','/html/body/div[3]/div/div[1]/ul/li[1]/span')
    upload_prove6 = ('xpath','//*[text()="查询"]')
    upload_prove7 = ('xpath','//*[@id="app"]/section/div[2]/section/div[3]/div[3]/table/tbody/tr[1]/td[12]/div/label/input')
    upload_prove_sucess = ('xpath','//*[@id="app"]/section/div[2]/section/div[3]/div[3]/table/tbody/tr[1]/td[12]/div/label')
    # 023 批量放款记录页面
    banth_loan1 = ('xpath','//*[@id="menu"]/li[4]/div/span')
    banth_loan2 = ('xpath','//*[@id="menu"]/li[4]/ul/li[2]')
    banth_loan_sucess = ('xpath','//*[@id="app"]/section/nav/div/span[3]/span[1]')
    # 024 批次放款记录
    banth_loan3 = ('xpath', '//*[@id="app"]/section/div[2]/section/div[1]/form/div[1]/div/div/input')
    banth_loan4 = ('xpath', '//*[@id="app"]/section/div[2]/section/div[1]/form/div[6]/div/button')
    banth_loan5 = ('xpath', '//*[@id="app"]/section/div[2]/section/div[2]/div[3]/table/tbody/tr[1]/td[10]/div/button[1]/span')
    banth_loan_sucess1 = ('xpath', '//*[@id="app"]/section/nav/div/span[3]/span[1]/a')
    #025 通过批次号查询放款订单
    check_banth_loan3 = ('xpath','//*[@id="app"]/section/div[2]/section/div[1]/form/div[1]/div/div/input')
    check_banth_loan3_1 = ('xpath','//*[@id="app"]/section/div[2]/section/div[1]/form/div[6]/div/button')
    check_banth_loan4_number = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/div[3]/table/tbody/tr[1]/td[4]/div')
    check_banth_loan5 = ('xpath','//*[@id="app"]/section/div[2]/section/div[1]/form/div[3]/div/div/input')
    check_banth_loan6 = ('xpath','//*[@id="app"]/section/div[2]/section/div[1]/form/div[6]/div/button')
    check_banth_loan_sucess2 = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/div[3]/table/tbody/tr[1]/td[4]/div')
    #026 赏金记录页面
    money1 = ('xpath','//*[@id="menu"]/li[5]/div/span')
    money2 = ('xpath','//*[@id="menu"]/li[5]/ul/li')
    money_sucess = ('xpath','//*[@id="app"]/section/nav/div/span[2]/span[1]/a')

    #027 赏金记录详情
    cancel_start_time = ('xpath','//*[@id="app"]/section/div[2]/section/div[1]/form/div[2]/div/div/input')
    query = ('xpath','//*[@id="app"]/section/div[2]/section/div[1]/form/div[8]/div/button[1]/span')
    no_record = ('xpath','//*[@id="app"]/section/div[2]/section/div[3]/div[3]/div/span')
    bounty_details = ('xpath','//*[@id="app"]/section/div[2]/section/div[3]/div[3]/table/tbody/tr/td[9]/div/button/span')
    bounty_details_sucess = ('xpath','//*[@id="app"]/section/div[2]/section/h2')

    # 028 赏金单号查询
    bounty_number = ('xpath','//*[@id="app"]/section/div[2]/section/div[3]/div[3]/table/tbody/tr/td[3]/div')
    bounty_number1 = ('xpath','//*[@id="app"]/section/div[2]/section/div[1]/form/div[4]/div/div/input')
    bounty_number_sucess = ('xpath','//*[@id="app"]/section/div[2]/section/div[3]/div[3]/table/tbody/tr/td[1]/div/div')

    # 029 销项发票管理
    invoice1 = ('xpath','//*[text()="财务管理"]')
    invoice2 = ('xpath','//li[text()="销项发票管理"]')
    invoice2_1 = ('xpath','//*[@id="app"]/section/div[2]/section/div[1]/form/div[1]/div/div/input')
    invoice2_2 = ('xpath','//*[@id="app"]/section/div[2]/section/div[1]/form/div[5]/div/div/div[1]/input')

    #状态为待处理
    invoice2_3_1 = ('xpath','/html/body/div[4]/div/div[1]/ul/li[2]/span')
    #状态为已处理
    invoice2_3_2 = ('xpath','/html/body/div[5]/div/div[1]/ul/li[1]')

    invoice2_4 = ('xpath','//*[@id="app"]/section/div[2]/section/div[1]/form/div[6]/div/button/span')
    #查询到暂无数据1.商户端判断是否有充值成功记录，没有的话提交新增充值2.运营端确认充值3.商户端提交开票申请
    #有的话直接提交开票申请
    invoice3 = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/div[3]/div/span')
    #查询到有数据，处理申请发票
    #点击申请详情
    invoice4 = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/div[3]/table/tbody/tr/td[8]/div/button/span')
    #点击发票信息设置
    invoice5 = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/div[1]/div/div[1]/div/div[4]')
    #获取税价合计金额
    invoice_money = ('xpath', '//*[@id="app"]/section/div[2]/section/table/tr[2]/td[3]')
    #5_1点击已开发票
    invoice5_1 = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/div[1]/div/div[1]/div/div[5]')
    # #5_2判断是新增发票还是填写快递单号
    invoice5_2 = ('xpath','//*[@id="app"]/section/div[2]/section/div[5]/button/span')
    #点击新增一张发票
    invoice6 = ('xpath','//*[@id="app"]/section/div[2]/section/div[3]/button/span')
    #已开发票下的新增一张发票
    invoice6_1 = ('xpath','//*[@id="app"]/section/div[2]/section/div[5]/button/span')
    #输入开票日期
    invoice7 = ('xpath','//*[@id="app"]/section/div[2]/section/div[5]/div/div[2]/form/table/tr[1]/td[2]/div/input')
    #输入发票代码
    invoice8 = ('xpath','//*[@id="app"]/section/div[2]/section/div[5]/div/div[2]/form/table/tr[3]/td[2]/div/input')
    #输入发票号码
    invoice9 = ('xpath','//*[@id="app"]/section/div[2]/section/div[5]/div/div[2]/form/table/tr[4]/td[2]/div/input')
    #输入税价合计金额
    invoice10 = ('xpath','//*[@id="app"]/section/div[2]/section/div[5]/div/div[2]/form/table/tr[6]/td[2]/div/input')
    #输入税率
    invoice11 = ('xpath','//*[@id="app"]/section/div[2]/section/div[5]/div/div[2]/form/table/tr[7]/td[2]/div/input')
    #点击确认
    invoice12 = ('xpath','//*[@id="app"]/section/div[2]/section/div[5]/div/div[3]/div/button/span')
    #点击填写快递单号
    invoice13 = ('xpath','//*[@id="app"]/section/div[2]/section/div[5]/button/span')
    #输入快递单号
    invoice14 = ('xpath','//*[@id="app"]/section/div[2]/section/div[8]/div/div[2]/table/tr[2]/td[2]/div/input')
    #点击确认
    invoice15 = ('xpath','//*[@id="app"]/section/div[2]/section/div[8]/div/div[3]/div/button/span')
    #判断申请状态为已处理
    invoice_sucess = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/div[3]/table/tbody/tr/td[7]/div')

    #030 已处理发票详情页
    #点击已开发票
    finish_invoice1 = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/div[3]/table/tbody/tr[1]/td[8]/div/button[2]/span')
    #点击详情
    finish_invoice2 = ('xpath','//*[@id="app"]/section/div[2]/section/div[3]/div[3]/table/tbody/tr/td[11]/div/button/span')
    #开票详情
    finish_invoice_sucesee = ('xpath','//*[@id="app"]/section/div[2]/section/h2')
    #判断是否有已处理记录
    norecord1 = ('xpath', '//*[@id="app"]/section/div[2]/section/div[2]/div[3]/div/span')

    #031 发包方钱包
    FBF_wallet1 = ('xpath','//*[@id="menu"]/li[6]/div/span')
    FBF_wallet2 = ('xpath','//*[@id="menu"]/li[6]/ul/li[2]')
    FBF_wallet3 = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/div[2]/table/thead/tr/th[2]/div')
    #032 详情按钮
    FBF_wallet4 = ('xpath', '//*[@id="app"]/section/div[2]/section/div[2]/div[3]/table/tbody/tr[1]/td[8]/div/button/span')
    #验证
    FBF_wallet5 = ('xpath','//*[@id="app"]/section/nav/div/span[3]/span[1]')

    # 033  承揽方钱包
    CLF_wallet1 = ('xpath','//*[@id="menu"]/li[6]/div/span')
    CLF_wallet2 = ('xpath','//*[@id="menu"]/li[6]/ul/li[3]')
    CLF_wallet3 = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/div[2]/table/thead/tr/th[2]/div')
    #034  承揽方钱包详情页
    CLF_wallet4 = ('xpath', '//*[@id="app"]/section/div[2]/section/div[2]/div[3]/table/tbody/tr[1]/td[7]/div/button/span')
    CLF_wallet5 = ('xpath', '//*[@id="app"]/section/nav/div/span[3]/span[1]/a')

    #035 打开平台钱包
    PT_wallet1 = ('xpath','//*[@id="menu"]/li[6]/div/span')
    PT_wallet2 = ('xpath','//*[@id="menu"]/li[6]/ul/li[4]')
    PT_wallet3 = ('xpath','//*[@id="app"]/section/div[2]/section/h2')
    #036 打开通道钱包页面
    TD_wallet1 = ('xpath','//*[@id="menu"]/li[6]/div/span')
    TD_wallet2 = ('xpath','//*[@id="menu"]/li[6]/ul/li[5]')
    TD_wallet3 = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/div[2]/table/thead/tr/th[2]/div')
    #037 商户账单
    merchants_bills1 = ('xpath','//*[@id="menu"]/li[7]/div/span')
    merchants_bills2 = ('xpath','//*[@id="menu"]/li[7]/ul/li[1]')
    merchants_bills3 = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/div[2]/table/thead/tr/th[2]/div')
    #038 通道账单
    TD_bills1 = ('xpath','//*[@id="menu"]/li[7]/div/span')
    TD_bills2 = ('xpath','//*[@id="menu"]/li[7]/ul/li[2]')
    TD_bills3 = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/div[2]/table/thead/tr/th[2]/div')
    # 039 打开我的账户页面
    account_management1 = ('xpath','//*[@id="menu"]/li[9]/div/span')
    account_management2 = ('xpath','//*[@id="menu"]/li[9]/ul/li[1]')
    account_management3 = ('xpath','//*[@id="app"]/section/div[2]/section/h2')

    #040 账户安全
    account_security1 = ('xpath','//*[@id="menu"]/li[9]/div/span')
    account_security2 = ('xpath','//*[@id="menu"]/li[9]/ul/li[2]')
    account_security3 = ('xpath','//*[@id="app"]/section/div[2]/section/div[1]/table/tr[1]/td')
    # 041 打开重新支付密码页面
    account_security4 = ('xpath','//*[@id="app"]/section/div[2]/section/div[1]/table/tr[2]/td[2]/button/span')
    account_security5 = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/div/div[1]/span')
    # 042 打开修改登录密码页面
    account_security6 = ('xpath','//*[@id="app"]/section/div[2]/section/div[1]/table/tr[3]/td[2]/button/span')
    account_security7 = ('xpath','//*[@id="app"]/section/div[2]/section/div[3]/div/div[1]/span')
    # 043 打开重新设置手机号码页面
    account_security8 = ('xpath','//*[@id="app"]/section/div[2]/section/div[1]/table/tr[4]/td[2]/button/span')
    account_security9 = ('xpath','//*[@id="app"]/section/div[2]/section/div[4]/div/div[1]/span')

    # 044 打开员工管理页面
    account_security10 = ('xpath','//*[@id="menu"]/li[9]/ul/li[3]')
    account_security11 = ('xpath','//*[@id="app"]/section/div[2]/section/div[3]/div[2]/table/thead/tr/th[2]/div')

    #45 新增员工
    add_staff1 = ('xpath','//*[@id="app"]/section/div[2]/section/div[2]/button/span')
    add_staff2 = ('xpath','//*[@id="app"]/section/div[2]/section/div[5]/div/div[2]/form/div[1]/div/div/input')
    add_staff3 = ('xpath','//*[@id="app"]/section/div[2]/section/div[5]/div/div[2]/form/div[2]/div/div/input')
    add_staff4 = ('xpath','//*[@id="app"]/section/div[2]/section/div[5]/div/div[2]/form/div[3]/div/div/input')
    add_staff5 = ('xpath','//*[@id="app"]/section/div[2]/section/div[5]/div/div[2]/form/div[4]/div/div/input')
    add_staff6 = ('xpath','//*[@id="app"]/section/div[2]/section/div[5]/div/div[2]/form/div[5]/div/div/div/div/div[1]/input')
    add_staff8 = ('xpath','//*[@id="app"]/section/div[2]/section/div[5]/div/div[3]/div/button[2]')
    add_staff9 = ('xpath','//*[@id="app"]/section/div[2]/section/div[3]/div[3]/table/tbody/tr[1]/td[3]/div')
    # 46 修改员工密码
    reset_staff_password1 = ('xpath','//*[@id="app"]/section/div[2]/section/div[3]/div[3]/table/tbody/tr[1]/td[8]/div/button[1]/span')
    reset_staff_password2 = ('xpath','//*[@id="app"]/section/div[2]/section/div[5]/div/div[2]/form/div[2]/div/div/input')
    reset_staff_password3 = ('xpath','//*[@id="app"]/section/div[2]/section/div[5]/div/div[2]/form/div[3]/div/div/input')
    reset_staff_password4 = ('xpath','//*[@id="app"]/section/div[2]/section/div[5]/div/div[3]/div/button[2]')
    reset_staff_password5 = ('xpath','/html/body/div[3]/div/p')

    #047 修改员工姓名
    reset_staff_name1 = ('xpath','//*[@id="app"]/section/div[2]/section/div[3]/div[3]/table/tbody/tr[1]/td[8]/div/button[2]/span')
    reset_staff_name2 = ('xpath','//*[@id="app"]/section/div[2]/section/div[5]/div/div[2]/form/div[2]/div/div/input')
    reset_staff_name3 = ('xpath','//*[@id="app"]/section/div[2]/section/div[5]/div/div[3]/div/button[2]')
    reset_staff_name4 = ('xpath','//*[@id="app"]/section/div[2]/section/div[3]/div[3]/table/tbody/tr[1]/td[3]/div')

    #048 删除员工
    delete_staff1 = ('xpath','//*[@id="app"]/section/div[2]/section/div[3]/div[3]/table/tbody/tr[1]/td[8]/div/button[3]/span')
    delete_staff2 = ('xpath','/html/body/div[3]/div/div[3]/button[2]')
    delete_staff3 = ('xpath','/html/body/div[4]/div/p')

    # 049 打开员工角色页面
    the_role1 = ('xpath','//*[@id="app"]/section/div[2]/section/div[1]/a[2]')
    the_role2 = ('xpath','//*[@id="app"]/section/div[2]/section/div[3]/div[2]/table/thead/tr/th[2]/div')

    # 50 打开系统设置
    sys_set1 = ('xpath','//*[@id="menu"]/li[10]/div/span')
    sys_set2 = ('xpath','//*[@id="menu"]/li[10]/ul/li[1]')
    sys_set3 = ('xpath','//*[@id="app"]/section/div[2]/section/div/table/tr[1]/td')

    #051 打开客服信息页面
    sys_set4 = ('xpath','//*[@id="app"]/section/div[2]/section/div/table/tr[2]/td[2]/button')
    sys_set5 = ('xpath','//*[@id="app"]/section/div[2]/section/h2')

    #052 打开发票类目页面
    sys_set6 = ('xpath', '//*[@id="app"]/section/div[2]/section/div/table/tr[3]/td[2]/button')
    sys_set7 = ('xpath', '//*[@id="app"]/section/div[2]/section/div[2]/button/span')

    #053 打开发票销方信息
    sys_set8 = ('xpath', '//*[@id="app"]/section/div[2]/section/div/table/tr[4]/td[2]/button')
    sys_set9 = ('xpath', '//*[@id="app"]/section/div[2]/section/table/tr[1]/td')
    #054 打开基础数据页面
    sys_set10 = ('xpath', '//*[@id="app"]/section/div[2]/section/div/table/tr[5]/td[2]/button')
    sys_set11 = ('xpath', '//*[@id="app"]/section/div[2]/section/div[2]/button/span')
    # 55 打开通道管理页面
    sys_set12 = ('xpath', '//*[@id="menu"]/li[10]/ul/li[2]')
    sys_set13 = ('xpath', '//*[@id="app"]/section/div[2]/section/div[2]/div[2]/table/thead/tr/th[2]/div')
    # 56 打开通道详情页面
    sys_set14 = ('xpath', '//*[@id="app"]/section/div[2]/section/div[2]/div[3]/table/tbody/tr/td[9]/div/button/span')
    sys_set15 = ('xpath', '//*[@id="app"]/section/div[2]/section/h2')
    # 57 打开公告管理页面
    sys_set16 = ('xpath', '//*[@id="menu"]/li[10]/ul/li[3]')
    sys_set17 = ('xpath', '//*[@id="app"]/section/div[2]/section/div[2]/button/span')

    # 58 新增公告
    sys_set18 = ('xpath', '//*[@id="app"]/section/div[2]/section/div[5]/div/div[2]/form/div/div[1]/div/div/input')
    sys_set19 = ('xpath', '//*[@id="app"]/section/div[2]/section/div[5]/div/div[2]/form/div/div[2]/div/div/textarea')

    sys_set20 = ('xpath', '//*[@id="app"]/section/div[2]/section/div[5]/div/div[2]/form/div/div[3]/div/div/label[2]/span[1]/span')
    sys_set21 = ('xpath', '//*[@id="app"]/section/div[2]/section/div[5]/div/div[3]/div/button[2]')
    sys_set22 = ('xpath', '//*[@id="app"]/section/div[2]/section/div[3]/div[3]/table/tbody/tr/td[2]/div')
    # 059 删除公告

    sys_set23 = ('xpath', '//*[@id="app"]/section/div[2]/section/div[3]/div[3]/table/tbody/tr[1]/td[6]/div/button[2]/span')

    sys_set24 = ('xpath', '/html/body/div[3]/div/div[3]/button[2]')
    sys_set25 = ('xpath', '/html/body/div[4]/div/p')














    def __init__(self,driver):

        self.driver = driver
        self.timeout = 10
        self.t = 1
        self.MC = Merchant(driver)


    #  登录
    def login(self,user='spman_admin',psd='111111'):
        self.driver.get('https://spman.shb02.net/admin/login')
        self.sendKeys(self.username,user)
        self.sendKeys(self.password,psd)
        self.click(self.buttom)
    # ----------判断登录是否成功-------------------------------001
    def get_login_name(self,text):
        result = self.is_text(self.login_sucess_name,text)
        return result

    # ------------判断用户名是否为空----------------------------002
    def get_username_null(self,text):
        result = self.is_text(self.username_null, text)
        return result

    # 003 判断密码是否为空-------------------------------------003
    def get_password_null(self,text):
        result = self.is_text(self.password_null, text)
        return result

    # 004 打开发包方管理页面------------------------------------004
    def FBF_page(self):
        self.login()
        self.click(self.user_control)
        time.sleep(1)
        self.click(self.FBF_control)
    def FBF_page_sucess(self,text):
        result = self.is_text(self.add_FBF,text)
        return result

    # 005 新增发包方--------------------------------------------005
    def addFbf(self,shortname,linkname,email,address,phone,businesslicense,
               registeredmoney,openname,banknumber,ratepayernumber,worktelphone,
               invoicecontent,workbusiness,platform,service):
        self.FBF_page()
        self.click(self.add_FBF)
        #基础信息，输入发包方简称、联系人、邮箱，办公地址、手机号、对接商务（可为空），点击下一步
        self.sendKeys(self.short_name,shortname)
        self.sendKeys(self.link_name,linkname)
        self.sendKeys(self.email,email)
        self.sendKeys(self.address,address)
        self.sendKeys(self.phone_number,phone)
        self.click(self.next)
        #营业执照，上传营业执照，重新输入营业执照号、法人姓名、点击直播，点击下一步
        self.sendKeys(self.upload_license,'C:\\Users\\a\\Desktop\\新建文件夹\\GELAIDI.jpg')
        time.sleep(3)
        self.clear(self.business_license)
        time.sleep(1)
        self.sendKeys(self.business_license,businesslicense)
        time.sleep(1)
        self.sendKeys(self.registered_money,registeredmoney)
        self.click(self.live)
        self.click(self.next)
        #结算账户，点击省、点击开户省、点击开户城市、点击城市、点击开户银行、点击银行、输入开户人、输入银行卡号、点击下一步
        self.click(self.open_province)
        time.sleep(2)
        self.click(self.province)
        time.sleep(3)
        self.click(self.open_city)
        time.sleep(2)
        self.click(self.city)
        time.sleep(3)
        self.click(self.open_bank)
        time.sleep(2)
        self.click(self.bank)
        time.sleep(2)
        self.click(self.open_bank1)
        time.sleep(2)
        self.click(self.bank1)
        time.sleep(1)
        self.sendKeys(self.open_name,openname)
        self.sendKeys(self.bank_number,banknumber)
        self.click(self.next)

        #开票信息，输入纳税人识别号、单位电话、发票内容、从事业务、业务平台、服务描述、点击下一步
        self.clear(self.ratepayer_number)
        self.sendKeys(self.ratepayer_number,ratepayernumber)
        self.sendKeys(self.work_telphone,worktelphone)
        self.sendKeys(self.invoice_content,invoicecontent)
        self.sendKeys(self.work_business,workbusiness)
        self.sendKeys(self.platform,platform)
        self.sendKeys(self.service,service)
        self.click(self.next)
    #判断发包方是否新增成功
    def addFbf_sucess(self,text):
        self.FBF_page()
        result = self.is_text(self.add_fbf_sucess,text)
        return result

    # 006 发包方简称查询-------------------------------------------006
    def checkShortname(self,name):
        self.FBF_page()
        self.sendKeys(self.check_shortname,name)
        self.click(self.check_button)
    def checkShortnameSucess(self,text):
        result = self.is_text(self.check_shortname_sucess,text)
        return result

    # -----------------纳税识别号查询----------------------------007
    def checkRatepayerNumber(self,number):
        self.FBF_page()
        self.sendKeys(self.check_ratepayer_number,number)
        self.click(self.check_button)
    def checkRatepayerSucess(self,text):
        result = self.is_text(self.check_ratepayer_sucess, text)
        return result

    # ---------------------跳转商户详情页面-----------------------------008
    def merchantdetails(self):
        self.FBF_page()
        time.sleep(1)
        self.click(self.merchant_details)
    def merchantDetailsSucess(self,text):
        result = self.is_text(self.merchant_details_sucess, text)
        return result

    # --------------跳转归属用户页面-------------------------------------009
    def affiliationUser(self):
        self.FBF_page()
        self.click(self.audit_status)
        time.sleep(1)
        self.click(self.the_audit_pass)
        self.click(self.check_button)
        self.click(self.affiliation_user)
    def affiliationUserSucess(self,text):
        result = self.is_text(self.affiliation_user_sucess, text)
        return result

    # --------------承揽方管理页面---------------------------------------010
    def userPages(self):
        self.login()
        self.click(self.user_control)
        time.sleep(1)
        self.click(self.user_pages)
    def userPagesSucess(self,text):
        result = self.is_text(self.user_pages_sucess,text)
        return result

    # -----------承揽方详情页面-----------------------------------------------011
    def userDetails(self):
        self.login()
        self.click(self.user_control)
        time.sleep(1)
        self.click(self.user_pages)
        self.click(self.user_details)
    def userDetailsSucess(self,text):
        result = self.is_text(self.user_details_sucess,text)
        return result

    # ---------------新增任务:1.点击任务管理、2.点击新增任务、3.点击发包方、
    # 4.输入发包方简称、5.点击查询、6.点击确定、7.输入任务标题、8.点击标签、
    # 9.点击内容主题#10.输入赏金、11.点击平台、12.输入招募人数、13.输入工作地点、14.输入任务描述、15.点击确认--------012

    def addTask(self,shortname,taskname,money,number,workpalce,taskdetails):
        self.login()
        self.click(self.add_task_1)
        time.sleep(1)
        self.click(self.add_task_2)
        self.click(self.add_task_3)
        self.sendKeys(self.add_task_4,shortname)
        self.click(self.add_task_5)
        time.sleep(1)
        self.click(self.add_task_5_1)
        time.sleep(1)
        self.click(self.add_task_6)
        time.sleep(1)
        self.sendKeys(self.add_task_7,taskname)
        self.click(self.add_task_8)
        self.click(self.add_task_9)
        self.sendKeys(self.add_task_10, money)
        self.click(self.add_task_11)
        self.sendKeys(self.add_task_12, number)
        self.sendKeys(self.add_task_13, workpalce)
        self.sendKeys(self.add_task_14, taskdetails)
        self.click(self.add_task_15)
    def addTaskSucess(self,text):
        result = self.is_text(self.add_task_16,text)
        return result

    # ------------跳转任务详情页面----------------------------------013
    def taskDetails(self):
        self.login()
        self.click(self.add_task_1)
        time.sleep(1)
        self.click(self.task_countorl)
        self.click(self.task_details)
    def taskDetailsSucess(self,text):
        result = self.is_text(self.task_details_sucess,text)
        return result

    #---------跳转报名信息页面------------------------------------------014
    def taskInformation(self):
        self.login()
        self.click(self.add_task_1)
        time.sleep(1)
        self.click(self.task_countorl)
        time.sleep(1)
        self.click(self.task_information)
    def taskInformationSucess(self,text):
        result = self.is_text(self.task_information_sucess,text)
        return result

    #  --------关闭任务---------------------------------------------------015
    #1.点击任务管理、2.点击任务管理、3.点击任务状态、4.点击已发布、
    # 5.点击查询、（判断：是否有已发布任务，有获取第一个任务标题，执行后面的步骤。如果是没有任务的情况：新增一个任务成功后，
    # 从第三个步骤开始执行后面的步骤。）
    # 6.获取第一个任务标题、7.点击第一个任务关闭、8.点击确定、9.点击新增任务、10点击任务管理、11.输入任务标题、12.点击查询
    def taskClose(self,shortname,taskname,money,number,workpalce,taskdetails,text):
        self.login()
        self.click(self.add_task_1)
        time.sleep(1)
        self.click(self.task_countorl)
        self.click(self.task_close3)
        time.sleep(2)
        self.click(self.task_close4)
        self.click(self.task_close5)
        #如果查询出来有已发布的任务
        result = self.is_text(self.task_state,text)
        if result == True:
            taskname1 = self.findEle(self.task_close6).text
            self.click(self.task_close7)
            self.click(self.task_close8)
            self.login()
            self.click(self.add_task_1)
            time.sleep(1)
            self.click(self.task_countorl)
            self.sendKeys(self.task_close11,taskname1)
            self.click(self.task_close12)
        else:
            self.addTask(shortname,taskname,money,number,workpalce,taskdetails)
            taskname1 = self.findEle(self.task_close6).text
            self.sendKeys(self.task_close11, taskname1)
            self.click(self.task_close5)
            self.click(self.task_close7)
            self.click(self.task_close8)

    def taskCloseSucess(self,text):
        result = self.is_text(self.task_close_sucess,text)
        return result

    # -----------跳转付款记录页面---------------------------------------016
    def pay(self):
        self.login()
        self.click(self.pay1)
        time.sleep(1)
        self.click(self.pay2)
    def paySucess(self,text):
        result = self.is_text(self.pay_sucess,text)
        return result

    # ---跳转充值详情页面,1.点击清除时间、2.点击查询、3.点击详情---------------------------017
    def payDetails(self):
        self.pay()
        self.clear(self.pay_details1)
        self.click(self.pay_details2)
        time.sleep(1)
        self.click(self.pay_details3)
    def payDetailsSucess(self,text):
        result = self.is_text(self.pay_details_sucess,text)
        return result

    # ---确认充值申请,付款记录--1.清除开始时间、2.点击付款状态3.点击等待确认4.点击查询5.点击详情6.点击手动确认7.点击汇款时间8.点击此刻9.点击确定-----018
    def addPay(self,money=100):
        self.pay()
        self.clear(self.add_pay1)
        self.click(self.add_pay2)
        time.sleep(1)
        #self.click(self.add_pay3)
        self.driver.find_element_by_xpath('//*[@id="app"]/section/div[2]/section/div[1]/form/div[6]/div/div/div[1]/input').send_keys(Keys.DOWN)
        self.driver.find_element_by_xpath('//*[@id="app"]/section/div[2]/section/div[1]/form/div[6]/div/div/div[1]/input').send_keys(Keys.DOWN)
        self.driver.find_element_by_xpath('//*[@id="app"]/section/div[2]/section/div[1]/form/div[6]/div/div/div[1]/input').send_keys(Keys.ENTER)
        self.click(self.add_pay4)
        #判断是否有记录，在执行后面操作
        noadd1 = self.is_text(self.no_add_pay1,'暂无数据')
        if noadd1 == True:
            self.MC.add_recharge(money)
            self.pay()
            self.clear(self.add_pay1)
            self.click(self.add_pay2)
            time.sleep(1)
            # self.click(self.add_pay3)
            self.driver.find_element_by_xpath(
                '//*[@id="app"]/section/div[2]/section/div[1]/form/div[6]/div/div/div[1]/input').send_keys(Keys.DOWN)
            self.driver.find_element_by_xpath(
                '//*[@id="app"]/section/div[2]/section/div[1]/form/div[6]/div/div/div[1]/input').send_keys(Keys.DOWN)
            self.driver.find_element_by_xpath(
                '//*[@id="app"]/section/div[2]/section/div[1]/form/div[6]/div/div/div[1]/input').send_keys(Keys.ENTER)
            self.click(self.add_pay4)
            self.click(self.add_pay5)
            self.click(self.add_pay6)
            self.click(self.add_pay7)
            time.sleep(1)
            self.click(self.add_pay8)
            self.click(self.add_pay9)
            print('新增充值处理成功')
        else :
            self.click(self.add_pay5)
            self.click(self.add_pay6)
            self.click(self.add_pay7)
            time.sleep(1)
            self.click(self.add_pay8)
            self.click(self.add_pay9)
            print('处理成功')

    def addPaySucess(self,text):
        result = self.is_text(self.add_pay_sucess,text)
        return result

    # -----------充值订单驳回--------------------------------019
    def addPayFail(self,money):
        self.pay()
        self.clear(self.add_pay1)
        self.click(self.add_pay2)
        time.sleep(1)
        # self.click(self.add_pay3)
        self.driver.find_element_by_xpath(
            '//*[@id="app"]/section/div[2]/section/div[1]/form/div[6]/div/div/div[1]/input').send_keys(Keys.DOWN)
        self.driver.find_element_by_xpath(
            '//*[@id="app"]/section/div[2]/section/div[1]/form/div[6]/div/div/div[1]/input').send_keys(Keys.DOWN)
        self.driver.find_element_by_xpath(
            '//*[@id="app"]/section/div[2]/section/div[1]/form/div[6]/div/div/div[1]/input').send_keys(Keys.ENTER)
        self.click(self.add_pay4)
        noadd1 = self.is_text(self.no_add_pay1,'暂无数据')
        if noadd1 == True:
            self.MC.add_recharge(money)
            self.pay()
            self.clear(self.add_pay1)
            self.click(self.add_pay2)
            time.sleep(1)
            # self.click(self.add_pay3)
            self.driver.find_element_by_xpath(
                '//*[@id="app"]/section/div[2]/section/div[1]/form/div[6]/div/div/div[1]/input').send_keys(Keys.DOWN)
            self.driver.find_element_by_xpath(
                '//*[@id="app"]/section/div[2]/section/div[1]/form/div[6]/div/div/div[1]/input').send_keys(Keys.DOWN)
            self.driver.find_element_by_xpath(
                '//*[@id="app"]/section/div[2]/section/div[1]/form/div[6]/div/div/div[1]/input').send_keys(Keys.ENTER)
            self.click(self.add_pay4)
            self.click(self.add_pay5)
            self.click(self.add_payfail1)
            self.click(self.add_payfail2)
            print('新增充值驳回成功')
        else:
            self.click(self.add_pay5)
            self.click(self.add_payfail1)
            self.click(self.add_payfail2)
            print('驳回成功')

    def addPayFailSucess(self,text):
        result = self.is_text(self.add_payfail_sucess, text)
        return result

    # -----------------平台放款记录------------------------------020
    def loanRecord(self):
        self.login()
        self.click(self.loan_manage)
        time.sleep(1)
        self.click(self.loan_record)
    def loanRecordSucess(self,text):
        result = self.is_text(self.loan_record_sucess, text)
        return result

    #-----------------------放款记录详情页面--------------------021
    def loanDetails(self):
        self.login()
        self.click(self.loan_details1)
        time.sleep(1)
        self.click(self.loan_details2)
        self.clear(self.loan_details3)
        self.click(self.loan_details4)
        self.click(self.loan_details5)
    def loanDetailsSucess(self,text):
        result = self.is_text(self.loan_details_sucess,text)
        return result

    # ---------------上传完税证明-----------------------------------022
    def upLoadProve(self):
        self.login()
        self.driver.maximize_window()
        self.click(self.loan_details1)
        time.sleep(1)
        self.click(self.loan_details2)
        self.clear(self.loan_details3)
        self.click(self.upload_prove4)
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@placeholder="放款状态"]').send_keys(Keys.DOWN)
        self.driver.find_element_by_xpath('//*[@placeholder="放款状态"]').send_keys(Keys.ENTER)
        time.sleep(1)
        self.click(self.upload_prove6)
        self.sendKeys(self.upload_prove7,'C:\\Users\\a\\Desktop\\新建文件夹\\6.png')
    def upLoadProveSucess(self,text):
        result = self.is_text(self.upload_prove_sucess,text)
        return result

    # ------------------------批量放款记录页面-------------------------------------023
    def banthLoan(self):
        self.login()
        self.click(self.banth_loan1)
        time.sleep(1)
        self.click(self.banth_loan2)
    def banthLoanSucess(self,text):
        result = self.is_text(self.banth_loan_sucess,text)
        return result
    # --------------------------批次放款记录---------------------------------024
    def banthLoan1(self):
        self.login()
        self.banthLoan()
        self.clear(self.banth_loan3)
        self.click(self.banth_loan4)
        self.click(self.banth_loan5)
    def banthLoan1Sucess(self,text):
        result = self.is_text(self.banth_loan_sucess1, text)
        return result
    #----------------------------通过批次号查询放款订单----------------------------025
    def checkBanthLoan(self):
        self.login()
        self.banthLoan()
        self.clear(self.check_banth_loan3)
        self.click(self.check_banth_loan3_1)
        number = self.is_get_text(self.check_banth_loan4_number)
        self.sendKeys(self.check_banth_loan5,number)
        self.click(self.check_banth_loan6)
        result = self.is_text(self.check_banth_loan_sucess2, number)
        return result
    #--------------------------------------赏金页面---------------------------------026
    def money(self):
        self.login()
        self.click(self.money1)
        time.sleep(1)
        self.click(self.money2)
    def moneySucess(self,text):
        result = self.is_text(self.money_sucess,text)
        return result

    #----------------------赏金记录详情-----------------------------------------027
    def bountyRecord(self,text):
        self.money()
        self.clear(self.cancel_start_time)
        self.click(self.query)
        norecord = self.is_text(self.no_record,text)
        if norecord == True:
            print('暂无赏金记录')
        else:
            self.click(self.bounty_details)

    def bountyRecordSucess(self,text):
        result = self.is_text(self.bounty_details_sucess,text)
        return result

    # ----------------------赏金单号查询-----------------------------------------028
    def bountyNumber(self,text):
        self.money()
        self.clear(self.cancel_start_time)
        self.click(self.query)
        norecord = self.is_text(self.no_record, text)
        if norecord == True:
            print('暂无赏金记录')
        else:
            number = self.findEle(self.bounty_number).text
            self.sendKeys(self.bounty_number1,number)
            self.click(self.query)

    def bountyNumberSucess(self,text):
        result = self.is_text(self.bounty_number_sucess,text)
        return result

    #----------------销项发票管理:处理发票开票申请--------------------------------------------029

    def invoiceManage(self,text,money,starttime,invoicecord,invoicenumber,tax_rate,express_number):
        self.login()
        self.click(self.invoice1)
        time.sleep(1)
        self.click(self.invoice2)
        #清除开始时间
        self.clear(self.invoice2_1)
        #选择待处理
        self.click(self.invoice2_2)
        time.sleep(1)
        self.click(self.invoice2_3_1)
        #点击查询
        self.click(self.invoice2_4)
        #判断是否为暂无数据
        norecord = self.is_text(self.invoice3,text)
        if norecord ==True:
            #商户新增开票申请
            self.MC.applyInvoice(text,money,)
            self.login()
            self.click(self.invoice1)
            time.sleep(1)
            self.click(self.invoice2)
            self.clear(self.invoice2_1)
            self.click(self.invoice2_2)
            time.sleep(1)
            self.click(self.invoice2_3_1)
            self.click(self.invoice2_4)
            self.click(self.invoice4)
            self.click(self.invoice5)
            total = self.findEle(self.invoice_money).text
            self.click(self.invoice6)
            #输入开票信息
            self.sendKeys(self.invoice7, starttime)
            self.sendKeys(self.invoice8, invoicecord)
            self.sendKeys(self.invoice9, invoicenumber)
            self.sendKeys(self.invoice10, total)
            self.sendKeys(self.invoice11, tax_rate)
            self.click(self.invoice12)
            self.click(self.invoice13)
            self.sendKeys(self.invoice14, express_number)
            self.click(self.invoice15)
            print('-----商户新增充值后提交开票申请--处理结果----')
        else:
            # 处理发票申请：4.点击申请详情,5.点击发票信息设置,total获取税价合计金额,5_1点击已开发票5_2判断是新增发票还是填写快递单号6.点击新增一张发票7.输入开票日期8.输入发票代码9.输入发票号码
            #10.输入税价合计金额11.输入税率12.点击确认13.点击填写快递单号14.输入快递单号 15.点击确认
            self.click(self.invoice4)
            self.click(self.invoice5)
            total = self.findEle(self.invoice_money).text
            #点击已开发票
            self.click(self.invoice5_1)
            #判断如果有填写快递单号元素执行点击快递单号后面的操作
            expressnumber = self.findEle(self.invoice5_2).text
            if expressnumber == '填写快递单号':
                self.click(self.invoice13)
                self.sendKeys(self.invoice14, express_number)
                self.click(self.invoice15)
                print('----已填写完开票信息--处理结果---')
            #不是快递单号则点击发片信息设置，在点击新增一张发票后面的操作
            else:
                self.click(self.invoice5)
                self.click(self.invoice6)
                self.sendKeys(self.invoice7,starttime)
                self.sendKeys(self.invoice8,invoicecord)
                self.sendKeys(self.invoice9,invoicenumber)
                self.sendKeys(self.invoice10,total)
                self.sendKeys(self.invoice11,tax_rate)
                self.click(self.invoice12)
                self.click(self.invoice13)
                self.sendKeys(self.invoice14,express_number)
                self.click(self.invoice15)
                print('----已填写开票信息--处理结果----')

    def invoiceManageSucess(self,text):
        result = self.is_text(self.invoice_sucess,text)
        return result

    #------------已处理发票详情页-------------------------------030
    def finishInvoice(self,text,money,starttime,invoicecord,invoicenumber,tax_rate,express_number):
        self.login()
        self.click(self.invoice1)
        time.sleep(1)
        self.click(self.invoice2)
        # 清除开始时间
        self.clear(self.invoice2_1)
        # 选择已处理
        self.click(self.invoice2_2)
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="app"]/section/div[2]/section/div[1]/form/div[5]/div/div/div[1]/input').send_keys(
            Keys.DOWN)
        self.driver.find_element_by_xpath(
            '//*[@id="app"]/section/div[2]/section/div[1]/form/div[5]/div/div/div[1]/input').send_keys(
            Keys.ENTER)
        # 点击查询
        self.click(self.invoice2_4)
        #如果没有已处理记录，1.调用处理待处理方法，2.处理好之后再次查询已处理记录

        norecord1 = self.is_text(self.norecord1,text)
        if norecord1 == True:
            self.invoiceManage(text,money,starttime,invoicecord,invoicenumber,tax_rate,express_number)
            self.login()
            self.click(self.invoice1)
            time.sleep(1)
            self.click(self.invoice2)
            # 清除开始时间
            self.clear(self.invoice2_1)
            # 选择已处理
            self.click(self.invoice2_2)
            time.sleep(1)
            self.driver.find_element_by_xpath(
                '//*[@id="app"]/section/div[2]/section/div[1]/form/div[5]/div/div/div[1]/input').send_keys(
                Keys.DOWN)
            self.driver.find_element_by_xpath(
                '//*[@id="app"]/section/div[2]/section/div[1]/form/div[5]/div/div/div[1]/input').send_keys(
                Keys.ENTER)
            # 点击查询
            self.click(self.invoice2_4)
            self.click(self.finish_invoice1)
            self.click(self.finish_invoice2)
            print('------没有已处理记录，查询待处理记录处理记录---------')
        else:
            self.click(self.invoice2_4)
            self.click(self.finish_invoice1)
            self.click(self.finish_invoice2)
            print('------已处理记录已存在，点击到详情页---------')

    def finishInvoiceSucess(self,text):
        result = self.is_text(self.finish_invoice_sucesee,text)
        return result
    #------------打开发包方钱包页面-------------------------------031
    def fbfWallet(self):
        self.login()
        self.click(self.FBF_wallet1)
        time.sleep(1)
        self.click(self.FBF_wallet2)
    def fbfWalletSucess(self,text):
        result = self.is_text(self.FBF_wallet3,text)
        return result

    #----------------打开发包方详情页面---------------------032
    def fbfWalletDetails(self):
        self.fbfWallet()
        self.click(self.FBF_wallet4)
    def fbfWalletDetailsSucess(self,text):
        result = self.is_text(self.FBF_wallet5,text)
        return result

    #-------------打开承揽方钱包页面------------------------033
    def clfWallet(self):
        self.login()
        self.click(self.CLF_wallet1)
        time.sleep(1)
        self.click(self.CLF_wallet2)
    def clfWalletSucess(self,text):
        result = self.is_text(self.CLF_wallet3,text)
        return result

    #-----------打开承揽方钱包详情页面---------------034
    def clfWalletDetails(self):
        self.clfWallet()
        self.click(self.CLF_wallet4)
    def clfWalletDetailsSucess(self,text):
        result = self.is_text(self.CLF_wallet5,text)
        return result
    #------------打开平台钱包页面----------------035
    def ptWallet(self):
        self.login()
        self.click(self.PT_wallet1)
        time.sleep(1)
        self.click(self.PT_wallet2)
    def ptWalletSucess(self,text):
        result = self.is_text(self.PT_wallet3,text)
        return result
    # ------------打开通道钱包页面----------------036
    def tdWallet(self):
        self.login()
        self.click(self.TD_wallet1)
        time.sleep(1)
        self.click(self.TD_wallet2)
    def tdWalletSucess(self,text):
        result = self.is_text(self.TD_wallet3,text)
        return result

    #----------打开商户账单页面--------------------037
    def merchantsBills(self):
        self.login()
        self.click(self.merchants_bills1)
        time.sleep(1)
        self.click(self.merchants_bills2)
    def merchantsBillsSucess(self,text):
        result = self.is_text(self.merchants_bills3,text)
        return result

    #----------打开通道账单页面----------------------038
    def tdBills(self):
        self.login()
        self.click(self.TD_bills1)
        time.sleep(1)
        self.click(self.TD_bills2)
    def tdBillsSucess(self,text):
        result = self.is_text(self.TD_bills3,text)
        return result
    #------------打开我的账户页面---------------------------039
    def accountManagement(self):
        self.login()
        self.click(self.account_management1)
        time.sleep(1)
        self.click(self.account_management2)
    def accountManagementSucess(self,text):
        result = self.is_text(self.account_management3,text)
        return result

    #------------打开账户安全页面----------------------------040
    def accountSecurity(self):
        self.login()
        self.click(self.account_security1)
        time.sleep(1)
        self.click(self.account_security2)
    def accountSecuritySucess(self,text):
        result = self.is_text(self.account_security3,text)
        return result

    #--------------打开重新支付密码页面----------------------041
    def resetPassword(self):
        self.accountSecurity()
        self.click(self.account_security4)
    def resetPasswordSucess(self,text):
        result = self.is_text(self.account_security4,text)
        return result

    #-----------打开修改登录密码页面------------------------042
    def resetLoginPassword(self):
        self.accountSecurity()
        self.click(self.account_security6)
    def resetLoginPasswordSucess(self,text):
        result = self.is_text(self.account_security7,text)
        return result

    #---------打开重新设置手机号码页面--------------------------043
    def resetPhone(self):
        self.accountSecurity()
        self.click(self.account_security8)
    def resetPhoneSucess(self,text):
        result = self.is_text(self.account_security9,text)
        return result

    #-----------打开员工管理页面---------------------------------------------044
    def staffManagement(self):
        self.login()
        self.click(self.account_security1)
        time.sleep(1)
        self.click(self.account_security10)
    def staffManagementSucess(self,text):
        result = self.is_text(self.account_security11,text)
        return result

    #--------------新增员工---------------------045
    def addStaff(self,name,phone,psd,psd1):
        self.staffManagement()
        self.click(self.add_staff1)
        self.sendKeys(self.add_staff2,name)
        self.sendKeys(self.add_staff3,phone)
        self.sendKeys(self.add_staff4,psd)
        self.sendKeys(self.add_staff5,psd1)
        self.click(self.add_staff6)
        self.driver.find_element_by_xpath('//*[@id="app"]/section/div[2]/section/div[5]/div/div[2]/form/div[5]/div/div/div/div/div[1]/input').send_keys(Keys.DOWN)
        self.driver.find_element_by_xpath('//*[@id="app"]/section/div[2]/section/div[5]/div/div[2]/form/div[5]/div/div/div/div/div[1]/input').send_keys(Keys.DOWN)
        self.driver.find_element_by_xpath('//*[@id="app"]/section/div[2]/section/div[5]/div/div[2]/form/div[5]/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
        self.click(self.add_staff8)
    def addStaffSucess(self,text):
        result = self.is_text(self.add_staff9,text)
        return result

    #----------------修改员工密码-------------------------046
    def resetStaffPassword(self,psd,psd1):
        self.staffManagement()
        self.click(self.reset_staff_password1)
        self.sendKeys(self.reset_staff_password2,psd)
        self.sendKeys(self.reset_staff_password3,psd1)
        self.click(self.reset_staff_password4)
    def resetStaffPasswordSucess(self,text):
        result = self.is_text(self.reset_staff_password5,text)
        return result

    #---------------------修改员工姓名----------------047
    def resetStaffName(self,name):
        self.staffManagement()
        self.click(self.reset_staff_name1)
        self.clear(self.reset_staff_name2)
        self.sendKeys(self.reset_staff_name2,name)
        self.click(self.reset_staff_name3)
    def resetStaffNameSucess(self,text):
        result = self.is_text(self.reset_staff_name4,text)
        return result

    #--------------------删除员工------------------048
    def deleteStaff(self,name,phone,psd,psd1):
        self.staffManagement()
        time.sleep(3)
        # r = ('xpath','//*[@id="app"]/section/div[2]/section/div[3]/div[3]/table/tbody/tr[1]/td[8]/div/button[3]/span')
        # norecord = self.is_text(r,'[删除]')
        # print(norecord)
        # if norecord == True:
        #     self.click(self.delete_staff1)
        #     time.sleep(1)
        #     self.click(self.delete_staff2)
        # else:
        self.addStaff(name,phone,psd,psd1)
        self.driver.refresh()
        time.sleep(3)
        self.click(self.delete_staff1)
        time.sleep(3)
        self.click(self.delete_staff2)

    def deleteStaffSucess(self,text):
        result = self.is_text(self.delete_staff3, text)
        return result



    #--------------打开员工角色页面-------------------------049
    def theRole(self):
        self.staffManagement()
        self.click(self.the_role1)
    def theRoleSucess(self,text):
        result = self.is_text(self.the_role2,text)
        return result

    #---------------系统设置页面-----------------------------050
    def sysSet(self):
        self.login()
        self.click(self.sys_set1)
        time.sleep(1)
        self.click(self.sys_set2)
    def sysSetSucess(self,text):
        result = self.is_text(self.sys_set3,text)
        return result

    #-----------------打开客服信息页面----------------------------051
    def infoService(self):
        self.sysSet()
        self.click(self.sys_set4)
    def infoServiceSucess(self,text):
        result = self.is_text(self.sys_set5,text)
        return result

    #-----------------打开发票类目页面----------------------------052
    def invoiceCategory(self):
        self.sysSet()
        self.click(self.sys_set6)
    def invoiceCategorySucess(self,text):
        result = self.is_text(self.sys_set7,text)
        return result

    #-----------------打开发票销方信息-----------------------------053
    def InvoiceXf(self):
        self.sysSet()
        self.click(self.sys_set8)
    def InvoiceXfSucess(self,text):
        result = self.is_text(self.sys_set9, text)
        return result

    #--------------------基础数据页面-----------------------------054
    def basicData(self):
        self.sysSet()
        self.click(self.sys_set10)
    def basicDataSucess(self,text):
        result = self.is_text(self.sys_set11, text)
        return result

    #------------------打开通道管理页面--------------------------055
    def channelManagement(self):
        self.login()
        self.click(self.sys_set1)
        time.sleep(1)
        self.click(self.sys_set12)
    def channelManagementSucess(self,text):
        result = self.is_text(self.sys_set13, text)
        return result

    #------------------打开通道详情页面---------------------056
    def channelDetails(self):
        self.channelManagement()
        self.click(self.sys_set14)
    def channelDetailsSucess(self,text):
        result = self.is_text(self.sys_set15, text)
        return result

    #----------------打开公告管理页面------------------------------057
    def notice(self):
        self.login()
        self.click(self.sys_set1)
        time.sleep(1)
        self.click(self.sys_set16)
    def noticeSucess(self,text):
        result = self.is_text(self.sys_set17, text)
        return result

    #---------------------新增公告--------------------------058
    def addNotice(self,bt,xq):
        self.notice()
        self.click(self.sys_set17)
        self.sendKeys(self.sys_set18,bt)
        self.sendKeys(self.sys_set19,xq)
        self.click(self.sys_set20)
        self.click(self.sys_set21)
    def addNoticeSucess(self,text):
        result = self.is_text(self.sys_set22, text)
        return result

    #-------------------删除公告-------------------------------059
    def deleteNotice(self,bt,xq):
        self.addNotice(bt,xq)
        time.sleep(2)
        self.click(self.sys_set23)
        self.click(self.sys_set24)
    def deleteNoticeSucess(self,text):
        result = self.is_text(self.sys_set25, text)
        return result



if __name__ == '__main__':
    driver = webdriver.Chrome()
    DP = drg_pages(driver)
    sj = SF()
    name = sj.name()
    phone = sj.phone()
    psd = '111111'
    psd1 = '111111'
    DP.deleteStaff(name,phone,psd,psd1)
    result = DP.deleteStaffSucess('删除成功')
    print(result)








