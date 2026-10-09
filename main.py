
import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# 1. Fixed-Point Function and Its Derivative
# ============================================================

def phi(x):
    """Fixed-point function: phi(x) = exp(-x) + 1."""
    return np.exp(-x) + 1


def derive_phi(x):
    """Derivative of the fixed-point function."""
    return -np.exp(-x)


# ============================================================
# 2. Calculate the Contraction Constant
# ============================================================

def calculer_k(a, b):
    """
    Calculate the contraction constant K on [a, b].

    For this function, |phi'(x)| = exp(-x),
    whose maximum on [a, b] is attained at a.
    """
    return max(abs(derive_phi(a)), abs(derive_phi(b)))


# ============================================================
# 3. Fixed-Point Iteration Algorithm
# ============================================================

def point_fixe(phi, x0, k, epsilon, max_iterations):
    """
    Approximate a fixed point using successive iterations.

    Returns:
        solutions: successive approximations
        erreurs: estimated error bounds
    """
    if not 0 <= k < 1:
        raise ValueError("K must satisfy 0 <= K < 1.")

    if epsilon <= 0:
        raise ValueError("The tolerance must be positive.")

    x = x0
    solutions = [x0]
    erreurs = []

    for i in range(max_iterations):
        x_next = phi(x)

        # Error estimate according to the exercise formula
        erreur = (k ** i / (1 - k)) * abs(x_next - x)

        solutions.append(x_next)
        erreurs.append(erreur)

        if erreur < epsilon:
            break

        x = x_next

    return solutions, erreurs


# ============================================================
# 4. Display the Iteration Table
# ============================================================

def tracer_tableau(solutions, erreurs):
    """Display iterations, approximations, and error estimates."""

    data = []

    for i, (solution, erreur) in enumerate(
        zip(solutions[1:], erreurs), start=1
    ):
        data.append([
            i,
            f"{solution:.8f}",
            f"{erreur:.8e}"
        ])

    if not data:
        print("No iterations were performed.")
        return

    fig, ax = plt.subplots(figsize=(9, max(3, len(data) * 0.4)))

    ax.axis("off")
    ax.set_title("Fixed-Point Iteration Results", pad=20)

    table = ax.table(
        cellText=data,
        colLabels=["Iteration", "Approximate Solution", "Error Estimate"],
        loc="center",
        cellLoc="center"
    )

    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 1.4)

    plt.tight_layout()
    plt.show()


# ============================================================
# 5. Main Program
# ============================================================

if __name__ == "__main__":

    # Initial parameters
    x0 = 1.0
    a = 1.0
    b = 2.0
    epsilon = 1e-6
    max_iterations = 100

    # Calculate the contraction constant
    k = calculer_k(a, b)

    print("========== FIXED-POINT ITERATION ==========")
    print(f"Interval: [{a}, {b}]")
    print(f"Initial value x0: {x0}")
    print(f"Contraction constant K: {k:.8f}")
    print(f"Tolerance: {epsilon}")
    print(f"Maximum iterations: {max_iterations}")

    # Verify the contraction condition
    if k < 1:
        print("The contraction condition is satisfied.")

        # Apply the fixed-point method
        solutions, erreurs = point_fixe(
            phi,
            x0,
            k,
            epsilon,
            max_iterations
        )

        # Display the final result
        print(f"\nApproximate solution: {solutions[-1]:.10f}")
        print(f"Number of iterations: {len(erreurs)}")

        if erreurs:
            print(f"Final error estimate: {erreurs[-1]:.8e}")

        # Display the iteration table
        tracer_tableau(solutions, erreurs)

    else:
        print("The contraction condition is not satisfied.")
