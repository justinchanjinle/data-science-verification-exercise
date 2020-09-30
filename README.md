# Data Science Verification Exercise


## Copyright

Copyright 2018 QxBranch Inc.
 
RELEASABILITY: This software is PROPRIETARY to QxBranch Inc. and is released under LICENSE
AGREEMENT or NON-DISCLOSURE AGREEMENT. See the terms of your AGREEMENT with QxBranch Inc. for
conditions of use and disclosure. QxBranch Inc. has NOT publicly published this work.

## Set up
1. Download and install [PyCharm Community Edition](https://www.jetbrains.com/pycharm/download/#section=windows)
according to your respective OS.
2. Select a Python 3.5 interpreter, Python 3.5.4 if possible. You can use your OS' native interpreter or an interpreter 
from a Python distribution such as [Anaconda](https://www.anaconda.com/download/). You can download Python 3.5.4 for 
your OS [here](https://www.python.org/downloads/release/python-354/). If you opt for Anaconda, follow the simple 
instructions on the download page to set up Python 3.5.4 on Anaconda. 
3. If you use PyCharm, PyCharm should be able to detect missing requirements in your interpreter based on the 
`requirements.txt` and prompt you to install it. Otherwise, run ` pip install -r requirements.txt` in your shell.
4. To select pytest as the unit test framework, navigate File | Settings | Tools | Python Integrated Tools and change 
the default test runner to py.test. Then you'll get the py.test option to create tests instead of the unittest one.