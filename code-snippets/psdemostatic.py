class ConnectionPool:
    connection_counter = 0  # static variable
    max_pool_size = 5

    def __init__(self, conn_id):
        ConnectionPool.connection_counter += 1
        ConnectionPool.check_limit()  # static method

        self.conn_id = conn_id

    @staticmethod
    def check_limit():
        if ConnectionPool.connection_counter > ConnectionPool.max_pool_size:
            raise RuntimeError('reached maximum limit')

        return True

    # print(check_limit)
    # check_limit = staticmethod(check_limit)  # applied the decor
    # print(check_limit)

    def __str__(self):
        """override the default to str"""
        return "<{} connection id:{}>".format(self.__class__.__name__, self.conn_id)


if __name__ == '__main__':
    for item in range(1, 8):
        conn = ConnectionPool(item)
        print(conn)
