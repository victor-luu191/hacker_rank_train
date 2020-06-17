import math

# find all subseqs of len k of a given sequence
# return a list of the subseqs, ie. a list of lists
def findSubs(k, numbers):
    # idea: as a subseq must start with some item in the numbers. So,
    # for each item n_i in the numbers, we find all subseqs of len k starting with n[i], ie.
    # subseqs of form [n_i, remain] where remain part is a subseq of len k-1, picked from n[i+1: ] (recursive)
    # The reason remain part is picked only in n[i+1:] is to avoid dups.
    # Ex: subseqs of len 2 of [n1, n2, n3, n4] are [n1,n2], [n1,n3], [n1,n4], [n2,n3], [n2,n4], [n3,n4]

    # stop condition
    if k == 0:
        return [list()]
    else:
        # print('finding subseqs of len ', k, ' of seq ', numbers)
        subsequences = []
        for i in range(len(numbers) - k + 1):
            n_i = numbers[i]
            # print('subseq starting with ', i, '-th item, which is ', n_i)
            subseq_start_with_ni = [[n_i] + ss for ss in findSubs(k - 1, numbers[i + 1:])]
            subsequences += subseq_start_with_ni
        return subsequences


def findGCD(arr):
    if len(arr) == 2:
        return math.gcd(arr[0], arr[1])
    else:
        return math.gcd(arr[0], findGCD(arr[1:]))


# Given a sequence of pos integers and a number k,
# return the longest subseq: i) of len at least k, and ii) gcd of items in the subseq is maximal
def findSubsequence(numbers, k):
    # obs: gcd(a, b, c) = gcd( gcd(a,b), c)
    # when adding a number to an array, gcd will reduce, as the new gcd must be a divisor of current gcd
    # thus, longer seqs will have smaller gcd. So, the subseq of len, k+1 and more will be no better then
    # subseq of len k. So we only need to search in subseqs of len k. Then add more items later.

    subseqs = findSubs(k, numbers)
    print('Subsequences of len ', k, ' : ', subseqs)

    max_gcd = 1
    best_seq_of_len_k = None
    for ss in subseqs:
        gcd_of_ss = findGCD(ss)
        if gcd_of_ss > max_gcd:
            max_gcd = gcd_of_ss
            best_seq_of_len_k = ss

    # add more items to get the longest subseq. We need to avoid reducing the gcd, thus an item can only be added
    # if it is a multiple of the gcd
    best_seq = best_seq_of_len_k
    remains = [n for n in numbers if n not in best_seq_of_len_k]
    for n in remains:
        if n % max_gcd == 0:
            best_seq += [n]

    return best_seq, max_gcd


if __name__ == '__main__':
    numbers_count = int(input().strip())

    numbers = []

    for _ in range(numbers_count):
        numbers_item = int(input().strip())
        numbers.append(numbers_item)

    k = int(input().strip())

    result = findSubsequence(numbers, k)
    print('Best subseq : ', result[0], ', with largest GCD: ', result[1])
