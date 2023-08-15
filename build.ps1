$exclude = @("venv", "bot-selenium.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot-selenium.zip" -Force