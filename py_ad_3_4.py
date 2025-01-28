'''
section 3
Concurrency, CPU Bound vs I/O Bound - I/O Bound(1) - Synchronous
Keyword - I/O Bound, request

'''

import requests
import time

# 실행 요청 1(다운로드)
def request_site(url, session):
    #세션 확인
    print(f"session : {session}")
    print(f"session.headers : {session.headers}")
    
    with session.get(url) as response:
        print(f'[Read Contents : {len(response.content)}, status code :  {response.status_code} from url]')

# 실행 요청 2
def request_all_sites(urls):
    with requests.Session() as session:
        for url in urls:
            request_site(url, session)


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
    