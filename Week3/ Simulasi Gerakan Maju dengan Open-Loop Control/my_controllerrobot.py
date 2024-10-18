from controller import Robot

TIME_STEP = 64
MAX_SPEED = 6.28

# Inisialisasi robot
robot = Robot()

# Langkah waktu simulasi (dalam milidetik)
timestep = int(robot.getBasicTimeStep())

# Mendapatkan referensi ke motor robot
motor_kiri = robot.getDevice('left wheel motor')
motor_kanan = robot.getDevice('right wheel motor')

# Mengatur posisi motor menjadi tak terbatas (untuk kontrol kecepatan)
motor_kiri.setPosition(float('inf'))
motor_kanan.setPosition(float('inf'))

# Mengatur kecepatan untuk kedua motor agar bergerak maju
kecepatan = 6.28  # Sesuaikan nilai ini berdasarkan kecepatan robot kamu
motor_kiri.setVelocity(kecepatan)
motor_kanan.setVelocity(kecepatan)

# Loop utama
while robot.step(timestep) != -1:
    # Loop ini akan menjaga robot terus bergerak maju
    pass

# Ketika simulasi berakhir, robot akan berhenti
motor_kiri.setVelocity(0)
motor_kanan.setVelocity(0)
