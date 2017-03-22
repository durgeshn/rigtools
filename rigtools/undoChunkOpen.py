from pymel import core as pm


class UndoChunkOpen(object):
    def __init__(self, chunkName=''):
        self._name = chunkName

    def __enter__(self):
        pm.undoInfo(chunkName=self._name, openChunk=True)

    def __exit__(self, *_):
        pm.undoInfo(chunkName=self._name, closeChunk=True)
