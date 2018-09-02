import unittest

from phonebook import Phonebook


class PhonebookTest(unittest.TestCase):

	def test_create_phonebook(self):
		phonebook = Phonebook()

	def test_lookup_entry_by_name(self):
		phonebook = Phonebook()
		phonebook.add("alice", "12345")
		self.assertEqual("12345", phonebook.lookup("alice"))

	def test_miss_entry_raises_KeyError(self):
		phonebook = Phonebook()
		with self.assertRaises(KeyError):
			phonebook.lookup('missing')
