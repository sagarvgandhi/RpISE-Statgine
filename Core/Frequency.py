    def findFreq(l,x):    #the list along with a no. whose freq we wish to find in the list are passed as the two arguments
      freq=0
      for i in l:
        if i==x:
          freq=freq+1     #freq counter is incremented every time a match is found
      return x,freq       #Returns the no. with it's corresponding freq
    
