import numpy as np

def scale_vin(vin, mass, B0, alpha):

    '''v_in scaling

    Returns:
        _type_: _description_
    '''
    return vin*(B0*(mass**alpha))


def scale_mt(m, mass, M0, alpha):
    '''maintanence scaling

    Args:
        m (_type_): _description_
        mass (_type_): _description_
        M0 (_type_): _description_
        alpha (_type_): _description_

    Returns:
        _type_: _description_
    '''
    return m*(M0*(mass**alpha))
    
def scale_vout(vout, mass, E0, gamma):

    '''leakge scaled

    Returns:
        _type_: _description_
    '''

    return vout*(E0*(mass**gamma))