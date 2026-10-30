def exercise1(tp,fp,fn):
  if type(tp) != int: 
    print("tp must be int")
    return
  if type(fn) != int: 
    print("fn must be int")
    return
  if type(fp) != int: 
    print("fp must be int")
    return
  if(tp*fp*fn == 0): 
    print("tp and fp and fn must be zero")
    return
  precision = tp/(tp+fp)
  recall = tp/(tp+fn)
  F1score = 2*(precision*recall)/(precision + recall)
  print(f"precision is {precision}\nrecall is {recall}\nf1-score is {F1score}")
exercise1(2,3,4)
exercise1('a',3,4)
exercise1(2,'a',4)
exercise1(2,3,'a')  
exercise1(2,3,0)  
exercise1(2.1,3,0)  
