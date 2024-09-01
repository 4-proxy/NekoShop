# -*- coding: utf-8 -*-

__all__: list[str] = ["load_and_get_env_key_value"]

import prototypes.external_scripts.env_handler as env_handler


# ----------------------------------------------------------------------------
def load_and_get_env_key_value(filepath: str, environment_key: str) -> str:
    """load_and_get_env_key_value returns the received value from the virtual environment.

    The function is intended for loading `.env` file into the current virtual environment,
    for further attempt to get the value by the specified key.

    Args:
        filepath (str): path to the file storing the token.
        environment_key (str): the name of the key in the file and virtual environment.

    Raises:
        EnvironmentError: Raises if key loading fails.

    Returns:
        str: the value of the key retrieved from the virtual environment.
    """
    if env_handler.load_env_file(filepath=filepath):
        key_value: str = env_handler.get_key_value_from_environment(key=environment_key)
    else:
        raise EnvironmentError(
            f"Uploading the env file to the virtual environment failed using the path: {filepath}"
        )

    return key_value
