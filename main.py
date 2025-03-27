import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as all_players_values:
        all_players = json.load(all_players_values)

    for player in all_players:
        person = all_players[player]
        print(person)

        # RACE
        if person["race"] is not None:
            race = person["race"]
            race_name = race["name"]
            race_description = race["description"]

            if not Race.objects.all().filter(name=race_name):

                Race.objects.create(name=race_name,
                                    description=race_description)
                # SKILLS
                skills = person["race"]["skills"]

                for element in skills:
                    skill_name, bonus = element["name"], element["bonus"]
                    Skill.objects.create(name=skill_name, bonus=bonus,
                                         race=Race.objects.get(
                                             name=race_name))

        # GUILD
        if person["guild"] is not None:
            guild = person["guild"]
            guild_name = guild["name"]
            guild_description = guild["description"]

            if not Guild.objects.all().filter(name=guild_name):
                Guild.objects.create(name=guild_name,
                                     description=guild_description)

        # PLAYER
        nickname = player
        email = person["email"]
        bio = person["bio"]

        if not Player.objects.all().filter(nickname=nickname):
            if person["guild"] is not None:
                Player.objects.create(nickname=nickname, email=email, bio=bio,
                                      race=Race.objects.get(name=race_name),
                                      guild=Guild.objects.get(
                                          name=guild_name))
            else:
                Player.objects.create(nickname=nickname, email=email, bio=bio,
                                      race=Race.objects.get(name=race_name))


if __name__ == "__main__":
    main()
