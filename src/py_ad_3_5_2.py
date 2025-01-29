'''
section 3
Concurrency, CPU Bound vs I/O Bound - I/O Bound(3) - threading vs asyncio vs multiprocessing1) - Synchronous
Keyword - I/O Bound, request

'''
import multiprocessing
import requests
import time

# multi pool 예제

# 각 프로세스 메모리 영역에 생성되는 객체(독립적)
# 함수 실행 할 때 마다 객체 생성은 좋지않음 -> 각 프로세스 마다 할당
# 멀티 스레드보다 빠른 결과
# 독립적, 병렬적인 작업 : 멀티프로세싱

session = None

def set_global_session():
    # 함수 실행시점에 만드는거보다 미리 만들어놓으면 더 실행시간 빨라질 수 있음.
    global session
    if not session: # 없으면 만들고 있으면 있는 session 활용
        session = requests.Session()

# 실행 요청 1(다운로드)
def request_site(url):
    
    #세션 확인
    print(f"session : {session}")
    print(f"session.headers : {session.headers}")
    
    with session.get(url) as response:
        name = multiprocessing.current_process().name
        print(f'{name} -> [Read Contents : {len(response.content)}, status code :  {response.status_code} from url]')


# 실행 요청 2
def request_all_sites(urls):
    # 멀티 프로세싱 실행
    # 반드시 processes 개수 조절 후 session 객체 및 실행 시간 확인
    with multiprocessing.Pool(initializer=set_global_session, processes=4) as pool:
        pool.map(request_site, urls)

def main():
    # 테스트 URLs
    urls = ["http://www.jython.org",
            "http://olympus.realpython.org/dice",
            "http://realpython.com"
            ] * 3
    
    # 실행시간 측정
    start_time = time.time()
    
    # 실행
    request_all_sites(urls)
    
    # 실행 시간 종료
    duration = time.time() - start_time
    
    print()
    
    print(f"Downloads {len(urls)} sites in {duration} seconds")
    
    

if __name__ == "__main__":
    main()
    