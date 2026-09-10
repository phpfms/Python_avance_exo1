# permet de récupérer/manipuler les personnes

# -*- coding: utf-8 -*-

"""
Gestion métier des personnes
"""

from daos.person_dao import PersonDao


class BusinessPerson:

    def __init__(self):
        self.person_dao = PersonDao()

    def get_person_by_id(self, id_person):
        """Récupère une personne grâce à son identifiant."""
        return self.person_dao.read(id_person)

    def add_person(self, person):
        """Ajoute une personne en base de données."""
        return self.person_dao.create(person)

    def update_person(self, person):
        """Modifie une personne."""
        self.person_dao.update(person)

    def delete_person(self, id_person):
        """Supprime une personne."""
        self.person_dao.delete(id_person)

