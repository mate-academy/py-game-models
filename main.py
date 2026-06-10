import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild

JSON_FILENAME = "players.json"


def main() -> None:
    with open(JSON_FILENAME) as f:
        player_data = json.load(f)

    for name, player_dict in player_data.items():
        guild_dict = player_dict.get("guild")
        if guild_dict:
            guild, _ = Guild.objects.get_or_create(
                name=guild_dict.get("name"),
                description=guild_dict.get("description")
            )
            guild.save()
        else:
            guild = None

        race_dict = player_dict["race"]
        race, _ = Race.objects.get_or_create(
            name=race_dict["name"],
            description=race_dict.get("description", "")
        )
        race.save()

        for skill_dict in race_dict.get("skills", []):
            skill, _ = Skill.objects.get_or_create(
                name=skill_dict["name"],
                bonus=skill_dict["bonus"],
                race=race
            )
            skill.save()

        player = Player.objects.create(
            nickname=name,
            email=player_dict["email"],
            bio=player_dict["bio"],
            race=race,
            guild=guild,
        )
        player.save()


if __name__ == "__main__":
    main()
