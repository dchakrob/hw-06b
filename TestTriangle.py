# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle


class TestTriangles(unittest.TestCase):

    def testRightTriangleA(self):
        self.assertEqual(
            classifyTriangle(3, 4, 5),
            'Right',
            '3,4,5 is a Right triangle'
        )

    def testRightTriangleB(self):
        self.assertEqual(
            classifyTriangle(5, 3, 4),
            'Right',
            '5,3,4 is a Right triangle'
        )

    def testRightTriangleC(self):
        self.assertEqual(
            classifyTriangle(4, 5, 3),
            'Right',
            '4,5,3 is a Right triangle'
        )

    def testEquilateralTriangles(self):
        self.assertEqual(
            classifyTriangle(1, 1, 1),
            'Equilateral',
            '1,1,1 should be Equilateral'
        )

    def testIsoscelesTriangleA(self):
        self.assertEqual(
            classifyTriangle(5, 5, 3),
            'Isoceles',
            '5,5,3 should be Isoceles'
        )

    def testIsoscelesTriangleB(self):
        self.assertEqual(
            classifyTriangle(5, 3, 5),
            'Isoceles',
            '5,3,5 should be Isoceles'
        )

    def testIsoscelesTriangleC(self):
        self.assertEqual(
            classifyTriangle(3, 5, 5),
            'Isoceles',
            '3,5,5 should be Isoceles'
        )

    def testScaleneTriangle(self):
        self.assertEqual(
            classifyTriangle(4, 5, 6),
            'Scalene',
            '4,5,6 should be Scalene'
        )

    def testNotATriangle(self):
        self.assertEqual(
            classifyTriangle(1, 2, 3),
            'NotATriangle',
            '1,2,3 should not form a triangle'
        )

    def testInvalidZero(self):
        self.assertEqual(
            classifyTriangle(0, 1, 1),
            'InvalidInput',
            '0,1,1 contains an invalid side length'
        )

    def testInvalidNegative(self):
        self.assertEqual(
            classifyTriangle(-1, 2, 2),
            'InvalidInput',
            '-1,2,2 contains an invalid side length'
        )

    def testInvalidOver200(self):
        self.assertEqual(
            classifyTriangle(201, 200, 200),
            'InvalidInput',
            '201,200,200 contains a side greater than 200'
        )

    def testInvalidNonInteger(self):
        self.assertEqual(
            classifyTriangle(3.0, 4, 5),
            'InvalidInput',
            '3.0,4,5 contains a non-integer input'
        )


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()