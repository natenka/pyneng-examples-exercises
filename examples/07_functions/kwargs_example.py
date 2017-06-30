def config_to_list(cfg_file, delete_excl=True,
                   delete_empty=True, strip_end=True):
    result = []
    with open( cfg_file ) as f:
        for line in f:
            if strip_end:
                line = line.rstrip()
            if delete_empty and not line:
                pass
            elif delete_excl and line.startswith('!'):
                pass
            else:
                result.append(line)
    return result


def clear_cfg_and_write_to_file(cfg, to_file, **kwargs):
    cfg_as_list = config_to_list(cfg, **kwargs)
    with open(to_file, 'w') as f:
        f.write('\n'.join(cfg_as_list))
