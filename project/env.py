from dataclasses import dataclass
from os import environ
from typing import Literal, TypeAlias

db_config: TypeAlias = dict[Literal["ENGINE", "NAME", "USER", "PASSWORD", "HOST", "PORT"], str]


@dataclass
class Enviroment:
    NAME: str
    SECRET_KEY: str
    DEBUG: bool
    ALLOWED_HOSTS: list[str]

    # database
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str

    def get_db_config(self) -> db_config:
        return {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": self.DB_NAME,
            "USER": self.DB_USER,
            "PASSWORD": self.DB_PASSWORD,
            "HOST": self.DB_HOST,
            "PORT": self.DB_PORT,
        }

def __get_env_name() -> str:
    try:
        return environ["ENV"]
    except KeyError as e:
        raise KeyError("Global variable 'ENV' not especified") from e

def __get_env_config() -> Enviroment:
    env = __get_env_name()
    if env == "dev":
        return Enviroment(
            NAME="dev",
            SECRET_KEY="dev",
            DEBUG=True,
            ALLOWED_HOSTS=environ["ALLOWED_HOSTS"].split(),
            DB_NAME=environ["DB_NAME"],
            DB_USER=environ["DB_USER"],
            DB_PASSWORD=environ["DB_PASSWORD"],
            DB_HOST=environ["DB_HOST"],
            DB_PORT=environ["DB_PORT"],
        )
    elif env == "staging":
        return Enviroment(
            NAME="staging",
            SECRET_KEY=environ["SECRET_KEY"],
            DEBUG=True,
            ALLOWED_HOSTS=environ["ALLOWED_HOSTS"].split(),
            DB_NAME=environ["DB_NAME"],
            DB_USER=environ["DB_USER"],
            DB_PASSWORD=environ["DB_PASSWORD"],
            DB_HOST=environ["DB_HOST"],
            DB_PORT=environ["DB_PORT"],
        )
    elif env == "prod":
        return Enviroment(
            NAME="prod",
            SECRET_KEY=environ["SECRET_KEY"],
            DEBUG=False,
            ALLOWED_HOSTS=environ["ALLOWED_HOSTS"].split(),
            DB_NAME=environ["DB_NAME"],
            DB_USER=environ["DB_USER"],
            DB_PASSWORD=environ["DB_PASSWORD"],
            DB_HOST=environ["DB_HOST"],
            DB_PORT=environ["DB_PORT"],
        )
    else:
        raise KeyError(f"Global (ENV={env}) is not mapped")

CONFIG = __get_env_config()
