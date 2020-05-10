Blackhole
=========

**01_bytecode.py** and **02_cyclomatic.py**

Performing static code analysis usually requires running an external tool onto the codebase, and while static code analysis tools usually provide good builtins it's not always convenient to extend them with custom rules for pattern enforcing, integrate them into the dev/test flow and make them properly work on a dynamic language like Python.

So I started to experiment with using Inspection and Python Bytecode as a representation of the original codebase such that it was possible to analyse functions and their usage from within testsuite itself and enforce bestpractices also on dynamic code.

**shelvedb.py**

Minimal lines of code to build a key-value DB in Python with only standard library.
