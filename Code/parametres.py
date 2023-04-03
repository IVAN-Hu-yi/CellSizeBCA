class Paras:
    '''
        define model parametres
    '''

    def __init__(self, N, M):

        # basic
        self.N = N # number of species
        self.M = M # number of resource types
        
        # ####### Model Paras defined
        # self.C = Ci # initial biomass for each species N*1 array
        # self.R = Ri # initial resource content for each resource type M*1 array
        # self.l = l # leakage fraction for each resource M*1 matrix
        # self.rho = rho # external resource supply M*1 array
        # self.p = p # resource preferences N*M matrix
        # self.v_in_max = vmax # max uptake/sigma func N*M matrix
        # self.m = m # maintainence N*1 array
        # self.D = D # conversion effciency

        ####### Model Paras fixed

        self.R_half = 10 # coefficient in sigma func
        self.mu = 1 # intrinsic growth rate  mass^-1
        self.km = 1 # individual per unit mass mass^-1
        self.rho_base = 20 # mean for rho
        self.l_base = 0.05 # mean for leakage

    ####### Scaling Paras

        self.B0 = 0.05 # Normalisation constant for resource inflow
        self.M0 = 0.05 # Normalisation constant for maintenance
        self.E0 = 0.05 # Normalisation constant for outflow
        self.alpha = - 0.25 # size-scaling exponent for inflow and maintainence
        self.gamma = 0.86 # size-scaling exponent for outflow

    ####### initialisation
        self.R = 50 # initial resource mass
        self.w = 2 # one parameter distribution 1 or 2 B(1, w)

        ####### relevant paras in consumer preferences (similar to Marsland 2019)
        self.mu_c = 0.1 # proportion of favor resources types
        self.c0 = 0.01 # fraction of uptake of non-favored resource type

        ####### relevant paras in conversion efficiency
        self.Dbase = 0.5 # base efficiency for all resource-resource pair 

    def paras(self, Ci, Ri, l, rho, p, vmax, m, D):

        ####### Model Paras defined
        self.C = Ci # initial biomass for each species N*1 array
        self.R = Ri # initial resource content for each resource type M*1 array
        self.l = l # leakage fraction for each resource M*1 matrix
        self.rho = rho # external resource supply M*1 array
        self.p = p # resource preferences N*M matrix
        self.v_in_max = vmax # max uptake/sigma func N*M matrix
        self.m = m # maintainence N*1 array
        self.D = D # conversion effciency