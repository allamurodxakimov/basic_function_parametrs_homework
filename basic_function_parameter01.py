# Create a function named get_data that takes no parameters.
# Inside the function, define a list variable named data and assign it [1, 2, 3, 4, 5].
# Return the data list.
def get_data():
    # data=[1,2,3,4,5]
    data=[]
    for i in range(1,6):
        data.append(i)
    return data
print(get_data())
