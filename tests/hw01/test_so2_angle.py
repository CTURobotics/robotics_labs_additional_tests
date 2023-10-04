#!/usr/bin/env python
#
# Copyright (c) CTU -- All Rights Reserved
# Created on: 2023-10-4
#     Author: Vladimir Petrik <vladimir.petrik@cvut.cz>
#
import unittest
import numpy as np

from robotics_toolbox.core import SO2


class TestSO2Angle(unittest.TestCase):
    def test_so2_angle(self):
        """Test computation of angle from rotation matrix. """
        np.random.seed(0)
        for _ in range(100):
            a = np.random.uniform(-np.pi + 0.01, np.pi - 0.01)
            self.assertAlmostEqual(SO2(angle=a).angle, a)


if __name__ == '__main__':
    unittest.main()
