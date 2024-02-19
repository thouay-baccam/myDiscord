class ChannelList:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def get_channels(self):
        # Query the database to get all channels
        cursor = self.db_connection.cursor()
        select_query = "SELECT name, port FROM channels"
        cursor.execute(select_query)
        result = cursor.fetchall()
        cursor.close()

        # Convert the result to a list of (channel_name, port) tuples
        channels = [(row[0], row[1]) for row in result]
        return channels
