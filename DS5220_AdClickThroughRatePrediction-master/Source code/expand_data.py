def repl(data):
    for index, row in data.iterrows():
        if row['Impression'] > 1:
            data = data.append([row]*(int(row['Impression']-1)),ignore_index=True)
        
        if index%10000 == 0:
            print("Rows completed : ", index)
    return data

