### TextFSM Python 3

Install:
```
pip install jtextfsm
```

Fix clitable:
```
$ ipython
Python 3.6.0 (default, May 31 2017, 07:04:38) 
Type 'copyright', 'credits' or 'license' for more information
IPython 6.0.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import clitable
---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
<ipython-input-1-58644db64de7> in <module>()
----> 1 import clitable

/home/vagrant/venv/py3_convert/lib/python3.6/site-packages/clitable.py in <module>()
     32 import copyable_regex_object
     33 import textfsm
---> 34 import texttable
     35 
     36 

/home/vagrant/venv/py3_convert/lib/python3.6/site-packages/texttable.py in <module>()
     26 import copy
     27 import textwrap
---> 28 import terminal
     29 
     30 

ModuleNotFoundError: No module named 'terminal'

In [2]: quit
```

Copy terminal.py content from [textfsm repo](https://github.com/google/textfsm/blob/master/terminal.py)
```
$ vi /home/vagrant/venv/py3_convert/lib/python3.6/site-packages/terminal.py

$ ipython
Python 3.6.0 (default, May 31 2017, 07:04:38) 
Type 'copyright', 'credits' or 'license' for more information
IPython 6.0.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import clitable

```


Change xrange to range in texttable.py:
```
$ python textfsm_clitable.py
Traceback (most recent call last):
  File "textfsm_clitable.py", line 5, in <module>
    cli_table = clitable.CliTable('index', 'templates')
  File "/home/vagrant/venv/py3_convert/lib/python3.6/site-packages/clitable.py", line 155, in Wrapper
    return func(main_obj, *args, **kwargs)  # pylint: disable-msg=E1102
  File "/home/vagrant/venv/py3_convert/lib/python3.6/site-packages/clitable.py", line 176, in __init__
    self.ReadIndex(index_file)
  File "/home/vagrant/venv/py3_convert/lib/python3.6/site-packages/clitable.py", line 191, in ReadIndex
    self.index = IndexTable(self._PreParse, self._PreCompile, fullpath)
  File "/home/vagrant/venv/py3_convert/lib/python3.6/site-packages/clitable.py", line 74, in __init__
    self._ParseIndex(preread, precompile)
  File "/home/vagrant/venv/py3_convert/lib/python3.6/site-packages/clitable.py", line 93, in _ParseIndex
    self.index.CsvToTable(self._index_handle)
  File "/home/vagrant/venv/py3_convert/lib/python3.6/site-packages/texttable.py", line 943, in CsvToTable
    header_row[entry] = entry
  File "/home/vagrant/venv/py3_convert/lib/python3.6/site-packages/texttable.py", line 90, in __setitem__
    for i in xrange(len(self)):
NameError: name 'xrange' is not defined

$ vi /home/vagrant/venv/py3_convert/lib/python3.6/site-packages/texttable.py

```
