class paras():
    '''
        define model parametres
    '''

def __init__(self, N, M, Ci, Ri, l, rho, p):

    # basic
    self.N = N # number of species
    self.M = M # number of resource types
    
    ####### Model Paras defined
    self.Ci = Ci # initial biomass for each species N*1 array
    self.Ri = Ri # initial resource content for each resource type M*1 array
    self.l = l # leakage fraction for each species and resource N*M matrix
    self.rho = rho # external resource supply M*1 array
    self.p = p # resource preferences N*M matrix

    ####### Model Paras fixed

    self.R_half = 0.5 # coefficient in sigma func
    self.v_in_max = 30 # max uptake/sigma func
    self.mu = 1 # intrinsic growth rate  mass^-1
    self.km = 1 # individual per unit mass mass^-1
    self.m = 1.5

    ####### Scaling Paras

    self.B0 = 0.05 # Normalisation constant for resource inflow
    self.M0 = 0.05 # Normalisation constant for maintenance
    self.E0 = 0.05 # Normalisation constant for outflow
    self.alpha = - 0.25 # size-scaling exponent for inflow and maintainence
    self.gamma = 0.86 # size-scaling exponent for outflow

