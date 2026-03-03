import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    for nickname, payload in data.items():
        race_data = payload.get("race", {})
        race, _ = Race.objects.get_or_create(
            name=race_data.get("name"),
            defaults={"description": race_data.get("description", "")},
        )

        skills_objs = []
        for skl in race_data.get("skills", []):
            skill, _ = Skill.objects.get_or_create(
                name=skl.get("name"),
                defaults={"bonus": skl.get("bonus"), "race": race}
            )
            skills_objs.append(skill)

        guild = None
        guild_data = payload.get("guild")
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                defaults={"description": guild_data.get("description")}
            )

        player_obj, created = Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": payload.get("email"),
                "bio": payload.get("bio"),
                "race": race,
                "guild": guild,
            }
        )

        if skills_objs:
            player_obj.skills.set(skills_objs)


if __name__ == "__main__":
    main()
