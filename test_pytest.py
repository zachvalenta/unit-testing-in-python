from phonebook import Phonebook


def test_add_and_lookup_entry():
	phonebook = Phonebook()
	phonebook.add('alice', '12345')
	assert "12345" == phonebook.lookup('alice')
