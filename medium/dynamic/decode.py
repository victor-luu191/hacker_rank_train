import string

values = string.ascii_uppercase
N_LETTER = len(values)
keys = [i + 1 for i in range(N_LETTER)]
letters = dict(zip(keys, values))
CONST = 10 ** 9 + 7


def can_decode(s):
    # given a string of at most two digits, check if it is a valid code of a letter
    if len(s) == 1:
        return int(s) > 0
    if len(s) == 2:
        # valid iff leading of two digits must be non-zero and value <= n_letter
        return s[0] != '0' and int(s) <= N_LETTER
    pass


def mapDecoding(message):
    # max value of a letter is 26, min value is 1.
    ## Invalid cases:
    # Any message that starts with the digit '0' is automatically invalid.
    # If sequences '00', '30', '40', '50', ...,'90' ever show up, the whole msg is also invalid
    if message.startswith('0'):
        return 0
    invalid_seqs = ['00', '30', '40', '50', '60', '70', '80', '90']
    for s in invalid_seqs:
        if s in message:
            return 0

    # VAlid cases
    # stop cond
    if not message:
        return 1

    if len(message) == 1:
        if message == '0':
            return 0
        return 1

    # When msg has at least 2 digits:
    # As at most 2 digits can be used to decode each time, the last letter is decoded by using
    # only one last digit
    # or two last digits

    if message[-1] == '0':  # cannot be used alone for decoding, thus 2 last digits must be used
        return can_decode(message[-2:]) * mapDecoding(message[:-2])

    # Last digit is not 0, we can either decode only it or both  2 last digits
    # if both are valid then return mapDecoding(message[:-1]) + mapDecoding(message[:-2])
    # there is duplicate here, when compute mapDecoding(message[:-1]) will recal mapDecoding(message[:-2])
    # to avoid it, use an array to store values which already computed.
    # Let decodes[i] be the number of ways to decode msg[:i], eg. i first digits of msg

    n = len(message)
    decodes = [1] + [0] * n
    decodes[1] = mapDecoding(message[:1])
    # no. of ways to decode first 2 digits
    decodes[2] = mapDecoding(message[1]) + can_decode(message[:2])

    for i in range(3, len(decodes)):
        one_digit = message[i - 1]
        two_digits = message[i - 2:i]
        decodes[i] = can_decode(one_digit) * decodes[i - 1] + can_decode(two_digits) * decodes[i - 2]

        print('msg: ' + message[:i])
        print('no. of ways to decode it:', decodes[i])

    return decodes[n] % CONST
