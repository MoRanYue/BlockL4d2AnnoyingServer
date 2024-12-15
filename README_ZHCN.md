# 过滤求生之路2烦人服务器

<div align="center">

[English](README.md) | <u>简体中文</u>

</div>

这个仓库主要为了过滤《求生之路2》服务器中的烦人服务器（比如提供RPG玩法的服务器）。

那些服务器可能会在你加入时，在左边显示1个窗口，尽管你离开那些服务器，你仍然会在你的本地服务器与单人游戏时看到那个窗口，除非重启游戏。**这样真的很令人讨厌！！！**
虽然我总是对RPG游戏玩法感到恼火，但积分商店通常是可以接受的。

除此之外，我认为将RPG玩法带入这个游戏，真的是超级愚蠢的想法。

---

该仓库提供了[IP黑名单](ipblacklist.txt)与[黑名单中服务器的信息](blocked_servers_details.json)。

> 工作流将会在每周六执行，因此黑名单会自动更新。

你需要一些软件来使用IP黑名单。

在Windows系统中，你可以通过[这个脚本](scripts/setup_firewall.ps1)来配置防火墙。除此之外，你可以手动设置“计划任务”来自动执行脚本。

另外，这个命令能够帮助你一键设置防火墙规则。

```powershell
# 使用管理员权限打开Powershell
iex (irm "https://raw.githubusercontent.com/MoRanYue/BlockL4d2AnnoyingServer/refs/heads/main/scripts/setup_firewall.ps1")
```