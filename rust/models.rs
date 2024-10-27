use pyo3::prelude::*;
use statrs::distribution::{Normal, Continuous, ContinuousCDF};

#[pyfunction]
fn norm_cdf(x: f64) -> f64 {
    let normal = Normal::new(0.0, 1.0).unwrap();
    normal.cdf(x)
}

#[pyfunction]
fn norm_pdf(x: f64) -> f64 {
    let normal = Normal::new(0.0, 1.0).unwrap();
    normal.pdf(x)
}

#[pyfunction]
fn bs_d1(s: f64, k: f64, t: f64, r: f64, sigma: f64) -> f64 {
    (s.ln() - k.ln() + (r + 0.5 * sigma.powi(2)) * t) / (sigma * t.sqrt())
}

#[pyfunction]
fn bs_d2(s: f64, k: f64, t: f64, r: f64, sigma: f64) -> f64 {
    bs_d1(s, k, t, r, sigma) - sigma * t.sqrt()
}

#[pyfunction]
fn bs_call_price(s: f64, k: f64, t: f64, r: f64, sigma: f64) -> f64 {
    let d1 = bs_d1(s, k, t, r, sigma);
    let d2 = bs_d2(s, k, t, r, sigma);
    s * norm_cdf(d1) - k * (-r * t).exp() * norm_cdf(d2)
}

#[pyfunction]
fn bs_put_price(s: f64, k: f64, t: f64, r: f64, sigma: f64) -> f64 {
    let d1 = bs_d1(s, k, t, r, sigma);
    let d2 = bs_d2(s, k, t, r, sigma);
    k * (-r * t).exp() * norm_cdf(-d2) - s * norm_cdf(-d1)
}

#[pyfunction]
fn bs_call_delta(s: f64, k: f64, t: f64, r: f64, sigma: f64) -> f64 {
    norm_cdf(bs_d1(s, k, t, r, sigma))
}

#[pyfunction]
fn bs_put_delta(s: f64, k: f64, t: f64, r: f64, sigma: f64) -> f64 {
    norm_cdf(bs_d1(s, k, t, r, sigma)) - 1.0
}

#[pyfunction]
fn bs_gamma(s: f64, k: f64, t: f64, r: f64, sigma: f64) -> f64 {
    norm_cdf(bs_d1(s, k, t, r, sigma)) / (s * sigma * t.sqrt())
}

#[pyfunction]
fn bs_vega(s: f64, k: f64, t: f64, r: f64, sigma: f64) -> f64 {
    s * norm_pdf(bs_d1(s, k, t, r, sigma)) * t.sqrt()
}

#[pyfunction]
fn bs_call_theta(s: f64, k: f64, t: f64, r: f64, sigma: f64) -> f64 {
    let d1 = bs_d1(s, k, t, r, sigma);
    let d2 = bs_d2(s, k, t, r, sigma);
    let term1 = -s * norm_pdf(d1) * sigma / (2.0 * t.sqrt());
    let term2 = r * k * (-r * t).exp() * norm_cdf(d2);
    term1 - term2
}

#[pyfunction]
fn bs_put_theta(s: f64, k: f64, t: f64, r: f64, sigma: f64) -> f64 {
    let d1 = bs_d1(s, k, t, r, sigma);
    let d2 = bs_d2(s, k, t, r, sigma);
    let term1 = -s * norm_pdf(d1) * sigma / (2.0 * t.sqrt());
    let term2 = r * k * (-r * t).exp() * norm_cdf(-d2);
    term1 + term2
}

#[pyfunction]
fn bs_call_rho(s: f64, k: f64, t: f64, r: f64, sigma: f64) -> f64 {
    k * t * (-r * t).exp() * norm_cdf(bs_d2(s, k, t, r, sigma))
}

#[pyfunction]
fn bs_put_rho(s: f64, k: f64, t: f64, r: f64, sigma: f64) -> f64 {
    -k * t * (-r * t).exp() * norm_cdf(-bs_d2(s, k, t, r, sigma))
}

#[pyfunction]
fn bk_d1(f: f64, k: f64, t: f64, sigma: f64) -> f64 {
    (f.ln() - k.ln() + 0.5 * sigma.powi(2) * t) / (sigma * t.sqrt())
}

#[pyfunction]
fn bk_d2(f: f64, k: f64, t: f64, sigma: f64) -> f64 {
    bk_d1(f, k, t, sigma) - sigma * t.sqrt()
}

#[pyfunction]
fn bk_call_price(f: f64, k: f64, t: f64, r: f64, sigma: f64) -> f64 {
    let d1 = bk_d1(f, k, t, sigma);
    let d2 = bk_d2(f, k, t, sigma);
    (-r * t).exp() * (f * norm_cdf(d1) - k * norm_cdf(d2))
}

#[pyfunction]
fn bk_put_price(f: f64, k: f64, t: f64, r: f64, sigma: f64) -> f64 {
    let d1 = bk_d1(f, k, t, sigma);
    let d2 = bk_d2(f, k, t, sigma);
    (-r * t).exp() * (k * norm_cdf(-d2) - f * norm_cdf(-d1))
}

#[pyfunction]
fn bk_call_delta(f: f64, k: f64, t: f64, r: f64, sigma: f64) -> f64 {
    (-r * t).exp() * norm_cdf(bk_d1(f, k, t, sigma))
}

#[pyfunction]
fn bk_put_delta(f: f64, k: f64, t: f64, r: f64, sigma: f64) -> f64 {
    -(-r * t).exp() * norm_cdf(-bk_d1(f, k, t, sigma))
}

#[pyfunction]
fn bk_gamma(f: f64, k: f64, t: f64, r: f64, sigma: f64) -> f64 {
    let d1 = bk_d1(f, k, t, sigma);
    (-r * t).exp() * f * norm_pdf(d1) / (f * sigma * t.sqrt())
}

#[pyfunction]
fn bk_vega(f: f64, k: f64, t: f64, r: f64, sigma: f64) -> f64 {
    let d1 = bk_d1(f, k, t, sigma);
    (-r * t).exp() * f * norm_pdf(d1) * t.sqrt()
}

#[pyfunction]
fn bk_call_rho(f: f64, k: f64, t: f64, r: f64, sigma: f64) -> f64 {
    -t * bk_call_price(f, k, t, r, sigma)
}

#[pyfunction]
fn bk_put_rho(f: f64, k: f64, t: f64, r: f64, sigma: f64) -> f64 {
    -t * bk_put_price(f, k, t, r, sigma)
}

#[pyfunction]
fn bk_call_theta(f: f64, k: f64, t: f64, r: f64, sigma: f64) -> f64 {
    let d1 = bk_d1(f, k, t, sigma);
    let d2 = bk_d2(f, k, t, sigma);
    let term1 = -f * (-r * t).exp() * norm_pdf(d1) * sigma / (2.0 * t.sqrt());
    let term2 = r * (-r * t).exp() * (f * norm_cdf(d1) - k * norm_cdf(d2));
    term1 + term2
}

#[pyfunction]
fn bk_put_theta(f: f64, k: f64, t: f64, r: f64, sigma: f64) -> f64 {
    let d1 = bk_d1(f, k, t, sigma);
    let d2 = bk_d2(f, k, t, sigma);
    let term1 = -f * (-r * t).exp() * norm_pdf(d1) * sigma / (2.0 * t.sqrt());
    let term2 = r * (-r * t).exp() * (k * norm_cdf(-d2) - f * norm_cdf(-d1));
    term1 + term2
}

#[pyfunction]
fn implied_volatility(
    p: f64,
    k: f64,
    t: f64,
    r: f64,
    market_price: f64,
    price_function: PyObject,
    vega_function: PyObject,
    sigma: f64,
    tol: f64,
    max_iteration: usize,
    py: Python
) -> PyResult<f64> {
    let mut sigma = sigma;
    for _ in 0..max_iteration {
        let price: f64 = price_function.call1(py, (p, k, t, r, sigma))?.extract(py)?;
        let diff = market_price - price;
        if diff.abs() < tol {
            return Ok(sigma);
        }
        let vega: f64 = vega_function.call1(py, (p, k, t, r, sigma))?.extract(py)?;
        sigma += diff / vega;
    }
    Ok(sigma)
}

#[pymodule]
fn optrush(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(norm_cdf, m)?)?;
    m.add_function(wrap_pyfunction!(norm_pdf, m)?)?;
    m.add_function(wrap_pyfunction!(bs_d1, m)?)?;
    m.add_function(wrap_pyfunction!(bs_d2, m)?)?;
    m.add_function(wrap_pyfunction!(bs_call_price, m)?)?;
    m.add_function(wrap_pyfunction!(bs_put_price, m)?)?;
    m.add_function(wrap_pyfunction!(bs_call_delta, m)?)?;
    m.add_function(wrap_pyfunction!(bs_put_delta, m)?)?;
    m.add_function(wrap_pyfunction!(bs_gamma, m)?)?;
    m.add_function(wrap_pyfunction!(bs_vega, m)?)?;
    m.add_function(wrap_pyfunction!(bs_call_theta, m)?)?;
    m.add_function(wrap_pyfunction!(bs_put_theta, m)?)?;
    m.add_function(wrap_pyfunction!(bs_call_rho, m)?)?;
    m.add_function(wrap_pyfunction!(bs_put_rho, m)?)?;
    m.add_function(wrap_pyfunction!(bk_d1, m)?)?;
    m.add_function(wrap_pyfunction!(bk_d2, m)?)?;
    m.add_function(wrap_pyfunction!(bk_call_price, m)?)?;
    m.add_function(wrap_pyfunction!(bk_put_price, m)?)?;
    m.add_function(wrap_pyfunction!(bk_call_delta, m)?)?;
    m.add_function(wrap_pyfunction!(bk_put_delta, m)?)?;
    m.add_function(wrap_pyfunction!(bk_gamma, m)?)?;
    m.add_function(wrap_pyfunction!(bk_vega, m)?)?;
    m.add_function(wrap_pyfunction!(bk_call_theta, m)?)?;
    m.add_function(wrap_pyfunction!(bk_put_theta, m)?)?;
    m.add_function(wrap_pyfunction!(bk_call_rho, m)?)?;
    m.add_function(wrap_pyfunction!(bk_put_rho, m)?)?;
    m.add_function(wrap_pyfunction!(implied_volatility, m)?)?;
    Ok(())
}