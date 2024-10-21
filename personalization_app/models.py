from main.settings import DATABASE

class Personal(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer,primary_key = True)
    user_id = DATABASE.Column(DATABASE.String(60))
    img = DATABASE.Column(DATABASE.Text)
    
    color_0 = DATABASE.Column(DATABASE.String(50))
    color_1 = DATABASE.Column(DATABASE.String(50))
    color_2 = DATABASE.Column(DATABASE.String(50))
    color_3 = DATABASE.Column(DATABASE.String(50))
    def __repr__(self) -> str:
        return f"title - {self.user_id}"