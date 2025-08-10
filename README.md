# p2c

A tiny Python library that takes two numbers and produces:
- `a` – their sum (`n1 + n2`)
- `b` – their difference (`n1 - n2`)
- `c` – `2*n1 - n2`
- `p2c(x)` – quadratic callable: `a*x**2 + b*x + c`
- `jac_p2c(x)` – derivative of `p2c(x)` with respect to `x`

## Install
The `pip install .` command installs your package into your current Python environment from the local directory where the `pyproject.toml` is located. The dot (`.`) means “this directory.”

For example:
```bash
cd /path/to/project/root
pip install .