#!/usr/bin/python3
"""Myint class that inverts equality"""


class MyInt(int):
    """MyInt class inverst operators == and !="""

    def __eq__(self, value):
        """Override == opeartor with != behavior"""
        return not super().__eq__(value)

    def __ne__(self, value):
        """Override != operator with == behavior"""
        return super().__eq__(value)
