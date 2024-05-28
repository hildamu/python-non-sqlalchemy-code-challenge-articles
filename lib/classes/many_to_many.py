class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        
class Author:
    def __init__(self, name):
        self.name = name

    def articles(self):
        pass

    def magazines(self):
        pass

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []

    def get_name(self):
        return self._name
    
    def set_name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
    
    name=property(get_name,set_name)

    def get_category(self):
        return self._category
    
    def set_category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        
    category=property(get_category,set_category)

    def add_article(self, article):
        self._articles.append(article)

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass