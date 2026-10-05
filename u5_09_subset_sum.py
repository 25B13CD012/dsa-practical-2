def subset_sum(nums, target):
    nums = sorted(nums)
    found = []
    chosen = []

    def go(i, remaining):
        if remaining == 0:
            found.append(chosen[:])
            return

        if i == len(nums) or nums[i] > remaining:
            return

        chosen.append(nums[i])
        go(i + 1, remaining - nums[i])

        chosen.pop()
        go(i + 1, remaining)

    go(0, target)

    return found


print(subset_sum([3, 34, 4, 12, 5, 2], 9))
print(subset_sum([1, 2, 3], 7))
