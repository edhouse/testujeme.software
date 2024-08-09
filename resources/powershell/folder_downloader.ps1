# Define the folder mask to match the directories
$folderMask = "my_app_*"

# Define the source and destination paths
$sourcePath = "\\my_network_path\my_app\builds\"
$destinationPath = "C:\builds\"


# Get the list of directories that match the folder mask
$directories = Get-ChildItem -Path $sourcePath -Directory | Where-Object { $_.Name -like $folderMask }

# Initialize the download index and list
$downloadIndex = 1
$downloadList = @()

# Get the directories, sort by their creation time
$directories | Sort-Object -Property LastWriteTime -Descending | Select-Object -Last 10 | ForEach-Object {

    # Check if the directory is already downloaded
    if((Test-Path -Path "$($destinationPath)$($_.Name)")) {$isDownloaded = $true}
    else {$isDownloaded = $false}

    # Add the directory to the download list
    $downloadList += [pscustomobject]@{
        Index = $downloadIndex;
        DateTime = $_.LastWriteTime.ToString("yyyy-MM-dd HH:mm");
        Name = $_.Name;
        FullName = $_.FullName;
        IsDownloaded = $isDownloaded;
    }
    $downloadIndex += 1
}

# Display the download list
$downloadList | Format-Table -Property Index, DateTime, Name, IsDownloaded -AutoSize

# Prompt the user to select a build to download
$PROMPT = Read-Host "Select a number of build to download"
$PROMPT = [int]$PROMPT

# Download the selected build
if($PROMPT -gt 0) {
    $downloadList | Foreach-Object {

        if($PROMPT -eq $_.Index) {
            Write-Host "`nDownloading: $($_.Name)"
            Copy-Item -Path $_.FullName -Destination $destinationPath -Recurse -Force
            Write-Host "`nDirectory downloaded to $destinationPath"
        }
    }
}

Write-Host "`nThis window will close in 10 seconds." ;
Start-Sleep -Seconds 10;