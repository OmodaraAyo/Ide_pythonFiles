def dict_cube(number):
    dict ={}
    for i in number:
        dict[i] = i**3
    return dict
print(dict_cube([1,2,3,4,5]))