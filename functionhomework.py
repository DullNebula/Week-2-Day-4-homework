#Complete the questions at the bottom of the notebook below and upload it to github.


#Q1: Create a function that returns the sum of the two lowest positive numbers
#  given an array of minimum 4 positive integers.
#  No floats or non-positive integers will be passed.


from itertools import count


number_list = [143, 27, 25, 255]

def sum_two_smallest_numbers(twosmol):
    twosmol.sort()
    return twosmol[0] + twosmol[1]

print(number_list())
#Q2: Given an array of integers.Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.
#  0 is neither positive nor negative.
#If the input array is empty or null, return an empty array.

def number_counter(numlist):
    count = 0
    adds = 0
    if numlist == []:
        return []
    if numlist == None:
        return []
    for num in numlist:

        if num > 0:
            count += 1
        if num < 0:
            adds += num


    return [count, adds]

print(number_counter())