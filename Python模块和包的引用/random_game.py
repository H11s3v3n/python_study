import random
target = random.randint(1,100)
print("猜一个 1 到 100 之间的数字")

while True:
    guesss = int(input("请输入你的猜测："))
    if guesss < target:
        print("太小了！")
    elif guesss > target:
        print("太大了！")
    else:
        print("恭喜你，猜对了！")
        break
