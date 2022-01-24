import dealership as Dealership


class Sales(Dealership):
    def __init__(self):
        self.total_cars = 375
        self.inventory = {
            'toyota': {
                'count': 200,
                'price': 10_000
            },
            'mercedes': {
                'count': 50,
                'price': 35_000
            },
            'honda': {
                'count': 125,
                'price': 15_000
            }
        }

    def validate_can_sell(self, model, wallet):
        return self.inventory[model].count > 0 and self.inventory[model].price <= wallet

    def sell_car(self, model, wallet):
        if self.validate_can_sell(model, wallet):
            self.inventory[model].count -= 1
            self.total_cars -= 1
            self.earnings += wallet
