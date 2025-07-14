param(
    [string]$tenantId,
    [string]$clientId,
    [string]$clientSecret,
    [string]$scope
)

$body = @{
    client_id     = $clientId
    scope         = $scope
    grant_type    = "client_credentials"
    client_secret = $clientSecret
}

$response = Invoke-RestMethod -Method Post `
    -Uri "https://login.microsoftonline.com/$tenantId/oauth2/v2.0/token" `
    -Body $body `
    -ContentType "application/x-www-form-urlencoded"

# Salva o token em arquivo temporário
$tokenPath = "$PSScriptRoot\access_token.txt"
$response.access_token | Out-File -FilePath $tokenPath -Encoding utf8

Write-Host "✅ Access token salvo em $tokenPath"
