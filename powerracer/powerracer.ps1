$car = "#"
$guideLeft = "<"
$guideRight = ">"

$roadWidth = 50
$consoleWidth = $Host.UI.RawUI.WindowSize.Width
$carX = $consoleWidth / 2
$roadX = ($consoleWidth - $roadWidth) / 2
$bendX = 0

$command = @{ A = -1; D = 1; }

function Limit-Value([float]$value, [float]$min, [float]$max) {
    if ($value -lt $min) { return $min }
    if ($value -gt $max) { return $max }
    return $value
}

while ($true)
{
    $iroadX = [int]$roadX
    $leftClearance = $carX - $iroadX - 1
    $rightClearance = $roadWidth - $leftClearance - 1
    $rest = $consoleWidth - $iroadX - $roadWidth - 4
    $road = "$(" " * $leftClearance)$($car)$(" " * $rightClearance)"
    Write-Host "$("." * $iroadX)$($guideLeft)$($road)$($guideRight)$("." * $rest)"

    while ([System.Console]::KeyAvailable)
    {
        $key = [System.Console]::ReadKey($true)
        $carX += $command[[string]$key.KeyChar]
    }

    $roadX = Limit-Value ($roadX + $bendX) 0 ($consoleWidth - $roadWidth - 3)
    $bendX = Limit-Value (($bendX + (Get-Random -Minimum -5 -Maximum 6)/20)) -2 2

    if ($carX -le $roadX -or $carX -ge ($roadX + $roadWidth)) {
        break
    }

    [System.Threading.Thread]::Sleep(70)
}

$boomIndent = " " * ($carX - 5)
Write-Host "$($boomIndent) * * * * *"
Write-Host "$($boomIndent)** Boom! **"
Write-Host "$($boomIndent) * * * * *"