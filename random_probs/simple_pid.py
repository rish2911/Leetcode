import numpy as np

a = [[1,2], [2,3]]
b = np.array(a)

print(b[1][1])

k_p, k_i, k_d = 0,0,0
integral = 100
v_precious = 0
v_present = 20
t_step = 0.2
e_v = v_present - v_precious
de_v = e_v/t_step
ie_v = e_v*t_step + integral
acc = k_p*e_v + k_d*de_v + k_i*ie_v


c = np.linalg.matrix_rank(a)

print(c)