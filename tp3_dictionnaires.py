"""TP 3 - Le stock d'une épicerie."""
import json
from collections import Counter

stock = {"riz": {"prix": 3200, "quantite": 50}, "huile": {"prix": 9500, "quantite": 12},
         "sucre": {"prix": 4000, "quantite": 30}, "savon": {"prix": 1500, "quantite": 0}}


def vendre(stock, produit, quantite):
    article = stock.get(produit)
    if article is None:
        return False, f"Produit inconnu : {produit}"
    if quantite > article["quantite"]:
        return False, "Quantité insuffisante"
    article["quantite"] -= quantite
    return True, "Vente effectuée"


def ajouter_produit(stock, nom, prix, quantite):
    if nom in stock:
        return False
    stock[nom] = {"prix": prix, "quantite": quantite}
    return True


for nom, article in stock.items():
    print(nom, article["prix"], "Ar", article["quantite"])
print("Valeur :", sum(a["prix"] * a["quantite"] for a in stock.values()), "Ar")
print("Rupture :", [nom for nom, a in stock.items() if a["quantite"] == 0])
print(vendre(stock, "riz", 3), vendre(stock, "café", 1), vendre(stock, "savon", 1))
print("Prix +10% :", {nom: round(a["prix"] * 1.10) for nom, a in stock.items()})
ventes = ["riz", "sucre", "riz", "huile", "riz"]
compte = {}
for produit in ventes:
    compte[produit] = compte.get(produit, 0) + 1
print(compte, dict(Counter(ventes)))
with open("stock.json", "w", encoding="utf-8") as fichier:
    json.dump(stock, fichier, ensure_ascii=False, indent=2)
with open("stock.json", encoding="utf-8") as fichier:
    print("JSON identique :", json.load(fichier) == stock)
