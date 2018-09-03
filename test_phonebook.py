import unittest

from phonebook import Phonebook


class PhonebookTest(unittest.TestCase):

	def setUp(self):
		self.phonebook = Phonebook()

	def test_lookup_entry_by_name(self):
		self.phonebook.add("alice", "12345")
		self.assertEqual("12345", self.phonebook.lookup("alice"))

	def test_miss_entry_raises_KeyError(self):
		with self.assertRaises(KeyError):
			self.phonebook.lookup('missing')
