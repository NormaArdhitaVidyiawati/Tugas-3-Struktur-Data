"""
    Kelompok 6_2023E - Kumpulan Tugas Struktur Data

    1. Tsalist Habibil Muzakki - 23091397163 
    2. Aditya Revangga D.P - 23091397167 
    3. Norma Ardhita Vidyiawati - 23091397169
"""

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
