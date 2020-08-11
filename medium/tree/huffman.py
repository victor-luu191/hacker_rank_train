import queue as Queue

cntr = 0


class Node:
    def __init__(self, freq, data):
        self.freq = freq
        self.data = data
        self.left = None
        self.right = None
        global cntr
        self._count = cntr
        cntr = cntr + 1

    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq < other.freq
        return self._count < other._count


def huffman_hidden():  # builds the tree and returns root
    q = Queue.PriorityQueue()

    for key in freq:
        q.put((freq[key], key, Node(freq[key], key)))

    while q.qsize() != 1:
        a = q.get()
        b = q.get()
        obj = Node(a[0] + b[0], '\0')
        obj.left = a[2]
        obj.right = b[2]
        q.put((obj.freq, obj.data, obj))

    root = q.get()
    root = root[2]  # contains root object
    return root


def dfs_hidden(obj, already):
    if (obj == None):
        return
    elif (obj.data != '\0'):
        code_hidden[obj.data] = already

    dfs_hidden(obj.right, already + "1")
    dfs_hidden(obj.left, already + "0")


"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
def find_char_by_follow_zero_one(s, root):
    current = root
    for i, d in enumerate(s):
        if d == '0':  # follow left path
            current = current.left
        else:
            current = current.right
        # if reach a leaf node, return the letter
        letter = current.data
        if letter != '\0':
            return letter, i


def decode(root, s):
    if not s:
        return ''

    # follow zeros and ones in s until reach leaf node, then get the letter from it
    letter, stop = find_char_by_follow_zero_one(s, root)
    return letter + decode(root, s[stop + 1:])


def decodeHuff(root, s):
    # for each decoding, always start from root, follow zeros and ones in s until reach a leaf node in the tree,
    # stop there and
    # i) get the letter in the leaf node
    # ii)    resume from where we stopped, eg. decode the remaining part
    print(decode(root, s))



if __name__ == '__main__':

    ip = input()
    freq = {}  # maps each character to its frequency

    cntr = 0

    for ch in ip:
        if (freq.get(ch) == None):
            freq[ch] = 1
        else:
            freq[ch] += 1

    root = huffman_hidden()  # contains root of huffman tree

    code_hidden = {}  # contains code for each object
    # generate codewords for letters
    dfs_hidden(root, "")

    if len(code_hidden) == 1:  # if there is only one character in the i/p
        for key in code_hidden:
            code_hidden[key] = "0"
    print('codewords:', code_hidden)

    toBeDecoded = ""
    for ch in ip:
        toBeDecoded += code_hidden[ch]

    print('encoded string:', toBeDecoded)
    print(decodeHuff(root, toBeDecoded))
