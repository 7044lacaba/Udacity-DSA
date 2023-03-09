


def half_round_up(value):
    if value % 2 == 1:
        return int((value / 2) + 0.5)
    else:
        return int(value / 2)





# 2 2 3 3 4 4

test_list = [0,1,2,3,4,5,6]

print(len(test_list))

print(half_round_up(7))


print(test_list[4])


test_list = test_list[:4]
print(test_list)