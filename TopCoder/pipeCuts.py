'''



 Problem Statement for PipeCuts


Problem Statement
    	A 100 meter long pipe must be cut in two places. It can only be cut at certain places, where it was originally welded from smaller pipes. If the two cut locations are chosen at random (each potential location has equal probability of being chosen), find the probability of a resulting pipe being longer than L meters.



Create a method named probability that accepts a int[] weldLocations and int L as parameters. It should calculate the probability of one or more resulting pipes being strictly longer than L if the two cut locations are chosen at random from weldLocations. Each element in weldLocations represents the number of meters from the left end of the pipe.
 
Definition
    	
Class:	PipeCuts
Method:	probability
Parameters:	int[], int
Returns:	double
Method signature:	double probability(int[] weldLocations, int L)
(be sure your method is public)
    
 
Notes
-	Your return value must have a relative or absolute error less than 1e-9.
 
Constraints
-	weldLocations will have between 2 and 50 elements, inclusive.
-	Each element in weldLocations will be between 1 and 99, inclusive.
-	weldLocations will not contain duplicate elements.
-	L will be between 1 and 100, inclusive.
 
Examples
0)	
    	
{25, 50, 75}
25
Returns: 1.0
Any random set of cuts results in a pipe being longer than 25 meters.
'''
import math


def probability(weldLocations: list, L: int):
    weldLocations.sort()
    no_of_welds = len(weldLocations)

    favorable_outcomes = 0
    total_outcomes = math.factorial(
        no_of_welds)/(math.factorial(2) * math.factorial(no_of_welds - 2))

    for i in range(no_of_welds):
        for j in range(i + 1, no_of_welds):
            if(weldLocations[i] > L or (weldLocations[j]-weldLocations[i] > L) or (100 - weldLocations[j] > L)):
                favorable_outcomes += 1
                
    return favorable_outcomes / total_outcomes


weldLocations = [int(x) for x in input().split(',')]
L = int(input())
print(probability(weldLocations,L))
