from mpu9250 import MPU9250
from time import sleep_ms
from machine import I2C

i2c = I2C(sda = 21, scl = 22)
imu = MPU9250(i2c)

N = 20
Dt = 50

t  = [0 for i in range(N)]
ax = [0 for i in range(N)]
ay = [0 for i in range(N)]
az = [0 for i in range(N)]

for i in range(N):
    t[i] = i*Dt/1000
    ax[i], ay[i], az[i] = imu.acceleration
    sleep_ms(50)

i2c.deinit()
print(ax)
print(ay)
print(az)