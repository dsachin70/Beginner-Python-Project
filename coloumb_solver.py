import sys

def compute_columb_force(q1:float, q2:float, r:float) -> float:
    if type(q1) != float and type(q1) != int:
        print("Bad type for q1")
        return None

    if type(q2) != float and type(q1) != int:
        print("Bad type for q2")
        return None

    if type(r) != float and type(r) != float:
        print("Bad type for r")
        return None

    K = 8.987555 * (10**9)
    F = (K *q1 * q2)/(r**2)

    return (F)

def main() -> None:
    q1 = float(input("Enter magnitude of charge 1:"))
    q2 = float(input("Enter magnitude of charge 2:"))
    r = float(input("Enter magnitude of charge 3:"))
    F = compute_columb_force(q1, q2, r)
    print("Magnitude of force of attraction or repulsion betwen particles with charges {} and {} and distance {} is {}".format(q1, q2, r, F))
main()