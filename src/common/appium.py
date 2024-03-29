from __future__ import annotations
import subprocess
import psutil
import src
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from psutil import NoSuchProcess
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from typing import NoReturn
from appium import webdriver
from appium.options.common import AppiumOptions
from src.common import SingletonMeta
from src.common.const import ConfigConst
from src.utils import Logger, Task


class AppiumStart(metaclass=SingletonMeta):
    _process: subprocess.Popen | None = None

    def start(self) -> NoReturn:
        if self._process is None:
            Task.submit(thread_name='AppiumThread', func=self._exec).start()

    def _exec(self) -> NoReturn:
        self._process = subprocess.Popen(
            ['appium', '-p', str(src.CONF.get(ConfigConst.APPIUM_CONFIG)['port'])],
            shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        try:
            while self._process.poll() is None:
                line = self._process.stdout.readline().strip()
                if line:
                    pass
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
    def __init__(self) -> NoReturn:
        self.package = src.CONF.get(ConfigConst.APPIUM_SECTION)['appPackage']
        self.activity = src.CONF.get(ConfigConst.APPIUM_SECTION)['appActivity']
        self._driver: WebDriver | None = None
        self._options = AppiumOptions()
        for k, v in src.CONF.get(ConfigConst.APPIUM_SECTION).items():
            self._options.set_capability(k, v)

    def driver(self) -> WebDriver:
        if self._driver is None:
            port = src.CONF.get(ConfigConst.APPIUM_CONFIG)["port"]
            self._driver = webdriver.Remote(
                command_executor=f'http://127.0.0.1:{port}', options=self._options)
            self.restart()
        return self._driver

    def restart(self) -> NoReturn:
        Logger.info('Application restart.')
        self._driver.terminate_app(self.package)
        self._driver.activate_app(f'{self.package}/{self.activity}')

    def quit(self) -> NoReturn:
        if self._driver is not None:
            # self._driver.terminate_app(self.package)
            self._driver.quit()
            self._driver = None
        Logger.info('Driver quit.')

    def wait(self, locator: tuple[str, str],
             timeout: int = int(
                 src.CONF.get(ConfigConst.APPIUM_CONFIG)['timeout'])) -> WebElement | bool:
        try:
            return (WebDriverWait(driver=self._driver, timeout=timeout, poll_frequency=0.5)
                    .until(expected_conditions.presence_of_element_located(locator)))
        except Exception as e:
            Logger.error(e)
            return False
