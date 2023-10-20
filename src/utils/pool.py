from __future__ import annotations
import queue
import threading
from typing import NoReturn, Optional, Callable, Any


class ThreadPool:
    def __init__(self, max_workers: Optional[int]):
        self.max_workers = max_workers
        self.tasks = queue.Queue()
        self.workers = []

    def submit(self, func: Optional[Callable], *args: Optional[Any], thread_name: Optional[str] = None,
               **kwargs: Optional[Any]) -> ThreadPool:
        self.tasks.put((func, args, kwargs, thread_name))
        return self

    def start(self) -> NoReturn:
        for i in range(self.max_workers):
            worker = threading.Thread(target=self._worker)
            worker.daemon = True
            worker.start()
            self.workers.append(worker)

    def _worker(self) -> NoReturn:
        while True:
            func, args, kwargs, thread_name = self.tasks.get()
            try:
                if thread_name:
                    threading.current_thread().name = thread_name
                func(*args, **kwargs)
            except Exception as e:
                print(e)
            finally:
                self.tasks.task_done()

    def wait_completion(self) -> NoReturn:
        self.tasks.join()
