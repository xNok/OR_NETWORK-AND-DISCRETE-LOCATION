from docplex.mp.model import Model

def uflp(I, J, f, c, name='UFLP'):
    """
    Inputs:
        I = Set of customers (1d-array)
        J = Set of Facilities (1d-array)
        f = Fixed cost associated to each facility (1d-array)
        c = Cost of connecting element of I with J (2d-arra)
    Ouputs:
        m = cplex Model Object
        X = decision variables related to the routing
        Y = decision variablse related to open facilities
    """
    
    ###################
    # create one model instance
    m = Model(name=name)

    ###################
    # Define variables

    # x(i,j) equals 1 if arc ij is in the solution
    X = m.binary_var_dict([(i,j) 
                          for i in I
                          for j in J], name="X")
    # y(j) equales 1 if node j is in the solution
    Y = m.binary_var_dict([(j) 
                          for j in J], name="Y")
    
    ###################
    # Define Objective
    m.minimize(m.sum(X[i,j] * c[i][j] for i in I for j in J) \
              + m.sum(Y[j] * f[j] for j in J))
    
    m.add_kpi(m.sum(X[i,j] * c[i][j] for i in I for j in J), "transportation cost")
    m.add_kpi(m.sum(Y[j] * f[j] for j in J), "fixed cost")

    ###################
    # Define constraints

    # constraint #1: each customer is affected to a facility
    for i in I:
        m.add_constraint(m.sum(X[i,j] for j in J) == 1, ctname='demande_%s' % i)

    # constraint #2: customer can only be associated to open facilities
    for i in I:
        for j in J:
            m.add_constraint(X[i,j] <= Y[j], ctname='flow_%s_%s' % (i,j))
            
    return m, X, Y