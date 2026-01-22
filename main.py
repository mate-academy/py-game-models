import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    def read_data_json(file_path: str) -> dict:
        try:
            with open(file_path) as json_file:
                data_json = json.load(json_file)
        except (FileNotFoundError, json.decoder.JSONDecodeError) as e:
            raise RuntimeError(e)

        return data_json

    players = read_data_json("players.json")

    for nickname, data in players.items():
        try:
            race_data = data["race"]
            race_obj, created = Race.objects.get_or_create(
                name=race_data["name"],
                description=race_data["description"],
            )

            for skill in race_data["skills"]:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race_obj)

            guild_data = data.get("guild")
            if guild_data and guild_data.get("name"):
                guild_obj, created = Guild.objects.get_or_create(
                    name=guild_data["name"],
                    description=guild_data["description"])
            else:
                guild_obj = None

            Player.objects.get_or_create(
                nickname=nickname,
                email=data["email"],
                bio=data["bio"],
                race=race_obj,
                guild=guild_obj
            )
        except Exception as e:
            raise RuntimeError(e)


if __name__ == "__main__":
    main()
