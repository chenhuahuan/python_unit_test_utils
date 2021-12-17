import os,sys
import unittest
import pathlib

sys.path.append(os.path.join(pathlib.Path(__file__).parent.parent))

import dot_env


class TestLoader(unittest.TestCase):
    def test_load_custom_dot_env_file(self):
        dot_env_path = os.path.join(os.getcwd(), "test", "test.env")
        env_variables_mapping = dot_env.load_dot_env_file(dot_env_path)
        self.assertIn("PROJECT_KEY", env_variables_mapping)
        self.assertEqual(env_variables_mapping["UserName"], "test")
        self.assertEqual(
            env_variables_mapping["content_type"], "application/json; charset=UTF-8"
        )

if __name__ == "__main__":
    unittest.main()