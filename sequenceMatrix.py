import numpy as np
import cmath
import math
"Pre voltages"
"With shunt and Q limit"
"""V1_pre = cmath.rect(1 , 0)
V2_pre = cmath.rect(0.942731 , -0.1649)
V3_pre = cmath.rect(0.94617 , -0.230721)
V4_pre = cmath.rect(0.920696 , -0.262869)
V5_pre = cmath.rect(1 , -0.16162)"""

"with Q_limit, No shunt"
V1_pre = cmath.rect(1 , 0)
V2_pre = cmath.rect(0.828 , -0.1698)
V3_pre = cmath.rect(0.7858 , -0.2536)
V4_pre = cmath.rect(0.7545 , -0.3009)
V5_pre = cmath.rect(0.8709 , -0.1621)
V_pre=[V1_pre, V2_pre, V3_pre, V4_pre, V5_pre]

"Result for load flow with Q_limit and shunt"
"""S2=complex(0.4, 0.6)
S3=complex(0.8, 0.4)
S4=complex(0.3, 0.2)
"""
"with Q limit, no shunt"
S2=complex(0.4, 0.6)
S3=complex(0.8, 0.4)
S4=complex(0.3, 0.2)
"""
V2_abs_pre = 0.942731
V3_abs_pre = 0.94617
V4_abs_pre = 0.920696"""


V2_abs_pre = 0.828
V3_abs_pre = 0.7858
V4_abs_pre = 0.7545

z_20 = np.square(V2_abs_pre)/np.conj(S2)
z_30 = np.square(V3_abs_pre)/np.conj(S3)
z_40 = np.square(V4_abs_pre)/np.conj(S4)


y_3shunt = complex(0,0.4)

"bus apparent power, with Q_limit "
"positiv sequence"
"Transmission lines"
z1_12=complex(0.05,0.25)
z1_23=complex(0.02,0.15)
z1_25=complex(0.025,0.1)
z1_34=complex(0.01,0.1)
z1_35=complex(0.02,0.1)

"Generators"
z1_10=complex(0,0.25)
z1_50=complex(0,0.25)

"Load"
"dividing by 3 to convert from delta to star (per phase)"
"with shunt and Qlimit"
"Divided by 3 to convert from delta to star connection"
z1_20 = z_20/3
z1_30 = z_30/3
z1_40 = z_40/3
"""
z1_30=complex(0.6023/3,-0.7994/3)
z1_40=complex(1.0375/3,-2.1097/3)"""
Ybus1=np.linalg
Ybus1=[[1/z1_12+1/z1_10, -1/z1_12, 0, 0, 0],[-1/z1_12, 1/z1_12+1/z1_23+1/z1_25+1/z1_20, -1/z1_23, 0, -1/z1_25],
      [0, -1/z1_23, 1/z1_23+1/z1_34+1/z1_35+1/z1_30+y_3shunt, -1/z1_34,-1/z1_35],[0, 0, -1/z1_34, 1/z1_34+ 1/z1_40, 0],
       [0,-1/z1_25,-1/z1_35,0,1/z1_25+1/z1_35+1/z1_50]]

Zbus1=np.linalg.inv(Ybus1)

"testmatrix=np.zeros(5,3,dtype=complex)"
"negative sequence"
"Transmission lines"
z2_12=complex(0.05,0.25)
z2_23=complex(0.02,0.15)
z2_25=complex(0.025,0.1)
z2_34=complex(0.01,0.1)
z2_35=complex(0.02,0.1)

"Generator"
z2_10=complex(0,0.15)
z2_50=complex(0,0.15)

"Load"
"From task 3 with Shunt and Qlimit"
"Divided by 3 to convert from delta to star connection"
z2_20 = z_20/3
z2_30 = z_30/3
z2_40 = z_40/3
"""z2_20=complex(0.3147/3,-1.1916/3)
z2_30=complex(0.6023/3,-0.7994/3)
z2_40=complex(1.0375/3,-2.1097/3)
"""
Ybus2=[[1/z2_12+1/z2_10, -1/z2_12, 0, 0, 0],[-1/z2_12, 1/z2_12+1/z2_23+1/z2_25+1/z2_20, -1/z2_23, 0, -1/z2_25],
      [0, -1/z2_23, 1/z2_23+1/z2_34+1/z2_35+1/z2_30+y_3shunt, -1/z2_34,-1/z2_35],[0, 0, -1/z2_34, 1/z2_34+1/z2_40, 0],
       [0,-1/z2_25,-1/z2_35,0, 1/z2_25+1/z2_35+1/z2_50]]

Zbus2=np.linalg.inv(Ybus2)


"zero sequence Ybus"

"Transmission line:"
z0_12=complex(0.125,1.1)
z0_23=complex(0.05,0.66)
z0_25=complex(0.063,0.44)
z0_34=complex(0.025,0.44)
z0_35=complex(0.05,0.44)

"Generator:"
z0_10=complex(0,0.075)
z0_50=complex(0,0.075)

"Loads: delta connected, no connection to ground--> not included in zero sequence impedance matrix"

Ybus0 = [[1/z0_12+1/z0_10, -1/z0_12, 0, 0, 0],[-1/z0_12, 1/z0_12+1/z0_23+1/z0_25, -1/z0_23, 0, -1/z0_25],
      [0, -1/z0_23, 1/z0_23+1/z0_34+1/z0_35, -1/z0_34,-1/z0_35],[0, 0, -1/z0_34,1/z0_34,0],
       [0,-1/z0_25,-1/z0_35,0,1/z0_25+1/z0_35+1/z0_50]]

Zbus0=np.linalg.inv(Ybus0)


myarray = np.asarray(Ybus0)
"Bus value in python(3,3) equals bus value [4,4] (normal matrix), since python starts at row 0 and not 1."
"I_f4 is fault current at bus 4, phase a."
"The other phase currents at bus 4 are zero, due to phase to ground fault "
I_f4 = 3*V4_pre/(Zbus0[3,3]+Zbus1[3,3]+Zbus2[3,3])

zero_complex = np.complex(0, 0)
V_post=np.array([[zero_complex,zero_complex,zero_complex],[zero_complex,zero_complex,zero_complex],[zero_complex,zero_complex,zero_complex],[zero_complex,zero_complex,zero_complex],[zero_complex,zero_complex,zero_complex]])
"V_012=np.zeros(3,dtype=complex)"
a=complex(-0.5, math.sqrt(3)/2)

"sequence voltages"
for i in range(5):
    "computing the sequence voltages"
    V_0 = -Zbus0[i, 4] * I_f4
    V_1 = V_pre[i] - Zbus1[i, 4] * I_f4
    V_2 = -Zbus2[i, 4] * I_f4
    "converting the sequence voltages to phase quantities"
    V_post[i, 0] = V_0+V_1+V_2
    V_post[i, 1] = V_0+a*a*V_1+a*V_2
    V_post[i, 2] = V_0+a*V_1+a*a*V_2

    """V_012[0] = -Zbus0[i, 4]*I_f4
    V_012[1] = V_pre[i]-Zbus1[i, 4]*I_f4
    V_012[2] = -Zbus2[i, 4]*I_f4
    V_post[i, 0] = V_012[0]+V_012[1]+V_012[2]
    V_post[i, 1] = V_012[0]+a*a*V_012[1]+a*V_012[2]
    V_post[i, 2] = V_012[0]+a*V_012[1]+a*a*V_012[2]
"""

"post currents in transmission lines"
z_12 = complex(0.05,0.25)
z_23 = complex(0.02,0.15)
z_25 = complex(0.025,0.1)
z_34 = complex(0.01,0.1)
z_35 = complex(0.02,0.1)
z = [z_12,z_23,z_34,z_25,z_35]
I_post = np.array([[zero_complex,zero_complex,zero_complex],[zero_complex,zero_complex,zero_complex],[zero_complex,zero_complex,zero_complex],[zero_complex,zero_complex,zero_complex],[zero_complex,zero_complex,zero_complex]])

"""I_post matrix 
rad: I_12,I_23, I_34, I_25, I_35 
column: phase a, phase b, phase c"""
"Lager I_12, I_23, I_34 med en for løkke"
for i in range(3):
    I_post[i, 0] = (V_post[i,0]-V_post[i+1,0])/z[i]
    I_post[i, 1] = (V_post[i, 1] - V_post[i+1, 1])/ z[i]
    I_post[i, 2] = (V_post[i, 2] - V_post[i+1, 2])/ z[i]

"I_25:"
I_post[3, 0] = (V_post[4,0] - V_post[1,0]) / z[3]
I_post[3, 1] = (V_post[4, 1] - V_post[1, 1]) / z[3]
I_post[3, 2] = (V_post[4, 2] - V_post[1, 2]) / z[3]

"I_35:"
I_post[4, 0] = (V_post[4,0] - V_post[2,0]) / z[4]
I_post[4, 1] = (V_post[4, 1] - V_post[2, 1]) / z[4]
I_post[4, 2] = (V_post[4, 2] - V_post[2, 2]) / z[4]