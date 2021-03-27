class sortalgo:
    def sort_distance(self,array):
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
        def mergesort(array):
            if len(array) > 1:
                mid = len(array)//2
                l = array[:mid]
                r = array[mid+1:]
                l = mergesort(l)
                r = mergesort(r)
                sortedarray = merge(l,r)
                return sortedarray
            else:
                return array
        return mergesort(array)