# CHAPTER 4: GRAPHS AND TREES

from chapter2 import *


class BNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def print(self):
        if not self:
            print("error")
        else:
            pass

    def in_order(self, arr=[]):

        if not self:
            return
        else:
            if self.left:
                self.left.in_order(arr)

            arr.append(self.data)

            if self.right:
                self.right.in_order(arr)

        return arr

    def pre_order(self, arr=[]):
        pass

    def post_order(self, arr=[]):
        pass
