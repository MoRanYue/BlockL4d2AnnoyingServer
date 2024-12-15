import httpx
import os
import re
import time
try:
    import ujson as json
except:
    import json

API_KEY = os.getenv("STEAM_API_KEY")
assert API_KEY

if __name__ == '__main__':
    print("Sending request...")
    res = httpx.get("https://api.steampowered.com/IGameServersService/GetServerList/v1", params={
        "key": API_KEY,
        "filter": r"\appid\550\nor\2\gametype\official\white\1",
        "limit": "9999999"
    }, headers={
        "Accept": "application/json; charset=utf-8",
        "User-Agent": "httpx/BlockAnnoyingServer"
    })

    result = json.loads(res.text)

    print("Filtering servers...")
    blocked_servers = []
    for i in result["response"]["servers"]:
        if (i.get("gametype") and re.search("rpg", i["gametype"], re.RegexFlag.I)) or \
        re.search("[^非]rpg|戮|弑|巅|凡|玄|天下|神域|完美世界|一念仙行录|窥仙之路|风花雪月|暗黑之魂|午夜狂欢|無人永生|神之右手|军魂|星缘|破晓|腐尸之地|猎人|通天塔|无法逃脱|穷途末路|众神传说|上帝|HTの|破晓|星缘天空|午夜狂欢|鹅服", i["name"], re.RegexFlag.I) or \
        i["steamid"] in ["90201354335194137", "90201354334376985", "90216653955784729", "90216653955877913"]:
            blocked_servers.append({
                "name": i["name"],
                "steamid": i["steamid"],
                "addr": i["addr"],
                "tags": i.get("gametype", ""),
                "os": i["os"]
            })
    
    with open("blocked_servers_details.json", "w", encoding="utf-8") as f:
        json.dump({
            "timestamp": int(time.time()),
            "game": "Left 4 Dead 2",
            "tag": "RPG",
            "servers": blocked_servers
        }, f, ensure_ascii=False, indent=4)
    print("Blocked servers details created")

    added_ips = []
    with open("ipblacklist.txt", "w", encoding="utf-8") as f:
        for i in blocked_servers:
            ip = i["addr"].split(":")[0]
            if ip in added_ips:
                continue
            added_ips.append(ip)
            f.write(ip + "\n")
    print("IP blacklist created")
