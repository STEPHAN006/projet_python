"""TP 2 - Les villes de Madagascar."""
import math
from itertools import combinations

villes = [("Antananarivo", -18.88, 47.51), ("Toamasina", -18.15, 49.40),
          ("Mahajanga", -15.72, 46.32), ("Fianarantsoa", -21.45, 47.09)]


def bornes(villes):
    coordonnees = [(lat, lon) for _, lat, lon in villes]
    latitudes, longitudes = zip(*coordonnees)
    return min(latitudes), max(latitudes), min(longitudes), max(longitudes)


def distance(p1, p2):
    return math.dist(p1, p2)


for nom, latitude, longitude in villes:
    print(f"{nom} : {latitude}, {longitude}")
print("Plus au nord :", max(villes, key=lambda ville: ville[1])[0])
lat_min, lat_max, lon_min, lon_max = bornes(villes)
print("Bornes :", lat_min, lat_max, lon_min, lon_max)
distances = {(a[0], b[0]): distance(a[1:], b[1:]) for a, b in combinations(villes, 2)}
print("Paires :", len(distances), distances)
try:
    villes[0][1] = -19
except TypeError:
    print("Un tuple est immuable : créez un nouveau tuple pour le corriger.")
