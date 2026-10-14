import json
import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players_data = json.load(f)
    for nickname, player_data in players_data.items():
        player_data["nickname"] = nickname

        # Extrai race (que é um dict com name, description e skills)
        race_dict = player_data.pop("race")

        # Extrai guild (que é um dict com name e description)
        guild_dict = player_data.pop("guild", None)

        # Cria/atualiza a race
        race, _ = Race.objects.get_or_create(
            name=race_dict["name"],
            description=race_dict.get("description", "")
        )

        # Cria/atualiza a guild
        guild = None
        if guild_dict:
            guild, _ = Guild.objects.get_or_create(
                name=guild_dict["name"],
                description=guild_dict.get("description", "")
            )

        # Cria o player
        Player.objects.create(race=race, guild=guild, **player_data)

        # Cria as skills (que estão dentro de race_dict!)
        skills_data = race_dict.get("skills", [])
        for skill_data in skills_data:
            Skill.objects.get_or_create(
                name=skill_data["name"],
                bonus=skill_data["bonus"],
                race=race
            )


if __name__ == "__main__":
    main()
