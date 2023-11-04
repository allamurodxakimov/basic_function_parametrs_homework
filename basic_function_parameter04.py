# Create a function named calculate_average that takes a list of numbers as a parameter.
# Inside the function, calculate the average of all the numbers in the given list.
# Return the average.
# Return the average.
# def calculate_average(ls):
#     sum=0
#     for i in ls:
#         sum+=i
#     return sum/len(ls)
# data=[1,2,3,4,5,6,7,8,9]
# print(calculate_average(data))
def main(ls):
    sum =0
    for i in ls:
        sum+=int(i)
    return sum
n=int(input())
ls=[]
for i in range(1,n+1):
    ls.append(input())
print(main(ls))