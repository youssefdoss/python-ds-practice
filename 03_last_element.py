def last_element(lst):
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """
    #just check if lst and the auto return will catch the None
    if lst == []:
        return
        # return None
    else:
        return lst[-1]