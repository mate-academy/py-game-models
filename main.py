import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    # abertura do arquivo json com o manager context
    with open("players.json", "r") as file:
        data = json.load(file)

    # definição do for pra cada nickname: dict do arquivo JSON lido
    for nickname, player_data in data.items():
        # informações do jogador -> raça
        race_data = player_data["race"]
        # criação da instancia do modelo de raça do jogador
        race, _ = Race.objects.get_or_create(name=race_data.get("name"),
                                             defaults={
                                                 "description":
                                                     race_data.get(
                                                         "description")
                                                     or "", },
                                             )
        # informações de todas as skills da raça
        for skill_data in race_data["skills"]:
            # criação da instancia da skill da raça do jogador
            Skill.objects.get_or_create(name=skill_data.get("name"),
                                        defaults={
                                            "bonus":
                                                skill_data.get("bonus") or "",
                                            "race": race, },
                                        )
        # informações da guilda
        guild_data = player_data.get("guild")
        # caso o jogador não tenha -> valor null
        guild = None
        if guild_data:
            # criação da instancia da guilda
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={
                    "description": guild_data["description"],
                },
            )

        # criação da instancia do player
        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player_data.get("email"),
                "bio": player_data.get("bio"),
                "race": race,
                "guild": guild,
            },
        )


if __name__ == "__main__":
    main()
