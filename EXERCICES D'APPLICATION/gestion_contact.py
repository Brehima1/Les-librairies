def ajouter_contact(contacts, nom, telephone):
    contacts[nom] = telephone
    print(f"Contact {nom} ajouté.")

def supprimer_contact(contacts, nom):
    if nom in contacts:
        del contacts[nom]
        print(f"Contact {nom} supprimé.")
    else:
        print("Contact non trouvé.")

def rechercher_contact(contacts, nom):
    if nom in contacts:
        print(f"Nom: {nom}, Téléphone: {contacts[nom]}")
    else:
        print("Contact non trouvé.")