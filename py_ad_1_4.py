'''
section 4
Multithreading - Thread(2) - Daemon, join
Keyword - DaemonThread, join

-----------------------------------------------------------------------------------

DaemonThread
(1). 백그라운드에서 실행
(2). 메인스레드 종료 시 즉시 종료
(3). 주로 백그라운드 무한 대기 이벤트 발생 실행하는 부분 담당 -> JVM(가비지컬렉션을 통해 메모리 관리 효율, 메인스레드 보조)
(4). 일반 스레드는 작업 종료시 까지 실행됨, 대몬스레드는 자기가 생성한 스레드가 종료되면 즉시 종료됨
(5). join()은 사용하지않는 것을 권장
(6). 일반스레드 내부에서 대몬스레드를 활용하여 비즈니스 로직을 구현하는 흐름으로 결과물을 낼 수 있도록 구조를 갖춰야함(일반스레드와 라이프사이클을 함께하도록 해야함)
'''

import logging
import threading
import time

# 스레드 실행 함수
def thread_func(name, d):
    logging.info(f"Sub-thread {name}: starting")
    
    for i in d:
        print(f"{i}")
    logging.info(f"Sub-thread {name}: finish")

# 메인 영역
if __name__ == '__main__':
    # Logging format 설정 (디버깅 용이하도록)
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main-thread: before creating thread")
    
    # 함수 인자 확인
    # Daemon : Default False
    x = threading.Thread(target=thread_func, args=('First',range(20000)),daemon=True)
    y = threading.Thread(target=thread_func, args=('Second',range(10000)),daemon=True)
    logging.info("Main-thread: before running thread")
    
    # 서브 스레드 시작
    x.start()
    y.start()
    
    # DaemonThread 확인
    print(x.isDaemon())
    # 주석 전후 결과
    #x.join() #자식 스레드가 마무리 될때까지 기다림
    #y.join()
    
    logging.info("Main-thread: wait for the thread to finish")
    logging.info("Main-thread: all done.")