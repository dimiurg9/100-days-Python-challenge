"""
two lists with no repeted numbers passed as arguments,
find out if list 2 is a sublist of list 1
"""

def is_sublist(list1, list2):
    count = 0
    for element in list1:
        for element2 in list2:
            if element == element2:
                # print(f"{element} is equal {element2}")
                count += 1
                break
            else:
                continue
                # print(f"element {element} is not equal {element2}")

    if count == len(list2):
        return True
    else:
        return False


def challenge():
    list1 = [1, 2, 3, 4, 5, 6, 7]
    list2 = [2, 3, 4]

    if is_sublist(list1, list2):
        print("is sublist")
    else:
        print("not sublist")

challenge()


