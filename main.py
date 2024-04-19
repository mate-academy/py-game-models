import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)

    for player_name, player_data in data.items():
        # Creating race with desc
        race_name = player_data["race"]["name"]
        race, _ = Race.objects.get_or_create(
            name=race_name,
            defaults={"description": player_data["race"]["description"]}
        )

        #  Creating guild if there is a guild in json or setting None value
        if player_data["guild"]:
            guild_name = player_data["guild"]["name"]
            guild, _ = Guild.objects.get_or_create(
                name=guild_name,
                defaults={"description": player_data["guild"]["description"]}
            )
        else:
            guild = None

        # Create and push player to DB
        player = Player(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild
        )
        player.save()
        # Add skill to race
        for skill_data in player_data["race"]["skills"]:
            skill_name = skill_data["name"]
            skill_bonus = skill_data["bonus"]
            skill, _ = Skill.objects.get_or_create(
                name=skill_name,
                bonus=skill_bonus,
                race=race
            )
            race.skill_set.add(skill)


if __name__ == "__main__":
    main()
