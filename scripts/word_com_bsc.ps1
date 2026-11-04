# Pasos del diagnóstico BSC que necesitan Word (COM). Lo llama scripts/generar_diagnostico_bsc.py.
#   -Accion convertir : abre un .doc y lo guarda como .docx en -Salida
#   -Accion grafico   : reemplaza el párrafo [[GRAFICO]] de -Entrada por un radar nativo de Word
#                       con -Valores (cuatro números separados por coma) y exporta un PNG en -Png
param(
    [Parameter(Mandatory)] [ValidateSet('convertir', 'grafico')] [string] $Accion,
    [Parameter(Mandatory)] [string] $Entrada,
    [string] $Salida,
    [string] $Valores,
    [string] $Png
)
$ErrorActionPreference = 'Stop'
$word = New-Object -ComObject Word.Application
$word.Visible = $false
$word.DisplayAlerts = 0
$word.AutomationSecurity = 3   # deshabilita macros del documento
try {
    if ($Accion -eq 'convertir') {
        $doc = $word.Documents.Open($Entrada, $false, $true)
        $doc.SaveAs2($Salida, 16)
        $doc.Close($false)
        return
    }
    $doc = $word.Documents.Open($Entrada)
    $rng = $doc.Content
    $f = $rng.Find
    if (-not $f.Execute('[[GRAFICO]]')) { throw 'No se encontró el marcador [[GRAFICO]]' }
    $rng.Text = ''
    $nombres = @('1. Enfoque estratégico', '2. Traslado hacia el BSC', '3. Sincronización y despliegue', '4. Cultura de ejecución')
    $v = $Valores.Split(',')
    $shape = $doc.InlineShapes.AddChart2(-1, 82, $rng)   # 82 = radar relleno
    $chart = $shape.Chart
    # Los datos se escriben en la serie y no en la hoja de datos: ChartData.Workbook devuelve
    # NULL desde PowerShell y deja una instancia de Excel abierta.
    while ($chart.SeriesCollection().Count -gt 1) { $chart.SeriesCollection($chart.SeriesCollection().Count).Delete() | Out-Null }
    $s = $chart.SeriesCollection(1)
    $s.Name = 'Línea base (octubre de 2026)'
    $s.Values = [double[]]$v
    $s.XValues = [string[]]$nombres
    $chart.HasTitle = $true
    $chart.ChartTitle.Text = 'Línea base de octubre de 2026: puntaje por elemento (máximo 100)'
    $chart.ChartTitle.Format.TextFrame2.TextRange.Font.Size = 12
    $chart.HasLegend = $false
    $ax = $chart.Axes(2)
    $ax.MinimumScale = 0
    $ax.MaximumScale = 100
    $ax.MajorUnit = 20
    $s = $chart.SeriesCollection(1)
    $s.Format.Fill.ForeColor.RGB = 0x5F3A1F       # azul 1F3A5F en BGR
    $s.Format.Fill.Transparency = 0.35
    $s.HasDataLabels = $true
    $s.DataLabels().Font.Size = 11
    $s.DataLabels().Font.Bold = $true
    $shape.Width = 430
    $shape.Height = 320
    $shape.Range.ParagraphFormat.Alignment = 1
    if ($Png) { $chart.Export($Png) | Out-Null }
    $doc.Save()
    $doc.Close()
}
catch {
    Write-Host ("Error en la línea " + $_.InvocationInfo.ScriptLineNumber + ": " + $_.Exception.Message)
    if ($doc) { $doc.Close([ref]0) }
    throw
}
finally {
    $word.Quit([ref]0)
    [System.Runtime.InteropServices.Marshal]::ReleaseComObject($word) | Out-Null
}
