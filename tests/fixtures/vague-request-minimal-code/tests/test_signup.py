import unittest

import signup


class SignupTests(unittest.TestCase):
    def setUp(self):
        signup.reset()

    def test_register_stores_account(self):
        record = signup.register("ada", "ada@example.com", "correct horse")
        self.assertEqual(record["username"], "ada")


if __name__ == "__main__":
    unittest.main()
