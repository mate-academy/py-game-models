import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as json_file:
        players_dict = json.load(json_file)

    for nickname, info in players_dict.items():
        race_name = info.get("race", {}).get("name")
        race_description = info.get("race", {}).get(
            "description", "default description"
        )

        race, created = Race.objects.get_or_create(
            name=race_name,
            defaults={"description": race_description}
        )

        player = Player.objects.create(
            nickname=nickname,
            email=info.get("email"),
            bio=info.get("bio"),
            race=race
        )

        guild_info = info.get("guild")
        if guild_info:
            guild_name = guild_info.get("name")
            guild_description = guild_info.get("description")

            guild, created = Guild.objects.get_or_create(
                name=guild_name,
                defaults={"description": guild_description}
            )
            player.guild = guild
            player.save()

        race_skills = info.get("race", {}).get("skills", [])
        for skill in race_skills:
            Skill.objects.get_or_create(
                name=skill.get("name"),
                race=race,
                defaults={"bonus": skill.get("bonus")}
            )


if __name__ == "__main__":
    main()
