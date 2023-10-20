from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import NoReturn


@dataclass
class BaseDto(ABC):

    @classmethod
    @abstractmethod
    def from_dict(cls, data: dict) -> NoReturn:
        pass


@dataclass
class Element(BaseDto):

    @classmethod
    def from_dict(cls, data: dict) -> NoReturn:
        pass
