#!/usr/bin/python3
"""
lazy matrix multiplication module
"""

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    try:
        result = np.dot(m_a, m_b)
        return result
    except ValueError:
        raise ValueError("Matrix dimensions must match")
