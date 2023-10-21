from src.event.event import ClockEvents
from src.handle import AbstractHandler, Handler
from src.utils import Logger


class StartHandler(AbstractHandler):
    def handle(self, request: ClockEvents) -> Handler | ClockEvents:
        if request == ClockEvents.START:
            Logger.info(f'StartHandler ==> {request.name}')
            activity = self.get_driver().current_activity
            match activity:
                case '.biz.LaunchHomeActivity':
                    return super().handle(ClockEvents.CLOCK)
                case 'com.alibaba.lightapp.runtime.ariver.TheOneActivityMainTaskSwipe':
                    return super().handle(ClockEvents.CLOCK)
                case _:
                    # TODO 执行登录操作
                    pass
            return super().handle(ClockEvents.get_event(request.do_action()))
        else:
            return super().handle(request)


class CheckHandler(AbstractHandler):
    def handle(self, request: ClockEvents) -> Handler | ClockEvents:
        if request == ClockEvents.CHECK:
            Logger.info(f'CheckHandler ==> {request.name}')
            return super().handle(ClockEvents.get_event(request.do_action()))
        else:
            return super().handle(request)


class ClockHandler(AbstractHandler):
    def handle(self, request: ClockEvents) -> Handler | ClockEvents:
        if request == ClockEvents.CLOCK:
            Logger.info(f'ClockHandler ==> {request.name}')
            return super().handle(ClockEvents.get_event(request.do_action()))
        else:
            return super().handle(request)


class RestartHandler(AbstractHandler):
    def handle(self, request: ClockEvents) -> Handler | ClockEvents:
        if request == ClockEvents.RESTART:
            Logger.info(f'RestartHandler ==> {request.name}')
            return super().handle(ClockEvents.get_event(request.do_action()))
        else:
            return super().handle(request)


class DoneHandler(AbstractHandler):
    def handle(self, request: ClockEvents) -> Handler | ClockEvents:
        if request == ClockEvents.DONE:
            Logger.info(f'DoneHandler ==> {request.name}')
            return super().handle(ClockEvents.get_event(request.do_action()))
        else:
            return super().handle(request)
