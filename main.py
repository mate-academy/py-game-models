import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def load_json_data() -> dict:
    with open("players.json", "r") as content_file:
        return json.load(content_file)


def main() -> None:
    players_data = load_json_data()

    for player, data in players_data.items():

        email, bio, race, guild = data.values()
        name, description, skills = race.values()
        player_race, _ = Race.objects.get_or_create(
            name=name,
            description=description,
        )

        if skills:
            for skill in skills:
                player_skill, _ = Skill.objects.get_or_create(
                    **skill,
                    race=player_race
                )

        player_guild = None

        if guild:
            player_guild, _ = Guild.objects.get_or_create(
                name=guild["name"],
                description=guild["description"]
            )

        Player.objects.get_or_create(
            nickname=player,
            email=email,
            bio=bio,
            race=player_race,
            guild=player_guild
        )


if __name__ == "__main__":
    main()
