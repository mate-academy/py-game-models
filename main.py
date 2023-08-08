import json

import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def wipe() -> None:  # TODO: delete
    Race.objects.all().delete()
    Skill.objects.all().delete()
    Guild.objects.all().delete()
    Player.objects.all().delete()


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)
    for player, details in data.items():  # dict




        race_details = data[player]["race"]  # race, not name
        skill_details = race_details["skills"]  # skill, not name
        # print(guild_details)
        # print(race_details)
        # print(skill_details)

        if not Race.objects.filter(name=race_details["name"]).exists():
            # print(f"we need to add {race_details['name']}")
            Race.objects.create(
                name=race_details["name"],
                description=race_details["description"]
            )
        current_race = Race.objects.get(name=race_details["name"]).id

        for skill in skill_details:
            #print(skill["name"])
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race_id=current_race
                )
        current_guild = data[player]["guild"]
        if current_guild is not None:
            print("NOT NONE")
            print(current_guild)
            if not Guild.objects.filter(name=current_guild["name"]).exists():
                Guild.objects.create(
                    name=current_guild["name"],
                    description=current_guild["description"]
                )
            current_guild = Guild.objects.get(name=current_guild["name"]).id
        print(current_guild)
        new_player = Player.objects.create(
            nickname=str(player).capitalize(),  # capitalize?
            email=data[player]["email"],
            bio=data[player]["bio"],
            race_id=current_race,
            guild_id=current_guild,
        )
        new_player.save() # looks like i don't need it


if __name__ == "__main__":
    wipe()
    main()
