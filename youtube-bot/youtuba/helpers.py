



def write_log(file_path : str = "data/logs.log", log : str = 'New text'):
    """This function helps you write logs
        Args:
        file_path (str, optional): You wnated write logs file. Defaults to None.
        log (str, optional): log text. Defaults to 'New text'.
    """
    with open(file_path, 'a') as file:
        file.write(log+"\n")
        file.close()