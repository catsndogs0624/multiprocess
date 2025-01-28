'''
section 2
Parallelism with Multiprocessing - Multiprocesing(4) - Sharing state
Keyword - memory sharing, array, value

-----------------------------------------------------------------------------------
'''

from multiprocessing import Process, current_process
import os

# 프로세스 메모리 공유 예제 (공유x)

# 실행 함수

def generate_update_number(v: int):
    for _ in range(50):
        v += 1
    print(f"{current_process().name}, 'data', {v}")
    
def main():
    # 부모 프로세스 아이디
    parent_process_id = os.getpid()
    # 출력
    print(f"Parent Process ID {parent_process_id}")
    
    # 프로세스 리스트 선언
    processes = list()
    
    # 프로세스 공유 확인 (메모리 공유 변수)
    shared_value = 0
    
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
    print('Final Data in parent process', shared_value)

if __name__ == '__main__':
    main()    

