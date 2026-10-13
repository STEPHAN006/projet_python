"""TP 5 - Projet de synthèse : carnet de notes."""
import json
from datetime import datetime
from functools import wraps

etudiants = {"L3-001": {"nom": "Rakoto", "prenom": "Soa", "notes": {"Python": [15, 14], "Réseaux": [12]}},
             "L3-002": {"nom": "Rabe", "prenom": "Andry", "notes": {"Python": [9, 13], "Réseaux": [11, 10]}}}
historique = []


def journaliser(f):
    @wraps(f)
    def w(*args, **kwargs):
        resultat = f(*args, **kwargs); historique.append((datetime.now().isoformat(timespec="seconds"), f.__name__, args)); return resultat
    return w

def etudiant_existe(f):
    @wraps(f)
    def w(matricule, *args, **kwargs):
        if matricule not in etudiants: raise KeyError(f"Matricule inconnu : {matricule}")
        return f(matricule, *args, **kwargs)
    return w

def note_valide(f):
    @wraps(f)
    def w(matricule, matiere, note):
        if not 0 <= note <= 20: raise ValueError("Une note doit être comprise entre 0 et 20")
        return f(matricule, matiere, note)
    return w

@journaliser
def ajouter_etudiant(matricule, nom, prenom):
    if matricule in etudiants: raise ValueError("Matricule déjà utilisé")
    etudiants[matricule] = {"nom": nom, "prenom": prenom, "notes": {}}

@journaliser
@etudiant_existe
@note_valide
def ajouter_note(matricule, matiere, note):
    etudiants[matricule]["notes"].setdefault(matiere, []).append(note)

@etudiant_existe
def moyenne_matiere(matricule, matiere):
    notes = etudiants[matricule]["notes"].get(matiere, [])
    return sum(notes) / len(notes) if notes else 0

@etudiant_existe
def moyenne_generale(matricule):
    moyennes = [sum(n) / len(n) for n in etudiants[matricule]["notes"].values() if n]
    return sum(moyennes) / len(moyennes) if moyennes else 0

def classement():
    return sorted(((f"{e['prenom']} {e['nom']}", moyenne_generale(m)) for m, e in etudiants.items()), key=lambda x: x[1], reverse=True)

def majors():
    matieres = {matiere for e in etudiants.values() for matiere in e["notes"]}
    return {matiere: max(etudiants, key=lambda m: moyenne_matiere(m, matiere)) for matiere in matieres}

def sauvegarder(fichier):
    with open(fichier, "w", encoding="utf-8") as f: json.dump(etudiants, f, ensure_ascii=False, indent=2)

def charger(fichier):
    global etudiants
    with open(fichier, encoding="utf-8") as f: etudiants = json.load(f)

def menu():
    print("\n1. Ajouter étudiant  2. Ajouter note  3. Bulletin  4. Classement  5. Majors  6. Historique  7. Sauvegarder  0. Quitter")
    while (choix := input("Choix : ")) != "0":
        try:
            if choix == "1": ajouter_etudiant(input("Matricule : "), input("Nom : "), input("Prénom : "))
            elif choix == "2": ajouter_note(input("Matricule : "), input("Matière : "), float(input("Note : ")))
            elif choix == "3":
                m = input("Matricule : "); print(etudiants[m], moyenne_generale(m))
            elif choix == "4": print(classement())
            elif choix == "5": print(majors())
            elif choix == "6": print(*historique, sep="\n")
            elif choix == "7": sauvegarder(input("Fichier : "))
        except (KeyError, ValueError) as erreur: print(erreur)

menu()
