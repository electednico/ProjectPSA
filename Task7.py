import numpy as np
import Ybus as ad



GenAd = 1/complex(0, 0.25)
z2 = V2*V2/S2
z3 = V3*V3/S3
z4 = V4*V4/S4

Aug_Ybus = ad.Ybus


Aug_Ybus[0, 0] = Aug_Ybus[0, 0] + GenAd
Aug_Ybus[0, 0] = Aug_Ybus[1, 1] + 1/z2
Aug_Ybus[0, 0] = Aug_Ybus[2, 2] + 1/z3
Aug_Ybus[0, 0] = Aug_Ybus[3, 3] + 1/z4
Aug_Ybus[0, 0] = Aug_Ybus[4, 4] + GenAd
