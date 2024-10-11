kume1 = set(["data","python"])
kume2 = set(["data","function","qcut","lambda","python","miuul"])

def func(set1,set2):
    if(kume1.issuperset(kume2)):
        return kume1.intersection(kume2)
    else:
        return kume2.difference(kume1)

func(kume1,kume2)
        