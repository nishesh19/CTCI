
class IDPool(object):
    '''
    Create a pool of IDs to allow reuse. The "new_id" function generates the next
    valid ID from the previous one. If not given, defaults to incrementing an integer.
    '''

    def __init__(self):
        self.ids_in_use = set()
        self.ids_free = set()
        self.new_id = lambda x:x+1
        self.last_id = 0

    def get_id(self):
        if len(self.ids_free) > 0:
            return self.ids_free.pop()

        self.last_id = self.new_id(self.last_id)
        self.ids_in_use.add(self.last_id)
        return self.last_id

    def release_id(self, the_id):
        if the_id in self.ids_in_use:
            self.ids_in_use.remove(the_id)
            self.ids_free.add(the_id)

if __name__ == '__main__':
    pool = IDPool()
    for i in range(5):
        print(pool.get_id())
    print('releasing id 3')
    pool.release_id(3)
    print (f'got id: {pool.get_id()}')
    print (f'got id: {pool.get_id()}')