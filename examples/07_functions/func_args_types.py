def cfg_to_list(cfg_file, delete_exclamation):
    result = []
    with open( cfg_file ) as f:
        for line in f:
            if delete_exclamation and line.startswith('!'):
                pass
            else:
                result.append(line.rstrip())
    return result

print cfg_to_list('r1.txt', False)

print cfg_to_list(delete_exclamation=False, cfg_file='r1.txt')
