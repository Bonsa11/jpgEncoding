import numpy as np
from trees import Node

def get_probs(block: np.array):
    total = block.shape[0] * block.shape[1]
    value, counts = np.unique(block, return_counts=True)

    return value, counts/total

def get_codes(node, val='', codes = {}):
    new_val = val + str(node.code)

    if node.left:
        get_codes(node.left, new_val, codes)
    if node.right:
        get_codes(node.right, new_val, codes)

    if not node.left and not node.right:
        codes[node.value] = new_val

    return codes


def huffman_encoding(block: np.array):
    value, probs = get_probs(block)
    nodes = [Node(prob, str(val))for val, prob in zip(value, probs)]

    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.prob)

        right_node = nodes[0]
        left_node = nodes[1]

        right_node.code = 1
        left_node.code = 0


        new_prob = left_node.prob + right_node.prob
        new_value = left_node.value + right_node.value
        new_node = Node(new_prob, new_value, left_node, right_node)

        nodes.remove(left_node)
        nodes.remove(right_node)
        nodes.append(new_node)

    codes = get_codes(nodes[0])

    diagonals = list(np.hstack([block[::-1].diagonal(offset=x) for x in np.arange(-block.shape[0]+1,block.shape[1]-1)]))
    encoded_block = [codes[str(c)] for c in diagonals]

    return codes, encoded_block


if __name__ == '__main__':
    block = np.array([[1,2,3,4],[5,6,7,8],[9,8,7,6],[3,3,2,1]])
    print(huffman_encoding(block))