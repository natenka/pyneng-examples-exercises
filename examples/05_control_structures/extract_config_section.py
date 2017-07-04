
interface = ''
result = []
section = []


with open('r1_config.txt') as f:
    for line in f:
        if line.startswith('int'):
            interface = line
            if section:
                result.append(section)
            section=[]
            section.append(line)
        elif interface:
            section.append(line)

print(result)
