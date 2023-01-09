import unittest
from breach_classifier import *
class BreachClassifierTest(unittest.TestCase):
  def test_infers_and_limits_as_per_cooling_type(self):
    self.assertTrue(classify_temperature_breach('PASSIVE_COOLING',100) == 'TOO_HIGH')
    self.assertTrue(classify_temperature_breach('PASSIVE_COOLING',36) == 'TOO_HIGH')
    self.assertTrue(classify_temperature_breach('PASSIVE_COOLING',35.1) == 'TOO_HIGH')
    self.assertTrue(classify_temperature_breach('PASSIVE_COOLING',35) == 'NORMAL') 
    self.assertTrue(classify_temperature_breach('PASSIVE_COOLING',25) == 'NORMAL') 
    self.assertTrue(classify_temperature_breach('PASSIVE_COOLING',0) == 'NORMAL') 
    self.assertTrue(classify_temperature_breach('PASSIVE_COOLING',-0.01) == 'TOO_LOW') 
    self.assertTrue(classify_temperature_breach('PASSIVE_COOLING',-1) == 'TOO_LOW') 
    self.assertTrue(classify_temperature_breach('PASSIVE_COOLING',-25) == 'TOO_LOW') 

    self.assertTrue(classify_temperature_breach('HI_ACTIVE_COOLING',100) == 'TOO_HIGH')
    self.assertTrue(classify_temperature_breach('HI_ACTIVE_COOLING',46) == 'TOO_HIGH')
    self.assertTrue(classify_temperature_breach('HI_ACTIVE_COOLING',45.1) == 'TOO_HIGH')
    self.assertTrue(classify_temperature_breach('HI_ACTIVE_COOLING',45) == 'NORMAL') 
    self.assertTrue(classify_temperature_breach('HI_ACTIVE_COOLING',25) == 'NORMAL') 
    self.assertTrue(classify_temperature_breach('HI_ACTIVE_COOLING',0) == 'NORMAL') 
    self.assertTrue(classify_temperature_breach('HI_ACTIVE_COOLING',-0.01) == 'TOO_LOW') 
    self.assertTrue(classify_temperature_breach('HI_ACTIVE_COOLING',-1) == 'TOO_LOW') 
    self.assertTrue(classify_temperature_breach('HI_ACTIVE_COOLING',-25) == 'TOO_LOW') 

    self.assertTrue(classify_temperature_breach('MED_ACTIVE_COOLING',100) == 'TOO_HIGH')
    self.assertTrue(classify_temperature_breach('MED_ACTIVE_COOLING',46) == 'TOO_HIGH')
    self.assertTrue(classify_temperature_breach('MED_ACTIVE_COOLING',40.1) == 'TOO_HIGH')
    self.assertTrue(classify_temperature_breach('MED_ACTIVE_COOLING',40) == 'NORMAL') 
    self.assertTrue(classify_temperature_breach('MED_ACTIVE_COOLING',25) == 'NORMAL') 
    self.assertTrue(classify_temperature_breach('MED_ACTIVE_COOLING',0) == 'NORMAL') 
    self.assertTrue(classify_temperature_breach('MED_ACTIVE_COOLING',-0.01) == 'TOO_LOW') 
    self.assertTrue(classify_temperature_breach('MED_ACTIVE_COOLING',-1) == 'TOO_LOW') 
    self.assertTrue(classify_temperature_breach('MED_ACTIVE_COOLING',-25) == 'TOO_LOW') 


if __name__ == '__main__':
  unittest.main()