python_example
==============

An example project built with [pybind11](https://github.com/pybind/pybind11).

Installation
------------

```Bash
git clone --recursive git@github.com:haruishi43/pybind_example.git
cd pybind_example
pip install .
```

Usage
-----

```Python
import cmake_example as m
m.add(1, 3)
>>> 4
```

Test call
---------

```python
import cmake_example
python_example.add(1, 2)
```
