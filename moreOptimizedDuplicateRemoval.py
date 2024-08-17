def removeDu(list1 : list)-> list :
    index = 0
    while index < len(list1):
        if list1[index] in list1[:index]:
            list1.remove(list1[index])
            continue
        index+=1    
    return list1




lis = [34.54,65,76,87,5,45,34,5,7,6,3,45,6,5,7,54]
print(removeDu(lis))
