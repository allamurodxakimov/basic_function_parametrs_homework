# Create a function named calculate_sum that takes a list of numbers as a parameter.
# Inside the function, calculate the sum of all the numbers in the given list.
# Return the sum.
def calculate_sum(data):
    # ls=sum(data)
    sum=0
    for i in data:
        sum+=i
    return sum
data = [1,2,3,4,7,8,9,12,34,5]
print(calculate_sum(data))