# This is already Deprecated it is going to be removed soon.


class Queue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        return self.queue.pop(0)


class DataContainer:

    def __init__(self, **metadata):
        self.metadata = metadata

    def edit_metadata(self, key, value):
        self.metadata[key] = value

    def add_metadata_key(self, key):
        for x in self.metadata.keys():
            self.metadata[x] += {key: None}

    def remove_metadata_key(self, key):
        for x in self.metadata.keys():
            del self.metadata[x][key]


class Product(DataContainer):

    def add_batch(self, batchname, **metadata):
        self.metadata += {batchname: metadata}

    def remove_batch(self, batchname):
        self.metadata.pop(batchname)

class Client(DataContainer):
    pass
