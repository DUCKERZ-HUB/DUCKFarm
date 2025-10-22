# DUCKFarm

This is a fork of [S4DFarm](https://github.com/C4T-BuT-S4D/S4DFarm) which is fork of [DestructiveFarm](https://github.com/DestructiveVoice/DestructiveFarm), adapted for our usage with new protocols.

## Running:
- Change the [./server/app/config.py](./server/app/config.py) file to your liking
    (don't forget to change the `SERVER_PASSWORD`).
- Change external_redis password in docker-compose.yml (of you're planning to use it).
- `docker compose up --build -d`
- **GLHF**

Some screenshots:

![flags](resources/flags.png)

![teams](resources/teams.png)
