'''
section 3
Concurrency, CPU Bound vs I/O Bound - I/O Bound(2) - threading vs asyncio vs multiprocessing
Keyword - I/O Bound, request

'''
import concurrent.futures
import threading
import requests
import time

# I/O Bound Threading 예제
# 일반적인 IO 바운드는 Threading, asyncio 활용하면 더 빠름

# 각 스레드에 생성되는 객체 (독립된 네임스페이스 영역을 활용함): 공유되지않는 메모리 생성하기위해서
thread_local = threading.local()

def get_sesssion():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session

# 실행 요청 1(다운로드)
def request_site(url):
    # 세션 획득
    session = get_sesssion()
    
    #세션 확인
    print(f"session : {session}")
    print(f"session.headers : {session.headers}")
    
    with session.get(url) as response:
        print(f'[Read Contents : {len(response.content)}, status code :  {response.status_code} from url]')


# 실행 요청 2
def request_all_sites(urls):
    # 멀티 스레드 실행
    # 반드시 max_worker 개수 조절 후 session 객체 확인
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(request_site, urls)

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
    