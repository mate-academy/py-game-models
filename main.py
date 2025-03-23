import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def load_data() -> dict:
    with open("players.json", "r") as file:
        return json.load(file)


def main() -> None:
    players_data = load_data()
    for player, data in players_data.items():
        email, bio, race, guild = data.values()
        name, description, skills = race.values()
        player_race, race_is_created = Race.objects.get_or_create(
            name=name, description=description
        )

        if race_is_created:
            for skill in skills:
                skill_name, _ = Skill.objects.get_or_create(
                    **skill, race=player_race
                )

        if guild:
            player_guild, _ = Guild.objects.get_or_create(
                name=guild["name"], description=guild["description"]
            )

            Player.objects.get_or_create(
                nickname=player,
                email=email,
                bio=bio,
                race=player_race,
                guild=player_guild if guild else None
            )
