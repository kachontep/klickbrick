import unittest
import subprocess


class TestHelloCommand(unittest.TestCase):
    def test_run_hello_command(self):
        proc = prog_run("klickbrick hello")
        self.assertEqual(proc.returncode, 0)
        self.assertEqual(proc.stdout, "Hello\n")

    def test_run_hello_command_with_name(self):
        proc = prog_run("klickbrick hello --name Ole")
        self.assertEqual(proc.returncode, 0)
        self.assertEqual(proc.stdout, "Hello Ole\n")


def prog_run(command: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, shell=True
    )
