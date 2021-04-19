# CHAPTER 2: LINKED LISTS



class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

    def print(self):
        if not self:
            print("error")
        else:
            temp = self
            result = ''

            while temp.next:
                result += str(temp.data) + '->'
                temp = temp.next

            result += str(temp.data)
            print(result)

    def remove_dups(self):
        current = self
        if not current.next:
            return

        else:
            values = []
            prev = current
            values.append(current.data)
            current = current.next

            while current:
                if current.data in values:
                    prev.next = current.next

                else:
                    values.append(current.data)
                    prev = current

                current = current.next

    def remove_dups_inefficiently(self):
        current = self
        if not current.next:
            return

        else:
            while current.next:
                current_value = current.data
                first = current

                while first.next:
                    second = first.next
                    while second.data == current_value:
                        second = second.next

                    first.next = second
                    second = second.next
                    first = first.next

                current = current.next

    def kth_to_last(self, k: int):
        if k <= 0 or not self:
            return "Error"
        else:
            first = self

            while k > 1 and first.next:
                first = first.next
                k -= 1

            if k > 1:
                return "Error"
            else:
                second = self
                while first.next:
                    first = first.next
                    second = second.next

                return second.data


def add_lists(L: Node, M: Node):
    carry = 0
    sum = Node(0)

    current_sum = sum
    current_L = L
    current_M = M

    while current_L or current_M:
        if not current_L:
            L_value = 0
        else:
            L_value = current_L.data

        if not current_M:
            M_value = 0
        else:
            M_value = current_M.data

        sum_value = L_value + M_value + carry

        current_sum.data = sum_value % 10
        carry = sum_value // 10

        if current_M:
            current_M = current_M.next
        if current_L:
            current_L = current_L.next

        if current_L or current_M:
            current_sum.next = Node(0)
            current_sum = current_sum.next
        elif carry != 0:
            current_sum.next = Node(carry)

    return sum


# NOT DONE!
def add_forward(L: Node, M: Node):
    current_L = L
    current_M = M

    while current_L.next and current_M.next:
        current_L = current_L.next
        current_M = current_M.next

    if current_M.next:
        longer = M
        shorter = L
        current_longer = current_M
    else:
        longer = L
        shorter = M
        current_longer = current_L

    current_longer = current_longer.next
    sum = Node(0)
    current_sum = sum

    while current_longer.next:
        current_sum.data = longer.data
        current_sum.next = Node(0)
        current_sum = current_sum.next

        longer = longer.next
        current_longer = current_longer.next

    value = 0

    while shorter:
        num = shorter.data + longer.next.data
        carry = num // 10
        current_sum.data = carry + value

        value = num % 10

        current_sum.next = Node(0)
        current_sum = current_sum.next
        shorter = shorter.next
        longer = longer.next

    return sum


def create(input: list):
    if len(input) == 0:
        return None
    else:
        head = Node()
        temp = head

        i = 0

        while i < len(input):
            if i + 1 < len(input):
                temp.data = input[i]
                temp.next = Node()
                temp = temp.next
            else:
                temp.data = input[i]

            i += 1

        return head


def reverse(X: Node):
    if not X:
        return

    current = X
    prev = None

    while current.next:
        second = current.next
        current.next = prev
        prev = current
        current = second

    current.next = prev
    return current


def circular(X: Node):
    current = X
    index = 0

    while current.next:
        current = current.next
        index += 1

        runner = X
        runner_val = 0

        while runner_val < index:
            if runner == current:
                return current
            else:
                runner = runner.next
                runner_val += 1

    return None
