
#mode: 
#mode is the element having highest frequency in the list

    list=[1,2,3,4,5,4,3,2,1]   

    def freqTuple(l,x):
    freq=0
    for v in l:
        if v==x:
            freq=freq+1
    return x,freq                           #x is the element of your list
                                                   #freq is the number of times x occured in the list
                                                   #(e.g.element x=1 has freq=2 as it occured 2 times in the list)
                                                   #so a tuple(1,2) is returned
    def findMode(l):
        t=[freqTuple(l,x) for x in l]  #t is a list where its each element is a tuple containing 2 values each
                                                   #the tuple contains return values of the freqTuple funtion
                                                   #first value of each tuple contains list elements
                                                   #second value of tuple contains frequencies of corresponding elements
                                                   # for e.g. t will be t=[(1,2),(2,2),(3,2),(4,2),(5,1),(4,2),(3,2),(2,2),(1,2)]

        a=t[0][1]            #algorithm to find the highest number among 2nd elements(frequencies) of tuples
        for i in t:                            
            if(i[1]>a):           #i[1] here means second element of tuple i
                a=i[1]            #when for loop ends 'a' points to the highest frequency
                                  #(e.g.here a=2 because 2 is the highest number among all 2nd elements of tuples)
        c=[]   
        for i in t:
            if(i[1]==a):
                c.append(i)         #list c contains all tuples of highest frequency numbers(i.e. 2 here)
                                           #(e.g. c=[(1,2),(2,2),(3,2),(4,2),(4,2),(3,2),(2,2),(1,2)] )
                                           #(x=5 is not present in c as its freq=1 i.e. not highest)
                                           #but tuples get repeated in this process
        d=[]
        for i in c:
            if i not in d:             #this algorithm removes repeated tuples
                d.append(i)         #(e.g. d=[(1,2),(2,2),(3,2),(4,2)]  )
        for i in d:
            print(i[0])               #the first element of every tuple is printed as i[0] means first element of tuple i
                                           #(e.g. 1,2,3,4 is printed as our list has 4 modes) 

    print("The mode is")
    findMode(list)
