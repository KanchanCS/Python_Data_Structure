import random
def search(seq, v):
    for i  in seq:
        if i == v:
            return True
    return False
seq = [3, 1, 6, 8, 4, 0]


v= int(input('Enter elment to search '))

print(search(seq, v))