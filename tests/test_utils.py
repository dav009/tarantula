from tarantula.utils import combine_parameters


class TestUtils:

    def test_combine_parameters(self):
        test_params = {
            "param1": ["a", "b", "c"],
            "param2": ["1", "2", "3"],
            "param3": ["la", "le", "li"]
        }
        combined_params = combine_parameters(test_params)
        assert({"param1": "a", "param2": "2", "param3": "le"} in combined_params)
        assert({"param1": "c", "param2": "2", "param3": "le"} in combined_params)
        assert({"param1": "a", "param2": "2", "param3": "li"} in combined_params)
        assert(len(combined_params)==27)
