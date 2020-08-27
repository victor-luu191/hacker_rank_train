#!/bin/python3

import os
import string

UPPERS = string.ascii_uppercase


# Complete the abbreviation function below.
def abbreviation(a, b):
    if can_match(b, a):
        return 'YES'
    else:
        return 'NO'


def has_capital_letter(s):
    # check if there is any capital letter in string s
    for ch in s:
        if ch in UPPERS:
            return True
    return False


def is_match(c1, c2):
    # given two letters c1, c2, return if c1 matches c2, where a match = (c1==c2) or (c1.upper()==c2)
    return (c1 == c2) or (c1.upper() == c2)


def is_exact_match(s1, s2):
    # an exact match := (len(s1) == len(s2)) and (is_match(s1[i], s2[i]), for all i)
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):
        if not is_match(s1[i], s2[i]):
            return False
    return True


def get_uppers(s):
    return [c for c in s if c in UPPERS]


def can_match(b, a):
    # In general, we will match b[k:] to a[j:] and dups will happen, bc when we match b[k-1:] with a[j':],
    # whre j' < j, we already check if b[k:] can be matched with a[j:].
    # To avoid dups, we will use an array to store the finished matches and go backward
    # Let match[k][j] be the result of matching b[-k:] against a[-j:],
    # ie. k last chars of b against UP TO j last chars of a,
    # NOTE: b[-k:] may match with just a[-j':], j' <= j, then extend to a[-j:]
    # Then final result is match[m][n], m = len(b), n = len(a).

    # init match array
    print('\nMatch str', b, 'against str', a)
    n, m = len(a), len(b)
    rows, cols = m + 1, n + 1
    match = [[False for j in range(cols)] for i in range(rows)]
    match[0][0] = True
    for i in range(1, cols):
        # an empty b can only be matched with a[-i:] if a[-i:] contain all lowercases
        match[0][i] = not has_capital_letter(a[-i:])

    # match last k letters of b, given that its last  k-1 letters are matchable.
    # Process:
    # i) find the shortest match for b[-k:]
    # ii) if found shortest match, extend to the longest match
    for k in range(1, rows):
        print('\tmatching last {} letters of b: {}'.format(k, b[-k:]))

        # Go backward to find all exact matches for b[-k:] ,
        # an exact match should start with a match for b[-k],
        # and the remaining part should be matchable with b[-(k-1):], known based on row k-1 of match matrix
        # Then for any two exact matches, check for each position j between them
        # if a[-j:] can also form a match

        # Find all exact matches
        exact_matches = []
        for i in range(1, cols):
            if is_match(a[-i], b[-k]) and match[k-1][i-1] :
                match[k][i] = True
                exact_matches.append(i)

        # for any two exact matches, check if a[-j:] can also form a match,
        # for each position j between the two matches
        def extend_till_hit_upper(m1, m2=cols):
            for j in range(m1 + 1, m2):
                if a[-j] not in UPPERS:
                    match[k][j] = True
                else:
                    break

        if exact_matches:
            if len(exact_matches) == 1:
                single_match = exact_matches[0]
                print('\tfound only one exact match at index {}, extending it until hitting upper case'.\
                      format(single_match)
                      )
                extend_till_hit_upper(single_match)

            if len(exact_matches) > 1:
                print('\tfound many exact matches at indices:', exact_matches)
                # for any two exact matches em[i] and em[i+1], check if a[-j:] can also form a match,
                # for em[i] < j < em[i+1]
                for i in range(len(exact_matches) - 1):
                    cur_match, next_match = exact_matches[i], exact_matches[i + 1]
                    extend_till_hit_upper(cur_match, next_match)
                last_match = exact_matches[-1]
                extend_till_hit_upper(last_match)

            print('\trow', k, 'of match matrix:', match[k][:])
        else:
            # no match, so even a substr of b cannot match,
            #  so full b also fails, must exit here
            print('Fail to match', k, 'last letters of b. False')
            return False

    res = match[m][n]
    print(res)
    return res


def get_in_between(a, j, i):
    # Given indices j > i,
    # return the part in between a[-j] and a[-i], excluding two ends
    # such a part only exists when j > i+1,
    # also working with a neg index -i require handle edge case when i=0

    if j == i + 1:
        return ''
    # else: j > i+1
    if i > 0:
        return a[-(j - 1): -i]
    return a[-(j - 1):]

    # if i > 0:
    #     in_between = a[-(j - 1): -i]
    # # if i=0 the above wrongly return '', instead need a[-(j - 1):]
    # if i == 0 and j == 1:
    #     in_between = ''
    # if i == 0 and j > 1:
    #     in_between = a[-(j - 1):]
    # print('\tsubstr of a from', -(j - 1), 'to', -(i + 1), ':', in_between)
    # return in_between


if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except PermissionError:
        test = int(input())
        fptr = open('../abbr-testcases/output/my_out_{}.txt'.format(test), 'w')

    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()
