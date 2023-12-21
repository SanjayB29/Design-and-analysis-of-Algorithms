import heapq
import collections

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # defining comparators less_than and equals
    def __lt__(self, other):
        return self.freq < other.freq

    def __eq__(self, other):
        if(other == None):
            return False
        if(not isinstance(other, Node)):
            return False
        return self.freq == other.freq

# Function to build the Huffman Tree
def build_huffman_tree(text):
    frequency = collections.Counter(text)
    priority_queue = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(priority_queue, merged)

    return priority_queue[0]

# Function to encode the characters
def encode(root, string, huffman_code):
    if root is None:
        return

    if root.char is not None:
        huffman_code[root.char] = string

    encode(root.left, string + "0", huffman_code)
    encode(root.right, string + "1", huffman_code)

# Function to decode the encoded string
def decode(root, index, s):
    if root is None:
        return index

    if root.char is not None:
        print(root.char, end='')
        return index

    index += 1
    if s[index] == '0':
        return decode(root.left, index, s)
    else:
        return decode(root.right, index, s)

# Main function to execute Huffman Coding
def huffman_coding(text):
    root = build_huffman_tree(text)
    huffman_code = {}
    encode(root, "", huffman_code)

    encoded_str = ''.join([huffman_code[char] for char in text])

    print("Encoded string is:", encoded_str)

    print("Decoded string is:", end=' ')
    index = -1
    while index < len(encoded_str) - 1:
        index = decode(root, index, encoded_str)
    print()

# Example usage
text = "Huffman coding algorithm"
huffman_coding(text)
