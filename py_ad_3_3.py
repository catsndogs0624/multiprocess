'''
section 3
Concurrency, CPU Bound vs I/O Bound - Multiprocessing vs. Threading vs. Async IO
Keyword - CPU Bound, I/O Bound, AsyncIO


CPU Bound vs. IO bound

    CPU Bound
    - 프로세스 진행이 CPU 속도에 의해 제한됨(결정) -> 행렬곱, 고속연산, 파일 압축, 집합 연산 등
    - CPU 연산 위주의 작업
    
    IO Bound
    - 파일 쓰기, 디스크 작업, 네트워크 통신, DB, 시리얼 포트 송수신 -> 작업에 의해서 병목(수행시간이 결정됨)
    - CPU 성능 지표가 수행시간 단축으로 크게 영향을 끼치지 않음
    
    
메모리 바인딩, 캐시바운딩

작업 목적에 따라서 적절한 동시성 라이브러리 선택이 중요


최종 비교

- Multiprocessing : Multiple processes, 고가용성(CPU) Utilization -> CPU Bound -> 10개의 부엌, 10명의 요리사, 10개의 요리
- Threading : Single(Multi) process, Multiple threads, OS decides task switching -> Fast I/O Bound -> 1개의 부엌, 10개의 요리사, 10개의 요리
- AsyncIO : Single process, single thread, cooperative multi tasking, tasks cooperatively decide switching -> Slow I/O Bound -> 1개의 부엌, 1개의 요리사, 10개의 요리

'''