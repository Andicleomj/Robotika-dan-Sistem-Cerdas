from controller import Robot

TIME_STEP = 32


def my_controller(z, u, x, P):
    # Prediksi langkah
    x_pred = x + u
    P_pred = P + 0.1  # Noise proses

    # Koreksi langkah
    K = P_pred / (P_pred + 1)  # Gain Kalman
    x = x_pred + K * (z - x_pred)  # Pembaruan posisi
    P = (1 - K) * P_pred  # Pembaruan ketidakpastian
    return x, P

# Inisialisasi robot
robot = Robot()

# Motor roda
left_motor = robot.getDevice("left wheel motor")
right_motor = robot.getDevice("right wheel motor")
left_motor.setPosition(float('inf'))  # Mode kecepatan
right_motor.setPosition(float('inf'))  # Mode kecepatan

# Set kecepatan motor
left_motor.setVelocity(1.0)  # Kecepatan motor kiri
right_motor.setVelocity(1.0)  # Kecepatan motor kanan

# Encoder roda
left_encoder = robot.getDevice("left wheel sensor")
right_encoder = robot.getDevice("right wheel sensor")
left_encoder.enable(TIME_STEP)
right_encoder.enable(TIME_STEP)

# Sensor jarak
distance_sensor = robot.getDevice("distance sensor")
distance_sensor.enable(TIME_STEP)

# Variabel untuk Kalman Filter
x = 0.0  # Posisi awal
P = 1.0  # Ketidakpastian awal

# Loop utama
while robot.step(TIME_STEP) != -1:
    # Ambil nilai encoder
    left_distance = left_encoder.getValue()
    right_distance = right_encoder.getValue()

    # Estimasi pergerakan robot (input u)
    u = (left_distance + right_distance) / 2.0  # Rata-rata pergerakan roda kiri dan kanan

    # Ambil pengukuran sensor jarak (z)
    z = distance_sensor.getValue()

    
    x, P = my_controller(z, u, x, P)

    # Tampilkan estimasi posisi robot
    print(f"Estimasi Posisi Robot: {x}")

