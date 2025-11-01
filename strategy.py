# simple text processor to 

from abc import ABC
from enum import Enum, auto


class OutputFormat(Enum):
    MARKDOWN = auto()
    HTML = auto()


# not required but a good idea to outline interfaces that we want the strategies to conform to 
# think about this like start, end, add_list_item 
# kind of a flexible interface
class ListStrategy(ABC):
    def start(self, buffer): pass

    def end(self, buffer): pass

    def add_list_item(self, buffer, item): pass

# in the below strategy all we do is implement the low level details 
# here no need for anything only *
class MarkdownListStrategy(ListStrategy):

    def add_list_item(self, buffer, item):
        buffer.append(f' * {item}\n')

# open and close and unordered list 
# <ul>
# <li></li>
# <li></li>
# <li></li>
# </ul>
class HtmlListStrategy(ListStrategy):

    def start(self, buffer):
        buffer.append('<ul>\n')

    def end(self, buffer):
        buffer.append('</ul>\n')

    def add_list_item(self, buffer, item):
        buffer.append(f'  <li>{item}</li>\n')


class TextProcessor:

    def __init__(self, list_strategy=HtmlListStrategy()):
        # default is html strategy
        self.buffer = []
        self.list_strategy = list_strategy

    # this will add the list of elements and add them to the buffer 
    def append_list(self, items):
        # start the list
        self.list_strategy.start(self.buffer)
        # for each element add whatever is needed 
        for item in items:
            self.list_strategy.add_list_item(
                self.buffer, item
            )
        # close the unordered list
        self.list_strategy.end(self.buffer)

    # this will help toggle between the format in flight (while running ie;)
    def set_output_format(self, format):
        if format == OutputFormat.MARKDOWN:
            self.list_strategy = MarkdownListStrategy()
        elif format == OutputFormat.HTML:
            self.list_strategy = HtmlListStrategy()

    def clear(self):
        self.buffer.clear()

    def __str__(self):
        return ''.join(self.buffer)


if __name__ == '__main__':
    items = ['foo', 'bar', 'baz']

    # at runtime we are able to flip between strategies
    # as and when required 

    tp = TextProcessor()
    tp.set_output_format(OutputFormat.MARKDOWN)
    tp.append_list(items)
    print(tp)

    tp.set_output_format(OutputFormat.HTML)
    tp.clear()
    tp.append_list(items)
    print(tp)

    # add the next as markdown 
    tp.set_output_format(OutputFormat.MARKDOWN)
    # this will be markdown
    tp.append_list(items)
    print(tp)
    tp.clear()
    print(tp)