
# MergeSort

def merge(list1, list2):
    (C,m,n) = ([], len(list1), len(list2))
    (i,j) = (0,0) # current position in list1, list2
    while i+j < m+n: # ! i+j  is number of elements merged so far
        if i ==m: # ! case 1 : list1 is empty
            C.append(list2[j])
            j = j+1
        elif j == n : # ! case 2 : list2 is empty
            C.append(list1[i])
            i = i+1
        elif list1[i] <= list2[j]: # ! case 3 : Head of list1 is smaller
            C.append(list1[i])
            i = i+1
        elif list1[i] >= list2[j]: # ! case 4 : Head of list2 is smaller
            C.append(list2[j])
            j = j+1
            
    return(C)
    
    
def  mergeSort(list1, left, right):
    # ! Sort the slice list1[left:right]
    
    if right -left <= 1: # ! base Case
        return(list1[left:right])
    
    if right -left > 1: # ! Reverse Case 
        mid = (left + right)//2
        L = mergeSort(list1, left, mid)
        R = mergeSort(list1, mid, right)
        return(merge(L,R))