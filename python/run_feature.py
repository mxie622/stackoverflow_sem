from absl import flags, app
import pandas as pd
import logging, os, sqlite3

LOGGER = logging.getLogger(__name__)
FLAGS = flags.FLAGS

# Feature engineering function

def main(unused_argv) -> None:
    """ETL"""
    logging.basicConfig(level=logging.INFO)
    feature_mapping  = os.getenv('FEATURE_MAPPING')
    title = os.getenv('TITLE')
    LOGGER.info("Use SQLite3 table for ETL")
    # Link to database
    # conn = sqlite3.connect(f"""./bash/{title}_questions.db""")
    conn = sqlite3.connect(f"""/home/stackoverflow_sem/{title}_questions.db""")
    df = pd.read_sql_query(f"""select *                        
                        from mbd_{title} ;""", conn)
    # features = pd.read_csv(f"""./python/{feature_mapping}""")
    features = pd.read_csv(f"""/home/stackoverflow_sem/python/{feature_mapping}""")
    features_list = []
    for i in features.values:
        print(i[0])
        features_list.append(i[0])
    df = df[features_list]
    df = (df - df.min()) / (df.max() - df.min()) # normalization
    df.to_sql(f"""feature_{title}""", conn, if_exists="replace")
    conn.close()

def common_entry():
    app.run(main)

if __name__ == '__main__':
    common_entry()



