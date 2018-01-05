from psdirlisting import DirectoryListing
import json
import os

class DirectoryListing2JSON(DirectoryListing):
    """demo for the simple inheritance"""
    def to_json(self, json_file):
        """serializes the python object into json string"""
        try:
            json.dump(self.container, open(json_file, 'w'), indent=4)
        except (FileNotFoundError, IOError) as err:
            print(err)


if __name__ == '__main__':
    DirectoryListing2JSON('/data', '/tmp').to_json('tmp.json')