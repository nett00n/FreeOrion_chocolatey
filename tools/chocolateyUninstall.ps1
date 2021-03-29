$packageName = 'FreeOrion'
$installerType = 'EXE'
$silentArgs = '/S'
$path = "${env:ProgramFiles}\FreeOrion\"
$path86 = "${env:ProgramFiles(x86)}\FreeOrion\"
$toolsDir       = $(Split-Path -parent $MyInvocation.MyCommand.Definition)

$ahkExe         = 'AutoHotKey'
$ahkFile        = Join-Path $toolsDir "FreeOrionUninstall.ahk"

Start-Process $ahkExe $ahkFile
if (Test-Path $path) {
    Uninstall-ChocolateyPackage $packageName $installerType $silentArgs "$path\uninstall.exe"
}

if (Test-Path $path86) {
    Uninstall-ChocolateyPackage $packageName $installerType $silentArgs "$path86\uninstall.exe"
}