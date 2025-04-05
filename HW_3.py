# Задание 3.

class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.new_list = []

    def __iter__(self):
        self.cursor = 0
        return self

    def __next__(self):
        if self.cursor >= len(self.list_of_list):
            if self.new_list:
                self.list_of_list, self.cursor = self.new_list.pop()
                return next(self)
            else:
                raise StopIteration
        item = self.list_of_list[self.cursor]
        self.cursor += 1

        if type(item) is not list:
            return item
        else:
            self.new_list.append((self.list_of_list, self.cursor))
            self.list_of_list = item
            self.cursor = 0
            return  next(self)


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()