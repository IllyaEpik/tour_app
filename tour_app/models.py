from main.settings import data_base

class Voucher(data_base.Model):
    id = data_base.Column(data_base.Integer,primary_key = True)
    title = data_base.Column(data_base.String(60))
    date = data_base.Column(data_base.String(60))
    country = data_base.Column(data_base.String(60))
    price = data_base.Column(data_base.String(60))
    description = data_base.Column(data_base.Text)
    def __repr__(self) -> str:
        return f"title - {self.title}"
    
