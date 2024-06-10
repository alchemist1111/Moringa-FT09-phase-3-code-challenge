from connection import CURSOR

class Article:

    # Class variable to store all instances of Article
    all = []

    def __init__(self, id, title, content, author_id, magazine_id):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id
        # Append the new article to the class variable 'all'
        Article.all.append(self)

    def __repr__(self):
        return f'<Article {self.id}: {self.title}, {self.content}, {self.author_id}, {self.magazine_id}>'

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if not hasattr(self, '_title'):  # Check if _title has not been set before
            if isinstance(value, str):
                self._title = value
            else:
                raise ValueError("Title must be a string.")
        else:
            raise AttributeError("Title can only be set once.")
        
    def get_author(self):
        pass   

    def get_magazine(self):
        pass 