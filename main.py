import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for nickname, data in players.items():
        data_race = data.get("race")
        race, _ = Race.objects.get_or_create(
            name=data_race.get("name"),
            defaults={"description": data_race.get("description")}
        )

        data_skill = data_race.get("skills")
        for skill in data_skill:
            skill, _ = Skill.objects.get_or_create(
                name=skill.get("name"),
                defaults={"bonus": skill.get("bonus"), "race": race}
            )

        data_guild = data.get("guild")
        guild = None
        if data_guild is not None:
            guild, _ = Guild.objects.get_or_create(
                name=data_guild.get("name"),
                defaults={"description": data_guild.get("description")}
            )

        player, _ = Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": data.get("email"),
                "bio": data.get("bio"),
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()
