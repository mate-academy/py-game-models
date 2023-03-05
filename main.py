import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)
    for player_name in data:
        race_name = data[player_name]["race"]["name"]
        race_description = data[player_name]["race"].get("description")
        create_race(race_name, race_description)
        if data[player_name]["guild"] is not None:
            guild_name = data[player_name]["guild"]["name"]
            guild_description = data[player_name]["guild"].get("description")
            create_guild(guild_name, guild_description)
        race_id = Race.objects.get(name=race_name).id
        guild_id = Guild.objects.get(
            name=data[player_name]["guild"]["name"]
        ).id if data[player_name]["guild"] else None
        create_player(player_name,
                      data[player_name]["email"],
                      data[player_name]["bio"],
                      race_id,
                      guild_id
                      )
        for skill in data[player_name]["race"]["skills"]:
            create_skills(skill["name"], skill["bonus"], race_id)


def create_race(race_name: str, race_description: str) -> None:
    if not Race.objects.filter(name=race_name).exists():
        Race.objects.create(name=race_name, description=race_description)


def create_guild(guild_name: str, guild_description: str) -> None:
    if not Guild.objects.filter(name=guild_name).exists():
        Guild.objects.create(name=guild_name, description=guild_description)


def create_player(
        nickname: str,
        email: str, bio: str,
        race_id: str,
        guild_id: str
) -> None:
    if not Player.objects.filter(nickname=nickname).exists():
        Player.objects.create(nickname=nickname,
                              email=email,
                              bio=bio,
                              race_id=race_id,
                              guild_id=guild_id,
                              )


def create_skills(name: str, bonus: str, race_id: str) -> None:
    if not Skill.objects.filter(name=name).exists():
        Skill.objects.create(
            name=name,
            bonus=bonus,
            race_id=race_id
        )


if __name__ == "__main__":
    main()
