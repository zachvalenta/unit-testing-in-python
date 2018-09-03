import pytest

from phonebook import Phonebook


@pytest.fixture
def phonebook():
	return Phonebook()


def test_add_and_lookup_entry(phonebook):
	phonebook.add('alice', '12345')
	assert "12345" == phonebook.lookup('alice')


def test_missing_entry_raises_KeyError(phonebook):
	with pytest.raises(KeyError):
		phonebook.lookup('missing')
