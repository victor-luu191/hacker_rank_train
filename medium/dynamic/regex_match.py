def is_empty_like(s):
    # a given string s is empty like if it is empty or can be turn to empty via dropping chars
    if not s:
        return True
    if len(s) == 1 and s == '*':
        return True
    try:
        k = s.index('*')
        # drop  * and its prev letter at index k-1
        if k >= 1:
            return (not s[:k - 1]) and (is_empty_like(s[k + 1:]))
        return is_empty_like(s[1:])
    except ValueError:
        print('string has no star')
        return False


def match_letters(c1, c2):
    # check if letter c1 match with c2
    print('matching letters: ', (c1, c2))
    if c1 == '.':
        return True
    return c1 == c2


def find_index_of_first_non_match(s):
    # given string s, find the first index k st s[k] != s[0]
    for i in range(1, len(s)):
        if s[i] != s[0]:
            return i
    return len(s)


from collections import namedtuple

Block = namedtuple('Block', ['start', 'end', 'text'])


def find_blocks_of_len(m, s):
    # given a string s and number m <= len(s), return all substrings of s with len m
    get_block = lambda i: Block(start=i, end=i + m, text=s[i:i + m])
    blocks = [get_block(i) for i in range(len(s) - m + 1)]
    print('substrings of len', m, 'in', s, ':')
    print(blocks)
    return blocks


def regularExpressionMatching(s, p):
    # Ask:
    # What if * has no element before it? eg. p='*' and s='a', is it a match?
    #  What if we have ** in p?

    # '.' Matches any single character = single wild card
    # '*' Matches zero or more of the element that comes before it = no match or
    # repeated match with prev item. So, when we have a star, its prev char can be either dropped or
    # copied as many times as needed.
    # So, "c*" can match a chunk "cc...c" and ".*" can match with any string

    # Idea: If p[1] not *, need to match p[0] with s[0] then match remaining parts of s and p.
    # Else, if p[0] is . then p[0]p[1] is ".*", so can match any string, only the remain p[2:] need to be
    # matched
    # if not . but a char c then "c*" can either not match or repeated match with a chunk of c's in s

    print('matching string', s, 'with string', p)

    # Stop  when either entire s has been matched or all letters in p have been used up
    if not s:  # match if p is empty or can be considered as empty
        return is_empty_like(p)

    # When s still has element to be matched
    # s[0] should be matched with p[0] unless p[1] is '*'
    if not p:
        return False
    if len(p) == 1:
        return len(s) == 1 and match_letters(p, s)
    # if p has at least two elements, so p[1] exist
    if p[1] != '*':
        # print('first items must match')
        return match_first_items_then_remains(p, s)
    else:
        if p[0] != '.':
            if p[0] != s[0]:  # no match, need to skip p[0]p[1]
                return regularExpressionMatching(s, p[2:])
            print('string', ''.join(p[:2]), 'will match with whole chunk of', s[0])
            # find where the chunk stop, eg the first letter diff from s[0]
            k = find_index_of_first_non_match(s)
            return regularExpressionMatching(s[k:], p[2:])
        print('p0p1 is .*, so can match any substring of s, including s')
        if len(p) == 2:
            return True

        ## need to match the remain p[2:]. But match with which part of s? having * can change the length
        remain_p = p[2:]
        try:
            k = remain_p.index('*')
            ## p = '.*' + remain_p = '.*' + bf_star + '*' + after_star
            if k == 0:  # no letter bf *; p = '.*' + remain_p = '.*' + '*' + after_star
                new_p = '.*' + p[3:]
                return regularExpressionMatching(s, new_p)
            else:
                no_star_block = remain_p[:k - 1]
                # must match this no star block with some block in s with same length
                m = len(no_star_block)
                blocks = find_blocks_of_len(m, s)
                for blk in blocks:
                    match_no_star_block = regularExpressionMatching(blk.text, no_star_block)
                    match_remains = regularExpressionMatching(s[blk.end:], remain_p[k - 1:])
                    if match_no_star_block and match_remains:
                        return True
                return False

        except ValueError:  # no star in remain_p, match with exact len
            rem_len = len(remain_p)
            return regularExpressionMatching(s[-rem_len:], remain_p)


def match_first_items_then_remains(p, s):
    return match_letters(p[0], s[0]) and regularExpressionMatching(s[1:], p[1:])
