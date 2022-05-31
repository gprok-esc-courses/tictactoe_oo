
class AbstractWindow:
    def display_status(self, msg):
        raise NotImplementedError

    def reset(self):
        raise NotImplementedError
