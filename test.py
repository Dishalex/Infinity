import unittest
from main import add_phone_command

class TestMainFuncions(unittest.TestCase):

    def test_add_phone_command(self):

        args = ("Dima", [11111111111])
        result = add_phone_command(args)
        self.assertEqual(
            result, "A number 11111111111 has been added to a contact Dima")


if __name__ == "__main__":
    unittest.main()
