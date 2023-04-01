import numpy as np
from parametres import paras


# Initial Conditions

def int_R(M, R): 
    '''
        Resource Content at t0
    '''
    return np.random.normal(R, 0.5, M).T

def int_C(N, w):
    '''
        Biomass Content drawn from beta distribution at t0
    '''
    return 10 ** np.random.beta(1, w, N).T

# define parametres

def int_l(M, l, same=True):
    '''
     return leakage
    '''
    if same: return np.array([l]*M).T
    else: return np.random.normal(l, 0.005, M).T 

def int_rho(M, rho):
    '''
    define external resource supply
    '''
    return np.array([rho]*M).T

def int_vmax(M, N, vmax):
    '''generate maximum uptake

    Args:
        M (int): int
        N (int): _description_
        vmax (int): _description_

    Returns:
        N*M matrix: _description_
    '''

    return np.random.normal(vmax, 0.01, (N, M))

def int_mt(N, m):

    return np.random.normal(m, 0.01, N)
