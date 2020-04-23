import pymysql
import logging

class Connection:
    """db connection"""
    conn  = None

    def openingconnection(self):
        try:
            if self.conn == None:
                self.conn = pymysql.connect('127.0.0.1','root','','watu')
        except pymysql.MySQLError as e:
            logging.INFO("Error in connection")
        finally:
            logging.INFO("Connection is open!")

    def run_query(self,query):
        try:
            self.openingconnection()
            with self.conn.cursor(pymysql.cursors.DictCursor) as cursor:
                if "select" in query.lower():
                   cursor.execute(query)
                   row = cursor.fetchall()
                   return row
                else:
                    cursor.execute(query)
                    self.conn.commit()
                    affectedrow = cursor.rowcount
                    return f"{affectedrow} number are affected"
        except pymysql.MySQLError as e:
            logging.INFO("Error in mysql connection")
        finally:
            if self.conn:
                self.conn.close()
                self.conn = None
                logging.INFO("Connection closed!")

