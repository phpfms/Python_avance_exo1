# -*- coding: utf-8 -*-

"""
Classe Dao[Address]
"""

from models.address import Address
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional

@dataclass
class AddressDao(Dao[Address]):

    def create(self, address: Address) -> int:
        with Dao.connection.cursor() as cursor:
            sql = "INSERT INTO address (street, city, postal_code) VALUES (%s, %s, %s)"
            cursor.execute( sql,(address.street, address.city, address.postal_code))
            id_address = cursor.lastrowid
        Dao.connection.commit()
        address.id = id_address
        return id_address

    def read(self, id_address: int) -> Optional[Address]:
        """Renvoie le cours correspondant à l'entité dont l'id est id_address
           (ou None s'il n'a pu être trouvé)"""
        address: Optional[Address]
        with Dao.connection.cursor() as cursor:
            sql = "SELECT * FROM address WHERE id_address=%s"
            cursor.execute(sql, (id_address,))
            record = cursor.fetchone()
        if record is not None:
            address = Address(record['street'], record['city'], record['postal_code'])
            address.id = record['id_address']
        else:
            address = None

        return address

    def update(self, address: Address) -> None:
        """Modifie une adresse existante en BDD."""
        with Dao.connection.cursor() as cursor:
            sql = " UPDATE address SET street=%s, city=%s, postal_code=%s WHERE id_address=%s "
            cursor.execute( sql,(address.street,address.city,address.postal_code,address.id))
        Dao.connection.commit()

    def delete(self, id_address: int) -> None:
        """Supprime une adresse de la BDD."""
        with Dao.connection.cursor() as cursor:
            sql = "DELETE FROM address WHERE id_address=%s"
            cursor.execute(sql, (id_address,))
        Dao.connection.commit()