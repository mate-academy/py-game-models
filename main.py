import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)

    for nickname, player_data in data.items():
        new_race, _ = Race.objects.get_or_create(
            name=player_data["race"]["name"],
            defaults={"description": player_data["race"]["description"]}
        )

        for skill in player_data["race"]["skills"]:
            if skill.get("name"):
                new_skil, _ = Skill.objects.get_or_create(
                    name=skill["name"],
                    defaults={"bonus": skill["bonus"], "race": new_race}
                )

        if player_data.get("guild"):
            new_guild, _ = Guild.objects.get_or_create(
                name=player_data["guild"]["name"],
                defaults={"description": player_data["guild"]["description"]}
            )
        else:
            new_guild = None

        Player.objects.create(
            nickname=nickname,
            email=(player_data["email"]),
            bio=(player_data["bio"]),
            race=new_race,
            guild=new_guild,
        )


if __name__ == "__main__":
    main()
