Read more at [pypa/sampleproject](https://github.com/pypa/sampleproject)

## Test package
```bash
conda create -n myproject python=3.8 - y && conda activate myproject
pip install tox
tox --recreate
```

## Build wheel file
```bash
python -m build
```
A wheel file will be created in the `dist` directory. It can use to install the package or upload to PyPI.

## Install package in editable mode
```bash
pip install -e .
```
