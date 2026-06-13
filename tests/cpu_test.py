import psutil

def test_cpu():
    print(psutil.cpu_freq(percpu=True))
    print('---------------------------------')
    print(f'User: {psutil.cpu_times().user:.2f}')
    print(f'System: {psutil.cpu_times().system:.2f}')
    print(f'Idle: {psutil.cpu_times().idle:.2f}')
    print(f'Percent: {psutil.cpu_percent(interval=1)}%')
    print(f'Logical Cores: {psutil.cpu_count(logical=True)}')
    print(f'Physical Cores: {psutil.cpu_count(logical=False)}')
test_cpu()