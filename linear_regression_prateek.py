# %%
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

df = pd.read_csv('Dataforia.csv', names=['Year', 'Emission'])

# %%
x = df['Emission']
y = df['Year']

# %%
def func(x, a, b, c, d, e, f):
    return f*(x**5) + a*(x**4) + b*(x**3) + c*(x**2) + d*x + e

# %%
popt, pcov = curve_fit(func, y, x)

# %%
plt.figure()
plt.scatter(y, x, s=1.3, label='original')
plt.plot(y, func(y, *popt), 'r-', label='fit function')
plt.legend()
plt.show()

# %%
def print_function(popt):
    print(f'{popt[0]} * x^5 + {popt[1]} * x^4 + {popt[2]} * x^3 + {popt[3]} * x^2 + {popt[4]} * x + {popt[5]}')

# %%
print_function(popt)

# %%
