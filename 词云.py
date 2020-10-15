import numpy as np
cond1=np.array([1,0,0,1])
cond2=np.array([0,1,0,1])
result=np.where(cond1&cond2,0,np.where(cond1,1,np.where(cond2,2,3)))
print(result)