from bitarray import bitarray


class IDPool(object):
    '''
    Create a pool of IDs to allow reuse. The "new_id" function generates the next
    valid ID from the previous one. If not given, defaults to incrementing an integer.
    '''

    def __init__(self, size):
        self.max_size = size
        self.IDs = bitarray(2*size-1)
        self.IDs.setall(0)
        self.last_id = 0

    def get_id(self):
        index = 0

        while index < self.max_size-1:
            if not self.IDs[2*index+1]:
                index = 2*index+1
            elif not self.IDs[2*index+2]:
                index = 2*index+2
            else:
                return -1

        self.IDs[index] = 1
        self.update_tree(index)
        return index - self.max_size + 1

    def update_tree(self, index):
        while index > 0:
            parent = (index-1) // 2
            if self.IDs[2*parent+1] and self.IDs[2*parent+2]:
                self.IDs[parent] = 1
            else:
                self.IDs[parent] = 0
            index = parent

    def release_id(self, the_id):
        if the_id < 0 or the_id >= self.max_size:
            return

        if self.IDs[the_id + self.max_size - 1]:
            self.IDs[the_id + self.max_size - 1] = 0
            self.update_tree(the_id + self.max_size - 1)


if __name__ == '__main__':
    pool = IDPool(8)
    for i in range(3):
        print(pool.get_id())
    print('releasing id 3')
    pool.release_id(1)
    print(pool.get_id())
    # pool.release_id(4)
    # pool.release_id(5)
    # pool.release_id(6)
    # pool.release_id(7)
    # print (f'got id: {pool.get_id()}')
    # print (f'got id: {pool.get_id()}')
    # print (f'got id: {pool.get_id()}')
    # print (f'got id: {pool.get_id()}')
    # print (f'got id: {pool.get_id()}')
