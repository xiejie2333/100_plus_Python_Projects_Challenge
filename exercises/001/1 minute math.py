# -*- coding: UTF-8 -*-
"""
需求
直接在控制台使用命令行运行
程序运行之后倒计时1分钟之后结束
随机出100以内的2个整数加减乘除运算题目（除法确保能够除尽，但除数不能为0）
每出一道题目，由玩家给出答案，然后程序判断对错，接着出下一题，并且显示剩余时间
1分钟时间结束，显示总题数和正确率（正确率精确到小数点后2位），并将之前的题目和答案显示出来
"""
import time
import random


def get_divisor(n):
    num_list = []
    for i in range(1, n + 1):
        if n % i == 0:
            num_list.append(i)
    return random.choice(num_list)


def main():
    ops = ['+', '-', '*', '/']
    start_time = time.time()
    res_trues = 0
    res_total = 0
    summary = ""

    while time.time() - start_time <= 60:
        res_total += 1
        op = random.choice(ops)
        number1 = random.randint(1, 10)
        if op != '/':
            number2 = random.randint(1, 10)
        else:
            number2 = get_divisor(number1)
        print(f"计算：{number1} {op} {number2}")
        eval_res = eval(f"{number1}{op}{number2}")
        res = input("结果：")
        if res and eval_res == int(res):
            print("√")
            res_trues += 1
            summary += f"{number1}\t{op}\t{number2}\t=\t{res}\t√\n"
            continue
        summary += f"{number1}\t{op}\t{number2}\t=\t{res}\t×\n"
        print("×")
        continue
    print(f"总题数：{res_total},正确率：{res_trues / res_total}%")
    print(summary)


if __name__ == '__main__':
    main()
