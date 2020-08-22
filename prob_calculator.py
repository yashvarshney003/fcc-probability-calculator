import copy
import random
# Consider using the modules imported above.

class Hat(object):
  
  def __init__(self,**kwargs):
    self.contents =[]
    for items,values in kwargs.items():
      for i in range(values):
        self.contents.append(items)
    #print(self.contents)
  def draw(self,n):
    self.ret_str =[]
    self.dummy = []
    for i in range(len(self.contents)):
      self.dummy.append(self.contents[i])
    if(len(self.contents)<n):
      return self.contents
    else:
      for i in range(n):
        
        j = random.randint(0,len(self.dummy)-1)
        self.ret_str.append(self.dummy[j])
        del self.dummy [j:j+1]
    return self.ret_str



    
  



def experiment(hat, expected_balls, num_balls_drawn, num_experiments): 
  #number of expectatio completed
    count = 0
    for i in range(num_experiments):
        
        sample = hat.draw(num_balls_drawn)
        prob_success = True
        for key in expected_balls.keys():
            if sample.count(key) < expected_balls[key]:
                prob_success = False
                break
        if prob_success:
            count += 1

    return count / num_experiments
    





  

  