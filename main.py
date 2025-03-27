import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild
import json


def main() -> None:
    data = ""
    with open("players.json", "r") as player_file:
        data = json.load(player_file)
    for person in data:
        race, *args = Race.objects.get_or_create(
            name=data[person]["race"]["name"],
            description=data[person]["race"]["description"],
        )
        guild = None
        if data[person]["guild"]:
            guild, *args = Guild.objects.get_or_create(
                name=data[person]["guild"]["name"],
                description=data[person]["guild"]["description"],
            )
        player = Player.objects.create(
            nickname=person,
            email=data[person]["email"],
            bio=data[person]["bio"],
            race_id=race.id,
            guild_id=guild.id if guild else None,
        )
        for skill in data[person]["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"], bonus=skill["bonus"], race=player.race
            )


if __name__ == "__main__":
    main()
