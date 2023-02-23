class User():
    
    def __init__(self, first_name, last_name, email, phone, _id=None):
        if _id:
            self._id = _id
        self.first_name = first_name
        self.last_name = last_name 
        self.email = email
        self.phone = phone

    def to_json():
        pass