class Author:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return f'<Author {self.id}: {self.name}>'
    
    @property
    def name(self):
        # Getter for the name property
        return self.name
    
    @name.setter
    def name(self, value):
         # Setter for the name property
        # Check if value is a string and the name has not been set before
        if isinstance(value, str) and not hasattr(self, 'name'):
         self.name = value
