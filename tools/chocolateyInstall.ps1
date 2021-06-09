$packageName = 'FreeOrion'
$fileType = 'exe'
$url = 'https://github.com//freeorion/freeorion/releases/download/v0.4.10.1/FreeOrion_v0.4.10.1_2020-09-25.39cfe10_Win32_Setup.exe'
$checksum = 'a80a4dbc780f8f08fd81aef71465ced65d46f7a89a1c3c78cac48ddba9793ef9'
$silentArgs = '/S'

Install-ChocolateyPackage $packageName $fileType "$silentArgs" "$url"