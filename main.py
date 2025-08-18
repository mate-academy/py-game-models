import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild
import json


def main() -> None:
	with open("players.json", "r") as json_file:
		json_data = json.load(json_file)
	for nickname, data in json_data.items():
		race, _ = Race.objects.get_or_create(
			name=data["race"]["name"],
			description=data["race"]["description"]
		)
		for skill in data["race"]["skills"]:
			Skill.objects.get_or_create(race=race, **skill)
		
		if data["guild"]:
			guild, _ = Guild.objects.get_or_create(**data["guild"])
		else:
			guild = None
		Player.objects.create(
			nickname=nickname,
			race=race,
			guild=guild,
			email=data["email"],
			bio=data["bio"]
		)


if __name__ == "__main__":
	main()
