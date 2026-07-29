import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)

    for nickname, player_data in data.items():
        new_race, _ = Race.objects.get_or_create(
            name=player_data.get("race", {}).get("name"),
            defaults={
                "description": player_data.
                get("race", {}).get("description")}
        )

        for skill in player_data.get("race", {}).get("skills", []):
            if skill.get("name"):
                new_skill, _ = Skill.objects.get_or_create(
                    name=skill.get("name"),
                    defaults={"bonus": skill.get("bonus"), "race": new_race}
                )

        if player_data.get("guild"):
            new_guild, _ = Guild.objects.get_or_create(
                name=player_data.get("guild", {}).get("name"),
                defaults={
                    "description": player_data.get("guild", {}).
                    get("description")}
            )
        else:
            new_guild = None

        Player.objects.create(
            nickname=nickname,
            email=player_data.get("email"),
            bio=player_data.get("bio"),
            race=new_race,
            guild=new_guild,
        )


if __name__ == "__main__":
    main()
