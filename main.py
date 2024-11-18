import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players_set = json.load(f)
    print(players_set)

    for user, info_user in players_set.items():

        race = Race.objects.get_or_create(name=info_user["race"]["name"],
                                          description=info_user["race"]["description"])

        for skill in info_user.get("skills", []):
            skill = Skill.objects.get_or_create(name=skill["name"],
                                                bonus=skill["bonus"],
                                                race=race
                                                )
        guild = None
        if info_user.get("guild"):
            guild = Guild.objects.get_or_create(name=info_user["guild"]["name"],
                                                description=info_user["guild"]["description"]
                                                )

        player = Player.objects.get_or_create(nickname=user,
                                              email=info_user["email"],
                                              bio=info_user["bio"],
                                              race=race,
                                              guild=guild
                                              )

        # print(player)


if __name__ == "__main__":
    main()
