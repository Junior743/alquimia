import traceback
from grant_types import (
    Password, 
    Implicit, 
    Whatever
)


class Oauth2(object):

    @staticmethod
    def handler_grant():
        """
        Method responsable for decide what handler of authorization will be used based in grant type provided
        """
        try:

            return True

        except Exception as ex:
            traceback.print_exc()
            raise ex


if __name__ == "__main__":
    Oauth2.handler_grant()