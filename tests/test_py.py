import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import math
from optrush import models


def test_erf_0():            assert math.erf(0) == 0
def test_erf_1e4():          assert math.erf(1e4) == 1.


def test_cdf_0():            assert models.norm_cdf(0) == 0.5
def test_cdf_1():            assert f'{models.norm_cdf(1):.2f}' == '0.84'
def test_cdf_1e4():          assert models.norm_cdf(1e4) == 1.


def test_bs_call_price_01(): assert f'{models.bs_call_price(100, 100, 1, 0.05, 0.10):.2f}' == '6.80'
def test_bs_call_price_02(): assert f'{models.bs_call_price(100, 120, 2, 0.10, 0.20):.2f}' == '12.05'

def test_bs_put_price_01():  assert f'{models.bs_put_price(100, 100, 1, 0.05, 0.10):.2f}'  == '1.93'
def test_bs_put_price_02():  assert f'{models.bs_put_price(100, 120, 2, 0.10, 0.20):.2f}'  == '10.29'

def test_bs_call_delta_01(): assert f'{models.bs_call_delta(100, 100, 1, 0.05, 0.10):.2f}' == '0.71'
def test_bs_call_delta_02(): assert f'{models.bs_call_delta(100, 120, 2, 0.10, 0.20):.2f}' == '0.58'

def test_bs_put_delta_01():  assert f'{models.bs_put_delta(100, 100, 1, 0.05, 0.10):.2f}'  == '-0.29'
def test_bs_put_delta_02():  assert f'{models.bs_put_delta(100, 120, 2, 0.10, 0.20):.2f}'  == '-0.42'

def test_bs_gamma_01():      assert f'{models.bs_gamma(100, 100, 1, 0.05, 0.10):.3f}'      == '0.034'
def test_bs_gamma_02():      assert f'{models.bs_gamma(100, 120, 2, 0.10, 0.20):.3f}'      == '0.014'

def test_bs_vega_01():       assert f'{models.bs_vega(100, 100, 1, 0.05, 0.10):.1f}'       == '34.3'
def test_bs_vega_02():       assert f'{models.bs_vega(100, 120, 2, 0.10, 0.20):.1f}'       == '55.3'

def test_bs_call_theta_01(): assert f'{models.bs_call_theta(100, 100, 1, 0.05, 0.10):.2f}' == '-4.92'
def test_bs_call_theta_02(): assert f'{models.bs_call_theta(100, 120, 2, 0.10, 0.20):.2f}' == '-7.37'

def test_bs_put_theta_01():  assert f'{models.bs_put_theta(100, 100, 1, 0.05, 0.10):.2f}'  == '-0.16'
def test_bs_put_theta_02():  assert f'{models.bs_put_theta(100, 120, 2, 0.10, 0.20):.2f}'  == '2.46'

def test_bs_call_rho_01():   assert f'{models.bs_call_rho(100, 100, 1, 0.05, 0.10):.2f}'   == '64.08'
def test_bs_call_rho_02():   assert f'{models.bs_call_rho(100, 120, 2, 0.10, 0.20):.2f}'   == '92.07'

def test_bs_put_rho_01():    assert f'{models.bs_put_rho(100, 100, 1, 0.05, 0.10):.2f}'    == '-31.04'
def test_bs_put_rho_02():    assert f'{models.bs_put_rho(100, 120, 2, 0.10, 0.20):.2f}'    == '-104.43'


def test_bk_call_price_01():
    s, k, t, r, sigma = 100, 100, 1, 0.05, 0.10
    f = s * math.exp(r * t)
    bs_call = models.bs_call_price(s, k, t, r, sigma)
    bk_call = models.bk_call_price(f, k, t, r, sigma)
    assert f'{bs_call:.3f}' == f'{bk_call:.3f}'

def test_bk_call_price_02():
    s, k, t, r, sigma = 100, 120, 2, 0.10, 0.20
    f = s * math.exp(r * t)
    bs_call = models.bs_call_price(s, k, t, r, sigma)
    bk_call = models.bk_call_price(f, k, t, r, sigma)
    assert f'{bs_call:.3f}' == f'{bk_call:.3f}'

def test_bk_put_price_01():
    s, k, t, r, sigma = 100, 100, 1, 0.05, 0.10
    f = s * math.exp(r * t)
    bs_put = models.bs_put_price(s, k, t, r, sigma)
    bk_put = models.bk_put_price(f, k, t, r, sigma)
    assert f'{bs_put:.3f}' == f'{bk_put:.3f}'

def test_bk_put_price_02():
    s, k, t, r, sigma = 100, 120, 2, 0.10, 0.20
    f = s * math.exp(r * t)
    bs_put = models.bs_put_price(s, k, t, r, sigma)
    bk_put = models.bk_put_price(f, k, t, r, sigma)
    assert f'{bs_put:.3f}' == f'{bk_put:.3f}'

def test_bk_call_delta_01():
    s, k, t, r, sigma = 100, 100, 1, 0.05, 0.10
    f = s * math.exp(r * t)
    bk_call = models.bk_call_delta(f, k, t, r, sigma)
    assert f'{bk_call:.2f}' == '0.67'

def test_bk_call_delta_02():
    s, k, t, r, sigma = 100, 120, 2, 0.10, 0.20
    f = s * math.exp(r * t)
    bk_call = models.bk_call_delta(f, k, t, r, sigma)
    assert f'{bk_call:.2f}' == '0.48'

def test_bk_put_delta_01():
    s, k, t, r, sigma = 100, 100, 1, 0.05, 0.10
    f = s * math.exp(r * t)
    bk_put = models.bk_put_delta(f, k, t, r, sigma)
    assert f'{bk_put:.2f}' == '-0.28'

def test_bk_put_delta_02():
    s, k, t, r, sigma = 100, 120, 2, 0.10, 0.20
    f = s * math.exp(r * t)
    bk_put = models.bk_put_delta(f, k, t, r, sigma)
    assert f'{bk_put:.2f}' == '-0.34'

def test_bk_gamma_01():
    s, k, t, r, sigma = 100, 100, 1, 0.05, 0.10
    f = s * math.exp(r * t)
    bk_gamma = models.bk_gamma(f, k, t, r, sigma)
    assert f'{bk_gamma:.3f}' == '0.031'

def test_bk_gamma_02():
    s, k, t, r, sigma = 100, 120, 2, 0.10, 0.20
    f = s * math.exp(r * t)
    bk_gamma = models.bk_gamma(f, k, t, r, sigma)
    assert f'{bk_gamma:.3f}' == '0.009'

def test_bk_vega_01():
    s, k, t, r, sigma = 100, 100, 1, 0.05, 0.10
    f = s * math.exp(r * t)
    bk_vega = models.bk_vega(f, k, t, r, sigma)
    assert f'{bk_vega:.1f}' == '34.3'

def test_bk_vega_02():
    s, k, t, r, sigma = 100, 120, 2, 0.10, 0.20
    f = s * math.exp(r * t)
    bk_vega = models.bk_vega(f, k, t, r, sigma)
    assert f'{bk_vega:.1f}' == '55.3'

def test_bk_call_rho_01():
    s, k, t, r, sigma = 100, 100, 1, 0.05, 0.10
    f = s * math.exp(r * t)
    bk_call = models.bk_call_rho(f, k, t, r, sigma)
    assert f'{bk_call:.2f}' == '-6.80'

def test_bk_call_rho_02():
    s, k, t, r, sigma = 100, 120, 2, 0.10, 0.20
    f = s * math.exp(r * t)
    bk_call = models.bk_call_rho(f, k, t, r, sigma)
    assert f'{bk_call:.2f}' == '-24.09'

def test_bk_put_rho_01():
    s, k, t, r, sigma = 100, 100, 1, 0.05, 0.10
    f = s * math.exp(r * t)
    bk_put = models.bk_put_rho(f, k, t, r, sigma)
    assert f'{bk_put:.2f}' == '-1.93'

def test_bk_put_rho_02():
    s, k, t, r, sigma = 100, 120, 2, 0.10, 0.20
    f = s * math.exp(r * t)
    bk_put = models.bk_put_rho(f, k, t, r, sigma)
    assert f'{bk_put:.2f}' == '-20.59'

def test_bk_call_theta_01():
    s, k, t, r, sigma = 100, 100, 1, 0.05, 0.10
    f = s * math.exp(r * t)
    bk_call = models.bk_call_theta(f, k, t, r, sigma)
    assert f'{bk_call:.2f}' == '-1.37'

def test_bk_call_theta_02():
    s, k, t, r, sigma = 100, 120, 2, 0.10, 0.20
    f = s * math.exp(r * t)
    bk_call = models.bk_call_theta(f, k, t, r, sigma)
    assert f'{bk_call:.2f}' == '-1.56'

def test_bk_put_theta_01():
    s, k, t, r, sigma = 100, 100, 1, 0.05, 0.10
    f = s * math.exp(r * t)
    bk_put = models.bk_put_theta(f, k, t, r, sigma)
    assert f'{bk_put:.2f}' == '-1.62'

def test_bk_put_theta_02():
    s, k, t, r, sigma = 100, 120, 2, 0.10, 0.20
    f = s * math.exp(r * t)
    bk_put = models.bk_put_theta(f, k, t, r, sigma)
    assert f'{bk_put:.2f}' == '-1.73'


def test_implied_vol_from_bs_call_01():
    s, k, t, r, sigma = 100, 100, 1, 0.05, 0.10
    f = s * math.exp(r * t)
    bs_call = models.bs_call_price(s, k, t, r, sigma)
    implied_vol = models.implied_volatility(s, k, t, r, bs_call, models.bs_call_price, models.bs_vega, 0.2, 1e-5, 100)
    assert f'{implied_vol:.2f}' == f'{sigma:.2f}'

def test_implied_vol_from_bs_call_02():
    s, k, t, r, sigma = 100, 120, 2, 0.10, 0.20
    f = s * math.exp(r * t)
    bs_call = models.bs_call_price(s, k, t, r, sigma)
    implied_vol = models.implied_volatility(s, k, t, r, bs_call, models.bs_call_price, models.bs_vega, 0.2, 1e-5, 100)
    assert f'{implied_vol:.2f}' == f'{sigma:.2f}'

def test_implied_vol_from_bs_put_01():
    s, k, t, r, sigma = 100, 100, 1, 0.05, 0.10
    f = s * math.exp(r * t)
    bs_put = models.bs_put_price(s, k, t, r, sigma)
    implied_vol = models.implied_volatility(s, k, t, r, bs_put, models.bs_put_price, models.bs_vega, 0.2, 1e-5, 100)
    assert f'{implied_vol:.2f}' == f'{sigma:.2f}'

def test_implied_vol_from_bs_put_02():
    s, k, t, r, sigma = 100, 120, 2, 0.10, 0.20
    f = s * math.exp(r * t)
    bs_put = models.bs_put_price(s, k, t, r, sigma)
    implied_vol = models.implied_volatility(s, k, t, r, bs_put, models.bs_put_price, models.bs_vega, 0.2, 1e-5, 100)
    assert f'{implied_vol:.2f}' == f'{sigma:.2f}'

def test_implied_vol_from_bk_call_01():
    s, k, t, r, sigma = 100, 100, 1, 0.05, 0.10
    f = s * math.exp(r * t)
    bk_call = models.bk_call_price(f, k, t, r, sigma)
    implied_vol = models.implied_volatility(f, k, t, r, bk_call, models.bk_call_price, models.bk_vega, 0.2, 1e-5, 100)
    assert f'{implied_vol:.2f}' == f'{sigma:.2f}'

def test_implied_vol_from_bk_call_02():
    s, k, t, r, sigma = 100, 120, 2, 0.10, 0.20
    f = s * math.exp(r * t)
    bk_call = models.bk_call_price(f, k, t, r, sigma)
    implied_vol = models.implied_volatility(f, k, t, r, bk_call, models.bk_call_price, models.bk_vega, 0.2, 1e-5, 100)
    assert f'{implied_vol:.2f}' == f'{sigma:.2f}'

def test_implied_vol_from_bk_put_01():
    s, k, t, r, sigma = 100, 100, 1, 0.05, 0.10
    f = s * math.exp(r * t)
    bk_put = models.bk_put_price(f, k, t, r, sigma)
    implied_vol = models.implied_volatility(f, k, t, r, bk_put, models.bk_put_price, models.bk_vega, 0.2, 1e-5, 100)
    assert f'{implied_vol:.2f}' == f'{sigma:.2f}'

def test_implied_vol_from_bk_put_02():
    s, k, t, r, sigma = 100, 120, 2, 0.10, 0.20
    f = s * math.exp(r * t)
    bk_put = models.bk_put_price(f, k, t, r, sigma)
    implied_vol = models.implied_volatility(f, k, t, r, bk_put, models.bk_put_price, models.bk_vega, 0.2, 1e-5, 100)
    assert f'{implied_vol:.2f}' == f'{sigma:.2f}'


def test_bach_call_price_01(): assert f'{models.bach_call_price(13.78, 12, 0.063, 0, 39.507504):.2f}'      == '4.91'
def test_bach_call_price_02(): assert f'{models.bach_call_price(25.78, 25.5, 0.00822, 0, 30.5340869):.2f}' == '1.25'

def test_bach_put_price_01(): assert f'{models.bach_put_price(42.97, 42.5, 0.057534, 0, 11.6973553):.2f}'  == '0.90'
def test_bach_put_price_02(): assert f'{models.bach_put_price(20.69, 22, 0.15616, 0, 30.6166935):.2f}'     == '5.51'

def test_bach_call_delta_01(): assert f'{models.bach_call_delta(13.78, 12, 0.063, 0, 39.507504):.2f}'      == '0.57'
def test_bach_call_delta_02(): assert f'{models.bach_call_delta(25.78, 25.5, 0.00822, 0, 30.5340869):.2f}' == '0.54'

def test_bach_put_delta_01(): assert f'{models.bach_put_delta(42.97, 42.5, 0.057534, 0, 11.6973553):.2f}'  == '-0.43'
def test_bach_put_delta_02(): assert f'{models.bach_put_delta(20.69, 22, 0.15616, 0, 30.6166935):.2f}'     == '-0.54'