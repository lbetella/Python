*This repository contains projects created as part of the 42 curriculum by lbetella.*

# 🐍 42 Python Curriculum: From Fundamentals to Software Architecture

Welcome to my **42 Python** repository! This space documents my complete learning journey through Python—progressing from basic syntax and object-oriented modeling to resilient data pipelines, packaging, software design patterns, data validation, and functional programming.

Each module is organized into its own directory and includes a dedicated, detailed `README.md` covering specific exercises, implementation choices, and execution instructions.

## 🗺️ Curriculum Overview

| Module | Project Title | Core Focus & Key Concepts Learned |
| :--- | :--- | :--- |
| **Module 00** | **Growing Code** | Python syntax & semantics, variables, expressions, control flow, iteration vs. recursion, basic string manipulation, and introductory type hints. |
| **Module 01** | **Code Cultivation** | Object-Oriented Programming (OOP), classes & objects, `__init__` constructors, encapsulation (`_protected` attributes), inheritance (`super()`), method overriding, `@classmethod`, `@staticmethod`, and nested classes. |
| **Module 02** | **Garden Guardian** | Defensive programming, exception handling (`try` / `except` / `finally` / `raise`), built-in exceptions, custom exception hierarchies, and fault-tolerant data validation pipelines. |
| **Module 03** | **Data Quest** | Core data structures (`list`, `tuple`, `set`, `dict`), command-line arguments (`sys.argv`), memory-efficient generators (`yield`), and list/dictionary comprehensions. |
| **Module 04** | **Data Archivist** | File I/O operations (`open`, `read`, `write`, `close`), standard I/O streams (`sys.stdin`, `sys.stdout`, `sys.stderr`), and safe resource management via context managers (`with`). |
| **Module 05bis** | **The Codex** | Virtual environments (`venv`), dependency management (`pip` vs. `Poetry`), environment variables & secrets (`.env`, `python-dotenv`), package architecture (`__init__.py`), absolute/relative imports, and resolving circular dependencies. |
| **Module 06bis** | **Code Nexus** | Software architecture & design patterns: Abstract Base Classes (`ABC`), subtype polymorphism, structural typing (`Protocol` / duck typing), Abstract Factory pattern, Capability composition, and Strategy pattern. |
| **Module 09** | **Cosmic Data** | Modern data validation with **Pydantic v2** (`BaseModel`, `Field`, `Enum`), custom business rule validation (`@model_validator`), automatic type coercion, and nested data models. |
| **Module 10** | **FuncMage** | Functional programming paradigms: `lambda` expressions, `map`/`filter`/`reduce`, higher-order functions, closures & lexical scoping (`nonlocal`), `functools` (`lru_cache`, `partial`, `singledispatch`), and custom decorators (`@wraps`). |

## 🛠️ Technical Standards & Tooling

Across all modules in this repository, the codebase adheres to strict engineering and quality standards:

* **Python Version:** Python 3.10+
* **Code Style:** Strictly compliant with **PEP 8** guidelines, verified using `flake8`.
* **Static Typing:** Comprehensive type annotations across functions, methods, and classes, verified using `mypy`.
* **Environment & Validation:** Isolated virtual environments (`venv` / `Poetry`) and schema validation powered by `Pydantic 2.x` where applicable.

## 📂 Repository Structure

```text
.
├── README.md               # General overview (you are here)
├── module_00/              # Growing Code (Fundamentals)
├── module_01/              # Code Cultivation (OOP)
├── module_02/              # Garden Guardian (Exceptions)
├── module_03/              # Data Quest (Collections & Generators)
├── module_04/              # Data Archivist (File I/O & Streams)
├── module_05bis/           # The Codex (Packaging & Environments)
├── module_06bis/           # Code Nexus (Design Patterns & Architecture)
├── module_09/              # Cosmic Data (Pydantic Data Validation)
└── module_10/              # FuncMage (Functional Programming)
```

*(Note: Navigate into any module directory to inspect its specific `README.md` and run its exercises.)*

## 🚀 Quick Start

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Verify code quality (optional):**
   ```bash
   flake8 .
   mypy .
   ```

3. **Explore a module:**
   Navigate to any module folder (e.g., `cd module_05bis`) and follow the instructions in its local `README.md`.

## 📚 Core Resources & AI Usage

### General References

* [Official Python 3 Documentation](https://docs.python.org/3/)
* [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)
* [Mypy Static Type Checker Documentation](https://mypy.readthedocs.io/)
* [Pydantic V2 Documentation](https://docs.pydantic.dev/latest/)

### AI Usage Disclosure

In accordance with the **42 AI Guidelines**, Artificial Intelligence tools were used responsibly throughout these projects as a learning aid and productivity tool—specifically to clarify architectural concepts, explore edge cases, review static typing warnings, and structure documentation. All code logic, data structures, and design patterns were written, tested, and verified manually.