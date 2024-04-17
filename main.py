import traceback

class Polynom:


    def __init__(self):
        self._coefs_dict = {}

    def get_power(self):
        return self._coefs_dict.keys()
    
    def get_coef(self, pwr):
        if pwr in self._coefs_dict:
            return self._coefs_dict[pwr]
        else:
            return 0.0

    def _process_line(self, line):
        data = line.split()
        if len(data):
            assert len(data) == 2
            try:
                pwr = int(data[0])
            except:
                traceback.print_exc()
                return False
            assert pwr >= 0
            try:
                coef = float(data[1])
            except:
                traceback.print_exc() # print('Incorrect coef in line:')
                return False
            self._coefs_dict[pwr] = coef
            return True
        
    def read_from_file(self, file_name):
        self._coefs_dict = {}
        try:
            with open(file_name) as f:
                for line in f:
                    self._process_line( line.strip() )
        except:
            print("Error while reading from file")

    def read_from_keyboard(self):
        self._coefs_dict = {}
        print("Input powers & coefs, one pair per line, or empty line to stop")
        while True:
            s = input()
            if s == "":
                break
            self._process_line( s )

    def set_coefs(self, poly):
        self._coefs_dict.update(poly)

    def evaluate_at_point(self, x):
        result = 0
        for pwr, coef in self._coefs_dict.items():
            term = x ** pwr * coef
            result += term
        return result

    def show(self):
        print(self._coefs_dict)


def add_two_polinoms(poly1, poly2):
    powers1 = poly1.get_power()
    powers2 = poly2.get_power()
    poly = {}
    for pwr in set(powers1) | set(powers2): #we need coefficients near similar powers in both of polynoms
        poly[pwr] = poly1.get_coef(pwr) + poly2.get_coef(pwr)
    new_polynom = Polynom()
    new_polynom.set_coefs(poly)
    return new_polynom


def substract_two_polinoms(poly1, poly2):
    powers1 = poly1.get_power()
    powers2 = poly2.get_power()
    poly = {}
    for pwr in set(powers1) | set(powers2):
        poly[pwr] = poly1.get_coef(pwr) - poly2.get_coef(pwr)
    new_polynom = Polynom()
    new_polynom.set_coefs(poly)
    return new_polynom
    

def multiply_two_polinoms(poly1, poly2):
    powers1 = poly1.get_power()
    powers2 = poly2.get_power()
    poly = {}
    for pwr1 in powers1:
        for pwr2 in powers2: 
            coef = poly1.get_coef(pwr1) * poly2.get_coef(pwr2)
            if (pwr1 + pwr2) in poly:
                poly[pwr1 + pwr2] += poly1.get_coef(pwr1) * poly2.get_coef(pwr2)
            else:
                poly[pwr1 + pwr2] = poly1.get_coef(pwr1) * poly2.get_coef(pwr2)
    new_polynom = Polynom()
    new_polynom.set_coefs(poly)
    
    return new_polynom
                
if __name__ == '__main__':
    P1 = Polynom()
    P1.read_from_file('input01.txt')
    P2 = Polynom()
    P2.read_from_file('input02.txt')

    Q1 = multiply_two_polinoms(P2, P1)
    Q2 = add_two_polinoms(P1, Q1)
    Q = substract_two_polinoms(Q2, P2) #q(x) = P1(x) + P2(x) * P1(x) - P2(x)
    print("Polynom object q(x):")
    Q.show()

    H1 = substract_two_polinoms(P1, P2)
    H2 = multiply_two_polinoms(H1, H1)
    H = multiply_two_polinoms(P2, H2)
    print("Polynom object h(x):")
    H.show() #h(x) = P2(x) * (P1(x) - P2(x))**2;

    while True:
        try:
            x = float(input("Input real number: "))
            break 
        except ValueError:
            print("Incorrect number. Please, try again with another value.")

    q_x = f"q(x) evaluated at point x: {Q.evaluate_at_point(x)}"
    h_x = f"h(x) evaluated at point x: {H.evaluate_at_point(x)}"
    list = [q_x, h_x]
    with open('output.txt', mode = 'w') as file:
        for el in list:
            file.write(el + '\n')

