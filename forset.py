import numpy as np
import MySQLdb

conn = MySQLdb.connect(host='localhost',user='root',passwd='shiva123',db='forsit')

query1 = "select * from challenges_properties"

result = conn.query(query1)

result = conn.store_result()

challenges = result.fetch_row(maxrows=0)

challenges = np.array(challenges)

query2 = "select * from user_properties"

conn.query(query2)

result = conn.store_result()

user = result.fetch_row(maxrows=0)

user = np.array(user)

query3 = "select * from  user_challenges"

conn.query(query3)

result = conn.store_result()

user_challenges = result.fetch_row(maxrows=0)        

R = user_challenges
 

N = len(R)

M = len(R[0])


P = user

Q = challenges


print(P)
print(Q)

K = len(P[0])

nP, nQ = matrix_factorization(R, P, Q, K)

print(nP)
print(nQ)

numpy.savetxt('P_matrix.txt', nP, fmt='%f', newline='\n' )



numpy.savetxt('Q_matrix.txt', nQ, fmt='%f',newline='\n')

nR = numpy.dot(nP, nQ.T)
print(R)
print(nR)


numpy.savetxt('New_R_matrix.txt',nR, fmt='%f',newline='\n')




def norm(P):
    Norm=0
    for i in range(len(P)):
        for j in range(len(P[0])):
            Norm+=pow(P[i][j],2)
            
    return Norm        


def matrix_factorization(R,U,I,K,steps=3000,alpha=0.002,beta=0.02):
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