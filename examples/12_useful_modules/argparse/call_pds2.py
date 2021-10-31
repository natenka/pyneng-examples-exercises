from parse_dhcp_snooping import parser

args = parser.parse_args('add test.txt test2.txt'.split())
args.func(args)
