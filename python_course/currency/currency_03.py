"""
 作者:XXX
 功能：汇率兑换
 版本：3.0
 日期：17/5/2020
 2.0 新增功能：根据输入判断是人名币还是美元，进行相应的转换计算
 3.0 增加用户自主选择是否退出
"""
# 汇率
USD_VS_RMB = 6.77

# 输入带单位的货币
currency_str_value = input('请输入带单位的货币金额（退出程序请输入Q):')
i = 0
while currency_str_value != 'Q':
    i = i + 1
    # print('循环次数：', i)

    # 获取货币单位：
    unit = currency_str_value[-3:]
    if unit == 'CNY':
        # 输入人名币：
        rmb_str_value = currency_str_value[:-3]

        # 将字符串转换位数字
        rmb_value = eval(rmb_str_value)

        # 汇率计算
        usd_value = rmb_value / USD_VS_RMB

        # 输出结果
        print('美元(USD)金额是:', usd_value)

    elif unit == 'USD':
        # 输入美元：
        usd_str_value = currency_str_value[:-3]

        # 将字符串转换位数字
        usd_value = eval(usd_str_value)

        # 汇率计算
        rmb_value = usd_value * USD_VS_RMB

        # 输出结果
        print('人名币（CNY）:', rmb_value)
    else:
        # 其他货币：
        print('该版本暂不支持此货币！')

    # 输入带单位的货币
    currency_str_value = input('请输入带单位的货币金额（退出程序请输入Q):')


print('程序已退出！')


