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
