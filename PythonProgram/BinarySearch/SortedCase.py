def BinarySearch(seq, value, start, end):
    if(end -start == 0):
        return False
    mid =(start+end)//2
    
    if value == seq[mid]:
        return(True)
    if value < seq[mid]:

        return(BinarySearch(seq, value, start, mid))
    else:

        return(BinarySearch(seq, value, mid+1, end))
  
start = int(input("Enter start value"))
end = int(input("Enter End Value"))

seq =list(range(start, end))

print(seq)
value = int(input("Enter search value"))
    
print(BinarySearch(seq, value, start, end))
