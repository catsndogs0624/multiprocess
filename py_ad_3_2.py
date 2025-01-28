'''
section 3
Concurrency, CPU Bound vs I/O Bound - Blocking vs Non-Blocking IO
Keyword - Blocking IO, No-Blocking IO, Sync, Async

----------------------------------------------------------------------------------

Blocking IO vs. Non-Blocking IO (대기 or 계속 완료여부 확인)

    Blocking IO
    - 시스템 콜 요청 시 -> 운영체제 커널 IO 작업 완료 시 까지 응답 대기 (카톡 보내놓고 가만히 기다림)
    - 제어권이 IO작업에게 있음 -> 커널이 소유 -> 응답(Response)전 까지 대기(Block) -> 다른 작업 수행 불가(대기)
    
    Non-blocking IO
    - 시스템 콜 요청 시 -> 운영체제 커널에서 IO 작업 완료 여부 상관 없이 즉시 응답 (카톡 보내놓고 완료됐는지 계속 확인)
    - 제어권이 IO작업에게 있음 -> 유저프로세스 -> 다른 작업 수행 가능(지속) -> 주기적으로 시스템 콜 통해서 IO 작업 완료 여부 확인
    
    Async vs. Sync (콜백을 누가 주느냐)

        Async : IO 작업 완료 여부에 대한 노티는 커널(호출되는 함수) -> 유저 프로세스(호출하는 함수)
        Sync : IO 작업 완료 여부에 대한 노티는 유저프로세스(호출하는 함수) -> 커널(호출되는 함수)


'''