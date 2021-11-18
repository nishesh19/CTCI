from collections import OrderedDict
class MyCalendarTwo:

    def __init__(self):
        self._single = OrderedDict()
        self._double = OrderedDict()

    def book(self, start: int, end: int) -> bool:
        
        for end_d in self._double:
            if (start < end_d) and (end > self._double[end_d]):
                return False
        
        for end_s in self._single:
            if (start < end_s) and (end > self._single[end_s]):
                temp_start = max(start,self._single[end_s])
                temp_end = min(end,end_s)
                
                self._double[temp_end] = temp_start
            
        if end not in self._single:
            self._single[end] = start
        else:
            self._single[end] = min(start,self._single[end])
        
        return True
                

if __name__ == '__main__':
    
# Your MyCalendarTwo object will be instantiated and called as such:
    obj = MyCalendarTwo()
    print(obj.book(10,20))
    print(obj.book(50,60))
    print(obj.book(10,40))
    print(obj.book(5,15))
    print(obj.book(5,10))
    print(obj.book(25,55))