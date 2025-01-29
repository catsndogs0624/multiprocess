'''
section 3
Concurrency, CPU Bound vs I/O Bound - CPU Bound(1) - Synchronous
Keyword - CPU Bound
'''

# CPU-Bound 예제
# I/O를 최소화하고 벡터연산등 할때 멀티프로세싱을 사용해야 성능이 압도적으로 좋아짐

import time

# 실행 함수 (계산)
def cpu_bound(number):
    return sum(i * i for i in range(number))

# 실행 함수 (계산)
def find_sums(numbers):
    result = []
    for number in numbers:
        result.append(cpu_bound(number))
    return result

def main():
    numbers = [3_000_000 + x for x in range(30)]
    
    print(numbers)
    
    
    # 실행 시간 측정
    start_time = time.time()
    
    # 실행
    total = find_sums(numbers)
    
    # 실행 시간 종료
    duration = time.time() - start_time
    
    print()
    
    # 결과 출력
    print(f"Total list : {total}")
    print(f"Sum : {sum(total)}")
    
    # 수행 시간
    print(f"Duration : {duration} seconds")
    

if __name__ == "__main__":
    main()