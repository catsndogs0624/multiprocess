'''
section 7
Multithreading - Thread(5) - Producer vs Consumer Using Queue
Keyword - 생산자 소비자 패턴(Producer/Consumer Pattern)

-----------------------------------------------------------------------------------

Producer-Consumer Pattern
(1). 멀티스레드 디자인 패턴의 정석
(2). 서버 측 프로그래밍의 핵심
(3). 주로 허리 역할 중요

Python Event 객체
(1). Flat 초기값(0)
(2). Set() -> 1, Claer() -> 0, Wait(1 -> 리턴, 0 -> 대기), isSet() -> 현 플래그 상태
    
'''

import concurrent.futures
import logging
import queue
import random
import threading
import time

def producer(queue, event):
    ''' 네트워크 대기 상태라 가정 (서버) ''' # IEO, 네트워크 작업(크롤링, 엑셀 데이터 읽어옴) # 네트워크 작업
    while not event.is_set(): # set 메소드가 호출 될 때 까지
        message = random.randint(1,11)
        logging.info(f'Producer got message: {message}')
        queue.put(message)
        
    logging.info(f'Producer received event. Exiting.')

def consumer(queue, event):
    ''' 응답 받고 소비하는 것으로 가정 or DB 저장 ''' # 프로듀서가 받아온 것을 응답을 주는 등의 역할 # CPU 작업
    while not event.is_set() or not queue.empty():
        message = queue.get()
        logging.info(
            f'Consumer storing message: {message}, (size={queue.qsize()})'
        )
        
    logging.info(f'Consumer received event. Exiting.')

if __name__ == '__main__':
    # Logging format 설정
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    
    
    # 사이즈 중요
    pipeline = queue.Queue(maxsize=10)
    
    # 이벤트 플래그 초기 값 0
    event = threading.Event()
    
    # With context
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)
        
        # 실행 시간 조정
        # while True:
        #     pass
        time.sleep(0.1)
    
    logging.info("Main :  about to set event ")
    
    # 프로그램 종료
    event.set()