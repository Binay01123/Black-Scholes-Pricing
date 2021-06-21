# Black Scholes Options Price Calculator
import numpy as np
from scipy.stats import norm

# Parameters Input
r = float(input('Please input the Risk- free interest rate: '))
S = float(input('Please input the Current Stock Price: '))
K = float(input ('Please input the Strike Price: '))
m = float(input ('Please input the the days till the expiration: '))
T = m/365
sigma = float(input ('Please input the volatility of the Stock movements: '))

def blackScholes(r, S, K, T, sigma, type="Call"):
    "Calculate BS option Price for a Call/Put"
    d1 = (np.log(S/K) + (r+ sigma**2/2)*T)/(sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    try:
        if type == "Call":
            price = S*norm.cdf(d1, 0, 1)- K*np.exp(-r*T)*norm.cdf(d2, 0, 1)
        elif type == "Put":
            price = K*np.exp(-r*T)*norm.cdf(-d2, 0, 1) - S*norm.cdf(-d1, 0, 1)
        return price
    except:
        print("Please Confirm all Option Parameters Above!")

print("Option Price is: ", blackScholes(r, S, K, T, sigma, type="Call") )

