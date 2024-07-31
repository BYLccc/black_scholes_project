import numpy as np
from scipy.stats import norm

def black_scholes_call(S, X, T, r, sigma):
    d1 = (np.log(S / X) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    call_price = S * norm.cdf(d1) - X * np.exp(-r * T) * norm.cdf(d2)
    return call_price

def black_scholes_put(S, X, T, r, sigma):
    d1 = (np.log(S / X) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    put_price = X * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    return put_price

# Example usage
if __name__ == "__main__":
    S = 100  # Current stock price
    X = 95   # Strike price
    T = 1    # Time to maturity in years
    r = 0.05 # Risk-free rate
    sigma = 0.2  # Volatility

    call_price = black_scholes_call(S, X, T, r, sigma)
    put_price = black_scholes_put(S, X, T, r, sigma)

    print(f"Call Option Price: {call_price:.2f}")
    print(f"Put Option Price: {put_price:.2f}")
