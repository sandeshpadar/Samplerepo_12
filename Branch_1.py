# How to find missing number......
# Solution....

def find_missing_number(nums):
    n = len(nums) +1
    expected_sum = n*(n-1)//2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

number= [0,1,2,3,4,5,7]
missing_number = find_missing_number(number)
print(f'The missing number is {missing_number}')
