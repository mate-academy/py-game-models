import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        players = json.load(players_file)
        for nickname, data in players.items():
            race, _ = Race.objects.get_or_create(
                name=data["race"]["name"],
                defaults={"description": data["race"]["description"]}
            )
            for skill in data["race"]["skills"]:
                skill, _ = Skill.objects.get_or_create(
                    name=skill["name"],
                    defaults={"bonus": skill["bonus"]},
                    race=race
                )

            if data.get("guild"):
                guild, _ = Guild.objects.get_or_create(
                    name=data.get("guild")["name"],
                    defaults={"description": data.get("guild")["description"]}
                )
            else:
                guild = None

            player, _ = Player.objects.get_or_create(
                nickname=nickname,
                defaults={"email": data["email"],
                          "bio": data["bio"],
                          "race": race,
                          "guild": guild}
            )


if __name__ == "__main__":
    main()
