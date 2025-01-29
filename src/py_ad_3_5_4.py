'''
section 3
Concurrency, CPU Bound vs I/O Bound - I/O Bound(3) - threading vs asyncio vs multiprocessing1) - Synchronous
Keyword - I/O Bound, asyncio

'''
import multiprocessing
#import requests # 동기식
import aiohttp # 비동기식
import asyncio
import time

# I/O Bound Asyncio 예제
# threading 보다 높은 코드 복잡도 -> Async, await 적절하게 코딩



# 실행 요청 1(다운로드)
async def request_site(url,session):
    
    #세션 확인
    print(f"session : {session}")
    print(f"session.headers : {id(session.headers)}")
    
    async with session.get(url) as response:
        print(f"Read Contents {response.content_length}, from {url}")

# 실행 요청 2
async def request_all_sites(urls):
    # 멀티 프로세싱 실행
    # 반드시 processes 개수 조절 후 session 객체 및 실행 시간 확인
    async with aiohttp.ClientSession() as session:
        # 작업 목록
        tasks = []
        
        for url in urls:
            task = asyncio.ensure_future(request_site(url, session))
            tasks.append(task)
            
        # 태스크 확인
        print(*tasks)
        print(tasks)
        
        await asyncio.gather(*tasks, return_exceptions=True) # 작업들을 모아줌

def main():
    # 테스트 URLs
    urls = ["http://www.jython.org",
            "http://olympus.realpython.org/dice",
            "http://realpython.com"
            ] * 3
    
    # 실행시간 측정
    start_time = time.time()
    
    # 실행
    # Async 실행
    # 파이썬 3.7이상
    #asyncio.run(request_all_sites(urls))
    
    # 파이썬 3.7이하
    #asyncio.get_event_loop().run_until_complete(process_async())
    asyncio.get_event_loop().run_until_complete(request_all_sites(urls))
    
    
    # 실행 시간 종료
    duration = time.time() - start_time
    
    print()
    
    print(f"Downloads {len(urls)} sites in {duration} seconds")
    
    

if __name__ == "__main__":
    main()
    