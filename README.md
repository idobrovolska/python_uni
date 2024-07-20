This is an implementation of class Polynom for modeling work with power polynomials. A polynomial is represented as a wrapper around Python's built-in dictionary 
containing "power:coefficient of this power" pairs. The full functionality of basic arithmetic operations on polynomials is implemented, in particular their addition, 
subtraction, multiplication, calculation of the value of the polynomial at the point x. 
Polynomials P1 and P2 are read from files input01.txt and input02.txt, then polynomials q(x) = P1(x) + P2(x) * P1(x) - P2(x) and 
h(x) = P2(x) * (P1(x) - P2(x))**2 are calculated at the real value of x read from the keyboard. The result of calculations is written to a file output.txt
