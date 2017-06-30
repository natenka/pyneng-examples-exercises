# -*- coding: utf-8 -*-
import argparse

# Default values:
DFLT_DB_NAME = 'dhcp_snooping.db'
DFLT_DB_SCHEMA = 'dhcp_snooping_schema.sql'


def create(args):
    print "Creating DB %s with DB schema %s" % (args.name, args.schema)


def add(args):
    if args.sw_true:
        print "Adding switch data to database"
    else:
        print "Reading info from file(s) \n%s" % ', '.join( args.filename )
        print "\nAdding data to db %s" % args.db_file


def get(args):
    if args.key and args.value:
        print "Geting data from DB: %s" % args.db_file
        print "Request data for host(s) with %s %s" % (args.key, args.value)
    elif args.key or args.value:
        print "Please give two or zero args\n"
        print show_subparser_help('get')
    else:
        print "Showing %s content..." % args.db_file


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(title='subcommands',
                                   description='valid subcommands',
                                   help='description')


create_parser = subparsers.add_parser('create_db', help='create new db')
create_parser.add_argument('-n', metavar='db-filename', dest='name',
                           default=DFLT_DB_NAME, help='db filename')
create_parser.add_argument('-s', dest='schema', default=DFLT_DB_SCHEMA,
                           help='db schema filename')
create_parser.set_defaults( func=create )


add_parser = subparsers.add_parser('add', help='add data to db')
add_parser.add_argument('filename', nargs='+', help='file(s) to add to db')
add_parser.add_argument('--db', dest='db_file', default=DFLT_DB_NAME, help='db name')
add_parser.add_argument('-s', dest='sw_true', action='store_true',
                        help='add switch data if set, else add normal data')
add_parser.set_defaults( func=add )


get_parser = subparsers.add_parser('get', help='get data from db')
get_parser.add_argument('--db', dest='db_file', default=DFLT_DB_NAME, help='db name')
get_parser.add_argument('-k', dest="key",
                        choices=['mac', 'ip', 'vlan', 'interface', 'switch'],
                        help='host key (parameter) to search')
get_parser.add_argument('-v', dest="value", help='value of key')
get_parser.add_argument('-a', action='store_true', help='show db content')
get_parser.set_defaults( func=get )



if __name__ == '__main__':
    args = parser.parse_args()
    args.func(args)

