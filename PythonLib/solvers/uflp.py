from docplex.mp.model import Model

def uflp(I, J, f, c, name='UFLP'):
    ###################
    # create one model instance
    m = Model(name='UFLP')

    ###################
    # Define variables

    # x(i,j) equals 1 if arc ij is in the solution
    X = {
        (i,j): m.binary_var(name='X_%d_%d' % (i,j))
         for i in I for j in J
    } 
    # y(j) equales 1 if node j is in the solution
    Y = {
        (j): m.binary_var(name='Y_%d' % (j))
        for j in J
    }

    ###################
    # Define Objective
    m.minimize(m.sum(X[i,j] * c[i][j] for i in I for j in J) \
              + m.sum(Y[j] * f[j] for j in J))

    ###################
    # Define constraints

    # constraint #1: each customer is affected to a facility
    for j in J:
        m.add_constraint(m.sum(X[i,j] for i in I) == 1, ctname='demande_%s' % j)

    # constraint #2: customer can only be associated to open facilities
    for i in I:
        for j in J:
            m.add_constraint(X[i,j] <= Y[j], ctname='flow_%s_%s' % (i,j))
            
    return m