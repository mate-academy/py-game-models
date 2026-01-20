import json
import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as json_file:
        players = json.load(json_file)

    for nickname, pdata in players.items():
        email = pdata.get("email")
        bio = pdata.get("bio")

        race_info = pdata.get("race", {})
        race_name = race_info.get("name")
        race_description = race_info.get("description")
        skills = race_info.get("skills", [])
        race, race_created = Race.objects.get_or_create(
            name=race_name,
            defaults={"description": race_description or ""}
        )
        if (not race_created and race.description is not None
                and race.description != race_description):
            race.description = race_description
            race.save()
        for skill_info in skills:
            skill_name = skill_info.get("name", "")
            skill_bonus = skill_info.get("bonus")
            if not skill_name:
                continue

            skill, skill_created = Skill.objects.get_or_create(
                name=skill_name,
                defaults={"bonus": skill_bonus, "race": race}
            )
            if not skill_created:
                updated = False
                if skill.race_id != race.id:
                    updated = True
                    skill.race = race
                if skill_bonus and skill.bonus != skill_bonus:
                    skill.bonus = skill_bonus
                    updated = True
                if updated:
                    skill.save()

        guild = None
        guild_info = pdata.get("guild")
        if guild_info:
            guild_name = guild_info.get("name")
            guild_description = guild_info.get("description")
            guild, guild_created = Guild.objects.get_or_create(
                name=guild_name,
                defaults={"description": guild_description}
            )
            if (not guild_created and guild_description is not None
                    and guild.description != guild_description):
                guild.description = guild_description
                guild.save()

        player, player_created = Player.objects.get_or_create(
            nickname=nickname,
            defaults={"email": email,
                      "bio": bio,
                      "race": race,
                      "guild": guild}
        )

        if not player_created:
            changed = False
            if player.email != email:
                player.email = email
                changed = True
            if player.bio != bio:
                player.bio = bio
                changed = True
            if player.race_id != race.id:
                player.race = race
                changed = True
            if guild is not None and player.guild_id != guild.id:
                player.guild = guild
                changed = True
            if changed:
                player.save()


if __name__ == "__main__":
    main()
