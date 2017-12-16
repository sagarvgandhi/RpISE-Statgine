  #PROGRAM FOR MODE
  
  list=[1,3,3,6,6,6,4,2,2]
    
    def findFreq(l,x):
      freq=0
      for v in l:
        if v==x:
          freq=freq+1
      return x,freq       #Returns no. and it's corresponding freq
    
    def findMode(l):
      l1=[findFreq(list,v) for v in l]   #A list with tuple elements gets created
                                         #The first element of each tuple contains the nos.
                                         #The second element of each tuple contains the corresponding frequencies
     
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
      
      
  #PROGRAM FOR MEDIAN 
  
    def Sort(l):
      temp=0
      for i in range(len(l)-1,0,-1):    #Traversing the list in reverse order to cover all the list elements(Outer iteration)
        for j in range(i):            #For every outer iteration, check two neighbouring elements starting from last(inner iteration)
          if l[j]>l[j+1]:     #Here, if the second last element is greater than the last element swap them and perform this operation until the largest element is placed at the last at the end of each inner iteration
            temp=l[j]
            l[j]=l[j+1]
            l[j+1]=temp    
      return l             #Here, the returned list is a sorted list in ascending order
          
    def findMedian(l1):
      l=Sort(l1)           #Sort the list first
      x=len(l)/2
     
      if len(l)%2==0:      #If the list is even
        a=(l[x]+l[x-1])/2
        return a           #return the average of the middle two elements
      
      else:                #if the list is odd
        b=len(l)//2
        return l[b]        #return the middle element
      
      
      #PROGRAM FOR RANGE
      
       def findMax(l):    #algo to find the greatest no. in a list
      max=l[0]
      for i in l:
        if i>max:
          max=i
      return max   
    
    def findMin(l):    #algo to find the smallest no. in a list
      min=l[0]
      for i in l:
        if i<min:
          min=i
      return min
    
    def findRange(l):
      return findMax(list)-findMin(list)
      
      
      
