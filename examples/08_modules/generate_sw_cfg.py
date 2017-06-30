from sw_data import sw1_fast_int
from generate_sw_int_cfg import generate_access_cfg
#from generate_sw_int_cfg2 import generate_access_cfg
from sw_cfg_templates import basic_cfg, lines_cfg


print basic_cfg
print '\n'.join(generate_access_cfg(sw1_fast_int))
print lines_cfg

