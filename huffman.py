class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(char_count_dict):
    import heapq

    priority_queue = [HuffmanNode(char, freq) for char, freq in char_count_dict.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged_node = HuffmanNode(None, left.freq + right.freq)
        merged_node.left = left
        merged_node.right = right
        heapq.heappush(priority_queue, merged_node)

    return priority_queue[0]

def build_huffman_codes(node, current_code, huffman_codes):
    if node is None:
        return

    if node.char is not None:
        huffman_codes[node.char] = current_code
    build_huffman_codes(node.left, current_code + '0', huffman_codes)
    build_huffman_codes(node.right, current_code + '1', huffman_codes)

def encode_text(text, huffman_codes):
    encoded_text = ''.join([huffman_codes[char] for char in text])
    return encoded_text

def decode_text(encoded_text, huffman_tree):
    decoded_text = ""
    current_node = huffman_tree
    for bit in encoded_text:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char is not None:
            decoded_text += current_node.char
            current_node = huffman_tree

    return decoded_text

# Input character counts from the user
user_text = input("Enter the text: ")

# Create a dictionary to store character counts
char_count_dict = {}
# user_text += "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM.,?!-_+=-()*"
# Count characters in the input text
for char in user_text:
    if char in char_count_dict:
        char_count_dict[char] += 1
    else:
        char_count_dict[char] = 1

# Build the Huffman tree
root = build_huffman_tree(char_count_dict)
huffman_codes = {}
build_huffman_codes(root, '', huffman_codes)
while 1:
# Input text from the user to encode
    user_text_to_encode = input("Enter the text to encode: ")

    # Encode the input text using the Huffman tree
    encoded_text = encode_text(user_text_to_encode, huffman_codes)

    # Print the encoded text
    print("Encoded text:", encoded_text)

    # Decode the encoded text
    decoded_text = decode_text(encoded_text, root)

    # Print the decoded text
    print("Decoded text:", decoded_text)
