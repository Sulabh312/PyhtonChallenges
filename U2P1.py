import random as rand, time
desired_speed = 10
Kp = 2
while True:
    measured_speed = rand.uniform(5, 15)
    error = desired_speed - measured_speed
    u = Kp * error
    print(f"Measured Speed: {measured_speed:.2f}, Control Output: {u:.2f}, error: {error:.2f}")
    time.sleep(0.1)
    
