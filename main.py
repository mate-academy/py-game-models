import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db import IntegrityError


def main() -> None:
    with open("players.json", "r") as players:
        data = json.load(players)

    for nickname, abilities in data.items():
        race = get_or_create_race(abilities)
        guild = get_or_create_guild(abilities)
        create_skills(abilities, race)
        create_player(nickname, abilities, race, guild)


def get_or_create_race(user_info: dict) -> Race | None:
    try:
        race, _ = Race.objects.get_or_create(
            name=user_info["race"]["name"],
            description=user_info["race"]["description"]
        )
    except KeyError as e:
        print(f"KeyError: Missing key {e} in user_info")
        return None
    except IntegrityError as e:
        print(f"IntegrityError: {e}")
        return None
    except ValidationError as e:
        print(f"ValidationError: {e}")
        return None
    except ObjectDoesNotExist as e:
        print(f"DoesNotExist Error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None
    return race


def get_or_create_guild(user_info: dict) -> Guild | None:
    guild = None
    if guild_info := user_info["guild"]:
        try:
            guild, _ = Guild.objects.get_or_create(
                name=guild_info["name"],
                description=guild_info["description"],
            )
        except KeyError as e:
            print(f"KeyError: Missing key {e} in user_info")
            return None
        except IntegrityError as e:
            print(f"IntegrityError: {e}")
            return None
        except ValidationError as e:
            print(f"ValidationError: {e}")
            return None
        except ObjectDoesNotExist as e:
            print(f"DoesNotExist Error: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None
    return guild


def create_skills(user_info: dict, race: Race) -> None:
    try:
        for skill in user_info["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race,
            )
    except KeyError as e:
        print(f"KeyError: Missing key {e} in user_info")
        return None
    except IntegrityError as e:
        print(f"IntegrityError: {e}")
        return None
    except ValidationError as e:
        print(f"ValidationError: {e}")
        return None
    except ObjectDoesNotExist as e:
        print(f"DoesNotExist Error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None


def create_player(nickname: str, user_info: dict,
                  race: Race, guild: Guild) -> None:
    try:
        Player.objects.get_or_create(
            nickname=nickname,
            email=user_info["email"],
            bio=user_info["bio"],
            race=race,
            guild=guild,
        )
    except KeyError as e:
        print(f"KeyError: Missing key {e} in user_info")
        return None
    except IntegrityError as e:
        print(f"IntegrityError: {e}")
        return None
    except ValidationError as e:
        print(f"ValidationError: {e}")
        return None
    except ObjectDoesNotExist as e:
        print(f"DoesNotExist Error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None


if __name__ == "__main__":
    main()
