
import os
from loguru import logger

def set_os_environ(variables_mapping):
    """ set variables mapping to os.environ
    """
    for variable in variables_mapping:
        os.environ[variable] = variables_mapping[variable]
        logger.debug(f"Set OS environment variable: {variable}")

def load_dot_env_file(dot_env_path):
    """ load .env file.

    Args:
        dot_env_path (str): .env file path

    Returns:
        dict: environment variables mapping

            {
                "UserName": "debugtalk",
                "Password": "123456",
                "PROJECT_KEY": "ABCDEFGH"
            }

    Raises:
        exceptions.FileFormatError: If .env file format is invalid.

    """
    if not os.path.isfile(dot_env_path):
        return {}

    logger.info(f"Loading environment variables from {dot_env_path}")
    env_variables_mapping = {}

    with open(dot_env_path, mode="rb") as fp:
        for line in fp:
            # maxsplit=1
            if b"=" in line:
                variable, value = line.split(b"=", 1)
            elif b":" in line:
                variable, value = line.split(b":", 1)
            else:
                raise exceptions.FileFormatError(".env format error")

            env_variables_mapping[
                variable.strip().decode("utf-8")
            ] = value.strip().decode("utf-8")

    set_os_environ(env_variables_mapping)
    return env_variables_mapping




# load_dot_env_file("test/test.env")
# print(os.environ.get("aaa", None))
# print(os.environ["PROJECT_KEY"])
# print(os.environ["aaa"])
# print(os.environ["PROJECT_KEY"])


