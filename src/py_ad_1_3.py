'''
section 3
Multithreading - Thread(1) - Basic
Keyword - Threading basic

-----------------------------------------------------------------------------------

'''

import logging
import threading
import time

# 스레드 실행 함수
def thread_func(name):
    logging.info(f"Sub-thread {name}: starting")
    time.sleep(3)
    logging.info(f"Sub-thread {name}: finish")

# 메인 영역
if __name__ == '__main__':
    # Logging format 설정 (디버깅 용이하도록)
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main-thread: before creating thread")
    
    # 함수 인자 확인
    x = threading.Thread(target=thread_func, args=('First',))
    logging.info("Main-thread: before running thread")
    
    # 서브 스레드 시작
    x.start()
    
    # 주석 전후 결과
    x.join() #자식 스레드가 마무리 될때까지 기다림
    
    logging.info("Main-thread: wait for the thread to finish")
    logging.info("Main-thread: all done.")