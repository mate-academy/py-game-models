import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for nickname, details in data.items():
        race_data = details.get("race")
        guild_data = details.get("guild")

        race, _ = Race.objects.get_or_create(
            name=race_data.get("name"),
            description=race_data.get("description"),
        )

        if skill_details := race_data.get("skills"):
            for skill_data in skill_details:
                skill, _ = Skill.objects.get_or_create(
                    name=skill_data.get("name"),
                    bonus=skill_data.get("bonus"),
                    race=race,
                )
                race.skill_set.add(skill)

        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                description=guild_data.get("description"),
            )
        else:
            guild = None

        player, _ = Player.objects.get_or_create(
            nickname=nickname,
            email=details.get("email"),
            bio=details.get("bio"),
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
