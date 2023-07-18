import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)
    for player_nickname, player_info in players.items():
        email = player_info.get("email")
        bio = player_info.get("bio")
        race_ = player_info.get("race")
        skills_ = race_.get("skills")
        guild_ = player_info.get("guild")

        race, _ = Race.objects.get_or_create(
            name=race_.get("name"),
            description=race_.get("description")
        )

        for skill in skills_:
            Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race_id=race.id
            )

        if guild_:
            guild, _ = Guild.objects.get_or_create(
                name=guild_.get("name"),
                description=guild_.get("description")
            )
        else:
            guild = None

        Player.objects.create(
            nickname=player_nickname,
            email=email,
            bio=bio,
            guild=guild,
            race=race
        )


if __name__ == "__main__":
    main()
