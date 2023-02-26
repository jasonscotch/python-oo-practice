from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary.
    
    >>> words = WordFinder('python-oo-practice/words3.txt')
    3 words read
    
    >>> words.random() in ['cat', 'dog','mouse']
    True
    """
    
    def __init__(self,file,print_words=True):
        self.file = file
        self.opened = open(self.file, 'r')
        self.words = self.opened.read().splitlines()
        if print_words:
            print(self.print_read_file())       
        self.opened.close()  
        
    def __repr__(self):
        return f"WordFinder(file={self.file})"

    def print_read_file(self):
        return f"{len(self.words)} words read"
        
    def random(self):
        return choice(self.words)
    
    
class SpecialWordFinder(WordFinder):
    """Special Word Finder: finds random words from a dictionary.
    
    >>> words2 = SpecialWordFinder('python-oo-practice/words2.txt')
    4 words read
    
    >>> words2.random() in ['kale', 'parsnips','apple', 'mango']
    True
    """
    
    def __init__(self, file):
        super().__init__(file, print_words=False)
        self.filter_words()
        print(self.print_filtered_file())
    
    def __repr__(self):
        return f"SpecialWordFinder(file={self.file})"
    
    def filter_words(self):
        self.words = [word for word in self.words if not word.startswith('#')]
        self.words = [word.strip() for word in self.words if word.strip()]
        while('' in self.words):
            self.words.remove('')

    def print_filtered_file(self):
        return f"{len(self.words)} words read"
    
    
     