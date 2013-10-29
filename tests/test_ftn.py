import unittest
from ftn import FormTreeNode

class TestFormTreeNode(unittest.TestCase):

  def setUp(self):
    self.t_1 = FormTreeNode(children=[ FormTreeNode(name='a'),
                                       FormTreeNode(name='b'),
                                       FormTreeNode(name='a'),
                                       FormTreeNode(name='c')],
                            name = 'a')
    self.d_1 = { 'a' : 'aabcb', 'b' : 'abc', 'c' : 'zzx' }

  def test_get_section_names_1(self):
    names = self.t_1.get_section_names()
    self.assertEqual(names,['aa','ab','aa','ac'])

  def test_grow_using_dict_1(self):
    ft = FormTreeNode(name = 'a', children = [])
    ft.grow_using_dict(self.d_1)
    names = ft.get_section_names()
    del ft
    self.assertEqual(names,['aa','aa','ab','ac','ab'])

  def test_grow_using_dict_2(self):
    ft2 = FormTreeNode(name = 'a', children = [])
    ft2.grow_using_dict(self.d_1)
    ft2.grow_using_dict(self.d_1)
    names = ft2.get_section_names()
    self.assertEqual(names,[  'aaa',
                              'aaa',
                              'aab',
                              'aac',
                              'aab',
                              'aaa',
                              'aaa',
                              'aab',
                              'aac',
                              'aab',
                              'aba',
                              'abb',
                              'abc',
                              'acz',
                              'acz',
                              'acx',
                              'aba',
                              'abb',
                              'abc'  ])

if __name__ == '__main__':
  unittest.main()

