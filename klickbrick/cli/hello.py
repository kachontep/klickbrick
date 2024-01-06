from .klickbrick import klickbrick


def hello(args):
    print((f"Hello {args.name}" if args.name else "Hello"))


subparsers = klickbrick.add_subparsers(
    title="subcommands", description="greeting words"
)

hello_parser = subparsers.add_parser("hello", help="Hello with someone")
hello_parser.add_argument("--name", type=str, required=False)
hello_parser.set_defaults(func=hello)
