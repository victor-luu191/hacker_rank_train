import string

values = string.ascii_uppercase
N_LETTER = len(values)
keys = [i + 1 for i in range(N_LETTER)]
letters = dict(zip(keys, values))
CONST = 10 ** 9 + 7


def mapDecoding(message):
    # max value of a letter is 26, min value is 1.
    # 1st digit surely decodes to a letter, then decode remaining part
    # if first 2 digits <= 26 then they can be decoded to a letter too, then decode remains

    # stop cond
    if not message:
        return 1

    if len(message) == 1:
        if message == '0':
            return 0
        return 1

    #  a case where no decoding is valid msg='130': all [1,3,0], [1, 30], [13,0] invalid
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
        can_decode_one_digit = (int(one_digit) > 0)
        if two_digits[0] == '0':  # if leading of two digits is 0, decoding two digits is invalid
            decodes[i] = can_decode_one_digit * decodes[i - 1]
        else:
            can_decode_two_digit = (int(two_digits) <= N_LETTER)
            decodes[i] = can_decode_one_digit * decodes[i - 1] + can_decode_two_digit * decodes[i - 2]

        print('msg: ' + message[:i])
        print('no. of ways to decode it:', decodes[i])

    return decodes[n] % CONST
