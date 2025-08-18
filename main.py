import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild
import json


def main() -> None:
	with open("players.json", "r") as json_file:
		json_data = json.load(json_file)
	for nickname, data in json_data.items():
		race, _ = Race.objects.get_or_create(
			name=data.get("race").get("name"),
			description=data.get("race").get("description")
		)
		for skill in data.get("race").get("skills"):
			Skill.objects.get_or_create(race=race, **skill)
		guild_data = data.get("guild")
		if guild_data:
			guild, _ = Guild.objects.get_or_create(**guild_data)
		else:
			guild = None
		Player.objects.get_or_create(
			nickname=nickname,
			race=race,
			guild=guild,
			email=data.get("email"),
			bio=data.get("bio")
		)


if __name__ == "__main__":
	main()
