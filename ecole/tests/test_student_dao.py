# -*- coding: utf-8 -*-

"""
Tests de la classe StudentDao
"""

from models.person import Person
from models.student import Student
from daos.person_dao import PersonDao
from daos.student_dao import StudentDao


def test_create():
    person_dao = PersonDao()
    student_dao = StudentDao()

    person = Person("Paul", "Dubois", 12)
    id_person = person_dao.create(person)

    student = Student("Paul", "Dubois", 12)
    student.id_person = id_person

    student_nbr = student_dao.create(student)

    assert student_nbr is not None
    assert student.student_nbr == student_nbr


def test_read():
    person_dao = PersonDao()
    student_dao = StudentDao()

    person = Person("Paul", "Dubois", 12)
    id_person = person_dao.create(person)

    student = Student("Paul", "Dubois", 12)
    student.id_person = id_person

    student_nbr = student_dao.create(student)

    result = student_dao.read(student_nbr)

    assert result is not None
    assert result.student_nbr == student_nbr
    assert result.id_person == id_person
    assert result.first_name == "Paul"
    assert result.last_name == "Dubois"
    assert result.age == 12


def test_update():
    person_dao = PersonDao()
    student_dao = StudentDao()

    person = Person("Paul", "Dubois", 12)
    id_person = person_dao.create(person)

    student = Student("Paul", "Dubois", 12)
    student.id_person = id_person

    student_nbr = student_dao.create(student)

    person.first_name = "Jean"
    person.last_name = "Dupont"
    person.age = 15

    person_dao.update(person)

    result = student_dao.read(student_nbr)

    assert result is not None
    assert result.student_nbr == student_nbr
    assert result.id_person == id_person
    assert result.first_name == "Jean"
    assert result.last_name == "Dupont"
    assert result.age == 15


def test_delete():
    person_dao = PersonDao()
    student_dao = StudentDao()

    person = Person("Paul", "Dubois", 12)
    id_person = person_dao.create(person)

    student = Student("Paul", "Dubois", 12)
    student.id_person = id_person

    student_nbr = student_dao.create(student)

    student_dao.delete(student_nbr)

    result = student_dao.read(student_nbr)

    assert result is None