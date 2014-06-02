from datetime import datetime
from datetime import timedelta
import unittest

class Task:
    @property
    def end(self):
        return self.start + self.duration

    def __init__(self, start, duration, title, description, is_note):
        self.start = start
        self.duration = duration
        self.title = title
        self.description = description
        self.is_note = is_note
        
        
    def overlap(self, other):
        return ((other.start < self.end and other.end > self.end) or
                (other.end < self.end and other.end > self.start))

class TestTask(unittest.TestCase):
    def setUp(self):
        self.t1 = Task(datetime(year=2014,month=1,day=1,hour=10)
                      , timedelta(minutes = 60), "gs", "mega gys", False)
        self.t2 = Task(datetime(year=2014,month=1,day=1,hour=11)
                      , timedelta(minutes = 30), "gs", "mega gys", False)

    def test_end(self):
        self.assertEqual(self.t1.end, datetime(year=2014,month=1,day=1,hour=11))
    def test_overlap(self):
        self.assertFalse(self.t1.overlap(self.t2))
        

class ModifyTasks(list):
    
    def add(self, other):
        if other.is_note:
            self.append(other)
            return True
        free_spot = True
        for task in self:
            if other.overlap(task) and not task.is_note:
                free_spot = False
        if free_spot:
            self.append(other)
            return True
        else:
            return False
    def print(self):
        for task in self:
            if task.is_note:
                note = 'Note: '
            else:
                note = ''
            print('{}{} from {} till {}'.format(note, task.title, task.start, task.end))

a = Task(9, 2, "a","", False)
m = ModifyTasks()
m.add(a)
b = Task(10, 3, "","", False)
m.add(b)
c = Task(12, 2, "c","", False)
d = Task(12, 1, "d","", True)
m.add(c)
m.add(d)
m.print()
