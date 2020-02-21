import unittest
from reverse import reverse_string

class stringTest(unittest.TestCase):

	def test_reverse(self):
		self.assertEqual(reverse_string('dog'),'god')



if __name__ == '__main__':
	unittest.main()