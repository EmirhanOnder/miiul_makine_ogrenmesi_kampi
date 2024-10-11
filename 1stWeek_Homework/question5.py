l = [2,13,18,93,22]

def func(lst):
    odd = []
    even = []
    for i in lst:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even,odd

even_list , odd_list = func(l)