def selectionSort(l):
    # scan slice l[0:len(l)] , l[1:len(l)], .........
    for start in range(len(l)):
        
        #find the minimum value in slice...
        
        minpos = start
        
        for i in range(start, len(l)):
            
            if l[i] < l[minpos]:
                minpos =  i
        # and  move  it to start of slice
        
        (l[start], l[minpos]) = (l[minpos], l[start])
            

l = [2,3,4,5,6,7,8,9]
print(len(l))

for start in range(len(l)):
    print(start)