import unittest
from typewise_alert import *

from breach_classifier import *
from sender import *
class TypewiseTest(unittest.TestCase):
  def test_check_and_alert(self):
    batteryChar = {}

    batteryChar['coolingType'] = 'PASSIVE_COOLING'
    alertTarget = 'TO_CONTROLLER'
    temperatureInC = 50
    self.assertTrue(check_and_alert(alertTarget,batteryChar,temperatureInC) == True) 

    batteryChar['coolingType'] = 'PASSIVE_COOLING'
    alertTarget = 'TO_EMAIL'
    temperatureInC = 50
    self.assertTrue(check_and_alert(alertTarget,batteryChar,temperatureInC) == True) 

    batteryChar['coolingType'] = 'PASSIVE_COOLING'
    alertTarget = 'TO_EMAIL'
    temperatureInC = 25
    self.assertTrue(check_and_alert(alertTarget,batteryChar,temperatureInC) == False) 

    batteryChar['coolingType'] = 'HI_ACTIVE_COOLING'
    alertTarget = 'TO_CONTROLLER'
    temperatureInC = 0
    self.assertTrue(check_and_alert(alertTarget,batteryChar,temperatureInC) == True) 

    batteryChar['coolingType'] = 'HI_ACTIVE_COOLING'
    alertTarget = 'TO_EMAIL'
    temperatureInC = 45
    self.assertTrue(check_and_alert(alertTarget,batteryChar,temperatureInC) == False) 

    batteryChar['coolingType'] = 'HI_ACTIVE_COOLING'
    alertTarget = 'TO_EMAIL'
    temperatureInC = 50
    self.assertTrue(check_and_alert(alertTarget,batteryChar,temperatureInC) == True) 

    batteryChar['coolingType'] = 'MED_ACTIVE_COOLING'
    alertTarget = 'TO_CONTROLLER'
    temperatureInC = 0
    self.assertTrue(check_and_alert(alertTarget,batteryChar,temperatureInC) == True) 

    batteryChar['coolingType'] = 'MED_ACTIVE_COOLING'
    alertTarget = 'TO_EMAIL'
    temperatureInC = 45
    self.assertTrue(check_and_alert(alertTarget,batteryChar,temperatureInC) == True) 

    batteryChar['coolingType'] = 'MED_ACTIVE_COOLING'
    alertTarget = 'TO_EMAIL'
    temperatureInC = 20
    self.assertTrue(check_and_alert(alertTarget,batteryChar,temperatureInC) == False) 
if __name__ == '__main__':
  unittest.main()
