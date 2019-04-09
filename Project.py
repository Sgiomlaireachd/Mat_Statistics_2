import math
from scipy.integrate import quad
import sympy as sp
import numpy as np

a = 0
sigma = 0
n = 9 #6
k = 11
alfa = 0.05
step = 100 #5
X = [[step * i,step * (i+1)] for i in range(n)]
M = [1,9 + k,18,33,40 - k, 52 - k, 29, 14 + k, 4]
# M = [133,45,15,4,2,1]
P = []
Sum = sum(M)

def printTable():
    print('\nTerm of service','\t','Number of transistors','\t\t','Pi')
    for x,m,p in zip(X,M,P):
        print(x[0],'-',x[1],"\t\t",m,"\t\t\t\t",p)
    print("In all:",'\t\t',Sum,'\t\t\t\t',sum(P))
def mergeIfNeeded():
    global n
    for i in reversed(range(len(M))):
        if M[i] < 5:
            if i < n - 1:
                M[i+1] += M[i]
                X[i+1][0] = X[i][0]
                X.pop(i)
                M.pop(i)
                n -= 1
            else:
                M[i-1] += M[i]
                X[i-1][1] = X[i][1]
                X.pop(i)
                M.pop(i)
                n -= 1
def average(keys,values):
    Sum = 0
    for key,val in zip(keys,values):
        Sum += key*val
    return Sum/sum(M)
def deviation(keys,values,avg):
    Sum = 0
    for key,val in zip(keys,values):
        Sum += val * ((key - avg) ** 2)
    return Sum
def f(x):
    return math.exp((-(x-a)**2)/(2*sigma**2))
def pirson():
    SUM = 0
    for m,p in zip(M,P):
        upper = (m - Sum * p)**2
        # print('upper:',upper)
        bottom = Sum*p
        # print('bottom:',bottom)
        SUM += upper/bottom
    return SUM
def Result(emp,crit):
    print('The hipotesis is true') if emp < crit else print('The hipotesis is false')
def method():
    global a,sigma,P
    a = average([((i[0] + i[1]) / 2) for i in X], M)
    sigma = math.sqrt(1/(Sum-1) * deviation([((i[0] + i[1]) / 2) for i in X], M,a))
    print('\na:',a,'\nσ:',sigma)
    for i,x in enumerate(X):
        if i > 0 and i < n-1:
            P.append((1/(sigma * math.sqrt(2*np.pi))) * (quad(f,x[0],x[1])[0]))
        if i == 0:
            P.append((1/(sigma * math.sqrt(2*np.pi))) * (quad(f,-np.inf,x[1])[0]))
        if i == n-1:
            P.append((1/(sigma * math.sqrt(2*np.pi))) * (quad(f,x[0],np.inf)[0]))
    emp = pirson()
    df = n - 3
    print('Χ²:',emp)
    print('\ndf:',df)
    print('Alpha:',alfa)
    return emp
        
def main():
    mergeIfNeeded()
    emp = method()
    printTable()
    crit = float(input('\nInput:'))
    Result(emp,crit)
main()