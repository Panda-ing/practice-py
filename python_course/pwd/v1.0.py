"""
功能：密码强弱判断
"""


def check_number_exist(password_str):
    """
    判断是否含有数字
    :param password_str:
    """
    for c in password_str:
        if c.isnumeric():
            return True
    return False

def check_letter_exist(password_str):
    """
    判断是否包含字母
    """
    for c in password_str:
        if c.isalpha():
            return True
    return False

def main():
    """
    主函数
    """
    password = input("请输入密码：")
    # 密码强度
    strength_level = 0
    # 规则1：密码长度大于8
    if len(password) >= 8:
        strength_level += 1
    else:
        print("密码输入要求大于8位！")
    # 规则2：判断是否含有数字
    if check_number_exist(password):
        strength_level += 1
    else:
        print('密码要求包含数字！')
    # 规则3：包含字母
    if check_letter_exist(password):
        strength_level += 1
    else:
        print('密码要求包含字母！')
    if strength_level == 3:
        print('输入成功，密码强度符合要求！')
    else:
        print('密码强度不符合要求，请重新输入')



if __name__ == '__main__':
    main()
