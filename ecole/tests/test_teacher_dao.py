# -*- coding: utf-8 -*-

"""
Tests de la classe TeacherDao
"""

from datetime import date

from models.person import Person
from models.teacher import Teacher
from daos.person_dao import PersonDao
from daos.teacher_dao import TeacherDao


def test_create():
    person_dao = PersonDao()
    teacher_dao = TeacherDao()

    person = Person("Victor", "Hugo", 23)
    id_person = person_dao.create(person)

    teacher = Teacher("Victor", "Hugo", 23, date(2023, 9, 4))
    teacher.id_person = id_person

    id_teacher = teacher_dao.create(teacher)

    assert id_teacher is not None
    assert teacher.id_teacher == id_teacher


def test_read():
    person_dao = PersonDao()
    teacher_dao = TeacherDao()

    person = Person("Victor", "Hugo", 23)
    id_person = person_dao.create(person)

    teacher = Teacher("Victor", "Hugo", 23, date(2023, 9, 4))
    teacher.id_person = id_person

    id_teacher = teacher_dao.create(teacher)

    result = teacher_dao.read(id_teacher)

    assert result is not None
    assert result.id_teacher == id_teacher
    assert result.id_person == id_person
    assert result.first_name == "Victor"
    assert result.last_name == "Hugo"
    assert result.age == 23
    assert result.hiring_date == date(2023, 9, 4)


def test_update():
    person_dao = PersonDao()
    teacher_dao = TeacherDao()

    person = Person("Victor", "Hugo", 23)
    id_person = person_dao.create(person)

    teacher = Teacher("Victor", "Hugo", 23, date(2023, 9, 4))
    teacher.id_person = id_person

    id_teacher = teacher_dao.create(teacher)

    teacher.hiring_date = date(2024, 9, 1)

    teacher_dao.update(teacher)

    result = teacher_dao.read(id_teacher)

    assert result is not None
    assert result.id_teacher == id_teacher
    assert result.hiring_date == date(2024, 9, 1)


def test_delete():
    person_dao = PersonDao()
    teacher_dao = TeacherDao()

    person = Person("Victor", "Hugo", 23)
    id_person = person_dao.create(person)

    teacher = Teacher("Victor", "Hugo", 23, date(2023, 9, 4))
    teacher.id_person = id_person

    id_teacher = teacher_dao.create(teacher)

    teacher_dao.delete(id_teacher)

    result = teacher_dao.read(id_teacher)

    assert result is None