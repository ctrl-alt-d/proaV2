from random import sample

_CARACTERSVALIDS = "ABCDDEFGHJKMNOPQRTVWXYZ2346789"


def calculacodi():
    return "".join(sample(_CARACTERSVALIDS, 5))
