from __future__ import unicode_literals
from __future__ import print_function

from ciscoconfparse import CiscoConfParse


def confparse_parent(config, parent, child):
    """Returns [match, parent_line, child_line]

    Where match is boolean indicating whether a match happened.
    parent_line is the parent line that was matched
    child_line is the child line that was matched

    if match is false, then parent_line will be set, but not child_line.
    """
    results = []
    try:
        # ConfParse requires a list, not a string
        config = config.splitlines()
    except AttributeError:
        pass

    try:
        # Automatically handle if 'show run' from _command module
        config = config['stdout_lines'][0]
    except (KeyError, IndexError, TypeError):
        pass

    cfg_obj = CiscoConfParse(config)
    search_results = cfg_obj.find_objects(parent)
    for parent_line in search_results:
        child_results = parent_line.re_search_children(child)
        if child_results:
            if len(child_results) > 1:
                raise ValueError("Currently only a single child match is supported")
            results.append((True, parent_line.text, child_results[0].text))
        else:
            results.append((False, parent_line.text, None))

    return results


class FilterModule(object):
    def filters(self):
        return {
            'confparse_parent': confparse_parent,
        }


if __name__ == "__main__":

    # Test code
    with open("config.txt") as f:
        config = f.read()

    confparse_parent(config, parent=r"^interface", child=r"switchport access vlan 100")
