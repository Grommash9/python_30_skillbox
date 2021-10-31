import collections


def can_be_poly(text):
    count_list = [y for x, y in collections.Counter(text).most_common()]
    if count_list.count(1) == 1 or count_list.count(1) == 0:
        for counters in count_list:
            if not counters // 2 == 0 and not counters != 1:
                return False
        return True
    return False


print(can_be_poly('ababc'))

print(can_be_poly('abbbc'))
