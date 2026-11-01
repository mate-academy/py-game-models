import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


import json


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)
        for player in players:
            race = player["race"]["name"]
            player_race, created = Race.objects.get_or_create(name=race)
            skills = player["race"]["skills"]["name"]
            for skill in skills:
                player_skill = skill["name"]
                player_skill, created = Skill.objects.get_or_create(name=skill)

            player_skills, created = Skill.objects.get_or_create(name=skills)
            guild = player["guild"]["name"]
            player_guild, created = Guild.objects.get_or_create(name=guild)





# "arthur": {
#     "email": "arthur@gmail.com",
#     "bio": "Arthur, elf mag",
#     "race": {
#       "name": "elf",
#       "description": "The magic race",
#       "skills": [
#         {
#           "name": "Teleportation",
#           "bonus": "The ability to move so fast they look like they're teleporting. Could be considered to technically be Teleportation."
#         },
#         {
#           "name": "Reality Warping",
#           "bonus": "The ability to Warp Reality. Make the impossible become possible but can't warp anything containing the structure that holds everything together (Which are many creatures.)"
#         }
#       ]
#     },
#     "guild": {
#       "name": "mags",
#       "description": "A community of the elf mags"
#     }
#   },


if __name__ == "__main__":
    main()
