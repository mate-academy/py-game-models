import init_django_orm  # noqa: F401

from db.models import Race, Guild, Skill, Player  # noqa: F401

from create_funcs.create_player import create_player
from players_json import players_data


def main() -> None:
    create_player(players_data)


if __name__ == "__main__":
    main()
