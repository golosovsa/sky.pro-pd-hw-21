"""
    main app entry point
"""

from implement import World, CreateRequestError


def main():
    world = World.create_from_json_file("data/data.json")
    world.compute_all_requests()
    while True:
        print("\nEnter new query or 'exit' to exit")
        query = input()
        if query == "exit":
            break
        try:
            world.append_request(query)
        except CreateRequestError as error:
            print(str(error))
        else:
            world.compute_all_requests()


if __name__ == "__main__":
    main()
