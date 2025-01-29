'''
section 3
Concurrency, CPU Bound vs I/O Bound - I/O Bound(3) - Asyncio basic
Keyword - Asyncio

'''
'''

동시 프로그래밍 패러다임 변화

* 싱글 코어 -> 처리향상 미미, 저하 -> 비동기 프로그래밍 -> CPU연산, DB연동, API 호출 대기 시간 늘어남
(논블럭킹에서 비동기적으로 사용함)
* 파이선 3.4 -> 비동기(asyncio), 표준라이브러리 등장

'''

import time
import asyncio

# Tip!
async def test1(): #-> coroutine object # 예약어 async를 붙임
    await test2() # 비동기함수에서 비동기함수를 실행할 때는 반드시 함수이름 앞에 await을 붙여야함
    
async def test2():
    pass

#.............................................................................

async def exe_calculate_async(name, n):
    for i in range(1, n+1):
        print(f"{name} -> {i} of {n} is calculating...")
        #time.sleep(1) #time.sleep은 동기 함수임
        #await asyncio.sleep(1)
    print(f'{name} - {n} working done!')

async def process_async():
    start = time.time()
    
    await exe_calculate_async('One',3),
    await exe_calculate_async('Two',2),
    await exe_calculate_async('Three',1),
    
    # await asyncio.wait([ # 리스트형태로 한번에 비동기화로
    #     exe_calculate_async('One',3),
    #     exe_calculate_async('Two',2),
    #     exe_calculate_async('Three',1),
    # ])

    end = time.time()
    
    print(f">>> total seconds : {end - start}")


def exe_calculate_sync(name, n): # 동기식
    for i in range(1, n+1):
        print(f"{name} -> {i} of {n} is calculating...")
        time.sleep(1)
        
    print(f'{name} - {n} working done!')

def process_sync():
    start = time.time()
    
    exe_calculate_sync('One',3)
    exe_calculate_sync('Two',2)
    exe_calculate_sync('Three',1)
    
    end = time.time()
    
    print(f">>> total seconds : {end - start}")


if __name__ == "__main__":
    # Sync 실행
    #process_sync()
    
    # Async 실행
    # 파이썬 3.7이상
    asyncio.run(process_async())
    
    # 파이썬 3.7이하
    #asyncio.get_event_loop().run_until_complete(process_async())
     