from datetime import datetime


def main():
    fake_nvidia_smi_output = """+------------------------------------------------------------------------------+
| NVIDIA-SMI 545.29.06     Driver Version: 545.29.06    CUDA Version: 11.8     |
|--------------------------------+----------------------+----------------------+
| GPU  Name         Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                                |                      |               MIG M. |
|================================+======================+======================|
|   0  NVIDIA H100 PCIe     Off  | 00000000:01:00.0 Off |                    0 |
| N/A   48C    P0     51W / 350W |      0MiB / 81559MiB |      0%      Default |
|                                |                      |             Disabled |
+--------------------------------+----------------------+----------------------+
|   1  NVIDIA H100 PCIe     Off  | 00000000:21:00.0 Off |                    0 |
| N/A   49C    P0     53W / 350W |      0MiB / 81559MiB |      0%      Default |
|                                |                      |             Disabled |
+--------------------------------+----------------------+----------------------+
|   2  NVIDIA H100 PCIe     Off  | 00000000:41:00.0 Off |                    0 |
| N/A   48C    P0     52W / 350W |      0MiB / 81559MiB |      0%      Default |
|                                |                      |             Disabled |
+--------------------------------+----------------------+----------------------+
|   3  NVIDIA H100 PCIe     Off  | 00000000:61:00.0 Off |                    0 |
| N/A   48C    P0     49W / 350W |      0MiB / 81559MiB |      0%      Default |
|                                |                      |             Disabled |
+--------------------------------+----------------------+----------------------+
|   4  NVIDIA H100 PCIe     Off  | 00000000:81:00.0 Off |                    0 |
| N/A   49C    P0     81W / 350W |      0MiB / 81559MiB |      0%      Default |
|                                |                      |             Disabled |
+--------------------------------+----------------------+----------------------+
|   5  NVIDIA H100 PCIe     Off  | 00000000:A1:00.0 Off |                    0 |
| N/A   51C    P0     81W / 350W |      0MiB / 81559MiB |      0%      Default |
|                                |                      |             Disabled |
+--------------------------------+----------------------+----------------------+
|   6  NVIDIA H100 PCIe     Off  | 00000000:C1:00.0 Off |                    0 |
| N/A   51C    P0     81W / 350W |      0MiB / 81559MiB |      0%      Default |
|                                |                      |             Disabled |
+--------------------------------+----------------------+----------------------+
|   7  NVIDIA H100 PCIe     Off  | 00000000:E1:00.0 Off |                    0 |
| N/A   50C    P0     81W / 350W |      0MiB / 81559MiB |      0%      Default |
|                                |                      |             Disabled |
+--------------------------------+----------------------+----------------------+

+------------------------------------------------------------------------------+
| Processes:                                                                   |
|  GPU   GI   CI        PID   Type   Process name                   GPU Memory |
|        ID   ID                                                    Usage      |
|==============================================================================|
|  No running processes found                                                  |
+------------------------------------------------------------------------------+
"""
    
    # an nvidia-smi output starts with a date and time
    print(datetime.now().strftime("%a %b %d %H:%M:%S %Y"))
    print(fake_nvidia_smi_output)

if __name__ == "__main__":
    main()