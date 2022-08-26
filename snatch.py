from typing import Callable, List
from enum import Enum

from middlewares.interface import SnatchMiddleware


class InjectionPoint(str, Enum):
    """
    These are the lifecycle events around the execution of a lambda handler
    """
    before = "before"
    after = "after"
    onfail = "onfail"


class Snatch():
    def __init__(self, method):
        self.method: Callable = method
        self.before: List[Callable] = []
        self.after: List[Callable] = []
        self.onfail: List[Callable] = []

    def apply(self, middleware: dict):
        if middleware.get(InjectionPoint.before):
            self.before.append(middleware[InjectionPoint.before])
        if middleware.get(InjectionPoint.after):
            self.after.append(middleware[InjectionPoint.after])
        if middleware.get(InjectionPoint.onfail):
            self.onfail.append(middleware[InjectionPoint.onfail])        
        return self

    def __call__(self, event, context):
        response = None
        print(event)
        print(context)
        try:
            self.apply_middlewares(self.before, event, context)
            response = self.method(event, context)
            self.apply_middlewares(self.after, event, context)
        except:
            self.apply_middlewares(self.onfail, event, context)
        return response

    def apply_middlewares(self, middlewares: List[SnatchMiddleware], event, context) -> None:
        for middleware in middlewares:
            print(middleware)
            print(middleware(1, 2))
