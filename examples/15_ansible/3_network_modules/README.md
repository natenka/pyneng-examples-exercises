## Ansible network modules with Py3

> Last update 01.06.17


### Error
```
(py3_convert) 
[~/pyneng_py3_convert/convert-pyneng-to-py3/examples/15_ansible/3_network_modules/ios_command]
vagrant@jessie-i386: [master|✔] 
04:40 $ ansible-playbook 1_ios_command.yml
SSH password: 

PLAY [Run show commands on routers] **************************************************************************************************

TASK [run sh ip int br] **************************************************************************************************************
An exception occurred during task execution. To see the full traceback, use -vvv. The error was: TypeError: string argument expected, got 'bytes'
fatal: [192.168.100.1]: FAILED! => {"failed": true, "msg": "Unexpected failure during module execution.", "stdout": ""}
An exception occurred during task execution. To see the full traceback, use -vvv. The error was: TypeError: string argument expected, got 'bytes'
fatal: [192.168.100.3]: FAILED! => {"failed": true, "msg": "Unexpected failure during module execution.", "stdout": ""}
An exception occurred during task execution. To see the full traceback, use -vvv. The error was: TypeError: string argument expected, got 'bytes'
fatal: [192.168.100.2]: FAILED! => {"failed": true, "msg": "Unexpected failure during module execution.", "stdout": ""}
    to retry, use: --limit @/home/vagrant/pyneng_py3_convert/convert-pyneng-to-py3/examples/15_ansible/3_network_modules/ios_command/1_ios_command.retry

PLAY RECAP ***************************************************************************************************************************
192.168.100.1              : ok=0    changed=0    unreachable=0    failed=1   
192.168.100.2              : ok=0    changed=0    unreachable=0    failed=1   
192.168.100.3              : ok=0    changed=0    unreachable=0    failed=1   

```

* [Issue](https://github.com/ansible/ansible/issues/24355)
* [Fix in ansible-devel](https://github.com/ansible/ansible/pull/24431)


### Ansible devel

Install:
```
(py3_convert) 
[~/pyneng_py3_convert/convert-pyneng-to-py3/examples/15_ansible/3_network_modules/ios_command]
vagrant@jessie-i386: [master|✔] 
04:41 $ pip install git+git://github.com/ansible/ansible.git@devel
Collecting git+git://github.com/ansible/ansible.git@devel
  Cloning git://github.com/ansible/ansible.git (to devel) to /tmp/pip-g6uu1vhg-build
Requirement already satisfied: jinja2 in /home/vagrant/venv/py3_convert/lib/python3.6/site-packages (from ansible==2.4.0)
Requirement already satisfied: PyYAML in /home/vagrant/venv/py3_convert/lib/python3.6/site-packages (from ansible==2.4.0)
Requirement already satisfied: paramiko in /home/vagrant/venv/py3_convert/lib/python3.6/site-packages (from ansible==2.4.0)
Requirement already satisfied: pycrypto>=2.6 in /home/vagrant/venv/py3_convert/lib/python3.6/site-packages (from ansible==2.4.0)
Requirement already satisfied: setuptools in /home/vagrant/venv/py3_convert/lib/python3.6/site-packages (from ansible==2.4.0)
Requirement already satisfied: MarkupSafe>=0.23 in /home/vagrant/venv/py3_convert/lib/python3.6/site-packages (from jinja2->ansible==2.4.0)
Requirement already satisfied: pyasn1>=0.1.7 in /home/vagrant/venv/py3_convert/lib/python3.6/site-packages (from paramiko->ansible==2.4.0)
Requirement already satisfied: cryptography>=1.1 in /home/vagrant/venv/py3_convert/lib/python3.6/site-packages (from paramiko->ansible==2.4.0)
Requirement already satisfied: packaging>=16.8 in /home/vagrant/venv/py3_convert/lib/python3.6/site-packages (from setuptools->ansible==2.4.0)
Requirement already satisfied: six>=1.6.0 in /home/vagrant/venv/py3_convert/lib/python3.6/site-packages (from setuptools->ansible==2.4.0)
Requirement already satisfied: appdirs>=1.4.0 in /home/vagrant/venv/py3_convert/lib/python3.6/site-packages (from setuptools->ansible==2.4.0)
Requirement already satisfied: asn1crypto>=0.21.0 in /home/vagrant/venv/py3_convert/lib/python3.6/site-packages (from cryptography>=1.1->paramiko->ansible==2.4.0)
Requirement already satisfied: idna>=2.1 in /home/vagrant/venv/py3_convert/lib/python3.6/site-packages (from cryptography>=1.1->paramiko->ansible==2.4.0)
Requirement already satisfied: cffi>=1.7 in /home/vagrant/venv/py3_convert/lib/python3.6/site-packages (from cryptography>=1.1->paramiko->ansible==2.4.0)
Requirement already satisfied: pyparsing in /home/vagrant/venv/py3_convert/lib/python3.6/site-packages (from packaging>=16.8->setuptools->ansible==2.4.0)
Requirement already satisfied: pycparser in /home/vagrant/venv/py3_convert/lib/python3.6/site-packages (from cffi>=1.7->cryptography>=1.1->paramiko->ansible==2.4.0)
Installing collected packages: ansible
  Found existing installation: ansible 2.3.0.0
    Uninstalling ansible-2.3.0.0:
      Successfully uninstalled ansible-2.3.0.0
  Running setup.py install for ansible ... done
Successfully installed ansible-2.4.0

```


Check:
```
(py3_convert) 
[~/pyneng_py3_convert/convert-pyneng-to-py3/examples/15_ansible/3_network_modules/ios_command]
vagrant@jessie-i386: [master|✚ 1…1] 
04:54 $ ansible-playbook 1_ios_command.yml
SSH password: 

PLAY [Run show commands on routers] **************************************************************************************************

TASK [run sh ip int br] **************************************************************************************************************
ok: [192.168.100.1]
ok: [192.168.100.3]
ok: [192.168.100.2]

TASK [Debug registered var] **********************************************************************************************************
ok: [192.168.100.1] => {
    "failed": false,
    "sh_ip_int_br_result.stdout_lines": [
        [
            "Interface                  IP-Address      OK? Method Status                Protocol",
            "Ethernet0/0                192.168.100.1   YES NVRAM  up                    up      ",
            "Ethernet0/1                192.168.200.1   YES NVRAM  up                    up      ",
            "Ethernet0/2                19.1.1.1        YES NVRAM  up                    up      ",
            "Ethernet0/3                192.168.230.1   YES NVRAM  up                    up"
        ]
    ]
}
ok: [192.168.100.2] => {
    "failed": false,
    "sh_ip_int_br_result.stdout_lines": [
        [
            "Interface                  IP-Address      OK? Method Status                Protocol",
            "Ethernet0/0                192.168.100.2   YES NVRAM  up                    up      ",
            "Ethernet0/1                unassigned      YES NVRAM  administratively down down    ",
            "Ethernet0/2                unassigned      YES NVRAM  administratively down down    ",
            "Ethernet0/3                unassigned      YES NVRAM  administratively down down"
        ]
    ]
}
ok: [192.168.100.3] => {
    "failed": false,
    "sh_ip_int_br_result.stdout_lines": [
        [
            "Interface                  IP-Address      OK? Method Status                Protocol",
            "Ethernet0/0                192.168.100.3   YES NVRAM  up                    up      ",
            "Ethernet0/1                unassigned      YES NVRAM  administratively down down    ",
            "Ethernet0/2                unassigned      YES NVRAM  administratively down down    ",
            "Ethernet0/3                unassigned      YES NVRAM  administratively down down"
        ]
    ]
}

PLAY RECAP ***************************************************************************************************************************
192.168.100.1              : ok=2    changed=0    unreachable=0    failed=0   
192.168.100.2              : ok=2    changed=0    unreachable=0    failed=0   
192.168.100.3              : ok=2    changed=0    unreachable=0    failed=0   


```


### Changes

* ios_config save option  - fixed




## Errors

### ios_config backup option

```
(py3_convert) 
[~/pyneng_py3_convert/convert-pyneng-to-py3/examples/15_ansible/3_network_modules/ios_config]
vagrant@jessie-i386: [master|✚ 5…1] 
05:15 $ ansible-playbook 5_ios_config_backup.yml -v
Using /home/vagrant/pyneng_py3_convert/convert-pyneng-to-py3/examples/15_ansible/3_network_modules/ios_config/ansible.cfg as config file

PLAY [Run cfg commands on routers] ***************************************************************************************************

TASK [Config line vty] ***************************************************************************************************************
An exception occurred during task execution. To see the full traceback, use -vvv. The error was: RuntimeError: dictionary changed size during iteration
fatal: [192.168.100.2]: FAILED! => {"failed": true, "msg": "Unexpected failure during module execution.", "stdout": ""}
An exception occurred during task execution. To see the full traceback, use -vvv. The error was: RuntimeError: dictionary changed size during iteration
fatal: [192.168.100.1]: FAILED! => {"failed": true, "msg": "Unexpected failure during module execution.", "stdout": ""}
An exception occurred during task execution. To see the full traceback, use -vvv. The error was: RuntimeError: dictionary changed size during iteration
fatal: [192.168.100.3]: FAILED! => {"failed": true, "msg": "Unexpected failure during module execution.", "stdout": ""}
    to retry, use: --limit @/home/vagrant/pyneng_py3_convert/convert-pyneng-to-py3/examples/15_ansible/3_network_modules/ios_config/5_ios_config_backup.retry

PLAY RECAP ***************************************************************************************************************************
192.168.100.1              : ok=0    changed=0    unreachable=0    failed=1   
192.168.100.2              : ok=0    changed=0    unreachable=0    failed=1   
192.168.100.3              : ok=0    changed=0    unreachable=0    failed=1   

```


With -vvv:
```
(py3_convert) 
[~/pyneng_py3_convert/convert-pyneng-to-py3/examples/15_ansible/3_network_modules/ios_config]
vagrant@jessie-i386: [master|✚ 5…5] 
05:16 $ ansible-playbook 5_ios_config_backup.yml -vvv
ansible-playbook 2.4.0
  config file = /home/vagrant/pyneng_py3_convert/convert-pyneng-to-py3/examples/15_ansible/3_network_modules/ios_config/ansible.cfg
  configured module search path = ['./library']
  ansible python module location = /home/vagrant/venv/py3_convert/lib/python3.6/site-packages/ansible
  executable location = /home/vagrant/venv/py3_convert/bin/ansible-playbook
  python version = 3.6.0 (default, May 31 2017, 07:04:38) [GCC 4.9.2]
Using /home/vagrant/pyneng_py3_convert/convert-pyneng-to-py3/examples/15_ansible/3_network_modules/ios_config/ansible.cfg as config file
Parsed /home/vagrant/pyneng_py3_convert/convert-pyneng-to-py3/examples/15_ansible/3_network_modules/ios_config/myhosts inventory source with ini plugin
...

<192.168.100.3> EXEC /bin/sh -c 'chmod u+x /home/vagrant/.ansible/tmp/ansible-tmp-1496294249.380864-253943902081895/ /home/vagrant/.ansible/tmp/ansible-tmp-1496294249.380864-253943902081895/ios_config.py && sleep 0'
<192.168.100.3> EXEC /bin/sh -c '/usr/bin/python /home/vagrant/.ansible/tmp/ansible-tmp-1496294249.380864-253943902081895/ios_config.py; rm -rf "/home/vagrant/.ansible/tmp/ansible-tmp-1496294249.380864-253943902081895/" > /dev/null 2>&1 && sleep 0'
The full traceback is:
Traceback (most recent call last):
  File "/home/vagrant/venv/py3_convert/lib/python3.6/site-packages/ansible/executor/task_executor.py", line 125, in run
    res = self._execute()
  File "/home/vagrant/venv/py3_convert/lib/python3.6/site-packages/ansible/executor/task_executor.py", line 526, in _execute
    result = self._handler.run(task_vars=variables)
  File "/home/vagrant/venv/py3_convert/lib/python3.6/site-packages/ansible/plugins/action/ios_config.py", line 57, in run
    for key in result.keys():
RuntimeError: dictionary changed size during iteration
...

```

Fix in file /home/vagrant/venv/py3_convert/lib/python3.6/site-packages/ansible/plugins/action/ios_config.py line 57:
```
-        for key in result.keys():
+        for key in result.copy().keys():
```

### This error can be safely ignored if jtextfsm installed

```
(py3_convert) 
[~/pyneng_py3_convert/convert-pyneng-to-py3/examples/15_ansible/3_network_modules/ios_config/library]
vagrant@jessie-i386: [master|✚ 6…3] 
05:33 $ pip install ntc-ansible
Collecting ntc-ansible
  Downloading ntc-ansible-0.1.0.tar.gz
Collecting pynxos (from ntc-ansible)
  Downloading pynxos-0.0.3.tar.gz
Collecting pyntc (from ntc-ansible)
  Downloading pyntc-0.0.5.tar.gz
Requirement already satisfied: netmiko in /home/vagrant/venv/py3_convert/lib/python3.6/site-packages (from ntc-ansible)
Collecting requests>=2.7.0 (from pynxos->ntc-ansible)
  Downloading requests-2.17.3-py2.py3-none-any.whl (87kB)
    100% |████████████████████████████████| 92kB 725kB/s 
Collecting future (from pynxos->ntc-ansible)
  Downloading future-0.16.0.tar.gz (824kB)
    100% |████████████████████████████████| 829kB 234kB/s 
Collecting jsonschema (from pyntc->ntc-ansible)
  Downloading jsonschema-2.6.0-py2.py3-none-any.whl
Requirement already satisfied: paramiko in /home/vagrant/venv/py3_convert/lib/python3.6/site-packages (from pyntc->ntc-ansible)
Collecting coverage (from pyntc->ntc-ansible)
  Downloading coverage-4.4.1-cp36-cp36m-manylinux1_i686.whl (193kB)
    100% |████████████████████████████████| 194kB 762kB/s 
Collecting mock>=1.3 (from pyntc->ntc-ansible)
  Downloading mock-2.0.0-py2.py3-none-any.whl (56kB)
    100% |████████████████████████████████| 61kB 1.7MB/s 
Collecting terminal (from pyntc->ntc-ansible)
  Downloading terminal-0.4.0.tar.gz
Collecting textfsm==1.0.1 (from pyntc->ntc-ansible)
  Could not find a version that satisfies the requirement textfsm==1.0.1 (from pyntc->ntc-ansible) (from versions: 0.3.2)
No matching distribution found for textfsm==1.0.1 (from pyntc->ntc-ansible)

```
