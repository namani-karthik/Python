def select_second(L):
    """Return the second element of the given list. If the list has no second
    element, return None.
    """
    if(len(L)<2):
        return None
    else:
        return L[1]
lst=[1,2,3,45]
print(select_second(lst))
lst=[100]
print(select_second(lst))

lst=[(1,2,3,4),(2,3,4,5),(4,5,6,7)]
