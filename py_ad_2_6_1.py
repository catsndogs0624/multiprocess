'''
section 2
Parallelism with Multiprocessing - Multiprocesing(6) - Queue, Pipe
Keyword - Queue, Pipe, Communications between processes

-----------------------------------------------------------------------------------
'''

# 프로세스 통신 구현 Queue

from multiprocessing import Process, Queue, current_process
import time
import os

def worker(id, baseNum, q):
    process_id = os.getpid()
    process_name = current_process().name

    # 누적
    sub_total = 0
    
    # 계산
    for i in range(baseNum):
        sub_total += 1
        
    # Produce
    q.put(sub_total)
    
    # 정보 출력
    print(f'Process ID: {process_id}')
    print(f'Process Name: {process_name}')
    print(f'ID: {id}')
    print(f'Result: {sub_total}')
    

def main():
    # 부모 프로세스 아이디
    parent_process_id = os.getpid()
    # 출력
    print(f"parent_process_id : {parent_process_id}")
    
    # 프로세스 리스트 선언
    processes = list()
    
    # 시작 시간
    start_time = time.time()
    
    # Queue 선언
    q = Queue()
    
    for i in range(100):
        # 생성
        p = Process(name=str(i), target=worker, args=(1, 100000000, q))
        
        # 배열에 담기
        processes.append(p)
        
        # 시작
        p.start()
    
    # Join : 완료될때까지 기다림
    for process in processes:
        process.join()
        
    # 순수 계산 시작
    print("---%s seconds ---" % (time.time()-start_time))
    
    # 종료 플래그
    q.put('exit')
    total = 0
    
    # 대기
    while True:
        tmp = q.get()
        if tmp == 'text':
            break
        else:
            total += tmp
            
    print()
    
    print('Main Processing Total Count={}',format(total))
    print('Main processing Done!')
        

if __name__ == '__main__':
    main()