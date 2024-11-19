import numpy as np

def synthetic_division(polynomial, divisor_polynomial):
    dividend_copy = list(polynomial)  # copy the dividend
    normalizer = divisor_polynomial[0]
    
    for i in range(len(polynomial) - len(divisor_polynomial) + 1):
        dividend_copy[i] /= float(normalizer)  # for a clean division
        coefficient = dividend_copy[i]
        if coefficient != 0:  # useless to multiply if coeff is 0
            for j in range(1, len(divisor_polynomial)):
                dividend_copy[i + j] += -divisor_polynomial[j] * coefficient
    
    separator = -(len(divisor_polynomial) - 1)
    return dividend_copy[:separator], dividend_copy[separator:]  # return quotient, remainder

def find_roots(polynomial_coefficients, max_iterations=1000, epsilon=1e-9):
    degree = len(polynomial_coefficients) - 1
    root_guesses = [complex(0.4 + 0.9j) ** i for i in range(degree)]
    
    for _ in range(max_iterations):
        new_root_guesses = []
        for i in range(degree):
            product = 1
            for j in range(degree):
                if i != j:
                    product *= (root_guesses[i] - root_guesses[j])
            new_root_guess = root_guesses[i] - synthetic_division(polynomial_coefficients, [1, -root_guesses[i]])[1][-1] / product
            new_root_guesses.append(new_root_guess)
        
        if all(abs(new_root_guesses[i] - root_guesses[i]) < epsilon for i in range(degree)):
            return new_root_guesses
        root_guesses = new_root_guesses

    return root_guesses  # Return the roots after iterations

def polynomial_roots(degree, polynomial_coefficients):
    if len(polynomial_coefficients) != degree + 1:
        raise ValueError("The number of coefficients must be equal to the degree + 1.")
    
    roots = find_roots(polynomial_coefficients)
    return roots

# Example usage:
degree = 8  # Example polynomial degree
coefficients = [1, -3, 2, 5, 6,7, 10,2, 1]  # Example coefficients for the polynomial: x^2 - 3x + 2

roots = polynomial_roots(degree, coefficients)
print("Roots:", roots)

expected_roots = np.roots(coefficients)
print("Expected roots (using numpy.roots):", expected_roots)
