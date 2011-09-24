import unittest

from fsegments import fsegments

cases = [
    ("one arg",
     [4],
            [(0.0, 0.25), (0.25, 0.5), (0.5, 0.75), (0.75, 1.0)]),
    ("two args",
     [3, 2.1],
            [(0.0, 0.7), (0.7, 1.4), (1.4, 2.1)]),
    ("three args",
     [3, 1.0, 2.2],
            [(1.0, 1.4), (1.4, 1.8), (1.8, 2.2)]),

    ("wide range",
     [2, -9e+307, 9e+307],
            [(-9e+307, 0.0), (0.0, 9e+307)])
]


class TestFSegments(unittest.TestCase):
    
    def test_output(self):
        for (case, args, expected) in cases:
            result = list(fsegments(*args))
            self.assertEqual(result, expected, msg=case)

    def test_wellformed(self):
        for (case, args, expected) in cases:
            result = list(fsegments(*args))
            for i in range(1, len(result)):
                self.assertEqual(result[i-1][1], result[i][0],
                    msg=("segment %d start != end of prior segment" % i))
    
    def test_startpresent(self):
        for (case, args, expected) in cases:
            result = list(fsegments(*args))
            start = 0.0
            if len(args) > 2:
                start = args[1]
            self.assertEqual(result[0][0], start)

    def test_endpresent(self):
        for (case, args, expected) in cases:
            result = list(fsegments(*args))
            end = 1.0
            if len(args) > 1:
                end = args[-1]
            self.assertEqual(result[-1][1], end)
            
    def test_numsegments(self):
        for (case, args, expected) in cases:
            result = list(fsegments(*args))
            self.assertEqual(len(result), args[0])

if __name__ == '__main__':
    unittest.main()

    