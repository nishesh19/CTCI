from bitarray import bitarray
class IDPool(object):
    '''
    Create a pool of IDs to allow reuse. The "new_id" function generates the next
    valid ID from the previous one. If not given, defaults to incrementing an integer.
    '''

    def __init__(self,size):
        self.max_size = size
        self.IDs = bitarray(size)
        self.IDs.setall(0)
        self.last_id = 0

    def get_id(self):
        if self.last_id == self.max_size:
            return -1

        self.IDs[self.last_id] = 1
        _id = self.last_id
        self.last_id = self.get_next_clear_bit(self.last_id)
        return _id


    def get_next_clear_bit(self,last_id):
        while last_id < self.max_size and self.IDs[last_id]:
            last_id += 1
        
        return last_id

    def release_id(self, the_id):
        if the_id < 0 or the_id >= self.max_size:
            return
        
        if self.IDs[the_id]:
            self.IDs[the_id] = 0
            self.last_id = min(self.last_id,the_id)
        

if __name__ == '__main__':
    pool = IDPool(100)
    for i in range(15):
        print(pool.get_id())
    print('releasing id 3')
    pool.release_id(3)
    pool.release_id(4)
    pool.release_id(5)
    pool.release_id(6)
    pool.release_id(7)
    print (f'got id: {pool.get_id()}')
    print (f'got id: {pool.get_id()}')
    print (f'got id: {pool.get_id()}')
    print (f'got id: {pool.get_id()}')
    print (f'got id: {pool.get_id()}')