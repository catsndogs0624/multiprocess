'''
section 2
Parallelism with Multiprocessing - Multiprocesing(4) - Sharing state
Keyword - memory sharing, array, value

-----------------------------------------------------------------------------------
'''

from multiprocessing import Process, current_process, Value, Array
import os

# 프로세스 메모리 공유 예제 (공유 O !!!!)

# 실행 함수

def generate_update_number(v: int): # Thread 처럼 락으로 처리할수도 있음
    for _ in range(50):
        v.value += 1 # 객체가 넘어 오기때문에 값에 접근할때는 .value
    print(f"{current_process().name}, 'data', {v.value}")
    
def main():
    # 부모 프로세스 아이디
    parent_process_id = os.getpid()
    # 출력
    print(f"Parent Process ID {parent_process_id}")
    
    # 프로세스 리스트 선언
    processes = list()
    
    # 프로세스 공유 확인 (메모리 공유 변수)
    '''
    https://docs.python.org/3/library/multiprocessing.shared_memory.html
    from multiprocess import shared_memory 사용 가능(python 3.8)
    from multiprocess import Manager 사용 가능
    '''
    # shared_numbers = Array('i',range(50)) # 공유할 타입을 리스트로 받아올 경우
    shared_value = Value('i', 0) # 공유할 타입 선언, 초기값 선언 # 프로그램에 크리티컬한 영향을 미치기때문에 엄격하게 처리
    
    for _ in range(1, 10):
        # 생성
        p = Process(target=generate_update_number, args=(shared_value,))
        # 배열에 담기
        processes.append(p)
        # 
        p.start()
        
    # Join
    for p in processes:
        p.join()
        
    # 최종 프로세스 부모 변수 확인
    print('Final Data in parent process', shared_value.value)

if __name__ == '__main__':
    main()    

