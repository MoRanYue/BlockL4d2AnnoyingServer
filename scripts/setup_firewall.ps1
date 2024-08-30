If (-NOT ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
    Start-Process powershell.exe -Verb RunAs -ArgumentList "-NoProfile -ExecutionPolicy Bypass -File `"$PSCommandPath`""
    exit
}

$blacklist_url = "https://github.com/MoRanYue/BlockL4d2AnnoyingServer/raw/main/ipblacklist.txt"

try {
    $response = Invoke-WebRequest -Uri $blacklist_url -UseBasicParsing
    $list = $response.Content -split "`n"
    Write-Host "Blacklist fetched"
}
catch {
    Write-Error "Failed to fetch blacklist, error: $($_.Exception.Message)"
    exit
}

$list = $list | ForEach-Object { $_.Trim() } | Where-Object { $_ -ne "" }
$list = $list -split "`n"
Write-Host $list

$inbound_rulename = "BlockAnnoyingServers_Inbound"
$outbound_rulename = "BlockAnnoyingServers_Outbound"

if (Get-NetFirewallRule -Name $inbound_rulename -ErrorAction SilentlyContinue) {
    Remove-NetFirewallRule -Name $inbound_rulename -ErrorAction SilentlyContinue
}
New-NetFirewallRule -Name $inbound_rulename -DisplayName "Block Annoying Servers (Inbound)" -Enabled 1 -Direction Inbound -Action Block -RemoteAddress $list -Profile Any
if (Get-NetFirewallRule -Name $outbound_rulename -ErrorAction SilentlyContinue) {
    Remove-NetFirewallRule -Name $outbound_rulename -ErrorAction SilentlyContinue
}
New-NetFirewallRule -Name $outbound_rulename -DisplayName "Block Annoying Servers (Outbound)" -Enabled 1 -Direction Outbound -Action Block -RemoteAddress $list -Profile Any