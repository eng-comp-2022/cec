# Firesolver

a tool to solve fires ;)

## Getting Started

1. First, ensure you have [Python](https://www.python.org/) installed. Downloads can be found on the [official Python page](https://www.python.org/), or it can be installed through your distribution:

   ```bash
   yay -S python       # ex. w/ yay
   apt install python3 # ex. w/ apt
   ```

2. Install system packages, listed below. These are supplementary packages that are not provided via the Python packages below.

   **tk**

   The Python package, *tk*, merely installs Python bindings to the *tk* library. Install the actual library on your system.

   ```bash
   yay -S tk # ex. /w yay
   ```

3. Then, ensure you create and activate a Python virtual environment in this
   project's root. This allows the following Python packages to be installed in an
   isolated environment, and the Python interpreter to run in this environment.

   ```bash
   python -m venv venv        # create
   source ./venv/bin/activate # activate
   ```

   > activate scripts exist for various shells

4. All *pip* dependencies are listed in the `requirements.txt` file, and can be
   installed with:

   ```bash
   pip install -r requirements.txt
   ```

5. Run the program:

   ```bash
   python firesolver/main.py
   ```

## Data & Config Files

**Data Files:**

- **data.txt:** explanation of data file
