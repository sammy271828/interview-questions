# CHAPTER 1: ARRAYS AND STRINGS

def isUnique(s: str):
    size = len(s)

    table = {}

    for i in range(0, size):
        if s[i] in table:
            return False
        table[s[i]] = True

    return True


def checkPerm(s: str, t: str):
    table = {}

    for a in s:
        if a not in table:
            table[a] = 1
        else:
            table[a] += 1

    for a in t:
        if a not in table:
            return False
        else:
            table[a] -= 1

    for a in table:
        if table[a] != 0:
            return False

    return True


def permPalindrome(s: str):
    table = {}

    s = s.lower()

    for a in s:
        if a == ' ':
            continue

        if a not in table:
            table[a] = 1
        else:
            table[a] += 1

    odd_count = 0
    sum = 0

    for a in table:
        if table[a] % 2 == 1:
            odd_count += 1
        sum += table[a]

    if sum % 2 == 0 and odd_count == 0:
        return True
    elif sum % 2 == 1 and odd_count == 1:
        return True
    else:
        return False


def oneAway(s: str, t: str):
    if (len(s) - len(t)) ** 2 > 1:
        return False
    else:
        table = {}

        for a in s:
            if a not in table:
                table[a] = 1
            else:
                table[a] += 1

        for a in t:
            if a not in table:
                table[a] = -1
            else:
                table[a] -= 1

        nonzero_count = 0

        for a in table:
            if table[a] != 0:
                nonzero_count += 1

        if len(s) == len(t) and nonzero_count == 2:
            return True
        elif len(s) != len(t):
            if nonzero_count != 1:
                return False
            else:
                return True
        else:
            return False
