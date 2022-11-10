obj = {
  "num": 1,
  "test": [3, {'a': 1.0, 'b': 1}],
  "data": {
    "val": 4,
    "info": {
      "isRight": True,
      "random": 66
    }
  }
}


def stringify_object_numbers(obj):
    assert hasattr(obj, '__iter__'), 'Obj must be iterable'

    if isinstance(obj, dict):
        for k, v in obj.items():
            if hasattr(v, '__iter__'):
                stringify_object_numbers(v)
            else:
                if type(v) is int:
                    obj[k] = str(v)

    if isinstance(obj, list):
        for i, v in enumerate(obj):
            if hasattr(v, '__iter__'):
                stringify_object_numbers(v)
            else:
                if type(v) is int:
                    obj[i] = str(v)

    return obj


print(stringify_object_numbers(obj))
