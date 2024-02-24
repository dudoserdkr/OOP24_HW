class initDelTest():
    def __init__(self):
        print("InitDelTest")

    def __del__(self):
        print("InitDeltest: __del__")


initDel = initDelTest()