import subprocess
import os
import psutil
import time
import threading


def start_game(on_close_callback):
    """Launches Valorant and watches it until the process ends."""
    riot_path = r"C:\Riot Games\Riot Client\RiotClientServices.exe"
    launch_cmd = f'"{riot_path}" --launch-product=valorant --launch-patchline=live'

    try:
        subprocess.Popen(launch_cmd, shell=True)

        monitor_thread = threading.Thread(
            target=watch_session, args=(on_close_callback,))
        monitor_thread.daemon = True
        monitor_thread.start()

        return True
    except Exception as e:
        print(f"Launch Error: {e}")
        return False


def watch_session(callback):
    """Watches for game start, then waits for game exit."""
    game_exe = "VALORANT-Win64-Shipping.exe"

    game_process = None
    while not game_process:
        for proc in psutil.process_iter(['name']):
            if proc.info['name'] == game_exe:
                game_process = proc
                break
        time.sleep(2)

    while game_process.is_running():
        time.sleep(5)

    callback()
