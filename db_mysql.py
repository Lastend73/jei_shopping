import mysql
import mysql.connector

from mysql.connector import Error

# MySQL 데이터베이스에 연결을 생성하는 함수
def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='mall.jeisys.com',
            user="jeisys_main",
            passwd="o4#BUtd61F",
            database="jeisys_main"
        )
        print("MySQL DB에 성공적으로 연결되었습니다")
    except Error as e:
        print(f"다음 오류가 발생했습니다: '{e}'")
    return connection

# MySQL 데이터베이스에서 데이터를 읽는 쿼리를 실행하는 함수
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"다음 오류가 발생했습니다: '{e}'")
        return None

def get_order_data() :
    try : 
        connection = create_connection()
        results = execute_read_query(connection,
                    """
                    SELECT 
                        o.id AS '웹주문번호',
                        c.first_name AS '고객코드',
                        m.date AS '오더일',
                        CURDATE() AS '납품예정일',
                        '' AS '영업사원명',
                        1 AS '판매구분',
                        '' AS 출하유형,
                        CONCAT(a.address_1, ' ', a.address_2) AS '납품처주소',
                        o.payment_method_title AS '결제유형',
                        '' as '카드사정보',
                        i.order_item_name AS '품목코드',
                        im1.meta_value AS '수량',
                        x.meta_value / im1.meta_value AS '단가',
                        'KRW' AS '통화',
                        ROUND(x.meta_value / 110 * 100, 0) AS '공급가액',
                        ROUND(x.meta_value / 110 * 10, 0) AS '부가세',
                        x.meta_value AS '총액',
                        1 AS '판매유형',
                        4 AS '수령방법',
                        '12개월' AS '보증개월 수',
                        'N' AS '무상여부',
                        CONCAT(a.phone,' ',o.customer_note) AS '비고',
                        'N' AS '가격정책예외'
                    FROM
                        jeisys_main.8sN2fUx_wc_orders o
                            INNER JOIN
                        jeisys_main.8sN2fUx_wc_order_addresses a ON o.id = a.order_id
                            AND a.address_type = 'shipping'
                            INNER JOIN
                        jeisys_main.8sN2fUx_wc_customer_lookup c ON o.customer_id = c.user_id
                            INNER JOIN
                        jeisys_main.8sN2fUx_woocommerce_order_items i ON o.id = i.order_id
                            AND i.order_item_type NOT LIKE 'shipping'
                            INNER JOIN
                        jeisys_main.8sN2fUx_woocommerce_order_itemmeta im1 ON i.order_item_id = im1.order_item_id
                            AND im1.meta_key = '_qty'
                            INNER JOIN
                        (SELECT 
                            order_item_id, meta_value
                        FROM
                            jeisys_main.8sN2fUx_woocommerce_order_itemmeta
                        WHERE
                            meta_key = '_line_total') x ON x.order_item_id = i.order_item_id
                            INNER JOIN
                        (SELECT 
                        order_id, date_format(date_add(date_paid_gmt, INTERVAL 9 HOUR),'%Y-%m-%d') as date
                        FROM
                            jeisys_main.8sN2fUx_wc_order_operational_data
                        ) m ON m.order_id = o.id
                    WHERE
                        o.status = 'wc-order-received'
                    ORDER BY o.id DESC
                    """)
        connection.close() # 연결을 닫습니다
        return results
    except mysql.connector.Error as err:
        print(f"Error: '{err}'") # 콘솔에 에러 표시
        return None

def get_point_use_list() :
    connection = create_connection()
    results = execute_read_query(connection,
                """
                SELECT order_id
                FROM
                    jeisys_main.8sN2fUx_wc_orders_meta
                WHERE
                    meta_key = '_mshop_point_purchase_processed'
                        AND meta_value = 'yes'
                ORDER BY order_id DESC
                limit 30
                """)
    connection.close() # 연결을 닫습니다
    return results

def get_hostpital_data() :
    try : 
        connection = create_connection()
        results = execute_read_query(connection,
                    """
                        SELECT 
                            c.user_id,
                            first_name,
                            CONCAT(d.meta_value, ' ', a.meta_value) AS address
                        FROM
                            jeisys_main.8sN2fUx_wc_customer_lookup c
                                INNER JOIN
                            jeisys_main.8sN2fUx_usermeta d ON d.user_id = c.user_id
                                AND d.meta_key = 'mshop_billing_address-addr1'
                                INNER JOIN
                            jeisys_main.8sN2fUx_usermeta a ON a.user_id = c.user_id
                                AND a.meta_key = 'mshop_billing_address-addr2'
                    """)
        connection.close() # 연결을 닫습니다
        return results
    except mysql.connector.Error as err:
        print(f"Error: '{err}'") # 콘솔에 에러 표시
        return None
def get_product_data() :
    connection = create_connection()
    results = execute_read_query(connection,
                """
                    SELECT i.meta_value, x.order_item_name
                    FROM jeisys_main.8sN2fUx_woocommerce_order_itemmeta as i
                    INNER JOIN jeisys_main.8sN2fUx_woocommerce_order_items as x ON i.order_item_id = x.order_item_id
                    where meta_key = '_product_id' 
                    group by x.order_item_name
                    order by meta_value 
                """)
    connection.close() # 연결을 닫습니다
    return results

