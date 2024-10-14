from main.settings import DATABASE

class Voucher(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer,primary_key = True)
    title = DATABASE.Column(DATABASE.String(60))
    date = DATABASE.Column(DATABASE.String(60))
    country = DATABASE.Column(DATABASE.String(60))
    price = DATABASE.Column(DATABASE.String(60))
    description = DATABASE.Column(DATABASE.Text)
    def __repr__(self) -> str:
        return f"title - {self.title}"
    
