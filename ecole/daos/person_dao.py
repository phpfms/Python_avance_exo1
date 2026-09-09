# -*- coding: utf-8 -*-

"""
Classe Dao[Person]
"""

from models.person import Person
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional

@dataclass
class PersonDao(Dao[Person]):

    def create(self, person: Person) -> int:
        with Dao.connection.cursor() as cursor:
            sql = "INSERT INTO person (first_name, last_name, age) VALUES (%s, %s, %s)"
            cursor.execute( sql,(person.first_name, person.last_name, person.age))
            id_person = cursor.lastrowid
        Dao.connection.commit()
        person.id_person = id_person
        return id_person

    def read(self, id_person: int) -> Optional[Person]:
        """Renvoie le cours correspondant à l'entité dont l'id est id_person
           (ou None s'il n'a pu être trouvé)"""
        person: Optional[Person]
        with Dao.connection.cursor() as cursor:
            sql = "SELECT * FROM person WHERE id_person=%s"
            cursor.execute(sql, (id_person,))
            record = cursor.fetchone()
        if record is not None:
            person = Person(record['first_name'], record['last_name'], record['age'])
            person.id_person = record['id_person']
        else:
            person = None

        return person

    def update(self, person: Person) -> None:
        """Modifie une adresse existante en BDD."""
        with Dao.connection.cursor() as cursor:
            sql = " UPDATE person SET first_name=%s, last_name=%s, age=%s WHERE id_person=%s "
            cursor.execute(sql, (person.first_name, person.last_name, person.age, person.id_person))
        Dao.connection.commit()

    def delete(self, id_person: int) -> None:
        """Supprime une adresse de la BDD."""
        with Dao.connection.cursor() as cursor:
            sql = "DELETE FROM person WHERE id_person=%s"
            cursor.execute(sql, (id_person,))
        Dao.connection.commit()