import subprocess
import psutil
import src
from appium.webdriver.webdriver import WebDriver
from psutil import NoSuchProcess
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from typing import NoReturn
from appium import webdriver
from appium.options.common import AppiumOptions
from src.common import SingletonMeta
from src.common.const import ConfigEnums
from src.utils import Logger, Task


class AppiumStart(metaclass=SingletonMeta):
    _process: subprocess.Popen | None = None

    def start(self) -> NoReturn:
        if self._process is None:
            Logger.info('AppiumStart.start')
            Task.submit(thread_name='AppiumThread', func=self._exec).start()

    def _exec(self) -> NoReturn:
        self._process = subprocess.Popen(['appium', '-p', ConfigEnums.APPIUM_PORT.value], shell=True,
                                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        try:
            while self._process.poll() is None:
                line = self._process.stdout.readline().strip()
                if line:
                    Logger.info(line.decode('utf-8'))
        except Exception as e:
            Logger.error(e)
        if self._process.returncode != 0:
            Logger.warning('Appium exit!')

    def kill(self) -> NoReturn:
        try:
            if self._process is not None:
                child_pid = psutil.Process(self._process.pid).children(recursive=True)
                self._process.kill()
                for i in child_pid:
                    i.kill()
                Logger.warning('Process Kill!')
        except NoSuchProcess as e:
            Logger.warning(f'Process Kill (pid={e.pid})')
            self._process = None


class AppiumDriver(metaclass=SingletonMeta):
    _driver: WebDriver

    def __init__(self) -> NoReturn:
        options = AppiumOptions()
        for k, v in src.CONF.get(ConfigEnums.APPIUM_SECTION.value).items():
            options.set_capability(k, v)
        self._driver = webdriver.Remote(
            command_executor=f'http://127.0.0.1:{ConfigEnums.APPIUM_PORT.value}',
            options=options
        )

    def driver(self) -> WebDriver:
        return self._driver

    def quit(self) -> NoReturn:
        if self._driver:
            self._driver.quit()

    @staticmethod
    def wait(driver: WebDriver, locator: tuple[str, str]) -> NoReturn:
        try:
            return WebDriverWait(driver=driver, timeout=int(src.CONF.get(ConfigEnums.APPIUM_CONFIG.value)['timeout']),
                                 poll_frequency=0.5).until(expected_conditions.presence_of_element_located(locator))
        except Exception as e:
            Logger.error(e)
