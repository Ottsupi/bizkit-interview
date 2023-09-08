from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!
    if not args: return [str(user) for user in USERS]

    found_users = list()

    if "id" in args.keys():
        for user in USERS:
            if user["id"] == args["id"]:
                found_users.append(str(user))

    if "name" in args.keys():
        for user in USERS:
            if args["name"].lower() in user["name"].lower():
                found_users.append(str(user))

    if "age" in args.keys():
        for user in USERS:
            if int(args["age"]) - 1 <= int(user["age"]) <= int(args["age"]) + 1:
                found_users.append(str(user))

    if "occupation" in args.keys():
        for user in USERS:
            if args["occupation"].lower() in user["occupation"].lower():
                found_users.append(str(user))

    # python magic to remove duplicates while keeping order
    return list(dict.fromkeys(found_users))
