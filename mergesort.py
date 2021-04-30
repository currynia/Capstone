def merge(l,r): 
    sortedarray = []
    while len(l) > 0 and len(r) > 0:
        if l[0]['distance'] > r[0]['distance']:
            element = r.pop(0)
        else:
            element = l.pop(0)
        sortedarray.append(element)
    sortedarray = sortedarray + l + r
    return sortedarray
    
def mergeSort(array):
    '''
Sorting function that uses Merge Sort to sort an array of bus stops based on their distance from a specified coordinate
Args:
    array (list): List containing the bus stop distances with respect to the specified coordinate 

Returns:
    list: List with the bus stop distances sorted from the nearest bus stop from that point to the furthest bus stop from that point
'''
    if len(array) > 1:
        mid = len(array)//2
        l = array[:mid]
        r = array[mid+1:]
        l = mergeSort(l)
        r = mergeSort(r)
        sortedarray = merge(l,r)
        return sortedarray
    else:
        return array
