import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def load_data_from_json() -> dict:
    with open("players.json", "r") as file:
        players_data = json.load(file)
    return players_data


def main() -> None:
    players_data = load_data_from_json()

    for nickname, player_data in players_data.items():
        race_data = player_data.get("race")
        guild_data = player_data.get("guild")

        race, created_race = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data.get("description", "")}
        )

        if created_race:
            print(f"Created race: {race.name}")

        if "skills" in race_data and race_data["skills"]:
            for skill_data in race_data["skills"]:
                skill, created_skill = Skill.objects.get_or_create(
                    name=skill_data["name"],
                    bonus=skill_data["bonus"],
                    race=race
                )

                if created_skill:
                    print(f"Created skill: {skill.name} for race: {race.name}")

        if guild_data:
            guild, created_guild = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description", "")}
            )

            if created_guild:
                print(f"Created guild: {guild.name}")
        else:
            guild = None

        player, created_player = Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player_data["email"],
                "bio": player_data["bio"],
                "race": race,
                "guild": guild
            }
        )

        if created_player:
            print(f"Created player: {player.nickname}")
        else:
            print(f"Player already exists in database: {player.nickname}")


if __name__ == "__main__":
    main()
