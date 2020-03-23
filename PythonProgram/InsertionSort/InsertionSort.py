def insertionSort(seq):
    for sliceEnd in range(len(seq)):
        
        # Build longer and longer sorted slices
        # In each iteration seq[0:sliceEnd] already sorted
        
        
        # Move First element after sorted slice left
        # till it is in the correct place
        
        pos = sliceEnd
        
        while pos > 0 and  seq[pos] < seq[pos-1]:
            (seq[pos], seq[pos-1]) = (seq[pos-1], seq[pos])
            pos = pos - 1
        
seq = list(range(5000,0,-1))

insertionSort(seq)

print(seq)