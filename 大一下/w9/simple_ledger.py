class SimpleLedger:
    def __init__(self):
        self.transcations = []

    def record(self , amount: float, description: str):
        self.transcations.append((amount , description))
    
    def get_balance(self) -> float:
        return sum(amount for amount , _ , _ , _ in self.transcations)
    
