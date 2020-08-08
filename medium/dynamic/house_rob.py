def houseRobber(nums):
    # The system will automatically trigger an alarm if two adjacent houses are broken
    # so cannot take 2 adjacent values

    # stop cond
    if not nums:
        return 0

    if len(nums) <= 2:
        return max(nums)

    # if there are >= 3 numbers, [a1, a2, a3,...]
    # if start robbing from a3 onwards, then also can rob a1 and get at least as much as start robbing from a1 (as a1 non-neg), so any way of robbing start from a3 should also include a1
    # if take a1 then cannot take a2, then rob max in houses from a3 onward
    # if take a2, then cannot take neither a1 or a3, so rob max amt in houses from a4 onward

    ## work but slow
    # best_rob_1st_house = nums[0] + houseRobber(nums[2:])
    # best_rob_2nd_house = nums[1] + houseRobber(nums[3:])
    # return max(best_rob_1st_house, best_rob_2nd_house)

    # there are overlap here, when compute max amount to rob in nums[2:], we need to compute max amt to rob in nums[3:], to avoid it we should compute backward and use an array to save max amt to rob
    max2rob = [0] * len(nums)
    last = len(nums) - 1
    max2rob[last] = nums[last]
    max2rob[last - 1] = max(nums[last], nums[last - 1])
    for i in range(last - 2, -1):
        max2rob[i] = max(nums[i] + max2rob[i+2], max2rob[i+1])

    return max2rob[0]
