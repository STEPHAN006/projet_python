notes = [12, 8, 15, 17, 9, 11, 14, 6, 13, 16]

print(f"{len(notes)} notes")
print(f"moyenne {sum(notes) / len(notes):.2f}")
print(f"min {min(notes)} ")
print(f"max {max(notes)} ")

notes_sup = [x for x  in notes if x>=10]
ajourner = len([x for x  in notes if x<10])

print(notes_sup)
print(f"{ajourner} ajourner")

notes_trier = sorted(notes)
meilleur_3_notes = notes_trier[-3:]
print(notes_trier)
print(sorted(meilleur_3_notes, reverse=True))

notes_apres_deliberation = [x if x > 10 else 10 if x > 8 else x + 2 for x in notes]

print(notes_apres_deliberation)


def histogramme(notes):
    for note in notes:
        print("0 - 4 |")
        if (note >= 0 and note <= 4):
            print("*")
        
        print("5 - 9 |")
        if (note >= 5 and note <= 9):
            print("*")
        
        print("10 - 14 |")
        if (note >= 10 and note <= 14):
            print("*")
        
        print("15 - 20 |")
        if (note >= 15 and note <= 20):
            print("*")

histogramme(notes)