
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
      
        
        
