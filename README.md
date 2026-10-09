# Fixed-Point Iteration Method in Python

## Overview

This project implements the Fixed-Point Iteration Method in Python to find an approximate solution to a nonlinear equation.

The method transforms an equation into the form:

\[
x = \varphi(x)
\]

It then generates successive approximations until the estimated error reaches the specified tolerance.

## Mathematical Problem

The project solves the equation:

\[
f(x) = x - 1 - e^{-x} = 0
\]

Using the fixed-point function:

\[
\varphi(x) = e^{-x} + 1
\]

The initial value is \(x_0 = 1\), and the method is studied on the interval \([1,2]\).

## Features

- Fixed-Point Iteration algorithm.
- Calculation of the contraction constant.
- Convergence analysis.
- Error estimation at each iteration.
- Configurable precision and maximum number of iterations.
- Results displayed in a table.

## Technologies

- Python 3
- NumPy
- Matplotlib

## Installation

Install the required libraries:

```bash
pip install numpy matplotlib
```

## How to Run

Run the Python script:

```bash
python main.py
```

## Project Structure

```text
fixed-point-iteration/
├── main.py
├── README.md
└── .gitignore
```

## Learning Objectives

- Understand the Fixed-Point Iteration Method.
- Implement iterative algorithms in Python.
- Study convergence and contraction conditions.
- Estimate numerical errors.
- Present numerical results in tabular form.

## License

Add a license file if you want to specify how others may use, modify, and distribute this project.
