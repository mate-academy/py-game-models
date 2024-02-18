import init_django_orm  # noqa: F401

from db.models import Race, Guild, Skill, Player  # noqa: F401

from create_funcs.create_race import create_race
from create_funcs.create_skill import create_skill
from create_funcs.create_guild import create_guild
from create_funcs.create_player import create_player


def main() -> None:
    create_race()
    create_skill()
    create_guild()
    create_player()


if __name__ == "__main__":
    main()
