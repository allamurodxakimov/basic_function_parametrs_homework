# Create a function named count_vowels that takes a string as a parameter.
# Inside the function, count the number of vowels (a, e, i, o, u, A, E, I, O, U) in the given string.
# Return the count of vowels.
def count_vowels(st):
    ls="a","e","u","i","o","A","E","I","O","U"
    # c={""}
    # for i in st:
    #     if i in ls:
    #         c.add(i)
    # return len(list(c))-1
    c=0
    for i in st:
        if i in ls:
            c+=1
    return c
string = "abshnajdzyweag8epdc eadsuybcln eiud dnui euicio"
print(count_vowels(string))