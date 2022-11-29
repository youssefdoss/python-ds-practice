def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of items.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    # max_value = 0
    # max_key = None
    # num_freq = {}

    # for num in nums:
    #     num_freq[num]=num_freq.get(num, 0)+1

    # for key in num_freq:
    #     if num_freq[key] > max_value:
    #         max_key = key
    #         max_value = num_freq[key]
    
    # return max_key


    num_freq = {}
    
    
    for num in nums:
        num_freq[num] = num_freq.get(num, 0) + 1

    max_value = max(num_freq.values())
    
    for (num, count) in num_freq.items():
        if count == max_value:
            return num

        
