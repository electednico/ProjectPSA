import numpy as np
from AuxIter import rectangular_to_polar

bus_num = 3

shunt = True
shunt_y = complex(0,0.4)

z12 = complex(0.05, 0.25)
z23 = complex(0.02, 0.15)
z25 = complex(0.025, 0.1)
z34 = complex(0.01, 0.1)
#z35 = complex(0.02, 0.1)

y12 = 1/z12
y23 = 1/z23
y25 = 1/z25
y34 = 1/z34

y11 = y12
y22 = y12 + y23 + y25
y33 = y34 + y23
y44 = y34
y55 = y25
if shunt:
    y33 = y33 + shunt_y  # + shunt_y*1.5
    y22 = y22  # + shunt_y*1.1
    y44 = y44  # + shunt_y*0.6

Ybus=np.matrix([[y11, -y12, 0, 0, 0], [-y12, y22, -y23, 0, -y25], [0, -y23, y33, -y34, 0], [0, 0, -y34, y44, 0],
                [0, -y25, 0, 0, y55]])

