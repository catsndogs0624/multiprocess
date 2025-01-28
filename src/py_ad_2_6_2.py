'''
section 2
Parallelism with Multiprocessing - Multiprocesing(6) - Queue, Pipe
Keyword - Queue, Pipe, Communications between processes

-----------------------------------------------------------------------------------
'''

# 프로세스 통신 구현 Queue

from multiprocessing import Process, Pipe, current_process
import time
import os

def worker(id, baseNum, conn):
    process_id = os.getpid()
    process_name = current_process().name

    # 누적
    sub_total = 0
    
    # 계산
    for _ in range(baseNum):
        sub_total += 1
        
    # Produce 보냄
    conn.send(sub_total)
    conn.close() # pipe는 보내고 무조건 닫아줘야함
    
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
    
    # 시작 시간
    start_time = time.time()
    
    # Pipe 선언
    parent_conn , child_conn = Pipe()
    
    # 생성
    t = Process(name=str(1), target=worker, args=(1, 100000000, child_conn))
    
    # 시작
    t.start()
    
    # join
    t.join()
        
    # 순수 계산 시작
    print("---%s seconds ---" % (time.time()-start_time))
            
    print()
    
    print('Main Processing Total Count={}'.format(parent_conn.recv()))
    print('Main processing Done!')
        

if __name__ == '__main__':
    main()