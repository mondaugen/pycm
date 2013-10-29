import unittest
from formfiller import augment_form_dict

def sf_1(s):
  return s[:3]

def gf_1():
  return [6,7,8,9,10]

class TestFormfiller(unittest.TestCase):

  def setUp(self):
    self.d_1 = { 'a' : [1,2,3,4,5] }
    self.fs_1 = 'aa'
    self.fs_2 = 'b'
    self.fs_3 = 'ba'


  def test_augment_form_dict_1(self):
    augment_form_dict(self.d_1, self.fs_1, sf_1, gf_1)
    self.assertEqual(self.d_1, { 'a' : [1,2,3,4,5], 'aa' : [1,2,3] })

  def test_augment_form_dict_2(self):
    augment_form_dict(self.d_1, self.fs_2, sf_1, gf_1)
    self.assertEqual(self.d_1, { 'a' : [1,2,3,4,5], 'b' : [6,7,8,9,10] })
    augment_form_dict(self.d_1, self.fs_1, sf_1, gf_1)
    augment_form_dict(self.d_1, self.fs_3, sf_1, gf_1)
    self.assertEqual(self.d_1, { 'a' : [1,2,3,4,5],
                                 'b' : [6,7,8,9,10],
                                 'aa': [1,2,3],
                                 'ba': [6,7,8] })

if __name__ == '__main__':
  unittest.main()

