from connection import CURSOR

class Magazine:
    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category

    def __repr__(self):
        return f'<Magazine {self.id}: {self.name}, {self.category}>'

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise ValueError("Magazine ID must be an integer.")
        self._id = value
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
        else:
            raise ValueError("Magazine name must be a string between 2 and 16 characters.")
    
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        else:
            raise ValueError("Category must be a non-empty string.")
        

    def articles(self):
        CURSOR.execute("SELECT * FROM articles WHERE magazine_id = ?", (self._id,))
        return CURSOR.fetchall()   

    def contributors(self):
        CURSOR.execute("""
        SELECT DISTINCT authors.* FROM authors
        JOIN articles ON authors.id = articles.author_id
        WHERE articles.magazine_id = ?
        """, (self._id,))
        return CURSOR.fetchall()

    def article_titles(self):
        CURSOR.execute("SELECT title FROM articles WHERE magazine_id = ?", (self._id,))
        titles = CURSOR.fetchall()
        return [title[0] for title in titles] if titles else None

    def contributing_authors(self):
        CURSOR.execute("""
        SELECT authors.*, COUNT(articles.id) as article_count FROM authors
        JOIN articles ON authors.id = articles.author_id
        WHERE articles.magazine_id = ?
        GROUP BY authors.id
        HAVING article_count > 2
        """, (self._id,))
        authors = CURSOR.fetchall()
        return [Author(id=author[0], name=author[1]) for author in authors] if authors else None