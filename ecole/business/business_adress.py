# permet de récupérer/manipuler les adresses

# -*- coding: utf-8 -*-

"""
Gestion métier des adresses
"""

from daos.address_dao import AddressDao


class BusinessAddress:

    def __init__(self):
        self.address_dao = AddressDao()

    def get_address_by_id(self, id_address):
        """Récupère une adresse grâce à son identifiant."""
        return self.address_dao.read(id_address)

    def add_address(self, address):
        """Ajoute une adresse en base de données."""
        return self.address_dao.create(address)

    def update_address(self, address):
        """Modifie une adresse."""
        self.address_dao.update(address)

    def delete_address(self, id_address):
        """Supprime une adresse."""
        self.address_dao.delete(id_address)

