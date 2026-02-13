import json

from db.models import Guild, Player, Race, Skill


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for player_data in data:
        race_data = player_data.get("race")
        if not race_data or not race_data.get("name"):
            raise ValueError("Dados da raca ou nome ausentes.")

        race_obj, _ = Race.objects.get_or_create(
            name=race_data.get("name"),
            defaults={
                "description": race_data.get("description", "")
            }
        )

        for skill_data in race_data.get("skills", []):
            skill_name = skill_data.get("name")
            skill_bonus = skill_data.get("bonus")
            if not skill_name or not skill_bonus:
                raise ValueError("Nome ou bonus da skill ausentes.")

            Skill.objects.get_or_create(
                name=skill_name,
                defaults={
                    "bonus": skill_bonus,
                    "race": race_obj
                }
            )

        guild_data = player_data.get("guild")
        guild_obj = None

        if guild_data:
            guild_name = guild_data.get("name")
            if not guild_name:
                raise ValueError("Nome da guilda ausente.")

            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_name,
                defaults={
                    "description": guild_data.get("description")
                }
            )

        nickname = player_data.get("nickname")
        email = player_data.get("email")
        bio = player_data.get("bio")

        if not nickname or not email or not bio:
            raise ValueError("Nickname, email ou bio do jogador ausentes.")

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": email,
                "bio": bio,
                "race": race_obj,
                "guild": guild_obj
            }
        )


if __name__ == "__main__":
    main()