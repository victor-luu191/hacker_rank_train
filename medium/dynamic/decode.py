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
    # Edge cases:
    # Any message that starts with the digit '0' is automatically invalid.
    # If sequences '00', '30', '40', '50', ...,'90' ever show up, the whole msg is also invalid
    if message.startswith('0'):
        return 0
    invalid_seqs = ['00', '30', '40', '50', ..., '90']
    for s in invalid_seqs:
        if s in message:
            return 0

    # 1st digit surely decodes to a letter, then decode remaining part
    # if first 2 digits <= 26 then they can be decoded to a letter too, then decode remains

    # stop cond
    if not message:
        return 1

    if len(message) == 1:
        if message == '0':
            return 0
        return 1

    # at most 2 digits can be used to decode each time, thus last letter is decoded by either the last digit
    # or two last digits

    if message[-1] == '0':  # cannot be used alone for decoding, thus 2 last digits must be used
        if int(message[-2:]) > N_LETTER:  # last 2 digits also invalid decoding
            return 0
        n2 = mapDecoding(message[:-2])
        return n2

    # Last digit is not 0, we can either decode only it or both  2 last digits
    # if both are valid then return mapDecoding(message[:-1]) + mapDecoding(message[:-2])
    # there is duplicate here, when compute mapDecoding(message[:-1]) will recal mapDecoding(message[:-2])
    # to avoid it, use an array to store values which already computed.

    # let decodes[i] be the number of ways to decode msg[:i], eg. i first digits of msg
    # then decodes[i] can be:
    # i) decodes[i-1] + decodes[i-2] if can decode either msg[i-1]  or msg[i-2: i]
    # ii) decodes[i-1] if only decoding msg[i-1] is valid
    # iii) decodes[i-2] if only decoding msg[i-2: i] is valid
    # iv) 0 if none is valid

    n = len(message)
    decodes = [0] * (n + 1)
    decodes[1] = mapDecoding(message[:1])
    # no. of ways to decode first 2 digits
    if message[0] != '0':
        if int(message[:2]) > N_LETTER:  # can only decode each digit
            decodes[2] = mapDecoding(message[1])
        else:  # decoding both gives 1 way plus no. of ways from decoding each
            decodes[2] = 1 + mapDecoding(message[1])
    else:  # this should not happen as the msg should not start with 0
        decodes[2] = 0

    for i in range(3, len(decodes)):
        one_digit = message[i - 1]
        two_digits = message[i - 2:i]
        decodes[i] = can_decode(one_digit) * decodes[i - 1] + can_decode(two_digits) * decodes[i - 2]

        print('msg: ' + message[:i])
        print('no. of ways to decode it:', decodes[i])

    return decodes[n] % CONST
