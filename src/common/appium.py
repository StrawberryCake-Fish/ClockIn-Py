import subprocess
import psutil
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import src
from typing import NoReturn
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.webdriver import WebDriver
from src.common import SingletonMeta
from src.common.enums import ConfigEnums
from src.env import Env
from src.utils import Logger, Task


class AppiumStart(metaclass=SingletonMeta):
    Env().argument()
    _process: subprocess.Popen = None

    def start(self) -> NoReturn:
        if self._process is None:
            Task.submit(thread_name='AppiumThread', func=self._exec).start()

    def _exec(self) -> NoReturn:
        self._process = subprocess.Popen(['appium', '-p', ConfigEnums.APPIUM_PORT.value], shell=True,
                                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        while self._process.poll() is None:
            line = self._process.stdout.readline().strip()
            if line:
                Logger.info(line.decode('utf-8'))
        if self._process.returncode != 0:
            Logger.warning('Appium exit!')

    def kill(self) -> NoReturn:
        if self._process is not None:
            child_pid = psutil.Process(self._process.pid).children(recursive=True)
            self._process.kill()
            for i in child_pid:
                i.kill()
            Logger.warning('Appium Kill!')


class AppiumDriver(metaclass=SingletonMeta):
    _driver: WebDriver = None

    def __init__(self) -> NoReturn:
        options = AppiumOptions()
        for k, v in src.CONF.dict().get(ConfigEnums.APPIUM_SECTION.value).items():
            options.set_capability(k, v)
        self._driver = webdriver.Remote(
            command_executor=f'http://127.0.0.1:{ConfigEnums.APPIUM_PORT.value}/wd/hub',
            options=options
        )

    def driver(self) -> NoReturn:
        return self._driver

    def quit(self) -> NoReturn:
        if self._driver:
            self._driver.quit()

    @staticmethod
    def wait(driver: WebDriver, locator: tuple[str, str]) -> NoReturn:
        try:
            return WebDriverWait(driver=driver, timeout=int(src.CONF.dict().get(ConfigEnums.APPIUM_CONFIG)['timeout']),
                                 poll_frequency=0.5).until(expected_conditions.presence_of_element_located(locator))
        except Exception as e:
            Logger.error(e)
