from middlewares.interface import SnatchMiddleware

class TestMiddleware(SnatchMiddleware):

    @staticmethod
    def before(event, context):
        pass

    @staticmethod
    def after(event, context):
        pass

    @staticmethod
    def onfail(event, context):
        pass

middleware = {
    "before" : TestMiddleware.before,
    "after": TestMiddleware.after,
}
