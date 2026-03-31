class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.keyage = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            # Increment all ages first
            for akey in self.keyage:
                if akey != key:
                    self.keyage[akey] += 1
            # Set accessed key's age to 0 (most recently used)
            self.keyage[key] = 0
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        # Update value if key exists
        if key in self.cache:
            self.cache[key] = value
            # Update ages like in get()
            for akey in self.keyage:
                if akey != key:
                    self.keyage[akey] += 1
            self.keyage[key] = 0
            return

        # If we're at capacity, remove least recently used
        if len(self.cache) >= self.capacity:
            key2remove = max(self.keyage, key=self.keyage.get)
            del self.cache[key2remove]
            del self.keyage[key2remove]

        # Add new key-value pair
        self.cache[key] = value
        self.keyage[key] = 0
        # Increment ages of all other keys
        for akey in self.keyage:
            if akey != key:
                self.keyage[akey] += 1


        
        
        
