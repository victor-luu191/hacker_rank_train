def find_end_of_1st_range(arr):
    # given a sorted array starting at 0, find end of the range containing 0
    # it is the first index i which arr[i] != i
    for i in range(0, len(arr)):
        if arr[i] != i:
            return i
    return len(arr)


def composeRanges(nums):
    # a single item can be a range.
    # say we can make a range [a0, ..., ak], then need to find ranges in remaining part.
    # So a simple sol is: ['a0 -> ak'] + composeRanges(a[k+1:])

    # stop cond
    if not nums:
        return []

    if len(nums) == 1:
        return ['{}'.format(nums[0])]

    first_range, k = find_1st_range(nums)
    return [first_range] + composeRanges(nums[k:])


def find_1st_range(nums):
    # a natural range is 0,1,2,..., thus  get back to the natural range by translating items by amount nums[0]
    trans_arr = [n - nums[0] for n in nums]
    # in the natural range, a[i] == i
    k = find_end_of_1st_range(trans_arr)
    if k > 1:
        first_range = '->'.join([str(nums[0]), str(nums[k - 1])])
    else:
        first_range = [str(nums[0])]
    print('first range: ', first_range)
    return first_range, k
