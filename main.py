import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    def get_or_create_by_name_with_description(
        player_data: dict,
        class_searched: type[Guild] | type[Race],
        attr_name_field: str,
        description_name_field: str
    ) -> Guild | Race:
        return class_searched.objects.get_or_create(
            name=player_data[attr_name_field]["name"],
            defaults={
                "description": (
                    player_data[attr_name_field][description_name_field]
                )
            }
        )[0]

    def get_or_create_skill_with_bonus_and_race(
        skill: dict, race: Race
    ) -> Skill:
        return Skill.objects.get_or_create(
            name=skill["name"],
            defaults={
                "bonus": skill["bonus"],
                "race": race
            }
        )[0]

    def create_players() -> None:
        with open('players.json', 'r', encoding='utf-8') as file:
            players_data = json.load(file)

        for nickname, player_data in players_data.items():
            email = player_data["email"]
            bio = player_data["bio"]
            race = get_or_create_by_name_with_description(
                player_data, Race, "race", "description"
            )
            guild = None
            skills_data = player_data["race"]["skills"]

            if player_data.get("guild") is not None:
                guild = get_or_create_by_name_with_description(
                    player_data, Guild, "guild", "description"
                )

            if skills_data:
                for skill in skills_data:
                    get_or_create_skill_with_bonus_and_race(skill, race)

            Player.objects.get_or_create(
                nickname=nickname,
                defaults={
                    "email": email,
                    "bio": bio,
                    "race": race,
                    "guild": guild
                }
            )
    create_players()


if __name__ == "__main__":
    main()
