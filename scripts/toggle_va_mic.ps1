# toggle_va_mic.ps1

Add-Type -TypeDefinition @"
using System.Runtime.InteropServices;
public class Audio {
    [DllImport("user32.dll")]
    public static extern int SendMessageW(int hWnd, int Msg, int wParam, int lParam);
}
"@

# Load audio endpoint interface via WASAPI (requires AudioDeviceCmdlets or similar)
function Toggle-DefaultMicMute {
    try {
        $device = Get-CimInstance -Namespace root\cimv2 -Class Win32_SoundDevice | Where-Object { $_.Status -eq 'OK' } | Select-Object -First 1
        if (-not $device) {
            Write-Output "No active input device found."
            return
        }

        $shell = New-Object -ComObject WScript.Shell
        $shell.SendKeys([char]173)  # simulate mute key (may vary)

        Write-Output "Toggled mute for default mic (Voice Access)."
    } catch {
        Write-Error "Failed to toggle mic mute: $_"
    }
}

Toggle-DefaultMicMute