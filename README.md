# Numerical ODE Solvers

<Add summary of project later>

# Project Structure
- `src/`: Core implementation containing the solvers and test equations.
- `notebooks/`: Interactive demonstration and visualization of results.
- `tests/`: Unit tests and mathematical validation scripts.
- `pyproject.toml`: Configuration to allow for "editable" installation.

# View the demonstration in your browser


[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/EvanGerns/ode_solvers/blob/main/notebooks/demo.ipynb)



# Local Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/EvanGerns/ode_solvers.git](https://github.com/EvanGerns/ode_solvers.git)
   cd ode_solvers

2. **Install the package:**
    ```bash
    pip install -e .
    
3. **Run the tests:**
    Verify the accuracy of the solvers
    ```bash
    pytest