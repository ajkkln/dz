from typing import List, Set, Tuple
from datetime import datetime

def process_logs(logs: List[str]) -> Tuple[int, List[str], List[int], List[int], List[Set[str]]]:
    players = {}
    total_blocks_placed = 0
    player_names = []
    player_online_times = []
    player_blocks_placed = []
    player_achievements = []

    for log_line in logs:
        parts = log_line.strip('[]').split(']')
        if len(parts) < 2:
            continue 

        timestamp_str = parts[0].strip()
        player_and_event = parts[1].strip()

        if ":" not in player_and_event:
            continue 

        player_name = player_and_event.split(":")[0].strip().replace("[","").replace("]","")
        event_data = player_and_event.split(":")[1].strip().split()

        if not event_data:
            continue 
            
        event_type = event_data[0]
        timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")


        if player_name not in players:
            players[player_name] = {"online_time": 0, "blocks_placed": 0, "achievements": set(), "last_connection": None}
            player_names.append(player_name)
            player_online_times.append(0)
            player_blocks_placed.append(0)
            player_achievements.append(set())


        if event_type == "connected":
             players[player_name]["last_connection"] = timestamp
        elif event_type == "disconnected":
            if players[player_name]["last_connection"]:
                time_diff = (timestamp - players[player_name]["last_connection"]).total_seconds()
                players[player_name]["online_time"] += int(time_diff)
                players[player_name]["last_connection"] = None
        elif event_type == "block_placed":
            players[player_name]["blocks_placed"] += 1
            total_blocks_placed +=1
        elif event_type == "achievement_unlocked":
            achievement_name = " ".join(event_data[1:])
            players[player_name]["achievements"].add(achievement_name)

    for i, player_name in enumerate(player_names):
        player_online_times[i] = players[player_name]["online_time"]
        player_blocks_placed[i] = players[player_name]["blocks_placed"]
        player_achievements[i] = players[player_name]["achievements"]

    return (
        total_blocks_placed,
        player_names,
        player_online_times,
        player_blocks_placed,
        player_achievements,
    )
logs = [
    "[2024-10-05 20:10:00] [Steve]: connected",
    "[2024-10-05 20:11:30] [Steve]: block_placed 647, -100, 251",
    "[2024-10-05 20:12:10] [Steve]: block_placed 648, -100, 270",
    "[2024-10-05 20:15:00] [Alex]: connected",
    "[2024-10-05 20:15:01] [Steve]: block_placed 649, -100, 280",
    "[2024-10-05 20:16:15] [Alex]: achivement_unlocked taking_inventory",
    "[2024-10-05 20:16:30] [Alex]: block_placed 125, 424, -1265",
    "[2024-10-05 20:17:00] [Steve]: block_placed 10, 64, -30",
    "[2024-10-05 20:18:00] [Steve]: achivement_unlocked getting_an_upgrade",
    "[2024-10-05 20:20:40] [Steve]: disconnected",
    "[2024-10-05 20:21:10] [Alex]: achivement_unlocked benchmarking",
    "[2024-10-05 20:22:00] [Alex]: disconnected"
]
result = process_logs(logs)
print(result)
