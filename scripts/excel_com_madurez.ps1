# Llena la Herramienta de Medición de Madurez Digital del MinTIC con Excel (COM).
# Lo llama scripts/generar_madurez_digital.py con -Libro (copia del .xlsm) y -Datos (JSON).
#
# Las macros "Calcular Nivel de Madurez" y "Crear Matriz" abren cuadros de diálogo que bloquean la
# automatización, así que sus efectos se repiten aquí línea por línea (Módulo3.CalcularndMadurez y
# Módulo1.matriz del libro). Los puntos calientes llegan en el JSON, calculados por scripts/vba_vecinos.py
# con el código de Módulo4.vecinos, y se escriben como lo haría esa macro.
param(
    [Parameter(Mandatory)] [string] $Libro,
    [Parameter(Mandatory)] [string] $Datos
)
$ErrorActionPreference = 'Stop'
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$d = Get-Content -Raw -Encoding UTF8 $Datos | ConvertFrom-Json

function Redondear([double] $x) {
    # Round de VBA redondea al par en los empates; la herramienta resta 0,01 antes de redondear.
    [Math]::Round($x - 0.01, 0, [MidpointRounding]::ToEven)
}

$xl = New-Object -ComObject Excel.Application
$xl.Visible = $false
$xl.DisplayAlerts = $false
$xl.AutomationSecurity = 3   # macros deshabilitadas: aquí no se ejecuta ninguna
Add-Type -Namespace Win32 -Name Ventana -MemberDefinition '[DllImport("user32.dll")] public static extern uint GetWindowThreadProcessId(System.IntPtr h, out uint p);'
$pidExcel = 0
[void] [Win32.Ventana]::GetWindowThreadProcessId([IntPtr] $xl.Hwnd, [ref] $pidExcel)
try {
    $wb = $xl.Workbooks.Open($Libro)
    [double] $hoy = (Get-Date).Date.ToOADate()
    $rangos2 = $wb.Worksheets.Item('Rangos2')

    # 1. Cuestionario: preguntas 1 a 9 en E6, E8… E22; 10 a 17 en I6, I8… I20. La hoja tiene contraseña
    #    (Unprotect abre un diálogo que bloquea la automatización); las celdas de respuesta están desbloqueadas.
    $fp = $wb.Worksheets.Item('Formulario de Preguntas')
    for ($n = 1; $n -le 17; $n++) {
        if ($n -le 9) { $fp.Cells(4 + 2 * $n, 5).Value2 = [int] $d.respuestas[$n - 1] }
        else { $fp.Cells(6 + 2 * ($n - 10), 9).Value2 = [int] $d.respuestas[$n - 1] }
    }

    # 2. Nivel de madurez, como CalcularndMadurez.
    $r = $d.respuestas
    $pyc = Redondear (($r[0] + $r[1] + $r[2] + $r[3]) / 4)
    $pdn = Redondear (($r[4] + $r[5] + $r[6]) / 3)
    $ddya = Redondear (($r[7] + $r[8] + $r[9] + $r[10]) / 4)
    $td = Redondear (($r[11] + $r[12] + $r[13] + $r[14] + $r[15] + $r[16]) / 6)
    $mad = [Math]::Round(($pyc + $pdn + $ddya + $td - 0.01) / 4, 0, [MidpointRounding]::ToEven)
    $mm = $wb.Worksheets.Item('Modelo de Madurez')
    $mm.Unprotect('')
    # [int]: sin la conversión, PowerShell pasa un PSObject a COM y Excel responde "conversión no válida".
    [int] $fila = $mm.Cells($mm.Rows.Count, 3).End(-4162).Row + 1   # xlUp
    $mm.Cells($fila, 2).Value2 = $hoy
    $mm.Cells($fila, 3).Value2 = [int] $pyc
    $mm.Cells($fila, 4).Value2 = [int] $pdn
    $mm.Cells($fila, 5).Value2 = [int] $ddya
    $mm.Cells($fila, 6).Value2 = [int] $td
    $mm.Cells($fila, 8).Value2 = [int] $mad
    $rangos2.Range('D5:J5').Copy() | Out-Null
    $mm.Range($mm.Cells($fila, 2), $mm.Cells($fila, 8)).PasteSpecial(-4122) | Out-Null   # xlPasteFormats
    $mm.Protect()

    # 3. Resultados Heatmap: la plantilla trae una fila de prueba de 2019 oculta en la fila 21. La macro
    #    escribe debajo de la última fila con datos, así que sin borrarla los resultados quedarían ocultos.
    $rh = $wb.Worksheets.Item('Resultados Heatmap')
    $rh.Unprotect('')
    $rh.Range('B21:N21').Clear() | Out-Null
    $rh.Protect()

    # 4. Mapa de calor, como matriz: procesos en la fila 5 desde E, áreas en la columna D desde la fila 6.
    $h = $wb.Worksheets.Item('Heatmap')
    $h.Unprotect('')
    [int] $np = $d.procesos.Count
    [int] $na = $d.areas.Count
    for ($j = 0; $j -lt $np; $j++) { $h.Cells(5, 5 + $j).Value2 = [string] $d.procesos[$j] }
    for ($i = 0; $i -lt $na; $i++) { $h.Cells(6 + $i, 4).Value2 = [string] $d.areas[$i] }
    $celdas = $h.Range($h.Cells(6, 5), $h.Cells(5 + $na, 4 + $np))
    $rangos2.Range('B5').Copy($celdas) | Out-Null                     # PasteAll: lista y colores
    for ($i = 0; $i -lt $na; $i++) { $h.Cells(6 + $i, 3).Value2 = [int] ($i + 1) }
    $h.Range('E5').Copy() | Out-Null
    $h.Range($h.Cells(5, 5), $h.Cells(5, 4 + $np)).PasteSpecial(-4122) | Out-Null
    $h.Range('D6').Copy() | Out-Null
    $h.Range($h.Cells(6, 4), $h.Cells(5 + $na, 4)).PasteSpecial(-4122) | Out-Null
    $h.Range($h.Cells(6, 3), $h.Cells(5 + $na, 3)).PasteSpecial(-4122) | Out-Null
    $ancho = $h.Columns(5).ColumnWidth
    for ($j = 1; $j -lt $np; $j++) { $h.Columns(5 + $j).ColumnWidth = $ancho }
    for ($i = 0; $i -lt $na; $i++) {
        for ($j = 0; $j -lt $np; $j++) { $h.Cells(6 + $i, 5 + $j).Value2 = [int] $d.matriz[$i][$j] }
    }

    # 5. Priorización. La macro vecinos lee los botones ActiveX "1, 2 o 3 Iniciativas", que Office no carga
    #    en un libro abierto por automatización (error 438). Python ejecuta la rama original de la macro
    #    (scripts/vba_vecinos.py) y aquí se escribe lo que ella escribiría, con los mismos formatos.
    $rh.Unprotect('')
    [int] $base = $rh.Cells($rh.Rows.Count, 3).End(-4162).Row + 1
    $k = 0
    foreach ($res in $d.resultados) {
        $rh.Cells($base + $k, 2).Value2 = $hoy
        $rh.Cells($base + $k, 3).Value2 = [string] $res[0]
        $rh.Cells($base + $k, 4).Value2 = [string] $res[1]
        $rh.Cells($base + $k, 5).Value2 = [double] $res[2]
        $rh.Cells($base + $k, 6).Value2 = [double] $res[3]
        $k++
    }
    $origen = @{ 1 = 'D9:H9'; 2 = 'D9:H9'; 3 = 'D9:P9' }[[int] $d.iniciativas]
    $rangos2.Range($origen).Copy() | Out-Null
    $rh.Range($rh.Cells($base, 2), $rh.Cells($base + $k - 1, 6)).PasteSpecial(-4122) | Out-Null
    $rh.Range($rh.Cells($base, 2), $rh.Cells($base + $k - 1, 6)).Rows.AutoFit() | Out-Null   # nombres largos
    $rh.Protect()

    # 6. Lo que quedó en el libro.
    "Modelo de madurez (fila {0}): personas {1}, procesos {2}, datos {3}, tecnología {4}; nivel {5}" -f `
        $fila, $mm.Cells($fila, 3).Text, $mm.Cells($fila, 4).Text, $mm.Cells($fila, 5).Text, $mm.Cells($fila, 6).Text, $mm.Cells($fila, 8).Text
    for ($f = 9; $rh.Cells($f, 3).Text -ne ''; $f++) {
        "Punto caliente: {0} | {1} | valor {2} | índice {3}" -f $rh.Cells($f, 3).Text, $rh.Cells($f, 4).Text, $rh.Cells($f, 5).Text, $rh.Cells($f, 6).Text
    }
    $wb.Worksheets.Item('Inicio').Activate()
    $wb.Save()

    # 7. Vistas previas en PNG junto al libro. El gráfico temporal va en un libro auxiliar porque las
    #    hojas protegidas no admiten objetos nuevos.
    $aux = $xl.Workbooks.Add()
    $vistas = [ordered]@{
        'Modelo de Madurez'  = @('madurez', ('B3:H' + $fila))
        'Heatmap'            = @('mapa_de_calor', "B2:$([char] (64 + 4 + $np))$(5 + $na)")
        'Resultados Heatmap' = @('resultados_mapa', ('B3:G' + ($base + $k - 1)))
    }
    foreach ($hoja in $vistas.Keys) {
        $nombre, $direccion = $vistas[$hoja]
        $rango = $wb.Worksheets.Item($hoja).Range($direccion)
        $rango.CopyPicture(1, 2) | Out-Null   # xlScreen, xlBitmap
        $co = $aux.Worksheets.Item(1).ChartObjects().Add(0, 0, $rango.Width, $rango.Height)
        $co.Activate() | Out-Null
        $co.Chart.Paste() | Out-Null
        $co.Chart.Export((Join-Path (Split-Path $Libro) "$nombre.png")) | Out-Null
        $co.Delete() | Out-Null
    }
    $aux.Close($false)
    $wb.Close($false)
}
catch {
    Write-Host ("Error en la línea " + $_.InvocationInfo.ScriptLineNumber + ": " + $_.Exception.Message)
    if ($wb) { $wb.Close($false) }
    throw
}
finally {
    $xl.Quit()
    [System.Runtime.InteropServices.Marshal]::ReleaseComObject($xl) | Out-Null
    # Las referencias COM que quedan en variables mantienen vivo el proceso; si sigue abierto, se cierra
    # ese proceso (solo el que abrió este script).
    [GC]::Collect()
    [GC]::WaitForPendingFinalizers()
    Start-Sleep -Seconds 2
    if ($pidExcel -and (Get-Process -Id $pidExcel -ErrorAction SilentlyContinue)) { Stop-Process -Id $pidExcel -Force }
}
