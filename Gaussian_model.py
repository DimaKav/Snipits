# Define gaussian model function
def gaussian_model(x, mu, sigma):
    coeff_part = 1/(np.sqrt(2 * np.pi * sigma**2))
    exp_part = np.exp( - (x - mu)**2 / (2 * sigma**2) )
    return coeff_part*exp_part

# Compute sample statistics
mean = np.mean(sample)
stdev = np.std(sample)

# Model the population using sample statistics
population_model = gaussian(sample, mu=mean, sigma=stdev)
