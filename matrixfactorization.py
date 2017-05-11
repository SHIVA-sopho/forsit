import numpy

def norm(P)
    Norm=0
    for i in range(len(P)):
        for j in range(len(P[0])):
            Norm+=pow(P[i][j],2)
            
    return Norm        


def matrix_factorization(R,U,I,K,steps=30000,alpha=0.0002,beta=0.02):
    I = I.T
    
    for step in range(steps):
        for user in range(len(R)):
            for item in range(len(R[0])):
                if R[user][item]>0 :
                    eij = R[user][item]-numpy.dot(U[user,:],I[:,item])

                    for k in range(K):
                        U[user][k]+=alpha*(2*eij*I[k][item]-beta*U[user][k])
                        I[k][item]+=alpha*(2*eij*U[user][k]-beta*I[k][item])

        currentR=numpy.dot(U,I)
        current_e2=0
        for i in range(len(R)):
            for j in range(len(R[0])):
                if R[i][j]>0:
                    current_e2+=pow(R[i][j] - currentR[i][j],2)

                
        current_e2+=(beta/2)*(pwo(norm(U),2) + pow(norm(I),2));

        if current_e2<0.001:
            break
    return U,I.T