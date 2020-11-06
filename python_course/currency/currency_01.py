"""
 作者:XXX
 功能：汇率兑换
 版本：v1.0
 日期：14/5/2020
"""
# 汇率
USD_VS_RMB = 6.77

# 人名币的输入
rmb_str_value = input('请输入人名币(CNY)金额:')

# 将字符串转换成数字
rmb_value = eval(rmb_str_value)

# 汇率计算
usd_value = rmb_value / USD_VS_RMB

print('美元(USD)金额是', usd_value)
