class Currency:
    def _init_(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def _str_(self):
        return f"{self.amount} {self.currency}s"

    def _repr_(self):
        return f"{self.amount} {self.currency}s"

    def _int_(self):
        return self.amount

    def _add_(self, other):
        if isinstance(other, int):
            return self.amount + other

        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(
                    f"Cannot add between Currency type <{self.currency}> and <{other.currency}>"
                )
            return self.amount + other.amount

        return NotImplemented

    def _iadd_(self, other):
        if isinstance(other, int):
            self.amount += other
            return self

        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(
                    f"Cannot add between Currency type <{self.currency}> and <{other.currency}>"
                )
            self.amount += other.amount
            return self

        return NotImplemented