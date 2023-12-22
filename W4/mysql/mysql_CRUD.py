from dotenv import load_dotenv
import os
import pymysql

load_dotenv()  # 加载.env文件中的变量
connection = pymysql.connect(host=os.getenv("DB_HOST"),
							 user=os.getenv("DB_USER"),
							 password=os.getenv("DB_PASS"),
							 database=os.getenv("DB_NAME")
							 )


def create_employee(name, address):
	try:
		with connection.cursor() as cursor:
			sql = "INSERT INTO employees (name, address) VALUES (%s, %s)"
			cursor.execute(sql, (name, address))
		connection.commit()
		return "Employee created successfully."
	except pymysql.MySQLError as e:
		return f"Error occurred: {e}"


def get_all_employees():
	try:
		with connection.cursor() as cursor:
			sql = "SELECT id, name, address FROM employees"
			cursor.execute(sql)
			result = cursor.fetchall()
			for emp in result:
				print(emp)
		return "Employees retrieved successfully."
	except pymysql.MySQLError as e:
		return f"Error occurred: {e}"


# def update_employee_address(emp_id, new_address):
# 	try:
# 		with connection.cursor() as cursor:
# 			sql = "UPDATE employees SET address = %s WHERE id = %s"
# 			cursor.execute(sql, (new_address, emp_id))
# 		connection.commit()
# 		return "Employee address updated successfully."
# 	except pymysql.MySQLError as e:
# 		return f"Error occurred: {e}"


def delete_employee(emp_id):
	try:
		with connection.cursor() as cursor:
			sql = "DELETE FROM employees WHERE id = %s"
			cursor.execute(sql, (emp_id,))
		connection.commit()
		return "Employee deleted successfully."
	except pymysql.MySQLError as e:
		return f"Error occurred: {e}"


# 示例使用
def update_employee_address(emp_id,new_address):
	try:
		with connection.cursor() as cursor:
			sql = "UPDATE employees SET address = %s WHERE id = %s"
			cursor.execute(sql, (new_address, emp_id))
		connection.commit()
		return "Employee address updated successfully."
	except pymysql.MySQLError as e:
		return f"Error occurred: {e}"


def close_connection():
	connection.close()


update_employee_address(2,'sdfsdf')
close_connection()
