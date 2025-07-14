param(
    [string]$databricksHost,
    [string]$applicationId,
    [string]$comentario,
    [int]$dias
)

$workspaceUrl = $databricksHost.TrimEnd('/')
$lifetimeSeconds = $dias * 86400

# Caminho do arquivo do token gerado pelo token.ps1
$tokenPath = "$PSScriptRoot\access_token.txt"

if (-Not (Test-Path $tokenPath)) {
    Write-Error "Arquivo de token de acesso não encontrado: $tokenPath"
    exit 1
}

$accessToken = Get-Content $tokenPath -Raw

$apiUrl = "$workspaceUrl/api/2.0/token/create"

$body = @{
    application_id    = $applicationId
    comment           = $comentario
    lifetime_seconds  = $lifetimeSeconds
} | ConvertTo-Json -Depth 3

try {
    $response = Invoke-RestMethod -Method Post -Uri $apiUrl `
        -Headers @{ Authorization = "Bearer $accessToken" } `
        -ContentType "application/json" `
        -Body $body

    if ($response.token_value) {
        Write-Host "Token do Databricks gerado com sucesso!"
        Write-Host "Token: $($response.token_value)"
    }
    else {
        Write-Error "Falha ao gerar token. Resposta: $($response | ConvertTo-Json -Depth 3)"
        exit 1
    }
}
catch {
    Write-Error "Erro na chamada REST: $_"
    exit 1
}
