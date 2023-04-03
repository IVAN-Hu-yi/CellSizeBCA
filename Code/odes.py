## define model functions

from initialisation import *
from utilities import *
from size_scaled_func import *

def odes_not_scaled(y, t, l, m, rho, mu, km, p, D, vmax, type):
    '''ODEs of our model -- non-scaled version

    Args:
        y (list): integrate over
        t (scaler/vector): dummies required for ode
        l (np.array): leakge M*1 matrix
        m (np.array): maintainence N*1 matrix 
        rho (np.array): external resource supply M*1
        mu (float): growth rate
        km (float): normalmisation constant
        p (np.array): preferences N*M matrix
        D (np.array): conversion efficiency M*M
        vmax (np.array): maximum uptake N*M matrix
        type (int): type of functional response 

    Returns:
        list: [dC/dt, dR/dt]
    '''

    R, C = y[0], y[1]
    v_in = vin(p, R, vmax, type)
    v_grow = vgrow(v_in, l)
    v_out = vout(vin, l, D)
    vdiff = v_out - v_in

    return [mu*C*(v_grow-m), rho+km*(vdiff.T @ C)]

def odes_scale_size(y, t, l, m, rho, mu, km, p, D, vmax, type, B0, M0, E0, alpha, gamma):
    '''ODEs of our model -- scaled version

    Args:
        y (list): integrate over
        t (scaler/vector): dummies required for ode
        l (np.array): leakge M*1 matrix
        m (np.array): maintainence N*1 matrix 
        rho (np.array): external resource supply M*1
        mu (float): growth rate
        km (float): normalmisation constant
        p (np.array): preferences N*M matrix
        D (np.array): conversion efficiency M*M
        vmax (np.array): maximum uptake N*M matrix
        type (int): type of functional response 
        B0 (float): normalmisation constant
        M0 (float): normalmisation constant
        E0 (float): normalmisation constant
        alpha (float): scaling constant
        gamma (float): scaling constant

    Returns:
        list: [dC/dt, dR/dt]
    '''

    R, C = y[0], y[1]
    v_in = vin(p, R, vmax, type)
    v_in = scale_vin(v_in, C, B0, alpha)
    v_grow = vgrow(v_in, l)
    v_out = vout(vin, l, D)
    v_out = scale_vout(v_out, C, E0, gamma)
    vdiff = v_out - v_in
    m_scale = scale_mt(m, C, M0, alpha)

    return [mu*C*(v_grow-m_scale), rho+km*(vdiff.T @ C)]