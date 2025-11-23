print('Mon module de taches!')

def ajouter_tache(taches, tache):
    taches.append(tache)
    print(f"{tache}a été ajoutée !")
    
def supprimer_tache(taches, indice):
    tache_supprimee = taches.pop(indice)
    print(f"{tache_supprimee}a été retirée de la liste !")

def afficher_taches(taches):
    if taches :
        print("voici la liste de taches:")
        for indice , tache in enumerate(taches, start = 1):
            print(f'{indice}.{tache}')
    else: 
        print('votre liste est vide')        