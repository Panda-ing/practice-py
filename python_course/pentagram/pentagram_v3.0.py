"""
    作者：xxx
    功能：五角星绘制
    版本：3.0
    日期：17/6/2020
    新增功能：加入循环操作绘制不同大小的图形
    新增功能：使用迭代绘制不同大小的图形
"""
import turtle


def draw_pentagram(size):
    count = 1
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        count = count + 1


def main():
    """
     主函数
    """
    size = 50
    while size <= 100:
        draw_pentagram(size)
        size += 10

    turtle.exitonclick()


if __name__ == '__main__':
    main()
