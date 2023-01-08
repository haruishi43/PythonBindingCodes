from setuptools import setup, Extension


pipcudemo_core = Extension(
    'pipcudemo.core',
    sources=['pipcudemo/core.cpp'],
    include_dirs=['.'],
    libraries=['mylib']
)

setup(
    name='pipcudemo',
    author='Haruya Ishikawa',
    author_email='haru.ishi43@gmail.com',
    version='0.0.1',
    description="""
        An example project showing how to build a pip-installable
        Python package that invokes custom CUDA/C++ code.
        """,
    ext_modules=[pipcudemo_core],
    packages=['pipcudemo']
)
