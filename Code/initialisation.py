import numpy as np
from parametres import paras


# Initial Conditions
seed = 100

def int_R(M, R): 
    '''
        Resource Content at t0
    '''
    np.random.seed(seed)
    return np.random.normal(R, 0.5, M).reshape(M, 1)

def int_C(N, w):
    '''
        Biomass Content drawn from beta distribution at t0
    '''
    np.random.seed(seed)
    return 10 ** np.random.beta(1, w, N).reshape(N, 1)

# define parametres

def int_preferences(N, M, mu_c, c0):
    
    '''Guassian sampling of preferences, assume all are generalilsts

    Returns:
        np.array: N*M matries
    '''

    p = np.full((N*M), c0)
    for i in range(N):
        np.random.seed(i) # ensure for each assembly, each species same preferences
        number = int(mu_c*M) if int(mu_c*M) > 0 else 1
        idx = np.random.randint(0, M-1, number) # select favored resoruces
        np.random.seed(i)
        p[i, :][idx] = np.random.normal(mu_c, 0.001, number) # assign values
        p[i, :] = p[i, :]/np.sum(p[i, :]) # normalised to 1
    return p


def int_l(M, l, same=True):
    '''
     return leakage
    '''
    np.random.seed(seed)
    if same: return np.array([l]*M).reshape(M, 1)
    else: return np.random.normal(l, 0.005, M).reshape(M, 1)

def int_rho(M, rho):
    '''
    define external resource supply
    '''
    np.random.seed(seed)
    return np.array([rho]*M).reshape(M, 1)

def int_vmax(N, M, vmax):
    '''generate maximum uptake

    Args:
        M (int): int
        N (int): _description_
        vmax (int): _description_

    Returns:
        N*M matrix: _description_
    '''
    np.random.seed(seed)
    return np.random.normal(vmax, 0.01, (N, M))

def int_mt(N, m):
    np.random.seed(seed)
    return np.random.normal(m, 0.01, (N, 1))
