# -*- coding: utf-8 -*-

"""
Tests de la classe PersonDao
"""

from models.person import Person
from daos.person_dao import PersonDao


def test_create():
    dao = PersonDao()
    person = Person("Paul", "Dubois", 12)

    id_person = dao.create(person)

    assert id_person is not None
    assert person.id == id_person


def test_read():
    dao = PersonDao()
    person = Person("Paul", "Dubois", 12)

    id_person = dao.create(person)

    result = dao.read(id_person)

    assert result is not None
    assert result.id == id_person
    assert result.first_name == "Paul"
    assert result.last_name == "Dubois"
    assert result.age == 12


def test_update():
    dao = PersonDao()
    person = Person("Paul", "Dubois", 12)

    id_person = dao.create(person)

    person.first_name = "Jean"
    person.last_name = "Dupont"
    person.age = 25

    dao.update(person)

    result = dao.read(id_person)

    assert result is not None
    assert result.id == id_person
    assert result.first_name == "Jean"
    assert result.last_name == "Dupont"
    assert result.age == 25


def test_delete():
    dao = PersonDao()
    person = Person("Paul", "Dubois", 12)

    id_person = dao.create(person)

    dao.delete(id_person)

    result = dao.read(id_person)

    assert result is None

