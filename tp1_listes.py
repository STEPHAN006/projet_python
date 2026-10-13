"""TP 1 - Les notes d'une classe."""

notes = [12, 8, 15, 17, 9, 11, 14, 6, 13, 16]

print(f"{len(notes)} notes, moyenne {sum(notes) / len(notes):.2f}, min {min(notes)}, max {max(notes)}")

admises = [note for note in notes if note >= 10]
print(admises, f"{len(notes) - len(admises)} ajournés")

print(sorted(notes))
print(sorted(notes, reverse=True)[:3])

corrigees = [min(note + 2, 10) if note < 10 else note for note in notes]
print(corrigees)


def histogramme(notes):
    tranches = ((0, 4), (5, 9), (10, 14), (15, 20))
    for debut, fin in tranches:
        nombre = sum(debut <= note <= fin for note in notes)
        print(f"{debut}-{fin} | {'*' * nombre}")


def rang(notes, note):
    classement = sorted(notes, reverse=True)
    return classement.index(note) + 1


histogramme(notes)
print("Rang de 14 :", rang(notes, 14))
fusion = list(dict.fromkeys(notes + [15, 6, 18]))
print("Fusion sans doublons :", fusion)
