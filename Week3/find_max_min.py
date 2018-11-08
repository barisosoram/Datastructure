#BARISO SORA

#Find Maximum value in the sequences of list L
def maximum(L):
    if len(L)==1:
        return L[0]
    else:
        return max(L[0],maximum(L[1:]))
        
    
L=[2,4,100,6,23,46,86,0]  #This is assumed sample  list of sequence(this program work for any list).
print("This is maximum value in the list L:",maximum(L))


#Find Minimum value in the sequences of list L
def minimum(L):
    if len(L)==1:
        return L[0]
    else:
        return min(L[0],minimum(L[1:]))  
    
L=[2,4,100,6,23,46,86,0]  #This is assumed sample  list of sequence(this program work for any list).
print("This is minimum value in the list L:",minimum(L))


