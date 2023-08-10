def w_prefers_m_over_m1(prefer, w, m, m1):
	for i in range(N):
		if (prefer[w][i] == m1):
			return True
		if (prefer[w][i] == m):
			return False


def stableMarriage(prefer):
	
    married = [False for _ in range(N)]
    pairingW = [-1 for _ in range(N)]

    freecount = N

    while freecount > 0:
        m = 0

        while m < N:
            if (married[m] == False):
                break
            m += 1

        i = 0
        while i < N and married[m] == False :
            w = prefer[m][i]

            # if woman is free 
            if pairingW[w - N] == -1 :
                pairingW[w - N] = m
                married[m] = True
                freecount -= 1

            # if woman is already married to some m1
            else :
                m1 = pairingW[w - N]

                if w_prefers_m_over_m1(prefer, w, m, m1) == True :
                    pairingW[w - N] = m
                    married[m] = True
                    married[m1] = False
                    
            i += 1

    return pairingW


A = 0
B = 1
C = 2
V = 3
W = 4
X = 5


prefer = [[V,W,X], [W,V,X],
		[V,W,X], [A,B,C],
		[B,C,A], [C,A,B]]

N = 3
wPartner = stableMarriage(prefer)

name = {
        0 : 'A',
        1 : 'B', 
        2 : 'C',
        3 : 'V',
        4 : 'W',
        5 : 'X'
    }

print("Woman ", " Man")
for i in range(N):
	print(name[i + N], "\t", name[wPartner[i]])

"""
-----------------------------------
Output:-

Woman   Man
V 	 C
W 	 A
X 	 B

-----------------------------------
TIME COMPLEXITY: O(N^2)
-----------------------------------

APPLICATIONS:
stable marriage, employer-employee  

------------------------------------
"""
