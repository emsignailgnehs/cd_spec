def file_load(path, name):
    s = path + '\\' + name
    raw_filename = r'{}'.format(s)

    with open(raw_filename , 'r') as f:
        raw_data = f.readlines()
        return raw_data