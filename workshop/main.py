import argparse
import sys
from src import c_course, cpp_course



def init_task(task: c_course.BaseTaskClass):
    print(task.init_task())


def check_task(task: c_course.BaseTaskClass):
    passed, msg = task.check()
    print("Passed:", passed)
    print(msg)
    if passed:
        sys.exit(0)

    sys.exit(1)


def dry_run_task(task: c_course.BaseTaskClass):
    task.generate_task()
    task._generate_tests()
    for i, test in enumerate(task.tests):
        print(f"TEST #{i + 1}:\n\t{test}")
    sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(required=True)

    for cli_parser in c_course.PARSERS:
        task_parser = subparsers.add_parser(cli_parser.name)
        cli_parser.add_cli_args(task_parser)

    # Регистратор для cpp задачек
    for cli_parser in cpp_course.PARSERS:
        task_parser = subparsers.add_parser(cli_parser.name)
        cli_parser.add_cli_args(task_parser)

    args = parser.parse_args()
    task = args.func(args)
    match args.mode:
        case "init":
            init_task(task)
        case "check":
            check_task(task)
        case "dry-run":
            dry_run_task(task)
