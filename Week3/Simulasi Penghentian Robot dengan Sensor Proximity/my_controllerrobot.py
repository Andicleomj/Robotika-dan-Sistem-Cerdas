from controller import Robot

# Inisialisasi robot
robot = Robot()

# Konstanta
TIME_STEP = 64  # waktu untuk menjalankan satu langkah simulasi
MAX_SPEED = 6.28  # kecepatan maksimal robot
DELAY_STEPS = 20  # jumlah langkah simulasi sebelum mulai bergerak

# Mendapatkan referensi ke motor robot
motor_kiri = robot.getDevice('left wheel motor')
motor_kanan = robot.getDevice('right wheel motor')

# Mendapatkan referensi ke sensor proximity
proximity_sensor = robot.getDevice('ps0')  # Sensor proximity pertama, misalnya 'ps0'
proximity_sensor.enable(TIME_STEP)

# Mengatur posisi motor menjadi tak terbatas (untuk kontrol kecepatan)
motor_kiri.setPosition(float('inf'))
motor_kanan.setPosition(float('inf'))

# Penundaan awal sebelum bergerak
step = 0
while step < DELAY_STEPS:
    robot.step(TIME_STEP)
    step += 1

# Loop utama
while robot.step(TIME_STEP) != -1:
    # Membaca nilai sensor proximity
    proximity_value = proximity_sensor.getValue()
    
    # Jika sensor mendeteksi objek di dekat robot (threshold disesuaikan)
    if proximity_value > 100:  # Nilai threshold dapat disesuaikan tergantung sensor
        # Berhenti jika objek terdeteksi
        motor_kiri.setVelocity(0)
        motor_kanan.setVelocity(0)
    else:
        # Gerak maju jika tidak ada objek
        motor_kiri.setVelocity(MAX_SPEED)
        motor_kanan.setVelocity(MAX_SPEED)

# Ketika simulasi berakhir, robot akan berhenti
motor_kiri.setVelocity(0)
motor_kanan.setVelocity(0)
