#segregate positive and negative

import numpy as np

a = np.array([9,-3,5,-2,-8,-6,1,3])


print(list(np.hstack((a[a<0], a[a>0]))))