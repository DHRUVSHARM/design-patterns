# another example with text based formatting
# naive method where we use somethign like a bitmap where we can toggle the letters to capitalize 
class FormattedText:
    def __init__(self, plain_text):
        self.plain_text = plain_text
        self.caps = [False] * len(plain_text)

    # simple switch
    def capitalize(self, start, end):
        for i in range(start, end):
            self.caps[i] = True

    # while writing decide to capitalize 
    def __str__(self):
        result = []
        for i in range(len(self.plain_text)):
            c = self.plain_text[i]
            result.append(c.upper() if self.caps[i] else c)
        return ''.join(result)


# we will use the flyweight pattern here
class BetterFormattedText:
    def __init__(self, plain_text):
        self.plain_text = plain_text
        # this is key the list contains in order for the formatter the FORMATTING applied by 
        # storing formatting config objects in the list 
        # this will help generate the output correctly at any point when we call the str function
        self.formatting = []

    # simple inner class that initally has all formats as false 
    # options can be in a separate enum as well, or they can be enumerated like show here 
    class TextRange:
        def __init__(self, start, end, capitalize=False, bold=False, italic=False):
            self.end = end
            self.bold = bold
            self.capitalize = capitalize
            self.italic = italic
            self.start = start
        
        # simple utility to check if in range of the applied formatting 
        def covers(self, position):
            return self.start <= position <= self.end
        
        def __str__(self):
            return f"bold : {self.bold} capitalize : {self.capitalize} italic : {self.italic} for range ( start : {self.start} , end : {self.end} )"

    def get_range(self, start, end):
        range = self.TextRange(start, end)
        self.formatting.append(range)
        return range

    def bold(self , text: str) -> str:
        print("bolding")
        return f"\033[1m{text}\033[0m"

    def unbold(self , text: str) -> str:
        # removes ANSI bold escape sequences
        print("unbolding")
        return text.replace("\033[1m", "").replace("\033[0m", "")

    def __str__(self):
        result = []
        for i in range(len(self.plain_text)):
            c = self.plain_text[i]
            for r in self.formatting:
                if r.covers(i):
                    c = c.upper() if r.capitalize else c.lower()
                    c = self.bold(c) if r.bold else self.unbold(c)
            result.append(c)
        return ''.join(result)


if __name__ == '__main__':
    ft = FormattedText('This is a brave new world')
    ft.capitalize(10, 15)
    print(ft)

    bft = BetterFormattedText('This is a brave new world')
    bft.get_range(16, 19).capitalize = True
    print(bft)
    print("////////////////////")
    bft.get_range(16, 19).bold = True
    print(bft)
    print("////////////////////")
    
    bft.get_range(16, 19).capitalize = False
    print(bft)
    print(bft.formatting[-1])
