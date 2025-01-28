'''
section 2
Parallelism with Multiprocessing - Multiprocesing(1) - Join, is_alive
Keyword - multiprocessing, processing state

-----------------------------------------------------------------------------------
'''
from multiprocessing import Process
import time
import logging

def proc_func(name):
    print(f'Sub-Process {name}: starting')
    time.sleep(3)
    print(f'Sub-Process {name}: finishing')

def main():
    # Logging format 설정
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    
    # 함수 인자 확인
    p = Process(target=proc_func, args=('First',))
    
    logging.info('Main-Process: before creating Process')
    
    # 프로세스
    p.start()
    
    logging.info('Main-Process: During Process')
    
    logging.info('Main-Process: Terminated Process')
    p.terminate() # 프로세스에서는 유휴시간이 길때 특정조건에 만족하면 프로세스 강제 kill 할수 있음.
    logging.info('Main-Process: Joined Process')
    
    p.join()
    
    # 프로세스 상태 확인
    print(f'Process p is alive: {p.is_alive()}')

# 메인 시작
if __name__ == '__main__':
    main()