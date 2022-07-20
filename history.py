from find import *
import json

hist_path = os.path.dirname(__file__) + "/"

def form_history(ser_name: str, replay: bool) -> (str, int, int):
    ser_name = find_dir(ser_name)
    season, episode = load_history(ser_name)
    if not replay:
        episode += 1
    print("-------------------------------------------------")
    print("#")
    print("#")
    print("playing from history: ", ser_name, "ep", episode, "season", season)
    print("#")
    print("#")
    save_history(ser_name, season, episode)
    return season, episode


def load_history(ser_name: str) -> (int, int):
    ser_name = find_dir(ser_name)
    with open(hist_path + ".history", "r") as f:
        history = json.load(f)
    if ser_name in history:
        season = history[ser_name]["season"]
        episode = history[ser_name]["episode"]
    else:
        season = 1
        episode = 1
    return season, episode


def save_history(ser_name: str, season: int, episode: int) -> None:
    ser_name = find_dir(ser_name)
    with open(hist_path + ".history", "r") as f:
        history = json.load(f)
    history[ser_name] = {"season": season, "episode": episode}
    with open(hist_path + ".history", "w") as f:
        json.dump(history, f, indent=4)
