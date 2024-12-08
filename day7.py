ans = 0


def canSolve(nums, target):
    def r(i, cur):
        if i == len(nums):
            if cur == target:
                return True
            return False
        if cur >= target:
            return False

        n = int(str(cur) + str(nums[i]))
        return r(i + 1, cur * nums[i]) or r(i + 1, cur + nums[i]) or r(i + 1, n)

    return r(0, 0)


with open("input.txt") as file:
    for line in file:
        l = line.strip()
        sp = line.split(":")
        target = int(sp[0].strip())
        print(line)
        nums = [int(x) for x in sp[1].strip().split(" ")]
        if canSolve(nums, target):
            ans += target

print(ans)
