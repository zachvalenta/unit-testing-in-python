import unittest
from unittest.mock import Mock

from phonebook import Phonebook, PhysicalDimensions


class PhonebookTest(unittest.TestCase):

	def setUp(self):
		self.phonebook = Phonebook()

	def test_lookup_entry_by_name(self):
		self.phonebook.add("alice", "12345")
		self.assertEqual("12345", self.phonebook.lookup("alice"))

	def test_miss_entry_raises_KeyError(self):
		with self.assertRaises(KeyError):
			self.phonebook.lookup('missing')

	def test_less_than_2_pounds_stop_publishing(self):
		mock_phys = Mock(PhysicalDimensions())
		"""
		`mock_phys.weight = 1` if commented out
		yields this error from unittest: TypeError: '<' not supported between instances of 'Mock' and 'int'
		if real Phys defaults to weight=0, why not the mock?
		why can we set the field only after instantiation?
		"""
		mock_phys.weight = 1
		pb = Phonebook(dimensions=mock_phys)
		self.assertEqual('stop publishing', pb.keep_publishing())
