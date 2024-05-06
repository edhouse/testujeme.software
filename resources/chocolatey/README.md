# Chocolatey Example

## Install Chocolatey

Go to https://chocolatey.org/install and follow the instructions.

## Add local repository

```powershell
choco source add -n localChoco -s .\testujeme.software\
```

## Install packages

```powershell
choco install testujeme.software
```

## Check installation(s)

```powershell
C:\influxdata\influxdb-1.8.10-1\influx.exe --version
```

```powershell
& "C:\Program Files\telegraf\telegraf.exe" --version
```