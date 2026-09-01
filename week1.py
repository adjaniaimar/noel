# DAY 1

# LIST
suhu_readings = [24.5, 25.1, 24.8, 30.2, 25.0]  # data sensor suhu (°C)
print(suhu_readings[3])  # 30.2 — index ke-3

# DICTIONARY
sensor_config = {
    "nama": "suhu_ruang1",
    "unit": "celsius",
    "threshold_max": 28.0
}
print(sensor_config["threshold_max"])  # 28.0

# FUNCTION
def cek_anomali(suhu, threshold):
    if suhu > threshold:
        return "WARNING: suhu di atas normal!"
    return "Normal"

print(cek_anomali(30.2, 28.0))  #kalo diatas angka dari data reading, maka akan muncul warning, jika tidak maka normal

# LOOPING
for suhu in suhu_readings:
    print(f"{suhu}°C -> {cek_anomali(suhu, 28.0)}")


# CLASS
class Sensor:
    def __init__(self, nama, threshold_max):
        self.nama = nama
        self.threshold_max = threshold_max
        self.readings = []

    def tambah_data(self, nilai):
        self.readings.append(nilai)

    def cek_status(self):
        terakhir = self.readings[-1]
        return "WARNING" if terakhir > self.threshold_max else "Normal"

sensor1 = Sensor("suhu_ruang1", 28.0)
sensor1.tambah_data(30.2)
print(sensor1.cek_status())  # warning, karena data reading diatas threshold max

# DAY 2