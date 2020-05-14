Snippets for Python Show Episode #3
===================================

https://www.youtube.com/watch?v=8Ux1OTXkSnc

**crashlog.py**

The ``logging`` module used to send track crashes and report them.
And ``smtpd`` module to test them -> ``python -m smtpd -n -c DebuggingServer localhost:1025``

PS: The backlash ( https://github.com/TurboGears/backlash ) Python package can solve the same need with a more ready made solution.

**testing**

Run ``python3 -m unittest discover -k one`` here to see what happens...

PS: The pytest ( https://github.com/pytest-dev/pytest ) Python package solves similar need with a more complete solution.

**shelvedb.py** and **shelvedb_client.py**

A simple key/value database based only on Standard Library provided modules.

PS: Maybe use Redis? ;)