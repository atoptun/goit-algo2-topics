

def test_1():
    numbers = [1, 2, 3, 4, 5]

    for i in map(lambda x: x ** 2, numbers):
        print(i)

    print("Test 1 completed.")


def test_2():
    numbers = [1, 2, 3, 4, 5]

    squared_nums = list(map(lambda x: x ** 2, numbers))
    print(squared_nums)

    print("Test 2 completed.")


def test_3():
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]
    sum_nums = map(lambda x, y: x + y, nums1, nums2)

    print(list(sum_nums))

    print("Test 3 completed.")


def test_4():
    nums = [1, 2, 3, 4, 5]
    squared_nums = [x * x for x in nums]
    print(squared_nums)

    print("Test 4 completed.")



if __name__ == "__main__":
    test_1()
    test_2()
    test_3()
    test_4()
