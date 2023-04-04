# Helper functions

## intermediate values calcualtions

import numpy as np

def vin(p, R, Rhalf, vmax=None, type=2):
    '''Calcualte Vin for each species

    Args:
        p (N by M matrix): preference 
        R (M by 1 matrix): resource concentration
        Rhalf ( float ): half-velocity constant
        vmax (N by M matrix, optional): maximum uptake rate. Defaults to None.
        type (int, optional): Type I or Type II functional response. Defaults to 2.

    Returns:
       N by 1 vector: Vin for each species
    '''
    # calculate uptake
    uptake = p * R.T[:, np.newaxis]
    uptake = uptake.reshape(p.shape)

    if type==2: # Monod function
        if vmax is None:
            print('Vmax required for monod function')
        else:
            return vmax*((uptake)/(Rhalf + uptake))

    elif type==1: # linear
        return uptake
    
def vgrow(vin, leakage):
    '''calculate resource flow needed for growth

    Args:
        vin (np.array): N*M matrix for resource inflow
        leakage (np.array): M*1 matrix -- leakage fraction

    Returns:
        N*1 vector: resource flow needed for growth

    '''
    return vin @ (1-leakage)

def vout(vin, leakage, D):
     
    '''caculate vout
    
    Args:
        vin (np.array): N*M matrix for resource inflow
        leakage (np.array): M*1 matrix -- leakage fraction
        D (np.array): N*M matrix for conversion efficiency

    Returns:
        np.array: N*M matrix
    '''

    vout = (vin @ D)* leakage.T[:, np.newaxis]
    vout = vout.reshape(vin.shape)
    return vout

