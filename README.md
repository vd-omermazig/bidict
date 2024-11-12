Two-Way Dictionary Assignment

Objective

Implement a two-way dictionary in Python where:

	•	Each key maps to a unique value.
	•	Each value maps back to the list of the keys the point to it.

Methods to Implement:

	get_keys_for_value(value: Any) -> Set: Returns a set of keys associated with the given value.

Example test:

	def test_add_and_get_keys_for_value(two_way_dict):
		two_way_dict["a"] = 1
		two_way_dict["b"] = 2
		two_way_dict["c"] = 1
		assert set(two_way_dict.get_keys_for_value(1)) == {"a", "c"}
		assert two_way_dict.get_keys_for_value(2) == ["b"]
		assert two_way_dict.get_keys_for_value(3) == []


Assume that the object is initialized empty, and only pop is used to remove values from it.