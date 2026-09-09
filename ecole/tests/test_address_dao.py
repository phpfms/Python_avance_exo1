from models.address import Address
from daos.address_dao import AddressDao


def test_create():
    dao = AddressDao()

    address = Address(
        "10 rue de Paris",
        "Toulouse",
        "31000"
    )

    id_address = dao.create(address)

    assert id_address is not None
    assert address.id == id_address


def test_read():
    dao = AddressDao()

    address = Address(
        "10 rue de Paris",
        "Toulouse",
        "31000"
    )

    id_address = dao.create(address)

    result = dao.read(id_address)

    assert result is not None
    assert result.id == id_address
    assert result.street == "10 rue de Paris"
    assert result.city == "Toulouse"
    assert result.postal_code == "31000"


def test_update():
    dao = AddressDao()

    address = Address(
        "10 rue de Paris",
        "Toulouse",
        "31000"
    )

    id_address = dao.create(address)

    address.street = "20 rue de Bordeaux"
    address.city = "Bordeaux"
    address.postal_code = "33000"

    dao.update(address)

    result = dao.read(id_address)

    assert result is not None
    assert result.street == "20 rue de Bordeaux"
    assert result.city == "Bordeaux"
    assert result.postal_code == "33000"


def test_delete():
    dao = AddressDao()

    address = Address(
        "10 rue de Paris",
        "Toulouse",
        "31000"
    )

    id_address = dao.create(address)

    dao.delete(id_address)

    result = dao.read(id_address)

    assert result is None