# Contributing to Task Manager App

Thank you for considering contributing to the Task Manager App! We welcome contributions of all kinds, including bug fixes, feature enhancements, and documentation improvements. Below you'll find a guide on how to contribute effectively.

## Table of Contents
1. [Code of Conduct](#code-of-conduct)
2. [Getting Started](#getting-started)
3. [How to Contribute](#how-to-contribute)
    - [Reporting Bugs](#reporting-bugs)
    - [Suggesting Features](#suggesting-features)
    - [Submitting Code Changes](#submitting-code-changes)
4. [Development Workflow](#development-workflow)
5. [Style Guide](#style-guide)
6. [License](#license)

## Code of Conduct

This project adheres to a [Code of Conduct](https://github.com/noellerjd/Task-Manager-App/blob/main/CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to [noellerjd@gmail.com](mailto:noellerjd@gmail.com).

## Getting Started

1. **Clone the repository:**
    ```bash
    git clone https://github.com/username/task-manager-app.git
    cd task-manager-app
    ```

2. **Set up a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application:**
    ```bash
    python TaskManagerApp.py
    ```

## How to Contribute

### Reporting Bugs

If you find a bug, please report it by opening an [issue](https://github.com/noellerjd/task-manager-app/issues). Please include details about the environment where the bug occurs, steps to reproduce, and any relevant log output.

### Suggesting Features

We’re always open to new ideas! Please feel free to open an [issue](https://github.com/noellerjd/task-manager-app/issues) or start a [discussion](https://github.com/noellerjd/task-manager-app/discussions) to propose new features or enhancements.

### Submitting Code Changes

1. **Fork the repository** and create your branch from `main`:
    ```bash
    git checkout -b feature/YourFeatureName
    ```

2. **Make your changes**:
    - Follow the [Style Guide](#style-guide) below.
    - Include tests where necessary.

3. **Commit your changes**:
    - Write clear, concise commit messages. Reference any issue numbers in the format `#123`.
    ```bash
    git commit -m "Add feature XYZ (#123)"
    ```

4. **Push your changes** to your fork:
    ```bash
    git push origin feature/YourFeatureName
    ```

5. **Create a Pull Request**:
    - Go to the original repository on GitHub and open a pull request.
    - Provide a description of what your changes do, why they are needed, and any relevant issue numbers.

## Development Workflow

1. **Keep your fork updated**:
    ```bash
    git fetch upstream
    git checkout main
    git merge upstream/main
    ```

2. **Run tests** before submitting:
    - Ensure that all tests pass before submitting your changes.
    - Add new tests for new features or bug fixes.

3. **Review Process**:
    - Your pull request will be reviewed by project maintainers.
    - You might be asked to make additional changes or clarifications.

## Style Guide

- **Code Formatting**: Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python code.
- **Naming Conventions**: Use meaningful names for variables, functions, and classes.
- **Comments**: Comment your code where necessary, especially in complex logic.
- **Documentation**: Update the `README.md` or other relevant documentation when making changes that require it.

## License

By contributing, you agree that your contributions will be licensed under the project's [MIT License](LICENSE).
