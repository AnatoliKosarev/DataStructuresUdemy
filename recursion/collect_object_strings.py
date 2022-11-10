obj = {
    "stuff": 'foo',
    "data": {
        "val": {
            "thing": {
                "info": 'bar',
                "moreInfo": {
                    "evenMoreInfo": {
                        "weMadeIt": 'baz'
                    }
                }
            }
        }
    }
}


def collect_object_strings(obj):
    assert isinstance(obj, dict), 'Obj must be an instance of dict'

    result_list = []

    for v in obj.values():
        if isinstance(v, dict):
            result_list += collect_object_strings(v)
        else:
            if type(v) is str:
                result_list.append(v)

    return result_list


print(collect_object_strings(obj))
