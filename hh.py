import numpy as np
arr=np.array([1,2,3,4])
print(np.sqrt((((arr-arr.mean())**2).sum())/4))
