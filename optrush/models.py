import math
from scipy.stats import norm
from typing import Callable


def norm_cdf(x):
    """Compute the cumulative distribution function of the standard normal distribution."""
    return norm.cdf(x)


def norm_pdf(x):
    """Compute the probability density function of the standard normal distribution."""
    return norm.pdf(x)


def bs_d1(s, k, t, r, sigma):
    """Calculate d1 used in various greeks."""
    return (math.log(s / k) + (r + 0.5 * sigma ** 2) * t) / (sigma * math.sqrt(t))


def bs_d2(s, k, t, r, sigma):
    """Calculate d2 used in various greeks."""
    return bs_d1(s, k, t, r, sigma) - sigma * math.sqrt(t)


def bs_call_price(s, k, t, r, sigma):
    """Compute the Black-Scholes price for a European call option on a stock."""
    d1 = bs_d1(s, k, t, r, sigma)
    d2 = bs_d2(s, k, t, r, sigma)
    return s * norm_cdf(d1) - k * math.exp(-r * t) * norm_cdf(d2)


def bs_put_price(s, k, t, r, sigma):
    """Compute the Black-Scholes price for a European put option on a stock."""
    d1 = bs_d1(s, k, t, r, sigma)
    d2 = bs_d2(s, k, t, r, sigma)
    return k * math.exp(-r * t) * norm_cdf(-d2) - s * norm_cdf(-d1)


def bs_call_delta(s, k, t, r, sigma):
    """Calculate Delta for a call option."""
    return norm_cdf(bs_d1(s, k, t, r, sigma))


def bs_put_delta(s, k, t, r, sigma):
    """Calculate Delta for a put option."""
    return norm_cdf(bs_d1(s, k, t, r, sigma)) - 1


def bs_gamma(s, k, t, r, sigma):
    """Calculate Gamma for both call and put options."""
    return norm_pdf(bs_d1(s, k, t, r, sigma)) / (s * sigma * math.sqrt(t))


def bs_vega(s, k, t, r, sigma):
    """Calculate Vega for both call and put options."""
    return s * norm_pdf(bs_d1(s, k, t, r, sigma)) * math.sqrt(t)


def bs_call_theta(s, k, t, r, sigma):
    """Calculate Theta for a call option."""
    d1 = bs_d1(s, k, t, r, sigma)
    d2 = bs_d2(s, k, t, r, sigma)
    term1 = -s * norm_pdf(d1) * sigma / (2 * math.sqrt(t))
    term2 = r * k * math.exp(-r * t) * norm_cdf(d2)
    return term1 - term2


def bs_put_theta(s, k, t, r, sigma):
    """Calculate Theta for a put opiton."""
    d1 = bs_d1(s, k, t, r, sigma)
    d2 = bs_d2(s, k, t, r, sigma)
    term1 = -s * norm_pdf(d1) * sigma / (2 * math.sqrt(t))
    term2 = r * k * math.exp(-r * t) * norm_cdf(-d2)
    return term1 + term2


def bs_call_rho(s, k, t, r, sigma):
    """Calculate Rho for a call option."""
    return k * t * math.exp(-r * t) * norm_cdf(bs_d2(s, k, t, r, sigma))


def bs_put_rho(s, k, t, r, sigma):
    """Calculate Rho for a put option."""
    return -k * t * math.exp(-r * t) * norm_cdf(-bs_d2(s, k, t, r, sigma))


def bk_d1(f, k, t, sigma):
    """Calculate d1 for the Black model."""
    return (math.log(f / k) + 0.5 * sigma ** 2 * t) / (sigma * math.sqrt(t))


def bk_d2(f, k, t, sigma):
    """Calculate d2 for the Black model."""
    return bk_d1(f, k, t, sigma) - sigma * math.sqrt(t)


def bk_call_price(f, k, t, r, sigma):
    """Calculate the Black model price for a European call option on a futures contract."""
    d1 = bk_d1(f, k, t, sigma)
    d2 = bk_d2(f, k, t, sigma)
    return math.exp(-r * t) * (f * norm.cdf(d1) - k * norm.cdf(d2))


def bk_put_price(f, k, t, r, sigma):
    """Calculate the Black model price for a European put option on a futures contract."""
    d1 = bk_d1(f, k, t, sigma)
    d2 = bk_d2(f, k, t, sigma)
    return math.exp(-r * t) * (k * norm.cdf(-d2) - f * norm.cdf(-d1))


def bk_call_delta(f, k, t, r, sigma):
    """Calculate the delta of a call option using the Black model."""
    return math.exp(-r * t) * norm.cdf(bk_d1(f, k, t, sigma))


def bk_put_delta(f, k, t, r, sigma):
    """Calculate the delta of a put option using the Black model."""
    return -math.exp(-r * t) * norm.cdf(-bk_d1(f, k, t, sigma))


def bk_gamma(f, k, t, r, sigma):
    """Calculate Gamma for both call and put options."""
    d1 = bk_d1(f, k, t, sigma)
    return math.exp(-r * t) * norm_pdf(d1) / (f * sigma * math.sqrt(t))


def bk_vega(f, k, t, r, sigma):
    """Calculate the vega for European options on a futures contract."""
    d1 = bk_d1(f, k, t, sigma)
    return math.exp(-r * t) * f * norm_pdf(d1) * math.sqrt(t)


def bk_call_rho(f, k, t, r, sigma):
    """Calculate Rho for a call option using the Black model."""
    return -t * bk_call_price(f, k, t, r, sigma)

def bk_put_rho(f, k, t, r, sigma):
    """Calculate Rho for a put option using the Black model."""
    return -t * bk_put_price(f, k, t, r, sigma)


def bk_call_theta(f, k, t, r, sigma):
    """Calculate Theta for a call option using the Black model."""
    d1 = bk_d1(f, k, t, sigma)
    d2 = bk_d2(f, k, t, sigma)
    term1 = -f * math.exp(-r * t) * norm_pdf(d1) * sigma / (2 * math.sqrt(t))
    term2 = r * math.exp(-r * t) * (f * norm_cdf(d1) - k * norm_cdf(d2))
    return term1 + term2


def bk_put_theta(f, k, t, r, sigma):
    """Calculate Theta for a put option using the Black model."""
    d1 = bk_d1(f, k, t, sigma)
    d2 = bk_d2(f, k, t, sigma)
    term1 = -f * math.exp(-r * t) * norm_pdf(d1) * sigma / (2 * math.sqrt(t))
    term2 = r * math.exp(-r * t) * (k * norm_cdf(-d2) - f * norm_cdf(-d1))
    return term1 + term2


def implied_volatility(
    p: float,
    k: float,
    t: float,
    r: float,
    market_price: float,
    price_function: Callable[[float, float, float, float, float], float],
    vega_function: Callable[[float, float, float, float, float], float],
    sigma: float = 0.2,
    tol: float = 1e-5,
    max_iterations: int = 100) -> float:
    """Compute the implied volatility for a European call option on a futures contract using the Newton-Raphson method."""
    for _ in range(max_iterations):
        price = price_function(p, k, t, r, sigma)
        diff = market_price - price
        if abs(diff) < tol:
            return sigma
        sigma += diff / vega_function(p, k, t, r, sigma)
    return sigma


# Bachelier Model Functions
def bach_d(f, k, t, sigma):
    return (f - k) / (sigma * math.sqrt(t))


def bach_call_price(f, k, t, r, sigma):
    """Calculate the Bachelier model price for a European call option."""
    d = bach_d(f, k, t, sigma)
    return math.exp(-r * t) * ((f - k) * norm_cdf(d) + sigma * math.sqrt(t) * norm_pdf(d))


def bach_put_price(f, k, t, r, sigma):
    """Calculate the Bachelier model price for a European put option."""
    d = bach_d(f, k, t, sigma)
    return math.exp(-r * t) * ((k - f) * norm_cdf(-d) + sigma * math.sqrt(t) * norm_pdf(d))


def bach_call_delta(f, k, t, r, sigma):
    """Calculate the delta of a call option using the Bachelier model."""
    d = bach_d(f, k, t, sigma)
    return math.exp(-r * t) * norm_cdf(d)


def bach_put_delta(f, k, t, r, sigma):
    """Calculate the delta of a put option using the Bachelier model."""
    d = bach_d(f, k, t, sigma)
    return -math.exp(-r * t) * norm_cdf(-d)


def bach_gamma(f, k, t, r, sigma):
    """Calculate Gamma for both call and put options using the Bachelier model."""
    d = bach_d(f, k, t, sigma)
    return math.exp(-r * t) * norm_pdf(d) / (sigma * math.sqrt(t))


def bach_vega(f, k, t, r, sigma):
    """Calculate Vega for both call and put options using the Bachelier model."""
    d = bach_d(f, k, t, sigma)
    return math.exp(-r * t) * math.sqrt(t) * norm_pdf(d)


def bach_call_theta(f, k, t, r, sigma):
    """Calculate Theta for a call option using the Bachelier model."""
    d = bach_d(f, k, t, sigma)
    term1 = -0.5 * math.exp(-r * t) * sigma * norm_pdf(d) / math.sqrt(t)
    term2 = r * math.exp(-r * t) * ((f - k) * norm_cdf(d) + sigma * math.sqrt(t) * norm_pdf(d))
    return term1 + term2


def bach_put_theta(f, k, t, r, sigma):
    """Calculate Theta for a put option using the Bachelier model."""
    d = bach_d(f, k, t, sigma)
    term1 = -0.5 * math.exp(-r * t) * sigma * norm_pdf(d) / math.sqrt(t)
    term2 = r * math.exp(-r * t) * ((k - f) * norm_cdf(-d) + sigma * math.sqrt(t) * norm_pdf(d))
    return term1 + term2


def bach_call_rho(f, k, t, r, sigma):
    """Calculate Rho for a call option using the Bachelier model."""
    d = bach_d(f, k, t, sigma)
    return t * math.exp(-r * t) * ((f - k) * norm_cdf(d) + sigma * math.sqrt(t) * norm_pdf(d))


def bach_put_rho(f, k, t, r, sigma):
    """Calculate Rho for a put option using the Bachelier model."""
    d = bach_d(f, k, t, sigma)
    return -t * math.exp(-r * t) * ((k - f) * norm_cdf(-d) + sigma * math.sqrt(t) * norm_pdf(d))
