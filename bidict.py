class TwoWayDictNaive(dict):
    def get_keys_for_value(self, value):
        return [key for key, val in self.items() if val == value]


class TwoWayDictReverse(dict):
    def __init__(self):
        super().__init__()
        self._reverse_dict = {}

    def __setitem__(self, key, value):
        # Remove the key from the old value's set in reverse dictionary if it exists
        if key in self:
            old_value = self[key]
            self._reverse_dict[old_value].discard(key)
            # No need to delete empty sets, as they will naturally be skipped in lookups

        # Set the new key-value pair
        super().__setitem__(key, value)
        self._reverse_dict.setdefault(value, set()).add(key)

    def pop(self, key):
        # Remove key from main dict and update reverse dict
        if key in self:
            value = super().pop(key)
            self._reverse_dict[value].discard(key)
            return value
        raise KeyError(f"Key {key} not found")

    def get_keys_for_value(self, value):
        return list(self._reverse_dict.get(value, []))
