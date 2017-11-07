def answer(l):

    #given a list of strings, separate it into 3 lists
    #based on the index of the strings in the list
    def splits(l, index):
        one = []
        two = []
        three = []
        split = []
        
        #split individual strings by period
        for str in l:
            split.append(str.split('.'))
    
        #go though the split array and create 3 lists
        #based on the splits
        for iX, x in enumerate(split):
            done = 0
            
            for iY, y in enumerate(x):
                if (iY == 0):
                    one.append(int(y))
                if (iY == 1):
                    two.append(int(y))
                if (iY == 2):
                    three.append(int(y))
                
                if (done == 0):
                    try:
                        split[iX][1]
                    except IndexError:
                        two.append(-1)
                        three.append(-1)
                        done = 1
                if (done == 0):
                    try:
                        split[iX][2]
                    except IndexError:
                        three.append(-1)
                        done = 1
        
        #return the list of index we want
        if (index == 3):
            return three
        if (index == 2):
            return two
        if (index == 1):
            return one
    
    #insertionsort
    #sort the given list, based on each sort that takes
    #place do the same for the input list based on indexs
    def sort(list, l):
        for iI in range(1, len(l)):
            key = list[iI]
            key2 = l[iI]
            iJ = iI - 1
            while (iJ >= 0) and (list[iJ] > key):
                list[iJ+1] = list[iJ]
                l[iJ+1] = l[iJ]
                iJ = iJ - 1
            list[iJ+1] = key
            l[iJ+1] = key2

    #basically radix sort
    #sort by index 3 first
    three = splits(l, index=3)
    sort(three, l)
    
    #then sort by index 2    
    two = splits(l, index=2)
    sort(two, l)

    #finally sort by index 1
    one = splits(l, index=1)
    sort(one, l)

    return l