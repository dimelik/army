class Army(object):
    _soldiers = []
    _weaponPrice = None

    def __init__(self, *args):
        if not issubclass(args, Soldier):
            raise Exception("TypeError")
        self._soldiers.append(args)


