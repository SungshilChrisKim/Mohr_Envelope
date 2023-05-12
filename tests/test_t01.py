import math
import Mohr_Envelope as mohr
import pandas as pd

''' 
LOAD DATA FROM CSV
'''

tn, sm, smj, cc, cr = mohr.read_csv(r'./mohr_trial_t01.csv')

# Create Envelope
env = mohr.getEnvelope()
ag = env.getreallineParam(cc, cr)
slp, icpt, mx, my = env.getlineParam(ag, cc, cr)

# Get c-Phi information
print("Cohesion\t%0.2f" % icpt)
print("Friction Angle\t%0.2f" % math.degrees(math.atan(slp)))

# Visualize Mohr Envelope
graph = mohr.Visualize()
graph.drawCircle(cr, cc, smj)
# graph.drawEnvelope(mx, my, slp, icpt, sm, cc, ag)

# Save Envelope
# graph.writepngFile(r'Absolute file path to save')

''' 
LOAD DATA AS DATAFRAME 
'''

# Data from testing Shale rock
# data = {'Name': ["TA", "TB", "TC"], "S3": [5, 10, 15], "S1": [84.5, 86.3, 111.0]}
# data = {'Name': ["TA", "TB", "TC", "TD"], "S3": [0.1, 0.5, 1.0, 1.5], "S1": [1.46, 3.0, 4.45, 5.9]}
# data = {'Name': ["TA", "TB", "TC", "TD"], "S3": [1.0, 10, 20, 30], "S1": [20.9, 46.1, 75.5, 109.3]}
data = {'Name': ["TA", "TB", "TC"], "S3": [5.0, 20, 50], "S1": [91.1, 138.4, 214.4]}

df = pd.DataFrame(data)
# Load DataFrame
tn, sm, smj, cc, cr = mohr.load_df(df)

# Create Envelope
env = mohr.getEnvelope()
ag = env.getreallineParam(cc, cr)
slp, icpt, mx, my = env.getlineParam(ag, cc, cr)

# Get c-Phi information
print("Cohesion\t%0.2f" % icpt)
print("Friction Angle\t%0.2f" % math.degrees(math.atan(slp)))

# Visualize Mohr Envelope
graph = mohr.Visualize()
graph.drawCircle(cr, cc, smj)
graph.drawEnvelope(mx, my, slp, icpt, sm, cc, ag)

# Save Envelope
graph.writepngFile(r'Absolute file path to save')