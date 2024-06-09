class Magazine:
    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category

    def __repr__(self):
        return f'<Magazine {self.id}: {self.name}, {self.category}>'
    
    @property
    def name(self):
        # Getter for the name property
        return self.name
    
    @name.setter
    def name(self, value):
        # Setter for the name property
        # Check if the value is a string with length between 2 and 16 characters
        if not isinstance(value, str) or len(value) < 2 or len(value) > 16:
            raise ValueError("Magazine name must be a string between 2 and 16 characters")
        self._name = value 

    @property
    def category(self):
        # Getter for the category property
        return self._category

    @category.setter
    def category(self, value):
        # Setter for the category property
        # Check if the value is a non-empty string
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._category = value    
