*This project has been created as part of the 42 curriculum by lbetella.*

# Growing Code: Python Fundamentals Through Garden Data

## Description
**Growing Code** is an introductory project from the 42 curriculum designed to build a solid foundation in Python 3.10+. Through the practical and relatable context of managing community garden data, this project covers core programming concepts including syntax, variables, basic input/output operations, arithmetic expressions, conditional statements, iterative and recursive loops, and static type annotations.

### Overview of Exercises
The repository is structured into 8 progressive exercises (`ex0` through `ex7`), each isolated in its own directory and containing a single standalone function:

* **`ex0/ft_hello_garden.py`**: Outputs a welcome message to the garden community using `print()`.
* **`ex1/ft_garden_name.py`**: Prompts the user for a garden name via `input()` and displays it alongside a fixed status message.
* **`ex2/ft_plot_area.py`**: Calculates and prints the area of a rectangular garden plot based on user-provided length and width.
* **`ex3/ft_harvest_total.py`**: Computes the total harvest weight across three different days using type casting (`int()`).
* **`ex4/ft_plant_age.py`**: Evaluates whether a plant is ready for harvest (strictly older than 60 days) using conditional logic (`if/else`).
* **`ex5/ft_water_reminder.py`**: Determines if plants need watering based on the number of days since the last watering session.
* **`ex6/ft_count_harvest_iterative.py` & `ft_count_harvest_recursive.py`**: Counts down the days until harvest using both an iterative approach (`range()`) and a recursive approach.
* **`ex7/ft_seed_inventory.py`**: Manages and formats seed inventory data (packets, grams, and coverage area) while enforcing strict Python type hints (`str`, `int`, `None`).

---

## Instructions

### Prerequisites
* **Python 3.10** or higher.
* **flake8** (for verifying code style and PEP 8 compliance).
* **mypy** (for static type checking, specifically required for `ex7`).

### Installation & Setup
Clone the repository to your local machine:
```bash
git clone <repository_url>
cd <repository_directory>
```

### Execution & Testing
Per the project guidelines, the submitted exercise files contain **only** the requested function definitions (no `if __name__ == "__main__":` blocks or direct function calls). 

To test the functions:
1. **Using the provided helper script:** Place the `main.py` helper file provided in the intranet attachments into the root directory (or alongside the exercise files) and run:
   ```bash
   python3 main.py
   ```
2. **Using the Python interactive shell:**
   ```bash
   python3 -c "from ex0.ft_hello_garden import ft_hello_garden; ft_hello_garden()"
   ```

### Linting & Type Checking
To ensure the code adheres to 42's quality standards before evaluation:
```bash
# Check PEP 8 style compliance across all exercises
flake8 ex0/ ex1/ ex2/ ex3/ ex4/ ex5/ ex6/ ex7/

# Check static type annotations (mandatory for Exercise 7)
mypy ex7/ft_seed_inventory.py
```

---

## Resources

### Classic References & Documentation
* [Official Python 3 Documentation](https://docs.python.org/3/) – Core language reference, built-in functions (`print`, `input`, `int`, `range`), and string methods.
* [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/) – Official coding conventions enforced by `flake8`.
* [Python `typing` Module Documentation](https://docs.python.org/3/library/typing.html) – Reference for type hints and annotations used in `ex7`.
* [Real Python: Recursion in Python](https://realpython.com/python-recursion/) – Guide on structuring base cases and recursive calls for `ex6`.
* [Mypy Documentation](https://mypy.readthedocs.io/en/stable/) – Static type checker documentation.

### AI Usage Disclosure
In accordance with the 42 AI guidelines, Artificial Intelligence tools were used strictly as a learning and productivity aid, never to blindly generate final solutions:
* **Documentation & Structuring:** AI was used to help structure and format this `README.md` file to ensure clarity and compliance with project requirements.
* **Concept Clarification:** AI was consulted to clarify edge cases regarding Python's recursion depth limits and nested helper functions (`ex6`), as well as best practices for PEP 484 type annotations (`ex7`).
* **Testing & Edge Cases:** AI was used to brainstorm test inputs and verify expected outputs against the subject specifications. All code logic was written, tested, and verified manually.
