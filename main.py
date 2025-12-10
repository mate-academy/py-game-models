import json
import os
from django.db import IntegrityError, transaction
from db.models import Race, Skill, Guild, Player


def find_file(file_name):
    """
    Pomocnicza funkcja do znajdowania pliku w różnych ścieżkach,
    co jest często problemem w testach.
    """
    if os.path.exists(file_name):
        return file_name

    test_path = os.path.join(os.path.dirname(__file__), 'tests', file_name)
    if os.path.exists(test_path):
        return test_path

    return None


def load_data_from_json(file_path):
    """
    Wczytuje dane z pliku JSON. Zwraca słownik lub listę.
    """
    resolved_path = find_file(file_path)

    if not resolved_path:
        print(f"Błąd: Plik {file_path} nie został znaleziony.")
        return None

    try:
        with open(resolved_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if isinstance(data, (list, dict)):
            return data

        print(f"Błąd: Wczytane dane nie są listą ani słownikiem. Typ: {type(data)}")
        return None

    except json.JSONDecodeError as e:
        print(f"Błąd: Nie można zdekodować pliku JSON: {resolved_path}. Szczegóły: {e}")
        return None


def main(json_file_path='players.json'):
    """
    Wczytuje dane graczy i dodaje je do bazy danych, dostosowując się do struktury słownika.
    """
    print(f"Rozpoczynanie importu danych z {json_file_path}...")
    raw_data = load_data_from_json(json_file_path)

    if not raw_data:
        print("Brak danych do przetworzenia lub błąd ładowania. Zakończenie.")
        return

    # Przekształcenie słownika (z players.json) na listę graczy
    if isinstance(raw_data, dict):
        player_data_list = []
        for nickname, player_details in raw_data.items():
            if isinstance(player_details, dict):
                player_details['nickname'] = nickname
                player_data_list.append(player_details)
        player_data = player_data_list
    elif isinstance(raw_data, list):
        player_data = raw_data
    else:
        print("Nieobsługiwany format danych po załadowaniu.")
        return

    players_created_count = 0
    print(f"Znaleziono {len(player_data)} wpisów graczy do przetworzenia.")

    with transaction.atomic():
        for i, data in enumerate(player_data):

            nickname = data.get('nickname')

            if not nickname or not data.get('email') or not data.get('bio'):
                print(f"[Wpis #{i + 1}] BŁĄD: Brakuje wymaganych pól (nickname/email/bio). Pominięto.")
                continue

            print(f"\nPrzetwarzanie gracza: {nickname}")

            try:
                # --- 1. Obsługa Rasy (Race) ---
                race_data = data.get('race', {})
                race_name = race_data.get('name')

                if not race_name:
                    print(f"  -> BŁĄD: Brakuje nazwy Rasy dla gracza {nickname}. Pominięto.")
                    continue

                race, race_created = Race.objects.get_or_create(
                    name=race_name,
                    defaults={'description': race_data.get('description', '')}
                )

                # --- 2. Obsługa Gildii (Guild) ---
                guild_data = data.get('guild', {})
                guild_name = guild_data.get('name')
                guild = None

                if guild_name:
                    guild, guild_created = Guild.objects.get_or_create(
                        name=guild_name,
                        defaults={'description': guild_data.get('description')}
                    )

                # --- 3. Obsługa Umiejętności (Skills) ---
                skills_list = race_data.get('skills', [])
                if isinstance(skills_list, list):
                    for skill_data in skills_list:
                        skill_name = skill_data.get('name') if isinstance(skill_data, dict) else None

                        if skill_name:
                            Skill.objects.get_or_create(
                                name=skill_name,
                                defaults={
                                    'bonus': skill_data.get('bonus', 'Brak opisu bonusu'),
                                    'race': race
                                }
                            )

                # --- 4. Tworzenie Gracza (Player) ---
                player, player_created = Player.objects.get_or_create(
                    nickname=nickname,
                    defaults={
                        'email': data['email'],
                        'bio': data['bio'],
                        'race': race,
                        'guild': guild,
                    }
                )

                if player_created:
                    players_created_count += 1
                    print(f"  -> UTWORZONO Gracza: {player.nickname}")

            except IntegrityError as e:
                print(f"  -> BŁĄD INTEGRALNOŚCI (DB): Nie można utworzyć gracza {nickname}. Szczegóły: {e}")

            except Exception as e:
                print(f"  -> KRYTYCZNY BŁĄD podczas przetwarzania gracza {nickname}: {type(e).__name__}: {e}")

    print("\n--- Podsumowanie Importu ---")
    print(f"Utworzono {players_created_count} nowych Graczy.")
    print("Zakończono import danych.")


if __name__ == '__main__':
    main('players.json')
