# fichier qui permet d'afficher le detail des menus choisis
# si l'utilisateur choisi 1 alors Application .py va recevoir 1 et le while qui aura appelé menu.py saura quoi en faire


class Menu:

    def display_main_menu(self):
        """Affiche le menu principal."""
        print("\n===== ÉCOLE =====")
        print("1. Opérations concernant les étudiants")
        print("2. Opérations concernant les professeurs")
        print("3. Opérations concernant les cours")
        print("4. Opérations concernant les adresses")
        print("0. Quitter")

        return input("Votre choix : ")

    def display_student_menu(self):
        """Affiche le sous-menu des étudiants."""
        print("\n===== ÉTUDIANTS =====")
        print("1. Afficher les étudiants")
        print("2. Afficher les cours d'un étudiant")
        print("3. Afficher les enseignants d'un étudiant")
        print("4. Ajouter un étudiant")
        print("5. Modifier un étudiant")
        print("6. Supprimer un étudiant")
        print("7. Inscrire un étudiant à un cours")
        print("8. Désinscrire un étudiant d'un cours")
        print("0. Retour")

        return input("Votre choix : ")

    def display_teacher_menu(self):
        """Affiche le sous-menu des professeurs."""
        print("\n===== PROFESSEURS =====")
        print("1. Afficher les professeurs")
        print("2. Afficher les élèves d'un professeur")
        print("3. Afficher les élèves qui suivent un cours")
        print("4. Afficher tous les élèves qui suivent au moins un cours du professeur")
        print("5. Créer un cours")
        print("6. Ajouter un professeur")
        print("7. Modifier un professeur")
        print("8. Supprimer un professeur")
        print("0. Retour")

        return input("Votre choix : ")

    def display_course_menu(self):
        """Affiche le sous-menu des cours."""
        print("\n===== COURS =====")
        print("1. Afficher la liste des cours")
        print("2. Afficher les étudiants d'un cours")
        print("3. Afficher l'enseignant d'un cours")
        print("4. Ajouter un cours")
        print("5. Modifier un cours")
        print("6. Supprimer un cours")
        print("0. Retour")

        return input("Votre choix : ")

    def display_address_menu(self):
        """Affiche le sous-menu des adresses."""
        print("\n===== ADRESSES =====")
        print("1. Afficher les adresses")
        print("2. Afficher les personnes habitant à une adresse")
        print("3. Ajouter une adresse")
        print("4. Modifier une adresse")
        print("5. Supprimer une adresse")
        print("0. Retour")

        return input("Votre choix : ")

