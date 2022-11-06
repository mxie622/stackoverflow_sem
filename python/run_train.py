from absl import flags, app
import semopy
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 
import logging, os, sqlite3, pickle
sns.set_style('darkgrid')

LOGGER = logging.getLogger(__name__)
FLAGS = flags.FLAGS

# Feature engineering function

def main(unused_argv) -> None:
    """ETL"""
    logging.basicConfig(level=logging.INFO)

    title = os.getenv('TITLE')
    LOGGER.info("Use SQLite3 table for ETL")
    # Link to database
#    conn = sqlite3.connect(f"""./bash/{title}_questions.db""")
    conn = sqlite3.connect(f"""/home/stackoverflow_sem/{title}_questions.db""")
    # Raw table 
    df = pd.read_sql_query(f"""select *                        
                        from feature_{title}
                                ;""", conn)
    # Model parameters
    model_spec = """
    # measurement model
        QA_complexity =~ no_tag + q_text_length + no_statement 
        Activeness =~ no_answer + avg_answer_length + no_bookmark
        QA_quality =~ no_answer_thumb + no_q_thumb
    # regressions
        QA_quality ~ QA_complexity + Activeness
                """
    # Instantiate the model
    model = semopy.Model(model_spec)

    # Fit the model using the data
    model.fit(df)

    # Show the results using the inspect method
    print(model.inspect())
    
    # Save model
    sem_model_df = model.inspect()
    sem_model_df.to_sql(f"""sem_model_df_{title}""", conn, if_exists="replace")
    path = os.getcwd()#获取当前路径
    # 打印路径下的文件/子文件/目录
    for root, dirs, files in os.walk(path, topdown=False):
        print('****final stage of train')
        print("当前目录路径:", root)
        print("当前目录下所有子目录:", dirs)
        print("当前路径下所有非目录子文件:", files) # 打印当前目录下所有文件
    conn.close()
def common_entry():
    app.run(main)

if __name__ == '__main__':
    common_entry()



