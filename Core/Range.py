    list=[2,5,4,8,7,6,9]
  
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
