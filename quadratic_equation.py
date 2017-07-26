from math import sqrt


def get_roots(leading_coefficient, middle_coefficient, free_member):
    discriminant = middle_coefficient ** 2 - 4 * leading_coefficient * free_member
    if discriminant < 0:
        return None, None
    root1 = (-middle_coefficient - sqrt(discriminant)) / (2 * leading_coefficient)
    root2 = (-middle_coefficient + sqrt(discriminant)) / (2 * leading_coefficient)
    if discriminant == 0:
        return root1, None
    else:
        return root1, root2
