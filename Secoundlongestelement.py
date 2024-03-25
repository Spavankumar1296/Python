def find_second_largest(list1):
    list1=[9,8,6,5,4,4,3,2];
    if len(list1) < 2:
        return None

    largest = float('-inf')
    second_largest = float('-inf')
    
    for num in list1:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    return second_largest
# print(second_largest)