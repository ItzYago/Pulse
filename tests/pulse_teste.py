from cpu_test import test_cpu
import time
import test_pc
import disk_test
import network_test
import process_test
import memory_test

def main():

   
    cputest = test_cpu()
    print(f'CPU Test: {cputest}%')
    memory = (f'Memeory: {memory_test()}%')
    print(memory)
main()

def test_diplay():
    print(f'Display CPU: {test_pc()}%')