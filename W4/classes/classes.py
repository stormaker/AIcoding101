import pymysql
import os
from dotenv import load_dotenv

load_dotenv()
# 配置数据库连接
conn = pymysql.connect(host=os.getenv('db_host'),
                       user=os.getenv('db_user'),
                       password=os.getenv('db_pass'),
                       db=os.getenv('db_name')
                       )

# 创建一个游标对象
cursor = conn.cursor()


#
# # 创建表的SQL语句
# create_students_table = """
# CREATE TABLE IF NOT EXISTS students (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(255),
#     height DECIMAL(3, 2),
#     class_id INT
# );
# """
#
# create_teachers_table = """
# CREATE TABLE IF NOT EXISTS teachers (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(255),
#     class_id INT
# );
# """
#
# create_classes_table = """
# CREATE TABLE IF NOT EXISTS classes (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(255),
#     teacher_id INT,
#     FOREIGN KEY (teacher_id) REFERENCES teachers(id)
# );
# """
#
#
#
# # 执行SQL语句创建表
# cursor.execute(create_students_table)
# cursor.execute(create_teachers_table)
# cursor.execute(create_classes_table)
#
#
# # 提交到数据库执行
# conn.commit()

# 添加老师
#
# add_teacher="""
# INSERT INTO teachers (name) VALUES ('老师A'), ('老师B');
# """
# cursor.execute(add_teacher)
# conn.commit()


# # 添加班级老师信息
# add_teacher_to_class="""INSERT INTO classes ( NAME, teacher_id )
# VALUES
# 	(
# 		'三年1班',
# 	( SELECT id FROM teachers WHERE NAME = '老师B' )),
# 	(
# 	'三年2班',
# 	( SELECT id FROM teachers WHERE NAME = '老师A' ))
# """
# cursor.execute(add_teacher_to_class)
# conn.commit()

#  添加学生信息
# add_students_to_class="""INSERT INTO students (name, height, class_id) VALUES
# ('学生1', 1.50, (SELECT id FROM classes WHERE name = '三年2班')),
# ('学生2', 1.55, (SELECT id FROM classes WHERE name = '三年2班')),
# ('学生3', 1.60, (SELECT id FROM classes WHERE name = '三年2班')),
# ('学生4', 1.45, (SELECT id FROM classes WHERE name = '三年1班')),
# ('学生5', 1.52, (SELECT id FROM classes WHERE name = '三年1班')),
# ('学生6', 1.58, (SELECT id FROM classes WHERE name = '三年1班'));
# """
# cursor.execute(add_students_to_class)
# conn.commit()


def get_students_by_class(class_name):
    sql = """
    SELECT s.name, s.height
    FROM students s
    JOIN classes c ON s.class_id = c.id
    WHERE c.name = %s
    ORDER BY s.height DESC
    """
    cursor.execute(sql, (class_name,))
    return cursor.fetchall()


def get_class_info(class_name):
    sql = """
    SELECT c.name as class_name,s.`name` as student_name,t.name as teacher_name FROM students s
    JOIN classes c ON s.class_id = c.id
    JOIN teachers t ON c.teacher_id = t.id  WHERE c.`name`=%s
    """
    cursor.execute(sql, (class_name,))
    return cursor.fetchone()


# students = get_students_by_class('三年2班')
# for student in students:
#     print(student)

info = get_class_info("三年2班")
print(info)
