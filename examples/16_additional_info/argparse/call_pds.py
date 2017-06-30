from parse_dhcp_snooping import parser

args = parser.parse_args()
args.func(args)

