import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as file:
        players = json.load(file)
    for nickname, pdata in players.items():
        race_data = pdata["race"]
        race_obj, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data["description"]})

        guild_obj = None
        if pdata.get("guild"):
            guild_data = pdata["guild"]
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data["description"]}
            )

        skill_list = []
        for skill in race_data["skills"]:
            skill_obj, _ = Skill.objects.get_or_create(
                name=skill["name"],
                defaults={"bonus": skill["bonus"], "race": race_obj}
            )
            skill_list.append(skill_obj)

        player_obj, _ = Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": pdata["email"],
                "bio": pdata["bio"],
                "race": race_obj,
                "guild": guild_obj}
        )


if __name__ == "__main__":
    main()
