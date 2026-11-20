*This project has been created as part of the 42 curriculum by lbetella.*

# Code Cultivation: Object-Oriented Garden Systems

## Description

**Code Cultivation** is the second Python module in the 42 curriculum, transitioning from procedural basics to **Object-Oriented Programming (OOP)** and modular software design. Through the context of building a scalable digital garden ecosystem, this project explores Python program execution patterns, class design, state mutation, constructors, encapsulation, inheritance, method overriding, static/class methods, nested classes, and strict static type annotations.

### Overview of Exercises

The repository is structured into 7 progressive exercises (`ex0` through `ex6`), each contained in its own directory and evolving a unified garden management architecture:

* **`ex0/ft_garden_intro.py`**: Introduces basic Python script execution using the `if __name__ == "__main__":` entry point to display initial plant variables.
* **`ex1/ft_garden_data.py`**: Introduces basic class modeling by implementing a `Plant` class with attributes (`name`, `height`, `age`) and a `show()` display method.
* **`ex2/ft_plant_growth.py`**: Adds state-mutating behavior (`grow()` and `age()` methods) to the `Plant` class to simulate and summarize a week of plant growth.
* **`ex3/ft_plant_factory.py`**: Streamlines object instantiation using the `__init__()` constructor to batch-create and initialize multiple distinct `Plant` instances cleanly.
* **`ex4/ft_garden_security.py`**: Implements data encapsulation using protected attributes (`_height`, `_age`) and validated getters/setters (`get_height()`, `set_height()`, `get_age()`, `set_age()`) to prevent data corruption.
* **`ex5/ft_plant_types.py`**: Implements class inheritance and polymorphism by deriving specialized `Flower`, `Tree`, and `Vegetable` classes from `Plant`, utilizing `super()` and method overriding.
* **`ex6/ft_garden_analytics.py`**: Combines advanced OOP patterns including `@staticmethod`, `@classmethod` (for anonymous plant instantiation), multi-level inheritance (`Seed` inheriting from `Flower`), encapsulated nested statistics classes, and standalone polymorphic reporting functions.

## Instructions

### Prerequisites

* **Python 3.10** or higher.
* **flake8** (for verifying PEP 8 style compliance).
* **mypy** (for static type checking, mandatory across all functions and methods in this module).

### Installation & Setup

Clone the repository to your local machine:

```bash
git clone <repository_url>
cd <repository_directory>
```

### Execution & Testing

Unlike Module 00, each exercise in this module is designed as a standalone executable script containing an `if __name__ == "__main__":` block to demonstrate and test the implemented classes.

Run any exercise directly from the root directory:

```bash
python3 ex0/ft_garden_intro.py
python3 ex1/ft_garden_data.py
python3 ex2/ft_plant_growth.py
python3 ex3/ft_plant_factory.py
python3 ex4/ft_garden_security.py
python3 ex5/ft_plant_types.py
python3 ex6/ft_garden_analytics.py
```

*(Note: For `ex0`, ensure you understand the role of the `#!/usr/bin/env python3` shebang line and executable permissions `chmod +x`, as this may be tested live during peer evaluation).*

### Linting & Type Checking

Verify that all code follows 42's strict formatting and static typing rules:

```bash
# Check PEP 8 compliance across all directories
flake8 ex0/ ex1/ ex2/ ex3/ ex4/ ex5/ ex6/

# Check mandatory type annotations across all directories
mypy ex0/ ex1/ ex2/ ex3/ ex4/ ex5/ ex6/
```

## Resources

### Classic References & Documentation

* [Official Python 3 Documentation – Classes](https://docs.python.org/3/tutorial/classes.html) – Core reference for Python OOP, inheritance, `super()`, and nested classes.
* [Python Execution Model & `__main__`](https://docs.python.org/3/library/__main__.html) – Explanation of top-level code environment and `if __name__ == "__main__":`.
* [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/) – Naming conventions (`PascalCase` for classes, `snake_case` for methods/variables) and protected attribute conventions (`_single_leading_underscore`).
* [Python `typing` Module Documentation](https://docs.python.org/3/library/typing.html) – Reference for type hints required on all functions and methods.
* [Real Python: Instance, Class, and Static Methods](https://realpython.com/instance-class-and-static-methods-demystified/) – Guide on `@classmethod` and `@staticmethod` decorators used in `ex6`.

### AI Usage Disclosure

In accordance with the 42 AI guidelines, Artificial Intelligence tools were used responsibly as a learning companion rather than a code generator:

* **Documentation:** AI assisted in structuring and formatting this `README.md` file to meet all 42 documentation criteria.
* **OOP Architecture & Concepts:** AI was consulted to clarify design nuances regarding Python's protected attribute conventions (`_attr` vs `__attr` name mangling in `ex4`), proper usage of `super()` during method overriding (`ex5`), and structuring nested statistics tracking classes (`ex6`).
* **Debugging & Edge Cases:** AI was used to review `mypy` type-checking warnings and brainstorm test scenarios for invalid negative values and inheritance chains. All classes, methods, and test suites were written and verified manually.