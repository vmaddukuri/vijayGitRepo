import unittest
from pssshclient import CustomSSHClient
from psemployee import Employee


def power(x, n):
    return x ** n


class CustomTestCase(unittest.TestCase):
    def test_power(self):
        self.assertEqual(power(2, 3), 8)

    def test_power_failure(self):
        self.assertNotEqual(power(2, 3), 9)


class TestCaseEmployee(unittest.TestCase):
    def test_employee(self):
        e = Employee('v4004', 'a', 'b')
        self.assertIs(type(e), Employee)


@unittest.skip
class TestCaseSSHClient(unittest.TestCase):
    def test_ssh_client(self):
        ssh = CustomSSHClient('localhost', 22, 'training', 'training')
        op = ssh.check_output('whoami')
        self.assertIn('training', op)


if __name__ == '__main__':
    unittest.main()
