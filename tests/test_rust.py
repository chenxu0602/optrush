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

def test_d1_d2():
    for r in [0, 0.05, 0.1, 0.2]:
        for t in range(1, 5):
            for sigma in [0.05, 0.1, 0.2, 0.5]:
                for s in range(10, 200, 15):
                    f = s * math.exp(r * t)
                    for k in [s - 8, s + 10]:
                        assert f'{models.bs_d1(s, k, t, r, sigma):.6f}' == f'{optrush.bs_d1(s, k, t, r, sigma):.6f}'
                        assert f'{models.bs_d2(s, k, t, r, sigma):.6f}' == f'{optrush.bs_d2(s, k, t, r, sigma):.6f}'
                        assert f'{models.bk_d1(f, k, t, sigma):.6f}'    == f'{optrush.bk_d1(f, k, t, sigma):.6f}'
                        assert f'{models.bk_d2(f, k, t, sigma):.6f}'    == f'{optrush.bk_d2(f, k, t, sigma):.6f}'

def test_call_price():
    for r in [0, 0.05, 0.1, 0.2]:
        for t in range(1, 5):
            for sigma in [0.05, 0.1, 0.2, 0.5]:
                for s in range(10, 200, 15):
                    f = s * math.exp(r * t)
                    for k in [s - 8, s + 10]:
                        assert f'{models.bs_call_price(s, k, t, r, sigma):.5f}' == f'{optrush.bs_call_price(s, k, t, r, sigma):.5f}'
                        assert f'{models.bk_call_price(s, k, t, r, sigma):.5f}' == f'{optrush.bk_call_price(s, k, t, r, sigma):.5f}'

def test_put_price():
    for r in [0, 0.05, 0.1, 0.2]:
        for t in range(1, 5):
            for sigma in [0.05, 0.1, 0.2, 0.5]:
                for s in range(20, 200, 15):
                    f = s * math.exp(r * t)
                    for k in [s - 8, s + 10]:
                        assert f'{models.bs_put_price(s, k, t, r, sigma):.5f}' == f'{optrush.bs_put_price(s, k, t, r, sigma):.5f}'
                        assert f'{models.bk_put_price(s, k, t, r, sigma):.5f}' == f'{optrush.bk_put_price(s, k, t, r, sigma):.5f}'

def test_gamma_vega():
    for r in [0, 0.05, 0.1, 0.2]:
        for t in range(1, 5):
            for sigma in [0.05, 0.1, 0.2, 0.5]:
                for s in range(10, 200, 15):
                    f = s * math.exp(r * t)
                    for k in [s - 8, s + 10]:
                        assert f'{models.bs_gamma(s, k, t, r, sigma):.5f}' == f'{optrush.bs_gamma(s, k, t, r, sigma):.5f}'
                        assert f'{models.bk_gamma(f, k, t, r, sigma):.5f}' == f'{optrush.bk_gamma(f, k, t, r, sigma):.5f}'
                        assert f'{models.bs_vega(s, k, t, r, sigma):.5f}'  == f'{optrush.bs_vega(s, k, t, r, sigma):.5f}'
                        assert f'{models.bk_vega(f, k, t, r, sigma):.5f}'  == f'{optrush.bk_vega(f, k, t, r, sigma):.5f}'

def test_rho():
    for r in [0, 0.05, 0.1, 0.2]:
        for t in range(1, 5):
            for sigma in [0.05, 0.1, 0.2, 0.5]:
                for s in range(10, 200, 15):
                    f = s * math.exp(r * t)
                    for k in [s - 8, s + 10]:
                        assert f'{models.bs_call_rho(s, k, t, r, sigma):.4f}' == f'{optrush.bs_call_rho(s, k, t, r, sigma):.4f}'
                        assert f'{models.bs_put_rho(s, k, t, r, sigma):.4f}'  == f'{optrush.bs_put_rho(s, k, t, r, sigma):.4f}'
                        assert f'{models.bk_call_rho(f, k, t, r, sigma):.4f}' == f'{optrush.bk_call_rho(f, k, t, r, sigma):.4f}'
                        assert f'{models.bk_put_rho(f, k, t, r, sigma):.4f}'  == f'{optrush.bk_put_rho(f, k, t, r, sigma):.4f}'

def test_theta():
    for r in [0, 0.05, 0.1, 0.2]:
        for t in range(1, 5):
            for sigma in [0.05, 0.1, 0.2, 0.5]:
                for s in range(10, 200, 15):
                    f = s * math.exp(r * t)
                    for k in [s - 8, s + 10]:
                        assert f'{models.bs_call_theta(s, k, t, r, sigma):.4f}' == f'{optrush.bs_call_theta(s, k, t, r, sigma):.4f}'
                        assert f'{models.bs_put_theta(s, k, t, r, sigma):.4f}'  == f'{optrush.bs_put_theta(s, k, t, r, sigma):.4f}'
                        assert f'{models.bk_call_theta(f, k, t, r, sigma):.4f}' == f'{optrush.bk_call_theta(f, k, t, r, sigma):.4f}'
                        assert f'{models.bk_put_theta(f, k, t, r, sigma):.4f}'  == f'{optrush.bk_put_theta(f, k, t, r, sigma):.4f}'