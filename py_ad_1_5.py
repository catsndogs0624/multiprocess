'''
section 5
Multithreading - Thread(3) - ThreadPoolExecutor
Keyword - Many threads, concurrent.futures, (xxx)PoolExecutor

-----------------------------------------------------------------------------------

GroupThread
(1). Python 3.2 이상 표준 라이브러리 사용
(2). concurrent.futures
(3). with 사용으로 생성, 소멸 라이프사이클 관리 용이
(4). 디버깅하기가 난해함(단점) -> 운영체제를 기반으로 지식을 표준화하여 사용할 수 있도록 할 것.
(5). 대기중인 작업 -> 내부적으로 Queue(FIFO) -> 완료 상태 조사 -> flag 값 조사해서 결과 또는 예외(ex.웹크롤링) -> 단일화(캡슐화)


'''

import logging
from concurrent.futures import ThreadPoolExecutor
import time


def task(name):
    logging.info(f'Sub-thread {name} : starting')
    result = 0
    for i in range(10001):
        result = result + i
    
    logging.info(f'Sub-Thread {name}: finishing result: {result}')
    return result

def main():
    # Logging format 설정 (디버깅 용이하도록)
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main-thread: before creating thread")
    
    logging.info("Main-Thread : before creating and running thread")
    
    # 실행 방법1
    # max_workers : 작업의 개수가 넘어가면 직접 설정이 유리
    executor = ThreadPoolExecutor(max_workers=3)
    #task1 = executor.submit(task,('First',))
    #task2 = executor.submit(task,('Second',))

    # 결과값 있을 경우
    # print(task1.result()) 
    # print(task1.result()) 
    
    # 실행 방법2
    with ThreadPoolExecutor(max_workers=3) as executor:
        tasks = executor.map(task, ['First','Second'])
        # 결과 확인
        print(list(tasks))

if __name__ == '__main__':
    main()
