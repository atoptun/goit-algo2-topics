import time
from typing import Dict
import random


class ThrottlingRateLimiter:
    def __init__(self, min_interval: float = 10.0):
        """
        Ініціалізація Rate Limiter з використанням Throttling

        Args:
            min_interval: Мінімальний інтервал між повідомленнями в секундах
        """
        self.min_interval = min_interval
        # Зберігаємо час останнього повідомлення для кожного користувача
        self.last_request_time: Dict[str, float] = {}

    def can_send_message(self, user_id: str) -> bool:
        """
        Перевірка можливості відправки повідомлення

        Алгоритм Throttling:
        1. Якщо користувач пише вперше - дозволяємо
        2. Інакше перевіряємо, чи пройшов мінімальний інтервал
        """
        current_time = time.perf_counter()

        if user_id not in self.last_request_time:
            return True

        time_passed = current_time - self.last_request_time[user_id]
        return time_passed >= self.min_interval

    def record_message(self, user_id: str) -> bool:
        """
        Запис нового повідомлення
        """
        if not self.can_send_message(user_id):
            return False

        self.last_request_time[user_id] = time.perf_counter()
        return True

    def time_until_next_allowed(self, user_id: str) -> float:
        """
        Розрахунок часу до можливості відправки наступного повідомлення
        """
        if user_id not in self.last_request_time:
            return 0

        current_time = time.perf_counter()
        time_passed = current_time - self.last_request_time[user_id]
        return max(0, self.min_interval - time_passed)


def test_throttling_limiter():
    limiter = ThrottlingRateLimiter(min_interval=10.0)

    print("\n=== Симуляція потоку повідомлень (Throttling) ===")
    for message_id in range(1, 11):
        user_id = message_id % 5 + 1

        result = limiter.record_message(str(user_id))
        wait_time = limiter.time_until_next_allowed(str(user_id))

        print(f"Повідомлення {message_id:2d} | Користувач {user_id} | "
              f"{'✓' if result else f'× (очікування {wait_time:.1f}с)'}")

        # Випадкова затримка між повідомленнями
        time.sleep(random.uniform(0.1, 1.0))

    print("\nОчікуємо 4 секунди...")
    time.sleep(4)

    print("\n=== Нова серія повідомлень після очікування ===")
    for message_id in range(11, 21):
        user_id = message_id % 5 + 1
        result = limiter.record_message(str(user_id))
        wait_time = limiter.time_until_next_allowed(str(user_id))
        print(f"Повідомлення {message_id:2d} | Користувач {user_id} | "
              f"{'✓' if result else f'× (очікування {wait_time:.1f}с)'}")
        time.sleep(random.uniform(0.1, 1.0))


if __name__ == "__main__":
    test_throttling_limiter()
