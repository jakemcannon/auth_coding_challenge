import unittest
from reverse import reverse_string
from reverse import reverse_sentence


class stringTest(unittest.TestCase):

	def test_reverse_string(self):
		self.assertEqual(reverse_string('dog'),'god')
		

	def test_reverse_sentence(self):
		self.assertEqual(reverse_sentence('hello world'), 'dlrow olleh')


if __name__ == '__main__':
	unittest.main()