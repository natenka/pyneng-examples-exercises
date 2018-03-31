"""
Filter to convert results from network device show commands obtained from ios_command,
eos_command, et cetera to structured data using TextFSM templates.
"""
#from __future__ import unicode_literals
#from __future__ import print_function
#from textfsm.clitable import CliTableError
#import textfsm.clitable as clitable

import os
from clitable import CliTableError
import clitable


def get_template_dir():
    """Find and return the ntc-templates/templates dir."""
    try:
        template_dir = os.environ['NET_TEXTFSM']
        index = os.path.join(template_dir, 'index')
        if not os.path.isfile(index):
            # Assume only base ./ntc-templates specified
            template_dir = os.path.join(template_dir, 'templates')
    except KeyError:
        # Construct path ~/ntc-templates/templates
        home_dir = os.path.expanduser("~")
        template_dir = os.path.join(home_dir, 'ntc-templates', 'templates')

    index = os.path.join(template_dir, 'index')
    if not os.path.isdir(template_dir) or not os.path.isfile(index):
        msg = """
Valid ntc-templates not found, please install https://github.com/networktocode/ntc-templates
and then set the NET_TEXTFSM environment variable to point to the ./ntc-templates/templates
directory."""
        raise ValueError(msg)
    return template_dir


def get_structured_data(raw_output, platform, command):
    """Convert raw CLI output to structured data using TextFSM template."""
    template_dir = get_template_dir()
    index_file = 'index'#CHANGED
    textfsm_obj = clitable.CliTable(index_file, template_dir)
    attrs = {'Command': command, 'Platform': platform}
    try:
        # Parse output through template
        textfsm_obj.ParseCmd(raw_output, attrs)
        return clitable_to_dict(textfsm_obj)
    except CliTableError:
        return raw_output


def clitable_to_dict(cli_table):
    """Converts TextFSM cli_table object to list of dictionaries."""
    objs = []
    for row in cli_table:
        temp_dict = {}
        for index, element in enumerate(row):
            temp_dict[cli_table.header[index].lower()] = element
        objs.append(temp_dict)
    return objs


def net_textfsm_parse(output, platform, command):
    """Process config find interfaces using ip helper."""
    try:
        output = output['stdout'][0]
    except (KeyError, IndexError, TypeError):
        pass
    return get_structured_data(output, platform, command)


class FilterModule(object):
    """Filter to convert results from network device show commands obtained from ios_command,
    eos_command, et cetera to structured data using TextFSM templates."""
    def filters(self):
        return {
            'net_textfsm_parse': net_textfsm_parse,
        }


if __name__ == "__main__":

    # Test code
    pass
