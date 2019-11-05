import numpy as np
import cmath
import math
import Ybus as Ad
np.set_printoptions(precision=3)


# Input values from load flow: Without shunt, and with reactive limits, results from 3b.
V1 = cmath.rect(1, 0)
V2 = cmath.rect(0.8228, -0.16982)
V3 = cmath.rect(0.7858 , -0.2536)
V4 = cmath.rect(0.7545 , -0.3009)
V5 = cmath.rect(0.8709 , -0.1621)
S2 = complex(0.4, 0.6)
S3 = complex(0.8, 0.4)
S4 = complex(0.3, 0.2)

# Line impedances
z12 = complex(0.05, 0.25)
z23 = complex(0.02, 0.15)
z25 = complex(0.025, 0.1)
z34 = complex(0.01, 0.1)
z35 = complex(0.02, 0.1)

# Need to find the augmented Zbus with generator and load impedances for further calculations
# Calculating the generator- and load impedances.
# Load impedances are delta connected and therefore needs to be divided by 3
# Ybus augmented is computed without shunt impedance
z1 = complex(0, 0.25)
z2 = 1/3*np.square(abs(V2))/np.conj(S2)
z3 = 1/3*np.square(abs(V3))/np.conj(S3)
z4 = 1/3*np.square(abs(V4))/np.conj(S4)
z5 = complex(0, 0.25)

# Adding Ybus from the script in part A of the project, and adding to the diagonal elements.
Ybus = Ad.Ybus  # Remember to set shunt = False in Ybus script
Ybus_aug = Ybus
Ybus_aug[0, 0] = Ybus[0, 0] + 1/z1
Ybus_aug[1, 1] = Ybus[1, 1] + 1/z2
Ybus_aug[2, 2] = Ybus[2, 2] + 1/z3
Ybus_aug[3, 3] = Ybus[3, 3] + 1/z4
Ybus_aug[4, 4] = Ybus[4, 4] + 1/z5

#Computing augmented Zbus and printing results
Zbus_aug = np.linalg.inv(Ybus_aug)
print(f'Ybus_aug =\n {Ybus_aug}\n')
print(f'Zbus_aug =\n {Zbus_aug}\n')
print(f'Z_44 =  {Zbus_aug[3, 3]}\n')

# Computing phase currents at the fault bus, using the Thevenin equivalent seen from the fault bus, bus 4:
a = complex(-0.5, math.sqrt(3)/2)
I_f4a = V4/Zbus_aug[3, 3]
I_f4b = a*a*I_f4a
I_f4c = a*I_f4a
print(f'Fault currents at bus 4, I_f4:\n phase a: {I_f4a}\n phase b: '
      f'{I_f4b}\n phase c: {I_f4c}\n')

# Computing the postfault bus voltages:
# Start by defining pre- and postfault voltage vectors:
V_pre = np.array([V1, V2, V3, V4, V5])
V_post_a = np.zeros(5, dtype=complex)
V_post_b = np.zeros(5, dtype=complex)
V_post_c = np.zeros(5, dtype=complex)

for j in range(5):
    V_post_a[j] = V_pre[j] - Zbus_aug[3, j] * I_f4a
    V_post_b[j] = a*a*V_pre[j] - Zbus_aug[3, j] * I_f4b
    V_post_c[j] = a*V_pre[j] - Zbus_aug[3, j] * I_f4c

for i in range(5):
    print(f'Post voltage at bus {i+1}\n phase a: {V_post_a[i]}\n phase b: {V_post_b[i]}\n phase c: {V_post_c[i]}\n')

# Postfault line currents between bus 3 and 4:
I_postfault_a = (V_post_a[3] - V_post_a[2])/z34
I_postfault_b = a*a*I_postfault_a
I_postfault_c = a*I_postfault_a
print(f'Line current between bus 3 and bus 4 during the short circuit:\n phase a: {I_postfault_a}\n phase b: '
      f'{I_postfault_b}\n phase c: {I_postfault_c}\n')

# Prefault line currents between bus 3 and 4:
I_prefault_a = (V4 - V3)/z34
I_prefault_b = a*a*I_prefault_a
I_prefault_c = a*I_prefault_a
print(f'Line current between bus 3 and bus 4 before the short circuit:\n phase a: {I_prefault_a}\n phase b: '
      f'{I_prefault_b}\n phase c: {I_prefault_c}\n')
