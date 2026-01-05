import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        data_players = json.load(players_file)

    for player in data_players:
        get_data_player = data_players.get(player)

        race_data = get_data_player.get("race")
        skills_data = race_data.get("skills")

        race_player, create_or_no = Race.objects.get_or_create(
            name=race_data.get("name"),
            description=race_data.get("description")
        )

        for skill in skills_data:
            Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=race_player
            )

        guilds_data = get_data_player.get("guild")
        if guilds_data:
            guild_playere, _ = Guild.objects.get_or_create(
                name=guilds_data.get("name"),
                description=guilds_data.get("description")
            )
        else:
            guild_playere = None

        Player.objects.create(
            nickname=player,
            email=get_data_player.get("email"),
            bio=get_data_player.get("bio"),
            race=race_player,
            guild=guild_playere
        )


if __name__ == "__main__":
    main()
