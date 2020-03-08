# Sequences of values

* Two basic Ways of storing a sequence of values
	* Arrays
	* Lists
* What's the differcence?

## Arrays
* Single block of memory, elements of uniform type
	* Typically size of sequence is fixed in advance
* Indexing is fast
	* Access __seq[i]__ in constant time for any i
	* Compute offset form start of memory block
* Inserting between __seq[i]__ and __seq[i+1]__ is expensive
* Contraction is expensive

## Lists
* Values scattered in memory
	* Each element point to the next - __"linked"__ list
	* Flexible Size
* Follow i links to access __seq[i]__
	* Cost proprotional to i 
* Inserting or deleting an element is easy 
	* __"Plumbing"__
	
# Operations 

* Exchange __seq[i]__ and __seq[j]__
	* Constant time in array, linear time in list
* Delete __seq[i]__  or insert __v__ after __seq[i]__ 
	* Constant time in list (if we are already at __seq[i]__ )
	* Linear time in array
* Algorithms on one data structure may not transfer to another
	* Example: **Binary Search**
	
# Search Problem

* Is a value v present in a collection seq ?
* Does the structure of __seq__ matter ?
 * Array vs Lists
* Does the organization of the information matter ?
 * Values sorted/unsorted
 
# The Unsorted Case
 
```python

seq = [4, 6, 7, 1, 9, 3, 5 ]
v = 4

def search (seq, v):
 for x in seq:
  if x == v:
   return True
 return Flase
	
# if number is find ! Output is True 
# if number is not !  Output is False

```

# Search a sorted sequence

* What if seq is sorted?
	* Compare v with midpoint of __seq__
	* if midpoint is v, the value is found 
	* if v < midpoint, search left half of __seq__
	* if v > midpoint, search right half of __seq__
* __Binary Search__
 
# Binary Search 

```Python

def binary_search(seq,v,l,r):
    # search for v in seq[l:r], seq is sorted
    if (r-l == 0):
        return False
    mid = (l+r)//2
    if(v==seq[mid]):
        return True
    if (v < seq[mid]):
        return (binary_search(seq,v,l,mid))
    else:
        return (binary_search(seq,v,mid+1, r))

```
	
