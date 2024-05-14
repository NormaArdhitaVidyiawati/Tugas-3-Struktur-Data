"""
    Kelompok 6_2023E - Kumpulan Tugas Struktur Data

    1. Tsalist Habibil Muzakki - 23091397163 
    2. Aditya Revangga D.P - 23091397167 
    3. Norma Ardhita Vidyiawati - 23091397169
"""

class KatakanPeta():
    def__init__(self):
       self.daftarKota = {}
       self.jumlahKota = 0

   def tampilkanPeta(self):
       for kota in self.daftarKota:
           print(f"{kota}")
           for kotaTetangga, jarak in self.daftarKota[kota].items():
               print(f"\t--> {jarak} km -- {kotaTetangga}")

        print(f"Jumlah Kota: {self.jumlahKota}")

    def tambahkanKota(self, kota):
        if kota not in self.daftarKota:
            self.daftarKota[kota] = {}
            self.jumlahKota += 1

    def tambahkanJalan(self, kota1, cities):
        for kota in cities:
            if kota1 and kota in self.daftarKota:
                self.daftarKota[kota1][kota] = cities[kota]
                self.daftarKota[kota][kota1] = cities[kota]

    def hapusKota(self, kotaDihapus):
        if kotaDihapus in self.daftarKota:
            for kota in self.daftarKota:
                if kotaDihapus in self.daftarKota[kota]:
                    del self.daftarKota[kota][kotaDihapus]
            del self.daftarKota[kotaDihapus]
            self.jumlahKota -= 1
            
    def hapusJalan(self, kota1, kota2):
        if kota1 and kota2 in self.daftarKota:
            del self.daftarKota[kota1][kota2]
            del self.daftarKota[kota2][kota1]
    
    def dijkstra(self, kota_awal):
        # inline loop
        unvisited_cities = [*self.daftarKota.keys()]
        distances = {}
        routes = {}

        for city in unvisited_cities:
            distances[city] = float("inf")
        distances[kota_awal] = 0
        
        while unvisited_cities:
            closest_city = None
            for city in unvisited_cities:
                if closest_city == None:
                    closest_city = city
                elif distances[city] < distances[closest_city]:
                    closest_city = city
                    
            for neighbour, distance in self.daftarKota[closest_city].items():
                total_distance = round(distances[closest_city] + distance, 1)
                if total_distance < distances[neighbour]:
                    distances[neighbour] = total_distance
                    routes[neighbour] = closest_city

            unvisited_cities.remove(closest_city)

        del distances[kota_awal]
        return distances, routes
        
 cities = ["Berlin", "Dresden", "Leipzig", "Magdeburg", "Hannover", "Hamburg", "Bremen", "Nurnberg", "Munchen", "Stuttgart", "Bielefeld", "Dortmund", "Frankfurt"]

petajerman = Peta()
for city in cities:
    petajerman.tambahkanKota(city)
    
petajerman.tambahkanJalan("Berlin", {"Dresden": 193.2, "Leipzig": 164, "Hamburg": 295.1, "Magdeburg": 160.2})
petajerman.tambahkanJalan("Dresden", {"Leipzig": 120.5, "Nurnberg": 390.6})
petajerman.tambahkanJalan("Leipzig", {"Magdeburg": 129.9})
petajerman.tambahkanJalan("Magdeburg", {"Hannover": 147.7})
petajerman.tambahkanJalan("Hannover", {"Hamburg": 150.9, "Bremen": 137.4, "Bielefeld": 107.6,})
petajerman.tambahkanJalan("Hamburg", {"Bremen": 125.9,})
petajerman.tambahkanJalan("Bremen", {"Bielefeld": 188.8, "Dortmund": 233.5,})
petajerman.tambahkanJalan("Bielefeld", {"Dortmund": 113.4})
petajerman.tambahkanJalan("Nurnberg", {"Munchen": 170.2, "Stuttgart": 210.8, "Frankfurt":224.9 })
petajerman.tambahkanJalan("Munchen", {"Stuttgart": 231.2})
petajerman.tambahkanJalan("Stuttgart", {"Frankfurt": 206})
petajerman.tambahkanJalan("Dortmund", {"Frankfurt": 227})


print("=== PETA JERMAN ===")
petajerman.tampilkanPeta()

[distances, routes] = petajerman.dijkstra("Berlin")
print(distances)
print(routes)
