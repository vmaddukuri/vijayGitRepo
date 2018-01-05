        import pandas as pd
        column_name = ['login', 'passwd', 'uid', 'gid', 'gecos', 'home', 'shell']
        df=pd.read_csv("/etc/passwd", sep=':', names=column_name)
        print(df.groupby('shell').groups)
