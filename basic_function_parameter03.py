# Create a function named find_smallest that takes a list of numbers as a parameter.
# Inside the function, find the smallest number in the given list.
# Return the smallest number.
def find_smallest(royxat):
    # royxat.sort()
    # return royxat[0]
    mi=royxat[0]
    for i in royxat:
        if mi>=i:
            mi=i
    return mi
royxat=[4,3,2,4,5,6,7,8,12]
print(find_smallest(royxat))