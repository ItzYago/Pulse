from dashing import VGauge, VSplit
from cpu_test import test_cpu
import time

ui = VSplit(
        VSplit(
            VGauge(val=50, title="CPU", border_color=50),
        )
    )
# access a tile by index
cpu = ui.items[0].items[0]

while True:
    cpu.value = test_cpu()
    ui.display()
    time.sleep(1)