import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    try:
        with open("players.json", "r") as plfl:
            players_data = json.load(plfl)
        for player_name in players_data:
            race, _ = Race.objects.get_or_create(
                name=players_data[player_name]["race"]["name"],
                description=players_data[player_name][
                    "race"]["description"]
            )
            for skill_data in players_data[player_name][
                    "race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skill_data["name"],
                    bonus=skill_data["bonus"],
                    race=race
                )
            guild_data = players_data[player_name].get("guild")

            if guild_data:
                guild, _ = Guild.objects.get_or_create(
                    name=players_data[player_name]["guild"]["name"],
                    description=players_data[
                        player_name]["guild"]["description"])
            else:
                guild = None
            Player.objects.get_or_create(
                nickname=player_name,
                email=players_data[player_name]["email"],
                bio=players_data[player_name]["bio"],
                race=race,
                guild=guild
            )
    except Exception as Ex: # noqa
        pass


if __name__ == "__main__":
    main()
