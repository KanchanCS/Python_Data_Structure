# Sorting

### Searching for a value 
    
   * Unsorted array - linear Scan, O(n)
   * Sorted array - binary Search, O(log(n))

### Other advantages of sorting

   * Finding median value, midpoint of sorted array
   * Checking for duplicates
   * Building a frequency table of values

# How to sort ?

* You are a Teaching Assistant for a course
* This instructor gives you a stack of exam answers papers with marks, ordered randomly
* You task is to arrange them is descending order


```python

# Selection Sort

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
            

```

# Analysis of Selection Sort

* Finding minimum in unsorted segment of length k requires one scan, k steps

* In each iteration, segment to be scanned reduces by 1

* T(n) = n+(n-1)+(n-2)+ ..........+1 = n(n+1)/2 = O(n^2)
