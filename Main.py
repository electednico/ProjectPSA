import Ybus as ad
import Ybus_outage_2_3 as ado23
import Ybus_outage_2_5 as ado25
import Ybus_outage_3_5 as ado35
import AuxIter as aux
import numpy as np


"""
Settings:
    outage  can be set to
    0: no outage
    1: line 2-3
    2: line 2-5
    3: line 3-5
    
Q_limit, lim_node and lim_size decides if there is a limit, which node it applies to and the limit size
Only works for one node.
"""
q_limit = True
lim_node = 5
lim_size = 1
outage = 0

"""
Initial values
"""
#  Voltages for 2,3,4 and the delta are guess initial values
slack_node = 1
V = {"1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
delta = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0}
# Q values from project
Q = {"1": None, "2": -0.6, "3": -0.4, "4": -0.2, "5": None}
# P values from project
P = {"1": None, "2": -0.4, "3": -0.8, "4": -0.3, "5": 0.9}

"""
Program
"""

print("\n*--- Newton Raphson method iteration ---*\n")

# Import ybus based on outage case (default no outage)
if outage == 1:
    print("Outage on line 2-3")
    Ybus = ado23.Ybus
elif outage == 2:
    print("Outage on line 2-5")
    Ybus = ado25.Ybus
elif outage == 3:
    print("Outage on line 3-5")
    Ybus = ado35.Ybus
else:
    print("No outage in the system")
    Ybus = ad.Ybus

# Initialize iteration counter
iter = 0

# Create Zbus by inverting Ybus
Zbus = np.linalg.inv(Ybus)

# Initialize a system object (stores information about the grid)
sys_obj = aux.System(P, Q, V, delta, slack_node)

# Iterate NS
while sys_obj.power_error() > 0.0001:
    print("\nIteration: {}\n".format(iter))
    sys_obj.calc_new_power(Ybus)
    sys_obj.check_limit(q_limit, lim_node, lim_size)
    sys_obj.error_specified_vs_calculated()
    sys_obj.print_nodes()
    sys_obj.create_jacobian(Ybus)
    print(sys_obj.jacobian)
    sys_obj.update_values()
    iter += 1
    if iter > 1000:
        print("No convergence")
        break

print("*--- ITERATION COMPLETED ---*")
print("Iterations: {}".format(iter))

# Get post analysis results
sys_obj.calculate_line_data(Ybus)
sys_obj.print_line_data()
sys_obj.calculate_slack_values()
sys_obj.print_nodes()
print("Total losses: P={}pu, Q={}pu".format(round(sys_obj.total_losses_p,5), round(sys_obj.total_losses_q,5)))