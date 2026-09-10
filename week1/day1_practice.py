humidity_readings = [56.1, 58.3, 55.0, 60.2, 57.5] # data sensor kelembaban (%)
print (humidity_readings[4])  # 57.5 — index ke-4

def anomali_humidity(humidity, threshold):
    if humidity > threshold:
        return "WARNING: kelembaban di atas normal!"
    return "Normal"
print(anomali_humidity(64.4, 62.0)) # kalo diatas angka dari data reading, maka akan muncul warning, jika tidak maka normal

for humidity in humidity_readings:
    print(f"{humidity}% -> {anomali_humidity(humidity, 60.0)}")

class sensor_humidity:
    def __init__(self, nama, threshold_max):
        self.nama = nama
        self.threshold_max = threshold_max
        self.readings = []

    def tambah_data(self, nilai):
        self.readings.append(nilai)

    def cek_status(self):
        terakhir = self.readings[-1]
        return "WARNING" if terakhir > self.threshold_max else "Normal"

sensor1 = sensor_humidity("kelembaban_ruang1", 60.0)
sensor1.tambah_data(64.4)
print(sensor1.cek_status())  # warning, karena data reading diatas threshold max