class MyMap:
    def __init__(self):
        self.map = {}

    def add(self, key, value):
        """Menambahkan elemen ke dalam map."""
        self.map[key] = value

    def get(self, key, default=None):
        """Mengambil nilai dari map berdasarkan kunci."""
        return self.map.get(key, default)

    def update(self, key, value):
        """Memperbarui nilai dari elemen dalam map."""
        if key in self.map:
            self.map[key] = value
        else:
            print(f"Kunci '{key}' tidak ditemukan dalam map.")

    def delete(self, key):
        """Menghapus elemen dari map."""
        if key in self.map:
            del self.map[key]
        else:
            print(f"Kunci '{key}' tidak ditemukan dalam map.")

    def contains(self, key):
        """Memeriksa apakah map mengandung kunci tertentu."""
        return key in self.map

    def clear(self):
        """Menghapus semua elemen dalam map."""
        self.map.clear()

    def items(self):
        """Mengembalikan semua elemen dalam map sebagai pasangan kunci-nilai."""
        return self.map.items()

    def print_map(self):
        """Menampilkan semua elemen dalam map."""
        for key, value in self.map.items():
            print(f"{key}: {value}")

# Contoh penggunaan:
my_map = MyMap()

# Menambahkan elemen ke dalam map
my_map.add("nama", "Ramaditya")
my_map.add("umur", 22)
my_map.add("pekerjaan", "Traveler")
my_map.add("kota", "Praya")

# Menampilkan map
print("Initial Map:")
my_map.print_map()

# Mengakses nilai dari map
print("\nNama:", my_map.get("nama"))  # Output: Ramaditya
print("Umur:", my_map.get("umur"))    # Output: 22

# Mengubah nilai dari map
my_map.update("umur", 22)
print("Updated Umur:", my_map.get("umur"))  # Output: 22

# Menghapus elemen dari map
my_map.delete("pekerjaan")

# Menampilkan semua elemen dalam map
print("\nAll items in the map after deletion:")
my_map.print_map()

# Mengecek apakah kunci ada dalam map
if my_map.contains("nama"):
    print("\nNama ada dalam peta.")

# Mendapatkan nilai dengan kunci, atau nilai default jika kunci tidak ada
pekerjaan = my_map.get("pekerjaan", "Tidak diketahui")
print("\nPekerjaan:", pekerjaan)  # Output: Pekerjaan: Tidak diketahui

# Menambah elemen lain
my_map.add("hobi", ["Gym", "Futsal", "Traveling"])

# Menggabungkan dua maps
additional_info = {"status": "Single", "tinggi": 178}
for key, value in additional_info.items():
    my_map.add(key, value)

# Menampilkan map yang telah diperbarui
print("\nUpdated Map with additional info:")
my_map.print_map()

# Menghapus semua elemen dari map
my_map.clear()
print("\nMap after clearing all items:")
my_map.print_map()  # Output: Map kosong