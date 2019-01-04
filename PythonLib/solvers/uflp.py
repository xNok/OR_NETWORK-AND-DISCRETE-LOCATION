from docplex.mp.model import Model

def uflp(I, J, f, c, name='UFLP'):
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
    for j in J:
        m.add_constraint(m.sum(X[i,j] for i in I) == 1, ctname='demande_%s' % j)

    # constraint #2: customer can only be associated to open facilities
    for i in I:
        for j in J:
            m.add_constraint(X[i,j] <= Y[j], ctname='flow_%s_%s' % (i,j))
            
    return m, X, Y