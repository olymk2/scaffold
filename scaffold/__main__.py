from scaffold.builder.__main__ import main as builder_main
from scaffold.core.data.migrations import export_schema, import_schema
import argparse

parser = argparse.ArgumentParser(description='Export database scheme or import the scheme')
parser.add_argument("--verbose", action='store_true', default='False')

sub_parser = parser.add_subparsers(help='Options', dest='cmd')
build_parsers = sub_parser.add_parser("init")
build_parsers.add_argument("--name", help='Project name')
build_parsers.add_argument("--path", help="Project path")

#~ build_parsers = sub_parser.add_parser("update")

build_parsers = sub_parser.add_parser("minify")
build_parsers.add_argument("--source", help='Folder to scan for content')
build_parsers.add_argument("--target", help="Folder to output minified content")

migrate_parsers = sub_parser.add_parser("migrate")
#~ migrate_parsers.add_argument("--install", action='store_true')
migrate_parsers.add_argument('--database', action='store_const', const=sum, default=None, help='database name')
migrate_parsers.add_argument('--username', action='store_const', const=sum, default=None, help='database username')
migrate_parsers.add_argument('--password', action='store_const', const=sum, default=None, help='database password')
migrate_parsers.add_argument('--host', action='store_const', const=sum, default=None, help='database host')
migrate_parsers.add_argument('--db', action='store_const', const=sum, default=None, help='')
migrate_parsers.add_argument('--port', action='store_const', const=sum, default=3306, help='')
#~ migrate_parsers.add_argument('--export', action='store_const', const=sum, default=False, help='Generate migrations')

migrate_parsers = sub_parser.add_parser("import")
#~ migrate_parsers.add_argument("--install", action='store_true')
migrate_parsers.add_argument('--database', action='store_const', const=sum, default=None, help='database name')
migrate_parsers.add_argument('--username', action='store_const', const=sum, default=None, help='database username')
migrate_parsers.add_argument('--password', action='store_const', const=sum, default=None, help='database password')
migrate_parsers.add_argument('--host', action='store_const', const=sum, default=None, help='database host')
migrate_parsers.add_argument('--db', action='store_const', const=sum, default=None, help='')
migrate_parsers.add_argument('--port', action='store_const', const=sum, default=3306, help='')

args = parser.parse_args()


if args.cmd in ('init', 'mason'):
    builder_main(args)
    
if args.cmd in ('update', 'architect'):
    builder_main(args)
    
if args.cmd in ('minify', 'decorator'):
    builder_main(args)

if args.cmd in ('import', 'construct'):
    import_schema(args)

if args.cmd in ('migrate', 'deconstruct'):
    export_schema(args)


