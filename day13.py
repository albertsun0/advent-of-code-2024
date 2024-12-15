import re

ans = 0

nums = []
with open("input.txt") as file:
    for line in file:
        l = line.strip()
        n = re.findall(r'\d+', l)
        if n:
            nums.append([int(x) for x in n])

ans = 0

for i in range(0, len(nums), 3):
    x1,y1 = nums[i]
    x2,y2 = nums[i+1]
    tx,ty = nums[i + 2]

    # Part one solution
    
    # minAttempts = float("inf")

    # for a in range(0, 100):
    #     b1 = (tx - a * x1) / x2
    #     b2 = (ty - a * y1) / y2
    #     if b1 != b2:
    #         continue
    #     minAttempts = min(minAttempts, a * 3 + b1)

    # if minAttempts < float("inf"):
    #     ans += minAttempts

    # X = tx * y1 / x1 - ty

    # Y = x2 * y1 / x1

    # b = X / (Y - y2)

    # a = (tx - b * y2) / x1

    # print(a,b)

print(ans)



    # a * x1 + b * x2 = tx
    # a * y1 + b * y2 = ty

    # a * x1 = tx - b * x2

    # a = (tx - b * x2) / x1

    # (tx - b * x2) / x1 * y1 + b y2 = ty

    # (tx/x1 - b * x2 / x1) * y1 + b y2 = ty
    # tx * y1 / x1 - b * x2 * y1 / x1 + b * y2 = ty

    # tx * y1 / x1 - ty = b * x2 * y1 / x1 - b * y2

    # X = tx * y1 / x1 - ty, Y = x2 * y1 / x1

    # X = Yb - b * y2
    # X = b (Y - y2)

    # b = X / (Y - y2)