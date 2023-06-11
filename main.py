import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for nickname, player in players_data.items():
        new_guild = None
        race_name = player["race"]["name"]
        race_description = player["race"]["description"]
        new_race, created = Race.objects.get_or_create(
            name=race_name,
            defaults={"description": race_description},
        )
        if player["guild"]:
            guild_name = player["guild"]["name"]
            guild_description = player["guild"]["description"]
            new_guild, created = Guild.objects.get_or_create(
                name=guild_name,
                defaults={"description": guild_description},
            )
        if player["race"]["skills"]:
            for skill in player["race"]["skills"]:
                skill_name = skill["name"]
                skill_bonus = skill["bonus"]
                if not Skill.objects.filter(name=skill_name).exists():
                    new_skill = Skill(
                        name=skill_name,
                        bonus=skill_bonus,
                        race=new_race
                    )
                    new_skill.save()

        new_player = Player(
            nickname=nickname,
            email=player["email"],
            bio=player["bio"],
            race=new_race,
            guild=new_guild
        )
        new_player.save()


if __name__ == "__main__":
    main()
