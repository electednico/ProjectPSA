import numpy as np
import cmath
import math
import Ybus as Ad

# input values from load flow:
V1 = cmath.rect(1, 0)
V2 = cmath.rect(0.8228, -0.1698)
V3 = cmath.rect(0.7858, -0.2563)
V4 = cmath.rect(0.7545, -0.3009)
V5 = cmath.rect(0.8709, -0.1621)
S1 = complex(0.6802, 0.62)
S2 = complex(-0.4, -0.6)
S3 = complex(-0.8, -0.4)
S4 = complex(-0.3, -0.2)
S5 = complex(0.9, 1)
# Line impedances
z12 = complex(0.05, 0.25)
z23 = complex(0.02, 0.15)
z25 = complex(0.025, 0.1)
z34 = complex(0.01, 0.1)
z35 = complex(0.02, 0.1)

# Computing phase currents at the fault bus, using the Zbus from the load flow
Ybus = Ad.Ybus
print(Ybus)
a = complex(-0.5, math.sqrt(3)/2)
I_f4a = complex(0.0944, 0.2999)
I_f4b = a*a*I_f4a
I_f4c = a*I_f4a
print("I_f4a:")
print(I_f4a)
print("I_f4b:")
print(I_f4b)
print("I_f4c:")
print(I_f4c)

# Need to find the augmented Zbus with generator and load impedances for further calculations
# Calculating the generator- and load impedances
z1 = complex(0, 0.25)
z2 = V2*V2/S2
z3 = V3*V3/S3
z4 = V4*V4/S4
z5 = complex(0, 0.25)

Ybus_aug = Ybus
Ybus_aug[0, 0] = Ybus[0, 0] + 1/z1
Ybus_aug[1, 1] = Ybus[1, 1] + 1/z2
Ybus_aug[2, 2] = Ybus[2, 2] + 1/z3
Ybus_aug[3, 3] = Ybus[3, 3] + 1/z4
Ybus_aug[4, 4] = Ybus[4, 4] + 1/z5

Zbus_aug = np.linalg.inv(Ybus_aug)
np.set_printoptions(precision=3)
print("Zbus augmented: ")
print(Zbus_aug)

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

print("V_post_a:")
print(V_post_a)
print("V_post_b:")
print(V_post_b)
print("V_post_c:")
print(V_post_c)

# Line currents: 0: 1-2, 1: 2-3, 2:2-5, 3: 3-4, 4: 3-5
# Declaring:
I_postfault_a = np.zeros(5, dtype=complex)
I_postfault_a[0] = (V_post_a[1] - V_post_a[0])/z12
I_postfault_a[1] = (V_post_a[2] - V_post_a[1])/z23
I_postfault_a[2] = (V_post_a[4] - V_post_a[1])/z25
I_postfault_a[3] = (V_post_a[3] - V_post_a[2])/z34
I_postfault_a[4] = (V_post_a[4] - V_post_a[2])/z35

I_postfault_b = a*a*I_postfault_a
I_postfault_c = a*I_postfault_a
print("I_postfault_a:")
print(I_postfault_a)
print("I_postfault_b:")
print(I_postfault_b)
print("I_postfault_c:")
print(I_postfault_c)
