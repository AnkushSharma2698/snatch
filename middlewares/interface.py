import abc

class SnatchMiddleware(metaclass=abc.ABCMeta):

    @abc.abstractstaticmethod
    def before(event, context):
        ...

    @abc.abstractstaticmethod
    def after(event, context):
        ...

    @abc.abstractstaticmethod
    def onfail(event, context):
        ...

