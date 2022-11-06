from absl import flags, app
import logging, os, sqlite3
import pandas as pd
LOGGER = logging.getLogger(__name__)
FLAGS = flags.FLAGS
 
# 打印某目录下的文件
def file_display(filepath):
    for each in os.listdir(filepath): #得出文件的绝对路径
        absolute_path = os.path.join(filepath,each)
        is_file = os.path.isfile(absolute_path) #判断文件或目录得出布尔值
        if is_file:
            print(absolute_path)
        else: file_display(absolute_path)

def main(unused_argv) -> None:
    """ETL"""
    logging.basicConfig(level=logging.INFO)
    pipeline_start_month = os.getenv('PIPELINE_START_MONTH')
    pipeline_end_month = os.getenv('PIPELINE_END_MONTH')
    title = os.getenv('TITLE')

    LOGGER.info("Use SQLite3 table for ETL")
# printing environment variables
    print(os.environ)

    # Link to database
#    conn = sqlite3.connect(f"""./bash/{title}_questions.db""") # db in image
    conn = sqlite3.connect(f"""/home/stackoverflow_sem/{title}_questions.db""") # db in localhost
    cursor = conn.cursor()
    path = os.getcwd()#获取当前路径
    # 打印路径下的文件/子文件/目录
    for root, dirs, files in os.walk(path, topdown=False):
        print('****')
        print("当前目录路径:", root)
        print("当前目录下所有子目录:", dirs)
        print("当前路径下所有非目录子文件:", files) # 打印当前目录下所有文件
    # 看当前db是否有table
    cursor.execute("SELECT * FROM sqlite_master WHERE type='table';") 
    # 文件内容测试 ----- start
    with open("./test_abc.txt", "a") as f:
        f.write('--------')
        f.write('--------')
        f.write('--------')
        f.write('test done')
        f.close()
    with open('./moshu.txt', 'w') as f:
        f.write('Create a new text file!')
        print('---test')
        f.close()
    # 文件内容测试 ----- end
    print(cursor.fetchall(), '---------')

    # df = pd.read_sql_query(f"""select * from qa_{title}
    #                         where no_tag is not null
    #                           and cast(substr(creation_timestamp, 0, 7) as integer) between {pipeline_start_month} and {pipeline_end_month};"""
    #                           , conn)
    df = pd.read_sql_query(f"""select * from qa_{title}
                            where no_tag is not null;"""
                              , conn)
    print(df.head(5))
    df.to_sql(f"""mbd_{title}""", conn, if_exists="replace")
    test= pd.read_sql_query(f"""select * from mbd_{title}
                            ;"""
                              , conn)
    print(test.head(5))
    conn.close()

def common_entry():
    app.run(main)

if __name__ == '__main__':
    common_entry()



