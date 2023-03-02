G = 6.673e-11
M = 5.98e24
accel_gravity = 0.0

dist_center = float(input())

accel_gravity = G * M / (dist_center * dist_center)

print(f"Acceleration of gravity: {accel_gravity:.2f}")
