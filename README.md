# Block L4D2 Annoying Servers

<div align="center">

<u>English</u> | [简体中文](README_ZHCN.md)

</div>

This repo is to block those annoying servers (such as RPG gameplay servers) on *Left 4 Dead 2*.

Those servers always show you a window at your left hand, though you left these servers, you will still see them in your local server or singleplayer unless restarting the game. **I RELLY HATE THIS!!!**
While I've always been annoyed by RPG gameplay, the points store is generally acceptable.

By the way, I think bringing RPG gameplay to the game is a fucking bad idea.

---

I provided [an IP Blacklist](ipblacklist.txt) and [details of the blocked servers](blocked_servers_details.json).

> The workflow will be executed at every Saturday, it'll update the backlists automatically.

You need something that can block your communication to the IPs.

On Windows, there is a firewall. You may set-up that by [the script](scripts/setup_firewall.ps1). In addition, you can let your system execute it automatically through Scheduled Tasks.

Besides, this command will help you set your firewall:

```powershell
# Open your Powershell with administration permission.
iex (irm "https://raw.githubusercontent.com/MoRanYue/BlockL4d2AnnoyingServer/refs/heads/main/scripts/setup_firewall.ps1")
```