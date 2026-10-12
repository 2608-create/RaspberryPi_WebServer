import pymysql
import config


def get_connection():
    """데이터베이스 연결을 만들어 돌려줌 (5차시와 같은 코드)"""
    return pymysql.connect(
        host=config.DB_HOST,
        user=config.DB_USER,
        password=config.DB_PASSWORD,
        db=config.DB_NAME,
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor
    )


class LedDB:
    """LED 기록을 다루는 계층"""

    def add(self, pin, is_on):
        conn = get_connection()
        try:
            cur = conn.cursor()
            cur.execute("insert into led_record (pin, is_on) values (%s, %s)", (pin, is_on)) 
            conn.commit()
        finally:
            conn.close()


def get_recent(self, pin):
    """해당 핀의 기록을 최신순으로 10개만 돌려줌"""
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("select * from led_record where pin = %s order by id desc limit 10", (pin,))
        return cur.fetchall()
    finally:
        conn.close()
