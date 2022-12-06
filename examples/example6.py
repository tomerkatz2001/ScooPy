#When synthesizing the whole function again. we can also collect the aux variables that were used in this spesific solution.

#! 1) l = [1,7,5] => sort(l) = [1,5,7] #added automatically after the function is complete.
def sort(l):
    res = []
    for i in l:
        added = False
        for idx,j in enumerate(res):     
            if i < j:
                #! 1) i = 2, j = 4, idx = 0, res = [4,6] => res = [2, 4, 6]
                #! 2) i = 2, j = 4, idx = 1, res = [4,6] => res = [4, 5, 6]
                res.insert(idx, i)
                added = True
                break
        if not added:
            res += [i]
    return res


sort([1,7,5])
