import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from optrush import models         # The Python libraries
from optrush import optrush        # The Rust libraries

import math


def test_cdf():
    for i in range(-10000, 10000):
        x = 0.5 * i
        assert f'{models.norm_cdf(x):.8f}' == f'{optrush.norm_cdf(x):.8f}'

def test_pdf():
    for i in range(-10000, 10000):
        x = 0.5 * i
        assert f'{models.norm_pdf(x):.8f}' == f'{optrush.norm_pdf(x):.8f}'