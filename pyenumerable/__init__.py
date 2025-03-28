"""
Implementation of .NET's IEnumerable interface in python W/ support for generics.
"""  # noqa: E501


from pyenumerable.implementations import PurePythonEnumerable
from pyenumerable.protocol import Enumerable

__all__ = ["Enumerable", "PurePythonEnumerable"]
__author__ = "AmirHossein Ahmadi"
__license__ = "WTFPL"
__version__ = "1.0.2"
__maintainer__ = "AmirHossein Ahmadi"
__email__ = "amirthehossein@gmail.com"
