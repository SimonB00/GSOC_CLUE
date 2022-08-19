#This python file is used to TRANSLATE (TRASLARE) and ROTATE points for 2D clustering algorithm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math 

#Translation of vector (Dx, Dy)
def translate(df, Dx, Dy):
    df_t = df.copy()
    df_t.x += Dx
    df_t.y += Dy
    return df_t

#Rotation of angle theta (Degrees)
def rotate(df, theta):
    thetaR = math.radians(theta)
    df_r = df.copy()
    df_r.x = (df.x)*math.cos(thetaR) - (df.y)*math.sin(thetaR)
    df_r.y = (df.x)*math.sin(thetaR) + (df.y)*math.cos(thetaR)

    return df_r

path = "data/moons_1000_nl.csv"

df = pd.read_csv(path)

#Components of translation vector
Dx = -500.
Dy = -1000.

plt.scatter(df.x, df.y, color = 'r', s = 20)

#df1 = translate(df, Dx, Dy)
#plt.scatter(df_t.x, df_t.y, s = 20)

theta = 40 #angle in DEGREES

df1 = rotate(df, theta)
plt.scatter(df1.x, df1.y, s = 20)

df1.to_csv("data/moons_1000_nl_rot.csv", index = False)

plt.show()
