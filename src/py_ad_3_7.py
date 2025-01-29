'''
section 3
Concurrency, CPU Bound vs I/O Bound - CPU Bound(2) - Multiprocessing
Keyword - CPU Bound
'''

# CPU-Bound Multiprocessing 예제
# I/O를 최소화하고 벡터연산등 할때 멀티프로세싱을 사용해야 성능이 압도적으로 좋아짐

# 프로세스의 처리 프로세싱에서 데이터쉐어가 정말 쉽게 공유가 되도록 함
# Manager shared memory

from multiprocessing import current_process, Array, Manager, Process,freeze_support
import time
import os

# 실행 함수 (계산)
def cpu_bound(number, total_list):
    process_id = os.getpid()
    process_name = current_process().name
    
    # Process 정보 출력
    print(f"Process ID : {process_id}, Process Name : {process_name}")
    
    total_list.append(sum(i * i for i in range(number)))



def main():
    numbers = [3_000_000 + x for x in range(30)]
    
    print(numbers)
    
    # 프로세스 리스트 선언
    processes = list()
    
    # 프로세스 공유 매니저 # 하나의 영역을 메모리에 공간을 생성하여 프로세스 리스트를 넘김
    manager = Manager()
    
    # 리스트 획득(프로세스 공유)
    total_list = manager.list()
    
    # 실행 시간 측정
    start_time = time.time()
    
    # 프로세스 생성 및 실행
    for i in numbers:
        # 생성
        t = Process(name=str(i), target=cpu_bound, args=(i,total_list)) #(process_id, 프로세스 리스트)
         
        # 배열에 담기
        processes.append(t)
        
        # 시작
        t.start()
        
    # Join
    for process in processes:
        process.join() #모든 프로세스가 작업완료될때까지 대기를 함    
    
    # 실행 시간 종료
    duration = time.time() - start_time
    
    print()
    
    # 결과 출력
    print(f"Total list : {total_list}")
    print(f"Sum : {sum(total_list)}")
    
    # 수행 시간
    print(f"Duration : {duration} seconds")
    

if __name__ == "__main__":
    # 윈도우에서 예외가 발생 시
    # freeze_support()
    main()