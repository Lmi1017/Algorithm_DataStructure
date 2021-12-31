from __future__ import annotations
from typing import Any, Sequence
import copy


class Node:
    def __init__(self, key: Any, value: Any, next: Node) -> None:
        self.key = key
        self.value = value
        self.next = next
        
class ChainedHash:
  def __init__(self, capacity: int) -> None:
      self.capacity = capacity
      self.table = [None] * self.capacity
      
  def hash_value(self, key: Any) -> int:
    if isinstance(key, int):
      return key % self.capacity
    return(int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)
