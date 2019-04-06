def knapsack_BB(items, capacity):
    NAME, WEIGHT, VALUE = range(3)

    # order by max value per item weight
    items = sorted(items, key=lambda item: item[VALUE] / float(item[WEIGHT]), reverse=True)
    print(items)
    # Sack keeps track of max value so far as well as the count of each item in the tab
    tab =  [0 for i in items]

    #INITIALIZING
    max_weight=capacity
    #Make a greedy choosing
    #Take as much as first item, then second then continue...
    for i,item in enumerate(items):
        maximum=int(max_weight/item[WEIGHT])
        if (maximum<0):
            maximum=0
        tab[i]=maximum
        max_weight=max_weight-(maximum*items[i][WEIGHT])

    current_value=sum(items[i][VALUE] * n for i, n in enumerate(tab))
    max_value=current_value

    #REDUCTION AND EXPANASION MOVE
    set= tab.copy()
    flag=True
    while flag:

        #Reduction and Expansion Step Loop Here
        #Seek the least significant (not zero) digit
        leastSignificant= len(set)-1
        for i in range(leastSignificant,-1,-1):
            if set[i]!= 0 :
                leastSignificant=i
                break
        #Reduction Move
        #Decrement the least significant digit or set it to 0 (zero) if it's on last position
        if (leastSignificant==len(set)-1):
            max_weight=max_weight+(set[leastSignificant]*items[leastSignificant][WEIGHT])
            set[leastSignificant]=0
        else:
            max_weight=max_weight+items[leastSignificant][WEIGHT]
            set[leastSignificant]-=1
            for i in range (leastSignificant+1, len(set)):
                maximum=int(max_weight/items[i][WEIGHT])
                if maximum >0:
                    set[i] = maximum
                else:
                    maximum=0
                max_weight-=(maximum*items[i][WEIGHT])
            current_value=sum(items[i][VALUE] * n for i, n in enumerate(set))

            if (current_value>max_value):
                max_value=current_value
                tab=set.copy()
        itemCount=sum(set)
        if itemCount==0:
            flag=False
    bagged = sorted((items[i][NAME], n) for i, n in enumerate(tab) if n)

    return max_value,max_weight,bagged
'''
capacity=8
items= [['a', 1, 10], ['b', 3, 40],['c', 4, 50],['d', 5, 70]]

print(items)
print (knapsack_BB(items,capacity))

'''