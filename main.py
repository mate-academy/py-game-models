import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as json_file:
        data = json.load(json_file)
    if Race.objects.exists():
        Race.objects.all().delete()
    if Skill.objects.exists():
        Skill.objects.all().delete()
    if Guild.objects.exists():
        Guild.objects.all().delete()
    if Player.objects.exists():
        Player.objects.all().delete()

    for player in data:
        current_player = data[player]
        if current_player.get("guild") is not None:
            fields = {
                "name": current_player["guild"]["name"],
                "description": current_player["guild"]["description"],
            }
            guild, _ = Guild.objects.get_or_create(
                **{
                    k: v for k, v in fields.items() if v is not None
                }
            )
        else:
            guild = None
        if current_player.get("race") is not None:
            race, _ = Race.objects.get_or_create(
                name=current_player["race"]["name"],
                description=current_player["race"]["description"],
            )
        else:
            race = None
        for skill in current_player["race"]["skills"]:
            kwargs = {
                "name": skill["name"],
                "bonus": skill["bonus"],
                "race": race,
            }
            Skill.objects.get_or_create(
                **{
                    k: v for k, v in kwargs.items() if v is not None
                }
            )

        kwargs = {
            "nickname": player,
            "email": current_player["email"],
            "bio": current_player["bio"],
            "race": race,
            "guild": guild,
        }
        player = Player(
            **{
                k: v for k, v in kwargs.items() if v is not None
            }
        )
        player.save()


if __name__ == "__main__":
    main()
