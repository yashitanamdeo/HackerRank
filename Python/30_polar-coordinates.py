# Enter your code here. Read input from STDIN. Print output to STDOUT 
import cmath

complexNumber = complex(input())
modulus = cmath.phase(complexNumber)
phaseAngle = abs(complexNumber)
print(phaseAngle)
print(modulus)