def freq_counter(nums):
    counter = {}

    for num in nums:
        counter[num] = counter.get(num , 0) + 1
    return counter

def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    return freq_counter(str(num1)) == freq_counter(str(num2))
    
