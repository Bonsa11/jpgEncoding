
class Node:
    def __init__(self, prob, value, left=None, right=None):
        # probability of symbol
        self.prob = prob

        # value 
        self.value = value

        # left node
        self.left = left

        # right node
        self.right = right

        # tree direction (0/1)
        self.code = ''

