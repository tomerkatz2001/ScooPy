# In this example we know how to code the simple case of the else, but not sure about the then stmt.
# Since res is empty in the beginning of the program, the user must to give examples manually. 
#Or we can use examples from outer scope? We know res is the output var, so maybe somwthing with that?


def sort(l):
    res = []
    for i in l:
        for idx,j in enumerate(res):     
            if i < j:
                #! 1) i = 2, j = 4, idx = 0, res = [4,6] => res = [2, 4, 6]
                #! 2) i = 2, j = 4, idx = 1, res = [4,6] => res = [4, 5, 6]
            else:
                res += [i]
    return res


sort([1,7,5])
