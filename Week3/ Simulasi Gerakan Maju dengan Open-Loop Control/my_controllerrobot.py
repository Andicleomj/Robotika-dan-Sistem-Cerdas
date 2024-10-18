from controller import Robot

# Inisialisasi robot
robot = Robot()

# Konstanta
TIME_STEP = 64  # waktu untuk menjalankan satu langkah simulasi
MAX_SPEED = 6.28  # kecepatan maksimum robot

# Dapatkan motor pada robot
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')

# Atur motor agar bergerak tanpa batas waktu
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

# Set kecepatan awal kedua motor ke 0
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

# Fungsi untuk menjalankan gerakan maju dengan kecepatan maksimal
def move_forward(speed):
    left_motor.setVelocity(speed)
    right_motor.setVelocity(speed)

# Jalankan simulasi
while robot.step(TIME_STEP) != -1:
    # Berikan kecepatan maksimum untuk bergerak maju
    move_forward(MAX_SPEED)
