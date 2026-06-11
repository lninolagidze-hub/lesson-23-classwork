import unittest
from main import get_allowed_users, register_user


class Testing(unittest.TestCase):

    def test_1(self):
        result = register_user("John")
        self.assertIn(result, get_allowed_users())

    def test_2(self):
        allowed_users = get_allowed_users()

        self.assertIn("john", allowed_users)
        self.assertIn("alice", allowed_users)
        self.assertNotIn("dato", allowed_users)


if __name__ == "__main__":
    unittest.main()
