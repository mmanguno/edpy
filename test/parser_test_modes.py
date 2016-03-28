import sys  # For quitting

class TestMode(object):

    def __init__(self, pre_args, post_args):
        raise NotImplementedError()

    def run():
        raise NotImplementedError()

    def getIdentifier():
        raise NotImplementedError()


class TestModeOne(TestMode):

    def __init__(self, pre_args, post_args):
        self.pre_args = pre_args
        self.post_args = post_args

    def run(self):
        return "Run testmode1"

    def getIdentifier():
        return '1'

class TestModeTwo(TestMode):

    def __init__(self, pre_args, post_args):
        self.pre_args = pre_args
        self.post_args = post_args

    def run(self):
        return "Run testmode2"

    def getIdentifier():
        return '2'

class TestModeQuit(TestMode):
    def __init__(self, pre_args, post_args):
        self.pre_args = pre_args
        self.post_args = post_args

    def run(self):
        return False

    def getIdentifier():
        return 'q'
