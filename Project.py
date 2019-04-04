n = 9
k = 11
alfa = 0.05

X = [(300 + (100 * i),300 + 100 * (i+1)) for i in range(n)]
N = [1,9 + k,18,33,40 - k, 52 - k, 29, 14 + k, 4]
Sum = sum(N)

def printTable():
    print('\nTerm of service','\t','Number of transistors')
    for x,n in zip(X,N):
        print(x[0],'-',x[1],"\t\t",n)
    print("In all:",'\t\t',Sum)

def main():
    printTable()
main()