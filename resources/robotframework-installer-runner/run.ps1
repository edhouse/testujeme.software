# Set variables
$currentLocation = Get-Location
$pythonInstallerUrl = "https://www.python.org/ftp/python/3.11.3/python-3.11.3-amd64.exe"
$pythonInstallerExe = "python-3.11.3-amd64.exe"

# Check/install Python
$pythonExe = "$currentLocation\python\python.exe"
if(Test-Path $pythonExe) {

    Write-Host "Python installed"

} else {

    # Download Python installer
    if(Test-Path "$currentLocation\$pythonInstallerExe") {

        Write-Host "'$pythonInstallerExe' already downloaded"

    } else {

        [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12 # (should resolve SSL errors)
        Write-Host "Downloading '$pythonInstallerExe'"
        Invoke-WebRequest -URI $pythonInstallerUrl -OutFile "$currentLocation\$pythonInstallerExe"

    }

    Write-Host "Installing Python"
    Start-Process $currentLocation/$pythonInstallerExe -ArgumentList "/passive InstallAllUsers=0 DefaultJustForMeTargetDir=$currentLocation\python AssociateFiles=0 Include_launcher=0 SimpleInstall=1 Include_pip=1" -NoNewWindow -Wait
}

# Install packages
if(Test-Path "$currentLocation/requirements.txt") {

    Start-Process $pythonExe -ArgumentList "-m pip install -r requirements.txt" -NoNewWindow -Wait

} else {

    Write-Host "'requirements.txt' not found"
    Write-Host "Installing Robot Framework"
    Start-Process $pythonExe -ArgumentList "-m pip install robotframework" -NoNewWindow -Wait

}

# Run tests
$rfExe = "$currentLocation\python\Scripts\robot.exe"
if(Test-Path $rfExe) {

    Start-Process $rfExe -ArgumentList $currentLocation -NoNewWindow -Wait

} else {
    Write-Host "'Robot Framework' not found"
}

Read-Host -Prompt "Press Enter to exit"