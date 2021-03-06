# 练习
# 对Student类编写单元测试，结果发现测试不通过，请修改Student类，让测试通过：


import unittest

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        if not isinstance(self.score, (int, float)):
            raise TypeError("%s is not int or float!" % self.score)
        if self.score < 0 or self.score > 100:
            raise ValueError("%s is not between 0 and 100!" % self.score)
        if self.score >= 80:
            return 'A'
        if self.score >= 60:
            return 'B'
        return 'C'
        
        
class TestStudent(unittest.TestCase):

    def test_80_to_100(self):
        s1 = Student('Bart', 80)
        s2 = Student('Lisa', 100)
        self.assertEqual(s1.get_grade(), 'A')
        self.assertEqual(s2.get_grade(), 'A')

    def test_60_to_80(self):
        s1 = Student('Bart', 60)
        s2 = Student('Lisa', 79)
        self.assertEqual(s1.get_grade(), 'B')
        self.assertEqual(s2.get_grade(), 'B')

    def test_0_to_60(self):
        s1 = Student('Bart', 0)
        s2 = Student('Lisa', 59)
        self.assertEqual(s1.get_grade(), 'C')
        self.assertEqual(s2.get_grade(), 'C')

    def test_invalid(self):
        s1 = Student('Bart', -1)
        s2 = Student('Lisa', 101)
        s3 = Student('Ling', 'A')
        with self.assertRaises(ValueError):
            s1.get_grade()
        with self.assertRaises(ValueError):
            s2.get_grade()
        with self.assertRaises(TypeError):
            s3.get_grade()
            
    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')
    
    
if __name__ == '__main__':
    unittest.main()