from math import sqrt


def get_roots(average_coefficient, leading_coefficient, free_member):
    discriminant = leading_coefficient ** 2 - 4 * average_coefficient * free_member
    if discriminant < 0:
        return None, None
    root1 = (-leading_coefficient - sqrt(discriminant)) / (2 * average_coefficient)
    root2 = (-leading_coefficient + sqrt(discriminant)) / (2 * average_coefficient)
    if discriminant == 0:
        return root1, None
    else:
        return root1, root2
