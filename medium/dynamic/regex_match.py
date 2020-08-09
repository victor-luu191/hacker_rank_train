def has_only_star(s):
    # check if given string s contains only *
    for c in s:
        if c != '*':
            return False
    return True


def match_letters(c1, c2):
    # check if letter c1 match with c2
    print('matching letters: ', (c1, c2))
    if c1 in ['.', '*']:
        return True
    return c1 == c2


def regularExpressionMatching(s, p):
    # '.' Matches any single character.
    # '*' Matches zero or more of the element that comes before it = no match or repeated match
    # The matching should cover the entire input string s.

    # Ask:
    # What if * has no element before it?
    #  What if we have ** in p?

    # Idea: If p[1] not *, need to match p[0] with s[0] then match remaining parts of s and p.
    # Else, p[0] not need match with s[0], so
    # either match p[0] with s[0], drop p[1]=*, then match s[1:] with p[2:]
    # OR drop first 2 letters of p and match s with p[2:]

    print('matching string', s, 'with string', p)

    # stop cond, when entire s has been matched
    if not s:
        return has_only_star(p)

    # When s still has element to be matched
    # s[0] should be matched with p[0] unless p[1] is '*'
    if not p:
        return False

    if len(p) == 1:
        return len(s) == 1 and match_letters(p, s)
    else:
        if p[1] != '*':
            # print('first letters must match')
            return match_first_items_then_remains(p, s)
        else:
            return match_first_items_then_remains(p, s) or \
                   (match_letters(p[0], s[0]) and regularExpressionMatching(s[1:], p[2:])) or \
                   (regularExpressionMatching(s, p[2:]))


def match_first_items_then_remains(p, s):
    return match_letters(p[0], s[0]) and regularExpressionMatching(s[1:], p[1:])
