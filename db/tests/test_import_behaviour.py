import json

import pytest

from main import Guild, Player, Race, Skill, main


@pytest.mark.django_db
def test_repeated_import_does_not_duplicate_records():
    main()
    main()

    assert Race.objects.count() == 2
    assert Skill.objects.count() == 2
    assert Guild.objects.count() == 3
    assert Player.objects.count() == 5


@pytest.mark.django_db
def test_deleting_guild_preserves_players_and_deleting_race_cascades():
    main()
    elf = Race.objects.get(name="elf")
    assert elf.skills.count() == 2
    assert elf.players.count() == 3

    guild = Guild.objects.get(name="mags")
    assert guild.players.count() == 2
    guild.delete()

    assert Player.objects.count() == 5
    assert Player.objects.get(nickname="max").guild is None
    assert Player.objects.get(nickname="arthur").guild is None

    elf.delete()

    assert Skill.objects.count() == 0
    assert set(Player.objects.values_list("nickname", flat=True)) == {
        "andrew", "nick",
    }


@pytest.mark.django_db
def test_player_can_omit_guild(tmp_path, monkeypatch):
    players = {
        "traveler": {
            "email": "traveler@example.com",
            "bio": "Independent traveler",
            "race": {
                "name": "human",
                "description": "Human race",
                "skills": [],
            },
        },
    }
    (tmp_path / "players.json").write_text(
        json.dumps(players), encoding="utf-8",
    )
    monkeypatch.chdir(tmp_path)

    main()

    assert Player.objects.get(nickname="traveler").guild is None
    assert Guild.objects.count() == 0
