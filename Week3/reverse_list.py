#BARISO SORA
#I need comment and feedback before summit it.


def reversList(L):
    if len(L) == 1:       
        return L #base case
    else:
        return reversList(L[1:]) + [L[0]] # Recursively reverse list of element  and concatenate first element of list to end  at last. 
    
L=[1,2,3,4,8,9,10] # This is sample of list. We can use any list including string list like L=['A','B','C'] or we can accept list from user with different data type.
print("This is before reverse L list: ",L)
print("This is after reverse L  list: ",reversList(L))
