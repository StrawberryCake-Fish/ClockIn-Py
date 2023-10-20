import subprocess
import psutil
from typing import NoReturn

from src.common import SingletonMeta
from src.utils import Logger, Task


class AppiumStart(metaclass=SingletonMeta):
    process: subprocess.Popen = None

    def start(self) -> NoReturn:
        if self.process is None:
            Task.submit(thread_name='AppiumThread', func=self._exec).start()

    def _exec(self) -> NoReturn:
        self.process = subprocess.Popen(['appium', '-p', '4723'], shell=True, stdout=subprocess.PIPE,
                                        stderr=subprocess.STDOUT)
        while self.process.poll() is None:
            line = self.process.stdout.readline().strip()
            if line:
                Logger.info(line.decode('utf-8'))
        if self.process.returncode != 0:
            Logger.warning('Appium exit!')

    def kill(self) -> NoReturn:
        if self.process is not None:
            child_pid = psutil.Process(self.process.pid).children(recursive=True)
            self.process.kill()
            for i in child_pid:
                i.kill()
            Logger.warning('Appium Kill!')
