from connection import CURSOR

class Author:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return f'<Author {self.id}: {self.name}>'

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise ValueError("Author ID must be an integer.")
        self._id = value
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not hasattr(self, '_name'):  # Ensure name is set only once
            if isinstance(value, str):
                self._name = value
            else:
                raise ValueError("Name must be a string.")
        else:
            raise AttributeError("Name can only be set once.")
        

    def articles(self):
        CURSOR.execute("SELECT * FROM articles WHERE author_id = ?", (self._id,))
        return CURSOR.fetchall()

    def magazines(self):
        CURSOR.execute("""
        SELECT DISTINCT magazines.* FROM magazines
        JOIN articles ON magazines.id = articles.magazine_id
        WHERE articles.author_id = ?
        """, (self._id,))
        return CURSOR.fetchall()
     