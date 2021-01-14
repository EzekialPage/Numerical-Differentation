#Ezekial Page
#Numerical Differentiation Program

from math import exp

#forward calculation
def forward_diff(f,x,h = 0.0001):
    df = (f(x + h) - f(x))/h
    return df

#Backward calculation
def backward_diff(f,x,h = 0.0001):
    df = (f(x) - f(x - h))/h
    return df

#Center-divided Calculation
def center_diff(f,x,h = 0.0001):
    df = (f(x + h) - f(x - h))/(2.0 * h)
    return df

#output
x = 3
func = (7*(x*x*x) - 5*(x) + 1) / (2*(x*x*x*x) + (x*x) + 1)
trueVal = 7.36
fwd = forward_diff(exp, x)
bck = backward_diff(exp, x)
cen = center_diff(exp, x)

fwdE = trueVal - fwd
bckE = trueVal - bck
bckRE = bck - fwd
cenE = trueVal - cen
cenRE = cen - bck

print("Expected value: " + str(trueVal) + "\n")

print("Forward value: " + str(fwd))
print("Forward true error of " + str(fwdE) + "\n")

print("Backward value: " + str(bck))
print("Backward true error of " + str(bckE))
print("Backward relative error of " + str(bckRE) + "\n")

print("Center value: " + str(cen))
print("Center true error of " + str(cenE))
print("Center relative error of " + str(cenRE) + "\n")



