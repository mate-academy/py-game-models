import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as player_file:
        players_data = json.load(player_file)

    for player in players_data.keys():
        race_obj, created = Race.objects.get_or_create(
            name=players_data[player]["race"]["name"],
            description=players_data[player]["race"]["description"]
        )
        for skill in players_data[player]["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race_id=race_obj.pk
            )
        guild_data = players_data[player].get("guild")
        if guild_data:
            guild_obj, created = Guild.objects.get_or_create(
                name=players_data[player]["guild"]["name"],
                description=players_data[player]["guild"]["description"]
            )
        else:
            guild_obj.pk = None
        Player.objects.get_or_create(
            nickname=player,
            email=players_data[player]["email"],
            bio=players_data[player]["bio"],
            race_id=race_obj.pk,
            guild_id=guild_obj.pk
        )


if __name__ == "__main__":
    main()
