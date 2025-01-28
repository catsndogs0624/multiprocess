'''
section 2
Multithreading - Python's GIL
Keyword - CPython, 메모리 관리, GIL 사용이유

-----------------------------------------------------------------------------------

GIL(Global Interpreter Lock)
    (1). CPython -> 작성된 python 코드를 bytecode로 바뀌어서 CPython이 실행됨
    -> 실행 시 여러 thread 사용할 경우
아래의 그림과 같이 여러 thread로 사용할때, 한 타이밍에 한 스레드에만 접근 할 수 있게 제한해놓음 -> GIL

 

(2) CPython 메모리 관리가 취약하기 때문(즉, Thread-safe)

 

(3) 단일 스레드로 충분히 빠르다

 

(4) 프로세스 사용 가능(Numpy,Scipy)등 GIL 외부 영역에서 효율적인 코딩

 

(5) 병렬 처리는 multiprocessing, asyncio 선택지 다양함

 

(6) thread 동시성 완벽 처리를 위해 -> Jypthon, IronPython, Stackless Python 등이 존재




'''