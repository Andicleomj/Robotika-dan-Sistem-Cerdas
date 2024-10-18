from controller import Robot

# Inisialisasi robot
robot = Robot()

# Konstanta
TIME_STEP = 64  # waktu untuk menjalankan satu langkah simulasi
MAX_SPEED = 6.28  # kecepatan maksimal robot

# Mendapatkan referensi ke motor robot
motor_kiri = robot.getDevice('left wheel motor')
motor_kanan = robot.getDevice('right wheel motor')

# Mengatur posisi motor menjadi tak terbatas (untuk kontrol kecepatan)
motor_kiri.setPosition(float('inf'))
motor_kanan.setPosition(float('inf'))

# Kecepatan untuk gerakan melingkar
kecepatan_motor_kiri = MAX_SPEED * 0.5  # Motor kiri bergerak lebih lambat
kecepatan_motor_kanan = MAX_SPEED  # Motor kanan bergerak dengan kecepatan maksimal

# Mengatur kecepatan untuk kedua motor
motor_kiri.setVelocity(kecepatan_motor_kiri)
motor_kanan.setVelocity(kecepatan_motor_kanan)

# Loop utama
while robot.step(TIME_STEP) != -1:
    # Robot akan bergerak melingkar dalam loop ini
    pass

# Ketika simulasi berakhir, robot akan berhenti
motor_kiri.setVelocity(0)
motor_kanan.setVelocity(0)
