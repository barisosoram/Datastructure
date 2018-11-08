
# correct too
l = [1,2,4,6,7,8,9]
def recursive(l):
    if len(l) == 0:
        return []  # base case
    else:
        return [l.pop()] + recursive(l)  # recusrive case

print("This is before reverse l list: ",l)
print("This is after reverse l list: ",recursive(l))