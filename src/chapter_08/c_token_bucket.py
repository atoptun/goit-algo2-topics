import time

class TokenBucket:
    def __init__(self, capacity, refill_rate):
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.tokens = capacity  
        self.last_refill_time = time.monotonic()  

    def refill(self):
        now = time.monotonic()  # Поточний час
        elapsed = now - self.last_refill_time  
        new_tokens = elapsed * self.refill_rate  
        self.tokens = min(self.capacity, self.tokens + new_tokens)
        self.last_refill_time = now 

    def consume(self, num_tokens):
        self.refill()  
        if self.tokens >= num_tokens:
            self.tokens -= num_tokens 
            return True
        return False


if __name__ == "__main__":
    bucket = TokenBucket(capacity=10, refill_rate=2)  # 10 токенів, 2 токени/с

    for i in range(20):
        if bucket.consume(3):  # Спроба спожити 3 токени
            print(f"Запит {i + 1}: дозволено")
        else:
            print(f"Запит {i + 1}: відхилено")
        time.sleep(0.5)  # Затримка між запитами
