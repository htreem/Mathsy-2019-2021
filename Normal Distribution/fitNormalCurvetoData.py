#Age of cancer patients

from pydataset import data
from matplotlib import pyplot as plt
from scipy.stats import norm
import numpy as np

plt.hist(data('cancer')['age'])
plt.xlabel("Value")
plt.ylabel("Density")
plt.show()

std = np.std(data('cancer')['age'], ddof = 1)
mean = np.mean(data('cancer')['age'])

domain = np.linspace(np.min(data('cancer')['age']),np.max(data('cancer')['age']))
plt.plot(domain, norm.pdf(domain,mean,std),label='$\mathcal{N}$' + f'$(\mu \\approx {round(mean)},'
                                                                   f' \sigma \\approx {round(std)})$')

plt.hist(data('cancer')['age'], edgecolor = 'black', alpha = 0.5, density = True)
plt.title("Normal Distribution (Age of Cancer Patients)")
plt.xlabel("Value")
plt.ylabel("Density")
plt.legend()
plt.show()