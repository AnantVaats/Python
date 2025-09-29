try:
    df=pd.read_excel("./m.excel")
    print(df)
except FileNotFoundError:
    print("Oops!")