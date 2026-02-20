
def function_1(data):
    ret_list = []
    for val in data:
        if val%2 != 0:
            ret_list.append(val)

    return ret_list
print(function_1([2,3,4,5,6,7,8,9,11,12,14,18]))


