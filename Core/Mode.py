
    list=[1,3,3,6,6,6,4,2,2]
    
    def findFreq(l,x):
      freq=0
      for v in l:
        if v==x:
          freq=freq+1
      return x,freq       #Returns no. and it's corresponding freq
    
    def findMode(l):
      l1=[findFreq(list,v) for v in l]   #A list with tuple elements gets created
                                         #The first elements of each tuple contains the nos.
                                         #The second elements of each tuple contains the corresponding frequencies
     
      a=l1[0][1]         #'a' is initialised with first tuple element from l1
      c=[]
      
      for i in l1:
        if i[1]>a:
          a=i[1]         #Now 'a' has the max freq elements from l1(only freq not it's corresponding nos.)
          
      for i in l1:
        if i[1]==a:
          c.append(i)    #'c' is a list which will contain only the max freq tuple elements from l1(including their duplicates)
          
      d=[]
      for i in c:
        if i not in d:
          d.append(i)    #algo to remove duplicates 
          
      for i in d:
        print(i[0])      #prints only the nos. corresponding to the max frequencies
        
     print("The mode is")
     findMode(list)
                          
