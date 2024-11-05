import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        players = json.load(players_file)

        for player_name, player_info in players.items():
            race_data = player_info["race"]
            race, created = Race.objects.get_or_create(
                name=race_data["name"],
                defaults={"description": race_data["description"]})
            for skill_data in race_data["skills"]:
                Skill.objects.get_or_create(
                    name=skill_data["name"],
                    defaults={"bonus": skill_data["bonus"], "race": race})
            guild = None
            if player_info["guild"]:
                guild_data = player_info["guild"]
                guild, created = Guild.objects.get_or_create(
                    name=guild_data["name"],
                    defaults={"description": guild_data["description"]}
                )

            Player.objects.get_or_create(nickname=player_name,
                                         defaults={
                                             "email": player_info["email"],
                                             "bio": player_info["bio"],
                                             "race": race,
                                             "guild": guild,
                                         })
            

if __name__ == "__main__":
    main()
