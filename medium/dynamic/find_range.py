def composeRanges(nums):
    # a single item can be a range
    # a range is made from contiguous integers, so if a_(i+1) - a_i = 1 then a range can be formed as [a_i, a_(i+1), ...]
    # say we can make a range [a0, ..., ak], then need to find ranges in remaining part.
    # So a simple sol is: ['a0 -> ak'] + composeRanges(a[k+1:])

    # stop cond
    if not nums:
        return []

    if len(nums) == 1:
        return ['{}'.format(nums[0])]

    i, range_contain_a0 = find_1st_range(nums)
    return [range_contain_a0] + composeRanges(nums[i:])


def find_1st_range(nums):
    # find the range containing first element a0

    in_range = True
    i = 0
    while in_range and i < len(nums):
        i += 1
        in_range = (nums[i] - nums[i - 1] == 1)

    # the range is from a0 to a[i-1]
    range_contain_1st_element = "{} -> {}".format(nums[0], nums[i - 1])
    return i, range_contain_1st_element
