import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        dados_json = json.load(file)

    for nickname, dados in dados_json.items():
        race_data = dados.get("race")

        if race_data:
            race, _ = Race.objects.get_or_create(
                name=race_data.get("name"),
                defaults={"description": race_data.get("description")},
            )

            for skill_data in race_data.get("skills", []):
                Skill.objects.get_or_create(
                    name=skill_data.get("name"),
                    bonus=skill_data.get("bonus"),
                    race=race,
                )
        else:
            race = None

        guild_data = dados.get("guild")
        if guild_data:
            desc = guild_data.get("description")
            guild, _ = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                defaults={"description": desc},
            )
        else:
            guild = None

        Player.objects.create(
            nickname=nickname,
            email=dados.get("email"),
            bio=dados.get("bio"),
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
