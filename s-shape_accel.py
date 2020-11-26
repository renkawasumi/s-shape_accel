import numpy as np
import matplotlib.pyplot as plt
import math

v_max = 5.0  # [m/s]
v_s = 0.0  # [m/s]
v_e = 2.0  # [m/s]
a_max = 4.0  # [m/s^2]
d_all = 30.0  # [m]
t_reso = 0.001  # [s] reso = resolution
t_0 = 0.0  # [s]

d_1 = np.pi * (v_max**2 - v_s**2) / (4 * a_max)
t_1 = np.pi * (v_max - v_s) / (2.0 * a_max)
t = np.arange(t_0, t_1, t_reso)
v_1 = (v_max - v_s) / 2.0 * \
    (1.0 - np.cos(2.0 * a_max * t / (v_max - v_s))) + v_s
plt.plot(t, v_1)
d_3 = np.pi * (v_max**2 - v_e**2) / (4 * a_max)

if d_1 + d_3 > d_all:
    plt.cla()
    v_max = np.sqrt(2 * a_max * (d_all / np.pi) + (v_s**2 + v_e**2) / 2.0)
    print("!!!!!!!!")
    print("v_max", v_max)
    print("!!!!!!!!")
    d_1 = np.pi * (v_max**2 - v_s**2) / (4 * a_max)
    t_1 = np.pi * (v_max - v_s) / (2.0 * a_max)
    t = np.arange(t_0, t_1, t_reso)
    v_1 = (v_max - v_s) / 2.0 * \
        (1.0 - np.cos(2.0 * a_max * t / (v_max - v_s))) + v_s
    plt.plot(t, v_1)
    d_3 = np.pi * (v_max**2 - v_e**2) / (4 * a_max)
    d_2 = d_all - d_1 - d_3
    t_2 = d_2 / v_max
    t_3 = np.pi * (v_max - v_e) / (2.0 * a_max)
    t = np.arange(0, t_3, t_reso)
    v_3 = (v_max - v_e) / 2.0 * \
        (1.0 + np.cos(2.0 * a_max * t / (v_max - v_e))) + v_e
    plt.plot(t + t_1 + t_2, v_3)
    t = np.arange(t_1, t_1 + t_2, t_reso)
    v_2 = [v_max] * len(t)
    plt.plot(t, v_2)
else:
    d_2 = d_all - d_1 - d_3
    t_2 = d_2 / v_max
    t_3 = np.pi * (v_max - v_e) / (2.0 * a_max)
    t = np.arange(0, t_3, t_reso)
    v_3 = (v_max - v_e) / 2.0 * \
        (1.0 + np.cos(2.0 * a_max * t / (v_max - v_e))) + v_e
    plt.plot(t + t_1 + t_2, v_3)
    t = np.arange(t_1, t_1 + t_2, t_reso)
    v_2 = [v_max] * len(t)
    plt.plot(t, v_2)

print("d_1", d_1)
print("d_2", d_2)
print("d_3", d_3)
print("t_1", t_1)
print("t_2", t_2)
print("t_3", t_3)

plt.axis("equal")
plt.show()
