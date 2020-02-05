from setuptools import setup

setup(
    name="regexer",
    version="0.0.1",
    description="Simplify work with regex.",
    author="Kurovkyi Vladyslav",
    python_requires=">=3.6",
    py_modules = ['regexer'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='test_regexer'    
)