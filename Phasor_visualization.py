
from firebase import firebase
import math
import matplotlib.pyplot as plt
import pylab
import time

t=100
fig = pylab.figure(figsize = [8.0, 8.0])
ax = fig.gca(projection = 'polar')
fig.canvas.set_window_title('Doppler')
ax.set_theta_zero_location('E')
ax.set_theta_direction(1)
line1, = ax.plot([0, 0],[0,t], color = 'r', linewidth = 2, label="Phase A")
line2, = ax.plot([0, 0],[0,t], color = 'y', linewidth = 2, label="Phase B")
line3, = ax.plot([0, 0],[0,t], color = 'b', linewidth = 2, label="Phase C")
plt.title("Voltage Phasors")
plt.legend()

data=firebase.FirebaseApplication("https://data-50743-default-rtdb.firebaseio.com")

#Retriving data for phase A
angle_A=data.get("/Phase A/voltage/Angle",None)
magnitude_A=data.get("/Phase A/voltage/Magnitude",None)
angle_ph_a = angle_A  * (math.pi/180)
mag_ph_a = magnitude_A


#Retriving data for phase B
angle_B=data.get("/Phase B/voltage/Angle",None)
magnitude_B=data.get("/Phase B/voltage/Magnitude",None)
angle_ph_b = angle_B  * (math.pi/180)
mag_ph_b = magnitude_B 


#Retriving data for phase C
angle_C=data.get("/Phase C/voltage/Angle",None)
magnitude_C=data.get("/Phase C/voltage/Magnitude",None)
angle_ph_c = angle_C  * (math.pi/180)
mag_ph_c = magnitude_C

ax.plot(angle_ph_a, mag_ph_a, color ='r', marker = 'o', markersize = '8')
ax.plot(angle_ph_b, mag_ph_b, color ='y', marker = 'o', markersize = '8')
ax.plot(angle_ph_c, mag_ph_c, color ='b', marker = 'o', markersize = '8')
line1.set_data([angle_ph_a, angle_ph_a],[0,mag_ph_a])
line2.set_data([angle_ph_b, angle_ph_b],[0,mag_ph_b])
line3.set_data([angle_ph_c, angle_ph_c],[0,mag_ph_c])
plt.savefig('Voltages_visualization.jpg', dpi=400, bbox_inches='tight')
plt.show()


#Current Phasors
u=2
fig_ = pylab.figure(figsize = [8.0, 8.0])
ax_ = fig_.gca(projection = 'polar')
fig_.canvas.set_window_title('Doppler')
ax_.set_theta_zero_location('E')
ax_.set_theta_direction(1)
line11, = ax_.plot([0, 0],[0,u], color = 'r', linewidth = 2, label="Phase A")
line21, = ax_.plot([0, 0],[0,u], color = 'y', linewidth = 2, label="Phase B")
line31, = ax_.plot([0, 0],[0,u], color = 'b', linewidth = 2, label="Phase C")
plt.title("Current Phasors")
plt.legend()


#Retriving current for phase A
c_angle_A=data.get("/Phase A/current/Angle",None)
c_magnitude_A=data.get("/Phase A/current/Magnitude",None)
c_angle_ph_a = c_angle_A  * (math.pi/180)
c_mag_ph_a = c_magnitude_A

#Retriving current for phase B
c_angle_B=data.get("/Phase B/current/Angle",None)
c_magnitude_B=data.get("/Phase B/current/Magnitude",None)
c_angle_ph_b = c_angle_B  * (math.pi/180)
c_mag_ph_b = c_magnitude_B

#Retriving current for phase C
c_angle_C=data.get("/Phase C/current/Angle",None)
c_magnitude_C=data.get("/Phase C/current/Magnitude",None)
c_angle_ph_c = c_angle_C  * (math.pi/180)
c_mag_ph_c = c_magnitude_C

ax_.plot(c_angle_ph_a, c_mag_ph_a, color ='r', marker = 'o', markersize = '8')
ax_.plot(c_angle_ph_b, c_mag_ph_b, color ='y', marker = 'o', markersize = '8')
ax_.plot(c_angle_ph_c, c_mag_ph_c, color ='b', marker = 'o', markersize = '8')
line11.set_data([c_angle_ph_a, c_angle_ph_a],[0,c_mag_ph_a])
line21.set_data([c_angle_ph_b, c_angle_ph_b],[0,c_mag_ph_b])
line31.set_data([c_angle_ph_c, c_angle_ph_c],[0,c_mag_ph_c])
plt.savefig('Current_visualization.jpg', dpi=400, bbox_inches='tight')
plt.show()

#phase A power parameters
act_power_a=data.get("/Phase A/active_power",None)
react_power_a=data.get("/Phase A/reactive_power",None)
apparent_power_a=data.get("/Phase A/apparent_power",None)
power_angle_a=data.get("/Phase A/power_angle",None)
power_factor_a=data.get("/Phase A/power_factor",None)

#phase B power parameters
act_power_b=data.get("/Phase B/active_power",None)
react_power_b=data.get("/Phase B/reactive_power",None)
apparent_power_b=data.get("/Phase B/apparent_power",None)
power_angle_b=data.get("/Phase B/power_angle",None)
power_factor_b=data.get("/Phase B/power_factor",None)

#phase C power parameters
act_power_c=data.get("/Phase C/active_power",None)
react_power_c=data.get("/Phase C/reactive_power",None)
apparent_power_c=data.get("/Phase AC/apparent_power",None)
power_angle_c=data.get("/Phase C/power_angle",None)
power_factor_c=data.get("/Phase C/power_factor",None)

print("Phase A")
print("Voltage =",magnitude_A,"<",angle_A,"V")
print("current =",c_magnitude_A,"<",c_angle_A,"A")
print("Active Power =",act_power_a,"W")
print("Reactive Power =",react_power_a,"VAR")
print("Apparent Power =",apparent_power_a,"VA")
print("Power Angle =",power_angle_a,"degree")
print("Power factor =",power_factor_a)

print("Phase B")
print("Voltage =",magnitude_B,"<",angle_B,"V")
print("current =",c_magnitude_B,"<",c_angle_B,"A")
print("Active Power =",act_power_b,"W")
print("Reactive Power =",react_power_b,"VAR")
print("Apparent Power =",apparent_power_b,"VA")
print("Power Angle =",power_angle_b,"degree")
print("Power factor =",power_factor_b)

print("Phase C")
print("Voltage =",magnitude_C,"<",angle_C,"V")
print("current =",c_magnitude_C,"<",c_angle_C,"A")
print("Active Power =",act_power_c,"W")
print("Reactive Power =",react_power_c,"VAR")
print("Apparent Power =",apparent_power_c,"VA")
print("Power Angle =",power_angle_c,"degree")
print("Power factor =",power_factor_c)