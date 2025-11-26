import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    file_json = ""
    with open("players.json") as file:
        file_json = json.load(file)

    for player in file_json:
        race, _ = Race.objects.get_or_create(
            name=file_json[player]["race"]["name"],
            description=file_json[player]["race"]["description"]
        )
        for skills_json in file_json[player]["race"]["skills"]:
            skill, _ = Skill.objects.get_or_create(
                name=skills_json["name"],
                bonus=skills_json["bonus"],
                race=race
            )
        guild = None
        if file_json[player]["guild"]:
            guild, _ = Guild.objects.get_or_create(
                name=file_json[player]["guild"]["name"],
                description=file_json[player]["guild"]["description"]
            )

        Player.objects.get_or_create(
            nickname=player,
            email=file_json[player]["email"],
            bio=file_json[player]["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
