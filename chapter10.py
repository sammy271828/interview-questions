# CHAPTER 10: SORTING AND SEARCHING


from chapter2 import *


def list_merge(a: Node, b: Node):
    if not a:
        return b
    elif not b:
        return a
    else:
        if a.data < b.data:
            head = a
            other = b
        else:
            head = b
            other = a

        current = head

        while current and other:
            print(current.data)
            if current.next:
                if current.next.data > other.data:
                    temp = other
                    other = current.next
                    current.next = temp

                current = current.next
            else:
                current.next = other
                other = None
        return head
