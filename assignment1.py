# Name: David KIm
# OSU Email: kimda5@oregonstate.edu 
# Course: CS261 - Data Structures
# Assignment: 1
# Due Date: 10/17
# Description:



import random
from static_array import *
import math

# ------------------- PROBLEM 1 - REVERSE -----------------------------------

def reverse(arr: StaticArray) -> None:
    """
    Takes in an array and reverses the order in place 
    """
    
    length = arr.length() -1 
    hold = 0 #temp container for number being replaced 
    move = 0 #starts from begining increments to halfway point
    # print(arr)
    while length > 1:
        hold = arr.get(length)
        arr.set(length,arr.get(move)) #shifts right to left 
        arr.set(move,hold) #shifts left to right 
        if move < length/2:
            move += 1 
        length -= 1 
        
        

# ------------------- PROBLEM 2 - ROTATE ------------------------------------

def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """
    Shifts the array left or right for the number of steps 
    """
    length = arr.length() 
    
    shift = + length - (steps% length)
    hold = 0
    # hold2 = arr.get(0) 
    # locCounter = 1 
    # print("shift amount is : " + str(shift))
    
    while shift >= 1:
        hold = arr[0]
        for x in range(length-1): #shifts it once to the left 
            arr[x] = arr[x+1]
        arr[length-1] = hold 
        shift -= 1

# ------------------- PROBLEM 3 - SA_RANGE ----------------------------------

def sa_range(start: int, end: int) -> StaticArray:
    """
    takes in two integers and returns an array of all numbers between the two integers, inclusve 
    """
    back = False
    length = 0 
    # count = 0
    
    if end > start:
        back = True 
        length = end - start + 1 
    else:
        length = start - end + 1 
        
    returnArr = StaticArray(length) 
    
    if back:
        for x in range(length):
            returnArr.set(x,start + x )

    else:
        for x in range(length):
            returnArr.set(x, start - x)

            
    return returnArr

# ------------------- PROBLEM 4 - IS_SORTED ---------------------------------

def is_sorted(arr: StaticArray) -> int:
    """
    checks static array to see if it is sorted and returns ascending (1) or descending (-1) or not sorted (0)
    """
    print(arr)
    if arr.get(0) > arr.get(arr.length()-1): #maybe descending 
        for x in range(arr.length()-1):
            if arr[x] < arr[x+1]: #if x is less than x+1 then it means it is not sorted, bc it should always be greater than 
                return 0
        return -1
                
    else: 
        for x in range(arr.length()-1):
            if arr[x] > arr[x+1]: #if x is greater than x+1 then it means it is not sorted, bc it should always be less than 
                return 0
        return 1
    


# case = ['apple']
# arr = StaticArray(len(case))
# for i, value in enumerate(case):
#     arr[i] = value
# print(is_sorted(arr))
    
# test_cases = (
# [-100, -8, 0, 2, 3, 10, 20, 100],
# ['A', 'B', 'Z', 'a', 'z'],
# ['Z', 'T', 'K', 'A', '5'],
# [1, 3, -10, 20, -30, 0],
# [-10, 0, 0, 10, 20, 30],
# [100, 90, 0, -90, -200],
# ['apple']
# )
# for case in test_cases:
#     arr = StaticArray(len(case))
#     for i, value in enumerate(case):
#         arr[i] = value
#     result = is_sorted(arr)
#     space = "  " if result and result >= 0 else " "
#     print(f"Result:{space}{result}, {arr}")
        
        

# ------------------- PROBLEM 5 - FIND_MODE -----------------------------------

def find_mode(arr: StaticArray) -> (int, int):
    """
    takes and ordered list and returns the frequency and value of most frequent item 
    """
    topFreq = 0
    topVal = 0
    curFreq = 1
    curVal = 0
    
    
    for x in range(arr.length()-1):

        if arr[x] == arr[x+1]:
            curVal = arr[x] 
            curFreq += 1
        else:
            curFreq = 1
        if curFreq > topFreq:
            topFreq = curFreq
            topVal = curVal
        
    return (topVal,topFreq)


# case = ["zebra", "sloth", "otter", "otter", "moose", "koala"]
# arr = StaticArray(len(case))
# for i, value in enumerate(case):
#     arr[i] = value

# print(find_mode(arr))
    
    
# ------------------- PROBLEM 6 - REMOVE_DUPLICATES -------------------------

def remove_duplicates(arr: StaticArray) -> StaticArray:
    """
    takes in a sorted list and returns a static array 
    """
    length = 1 
    for x in range(arr.length()-1):
        if arr[x] != arr[x+1]:
            length += 1 
    
    newArr = StaticArray(length)
    count = 0
    for x in range(arr.length()-1):
        if arr[x] != arr[x+1]:
            newArr.set(count,arr[x])
            count += 1 
    newArr.set(count,arr[arr.length()-1])
    return newArr
        

# case =  [5, 5, 5, 4, 4, 3, 2, 1, 1]
# arr = StaticArray(len(case))
# for i, value in enumerate(case):
#     arr[i] = value

# print(arr)
# print(remove_duplicates(arr))

# ------------------- PROBLEM 7 - COUNT_SORT --------------------------------

def count_sort(arr: StaticArray) -> StaticArray:
    """
    takes in a static array of unsorted values and returns a new descending static array
    """
    highVal = -999999999999999 
    count = 1
    length = arr.length()
    setCounter = 0
    
    newArr = StaticArray(arr.length())
    while length > 0:
        for x in range(arr.length()):
            if arr[x] > highVal:  #find the largest value 
                highVal = arr[x]
                count = 1 
            elif arr[x] == highVal:
                count += 1 
        print(highVal,count)
        for x in range(count): #adds the highest value to new array
            newArr.set(setCounter,highVal)
            setCounter +=1 
        
        for x in range(arr.length()):
            if arr[x] == highVal: #remove all the high values from the list 
                arr[x] = -999999999999999
        #reset so we can keep track of next highest value        
        highVal = -999999999999999
        length -= count 
        count = 1         
    return newArr
                
    
    
# case =   [-100320, -100450, -100999, -10000]
# arr = StaticArray(len(case))
# for i, value in enumerate(case):
#     arr[i] = value


# print(count_sort(arr))


array_size = 5_000_000
min_val = random.randint(-10**9, 10**9 - 998)
max_val = min_val + 998
case = [random.randint(min_val, max_val) for _ in range(array_size)]
arr = StaticArray(len(case))
for i, value in enumerate(case):
    arr[i] = value
print(f'Started sorting large array of {array_size} elements')
result = count_sort(arr)
print(f"Finished sorting large array of {array_size} elements")

# ------------------- PROBLEM 8 - SORTED SQUARES ---------------------------

def sorted_squares(arr: StaticArray) -> StaticArray:
    """
    TODO: Write this implementation
    """
    pass

# ------------------- BASIC TESTING -----------------------------------------


# if __name__ == "__main__":

    print('\n# reverse example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)

    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100, 2 ** 28, -2 ** 31]:
        space = " " if steps >= 0 else ""
        print(f"{rotate(arr, steps)} {space}{steps}")
    print(arr)

    print('\n# rotate example 2')
    array_size = 1_000_000
    source = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(f'Started rotating large array of {array_size} elements')
    rotate(arr, 3 ** 14)
    rotate(arr, -3 ** 15)
    print(f'Finished rotating large array of {array_size} elements')

    print('\n# sa_range example 1')
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-95, -89), (-89, -95)]
    for start, end in cases:
        print(f"Start: {start: 4}, End: {end: 4}, {sa_range(start, end)}")

    print('\n# is_sorted example 1')
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '5'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        result = is_sorted(arr)
        space = "  " if result and result >= 0 else " "
        print(f"Result:{space}{result}, {arr}")

    print('\n# find_mode example 1')
    test_cases = (
        [1, 20, 30, 40, 500, 500, 500],
        [2, 2, 2, 2, 1, 1, 1, 1],
        ["zebra", "sloth", "otter", "otter", "moose", "koala"],
        ["Albania", "Belgium", "Chile", "Denmark", "Egypt", "Fiji"]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value

        result = find_mode(arr)
        if result:
            print(f"{arr}\nMode: {result[0]}, Frequency: {result[1]}\n")
        else:
            print("find_mode() not yet implemented\n")

    print('# remove_duplicates example 1')
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)

    print('\n# count_sort example 1')
    test_cases = (
        [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
        [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
        [10100, 10721, 10320, 10998], [-100320, -100450, -100999, -100001],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        before = arr if len(case) < 50 else 'Started sorting large array'
        print(f"Before: {before}")
        result = count_sort(arr)
        after = result if len(case) < 50 else 'Finished sorting large array'
        print(f"After : {after}")

    print('\n# count_sort example 2')
    array_size = 5_000_000
    min_val = random.randint(-1_000_000_000, 1_000_000_000 - 998)
    max_val = min_val + 998
    case = [random.randint(min_val, max_val) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(case):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = count_sort(arr)
    print(f'Finished sorting large array of {array_size} elements')

    print('\n# sorted_squares example 1')
    test_cases = (
        [1, 2, 3, 4, 5],
        [-5, -4, -3, -2, -1, 0],
        [-3, -2, -2, 0, 1, 2, 3],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(sorted(case)):
            arr[i] = value
        print(arr)
        result = sorted_squares(arr)
        print(result)

    print('\n# sorted_squares example 2')
    array_size = 5_000_000
    case = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(sorted(case)):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = sorted_squares(arr)
    print(f'Finished sorting large array of {array_size} elements')
