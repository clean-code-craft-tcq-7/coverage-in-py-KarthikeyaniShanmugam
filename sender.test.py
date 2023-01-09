import unittest
from sender import *
class SenderTest(unittest.TestCase):
    def test_sender(self):
        self.assertTrue(send_to_controller('TOO_HIGH') == True) 
        self.assertTrue(send_to_controller('TOO_LOW') == True) 
        self.assertTrue(send_to_controller('NORMAL') == True) 

        self.assertTrue(send_to_email('TOO_HIGH') == True) 
        self.assertTrue(send_to_email('TOO_LOW') == True) 
        self.assertTrue(send_to_email('NORMAL') == False) 

if __name__ == '__main__':
  unittest.main()