import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for nickname, player in players.items():
        race, created = Race.objects.get_or_create(
            name=player["race"]["name"],
            defaults={"description": player["race"]["description"]})
        for skill_data in player["race"]["skills"]:
            skill, created = Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={"bonus": skill_data["bonus"],
                          "race": race})
        if player.get("guild"):
            guild, created = Guild.objects.get_or_create(
                name=player["guild"]["name"],
                defaults={"description": player["guild"]["description"]}
            )
        else:
            guild = None
        player_model, created = Player.objects.get_or_create(
            nickname=nickname,
            defaults={"email": player["email"],
                      "bio": player["bio"],
                      "race": race,
                      "guild": guild}
        )


if __name__ == "__main__":
    main()
