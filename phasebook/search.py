from flask import Blueprint, request
from .data.search_data import USERS

bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    param = [i for i in args]
    value = [i.casefold() for i in args.values()]
    result = []
    if len(args) != 0:
        for i in range(len(args)):
            for item in USERS:
                if param[i] == 'age':
                    age = int(value[i])
                    for ages in range(age - 1, age + 2):
                        if str(ages) in str(item[param[i]]).casefold() and item not in result:
                            result.append(item)
                elif value[i] in str(item[param[i]]).casefold():
                    if item not in result:
                        result.append(item)
    else:
        return USERS
    return result
