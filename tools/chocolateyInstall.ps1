$packageName = 'FreeOrion'
$fileType = 'exe'
$url = 'https://github.com/freeorion/freeorion/releases/download/v0.4.10.1/FreeOrion_v0.4.10.1_2020-09-25.39cfe10_Win32_Setup.exe'
checksum = 'b803d34059a9fe9d4787cfc92de0cfc56c05922b9412ec2c9198fd9f81daf985'
$silentArgs = '/S'

Install-ChocolateyPackage $packageName $fileType "$silentArgs" "$url"