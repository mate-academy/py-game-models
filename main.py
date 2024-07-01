import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def load_data_from_json(filename: str) -> dict:
    with open(filename) as file:
        data = json.load(file)
        return data


def process_players_data(data: dict) -> None:
    for nickname, player_data in data.items():
        race_data = player_data["race"]
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data.get("description", "")}
        )

        guild = None

        guild_data = player_data.get("guild")
        if guild_data:
            guild_name = guild_data.get("name", "")
            guild_description = guild_data.get("description", None)
            guild, _ = Guild.objects.get_or_create(
                name=guild_name,
                defaults={"description": guild_description}
            )

        skills_data = race_data.get("skills", [])
        for skill_data in skills_data:
            skill, _ = Skill.objects.get_or_create(
                name=skill_data["name"],
                bonus=skill_data["bonus"],
                race=race
            )

        email = player_data["email"]
        bio = player_data["bio"]
        player, _ = Player.objects.get_or_create(
            nickname=nickname,
            email=email,
            bio=bio,
            race=race,
            guild=guild
        )


def main() -> None:
    data = load_data_from_json("players.json")
    process_players_data(data)


if __name__ == "__main__":
    main()
