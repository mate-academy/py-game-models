import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "rb") as file:
        players_data = json.load(file)

    for key_name in players_data:
        race = Race.objects.get_or_create(
            name=players_data[key_name].get("race").get("name"),
            description=players_data[key_name].get(
                "race"
            ).get("description")
        )[0]

        for skill in players_data[key_name].get("race").get("skills"):
            Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race_id=race.id
            )

        guild = None

        if players_data[key_name].get("guild"):
            guild = Guild.objects.get_or_create(
                name=players_data[key_name].get("guild").get("name"),
                description=players_data[key_name].get(
                    "guild"
                ).get("description")
            )[0]

        player = Player(
            nickname=key_name,
            email=players_data[key_name].get("email"),
            bio=players_data[key_name].get("bio"),
            race=race,
            guild=guild,

        )
        player.save()


if __name__ == "__main__":
    main()
