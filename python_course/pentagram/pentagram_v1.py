"""
    作者：xxx
    功能：五角星绘制
    版本：1.0
    日期：21/5/2020
"""
import turtle


def main():
    """
     主函数
    """
    # 计数器
    count = 1
    while count <= 5:
        turtle.forward(100)
        turtle.right(144)
        count = count + 1

    turtle.exitonclick()


if __name__ == '__main__':
    main()
