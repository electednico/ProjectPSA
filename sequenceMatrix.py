import numpy as np
import cmath
import math

"Pre voltages"
"with Q_limit, No shunt"
V1_pre = cmath.rect(1 , 0)
V2_pre = cmath.rect(0.828 , -0.1698)
V3_pre = cmath.rect(0.7858 , -0.2536)
V4_pre = cmath.rect(0.7545 , -0.3009)
V5_pre = cmath.rect(0.8709 , -0.1621)
V_pre=[V1_pre, V2_pre, V3_pre, V4_pre, V5_pre]


"with Q limit, no shunt"
S2 = complex(0.4, 0.6)
S3 = complex(0.8, 0.4)
S4 = complex(0.3, 0.2)

"Load delta connected"
z_20 = np.square(abs(V2_pre))/np.conj(S2)
z_30 = np.square(abs(V3_pre))/np.conj(S3)
z_40 = np.square(abs(V4_pre))/np.conj(S4)


y_3shunt = complex(0, 0.4)

"positiv sequence"
"Transmission lines"
z1_12 = complex(0.05, 0.25)
z1_23 = complex(0.02, 0.15)
z1_25 = complex(0.025, 0.1)
z1_34 = complex(0.01, 0.1)
z1_35 = complex(0.02, 0.1)

"Generators"
z1_10 = complex(0, 0.25)
z1_50 = complex(0, 0.25)

"Load"
"dividing by 3 to convert from delta to star (per phase)"
z1_20 = z_20/3
z1_30 = z_30/3
z1_40 = z_40/3

Ybus1 = [[1/z1_12+1/z1_10, -1/z1_12, 0, 0, 0], [-1/z1_12, 1/z1_12 + 1/z1_23 + 1/z1_25 + 1/z1_20, -1/z1_23, 0, -1/z1_25],
      [0, -1/z1_23, 1/z1_23 + 1/z1_34 + 1/z1_35 + 1/z1_30, -1/z1_34, -1/z1_35], [0, 0, -1/z1_34, 1/z1_34 + 1/z1_40, 0],
       [0, -1/z1_25, -1/z1_35, 0, 1/z1_25 + 1/z1_35 + 1/z1_50]]

Zbus1 = np.linalg.inv(Ybus1)

"negative sequence"
"Transmission lines"
z2_12 = complex(0.05, 0.25)
z2_23 = complex(0.02, 0.15)
z2_25 = complex(0.025, 0.1)
z2_34 = complex(0.01, 0.1)
z2_35 = complex(0.02, 0.1)

"Generator"
z2_10 = complex(0, 0.15)
z2_50 = complex(0, 0.15)

"Load"
"Divided by 3 to convert from delta to star connection"
z2_20 = z_20/3
z2_30 = z_30/3
z2_40 = z_40/3

Ybus2 = [[1/z2_12+1/z2_10, -1/z2_12, 0, 0, 0], [-1/z2_12, 1/z2_12+1/z2_23+1/z2_25+1/z2_20, -1/z2_23, 0, -1/z2_25],
      [0, -1/z2_23, 1/z2_23+1/z2_34+1/z2_35+1/z2_30, -1/z2_34,-1/z2_35], [0, 0, -1/z2_34, 1/z2_34+1/z2_40, 0],
       [0, -1/z2_25, -1/z2_35, 0, 1/z2_25+1/z2_35+1/z2_50]]

Zbus2 = np.linalg.inv(Ybus2)


"zero sequence Ybus"

"Transmission line:"
z0_12 = complex(0.125, 1.1)
z0_23 = complex(0.05, 0.66)
z0_25 = complex(0.063, 0.44)
z0_34 = complex(0.025, 0.44)
z0_35 = complex(0.05, 0.44)

"Generator:"
z0_10 = complex(0,0.075)
z0_50 = complex(0,0.075)

"Loads: delta connected, no connection to ground--> not included in zero sequence impedance matrix"

Ybus0 = [[1/z0_12+1/z0_10, -1/z0_12, 0, 0, 0], [-1/z0_12, 1/z0_12+1/z0_23+1/z0_25, -1/z0_23, 0, -1/z0_25],
      [0, -1/z0_23, 1/z0_23+1/z0_34+1/z0_35, -1/z0_34, -1/z0_35], [0, 0, -1/z0_34, 1/z0_34, 0],
       [0, -1/z0_25, -1/z0_35, 0, 1/z0_25+1/z0_35+1/z0_50]]

Zbus0 = np.linalg.inv(Ybus0)


Ybus1_array = np.asarray(Ybus1)
Ybus2_array = np.asarray(Ybus2)
Ybus0_array = np.asarray(Ybus0)


"The other phase currents at bus 4 are zero, due to phase to ground fault "
I_f4 = 3*V4_pre/(Zbus0[3,3]+Zbus1[3,3]+Zbus2[3,3])

zero_complex = np.complex(0, 0)
V_post = np.array([[zero_complex,zero_complex,zero_complex],[zero_complex,zero_complex,zero_complex],[zero_complex,zero_complex,zero_complex],[zero_complex,zero_complex,zero_complex],[zero_complex,zero_complex,zero_complex]])
V_012 = np.array([[zero_complex,zero_complex,zero_complex],[zero_complex,zero_complex,zero_complex],[zero_complex,zero_complex,zero_complex],[zero_complex,zero_complex,zero_complex],[zero_complex,zero_complex,zero_complex]])

"V_012=np.zeros(3,dtype=complex)"
a = complex(-0.5, math.sqrt(3)/2)

"sequence voltages"
for i in range(5):
    "computing the sequence voltages"
    V_012[i, 0] = -Zbus0[i, 3] * I_f4/3
    V_012[i, 1] = V_pre[i] - Zbus1[i, 3] * I_f4/3
    V_012[i, 2] = -Zbus2[i, 3] * I_f4/3
    "Dividing If4 by 3 to get the sequence component"
    "converting the sequence voltages to phase quantities"
    V_post[i, 0] = V_012[i, 0] + V_012[i, 1] + V_012[i, 2]
    V_post[i, 1] = V_012[i, 0] +a*a* V_012[i, 1]+a*V_012[i, 2]
    V_post[i, 2] = V_012[i, 0] +a*V_012[i, 1]+a*a*V_012[i, 2]

"Line current between bus 3 and 4 during/after fault"
"Sequence component"
I_0_34 = (V_012[2, 0] - V_012[3, 0]) / z0_34
I_1_34 = (V_012[2, 1] - V_012[3, 1]) / z1_34
I_2_34 = (V_012[2, 2] - V_012[3, 2]) / z2_34
"Transformation to phase values"
I_post_34_a = I_0_34 + I_1_34 + I_2_34
I_post_34_b = I_0_34 + a * a * I_1_34 + a * I_2_34
I_post_34_c = I_0_34 + a * I_1_34 + a * a * I_2_34

print(f'sequence impedance buses: \n')
print(f'Zero sequence impedance bus: \n{Zbus0}\n')
print(f'Positive sequence impedance bus: \n{Zbus1}\n')
print(f'Negative sequence impedance bus: \n{Zbus2}\n')

print(f'Fault current at bus 4: {I_f4}\n')
print(f'Post voltage at each bus \n{V_post}\n')

print(f'Line current between bus 3 and bus 4 during the short circuit:\n phase a: {I_post_34_a}\n phase b: {I_post_34_b}\n phase c: {I_post_34_c}')
print(f'The line current before the fault is found in task 3B.')
print(f'\nSee report for more info, and better layout \n ')
