from employe import Employe
from entreprise.gestionnaire import Gestionnaire

# Création d'employés
emp1 = Employe("Dupont", "Jean", 3000)
emp2 = Employe("Martin", "Sophie", 3500)

# Création de gestionnaires
gest1 = Gestionnaire("Durand", "Paul", 5000, "Informatique")
gest2 = Gestionnaire("Lemoine", "Claire", 5500, "RH")

# Affichage
print("=== Employés ===")
emp1.afficher_infos()
print()
emp2.afficher_infos()

print("\n=== Gestionnaires ===")
gest1.afficher_infos()
print()
gest2.afficher_infos()