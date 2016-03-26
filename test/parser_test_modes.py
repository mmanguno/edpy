from edpy.modes import Mode

class TestModeOne(Mode):

    def __init__(self, pre_args, post_args):
        self.pre_args = pre_args
        self.post_args = post_args

    def run():
        return "Run testmode1"

    def getIdentifier():
        return 'test1'

class TestModeTwo(Mode):

    def __init__(self, pre_args, post_args):
        self.pre_args = pre_args
        self.post_args = post_args

    def run():
        return "Run testmode2"

    def getIdentifier():
        return 'test2'
