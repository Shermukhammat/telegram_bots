import os, unicodedata, re 



def write_log(file_path : str = "data/logs.log", log : str = 'New text'):
    """This function helps you write logs
        Args:
        file_path (str, optional): You wnated write logs file. Defaults to None.
        log (str, optional): log text. Defaults to 'New text'.
    """
    with open(file_path, 'a') as file:
        file.write(log+"\n")
        file.close()
        

def remove_file(file_name : str, directory : str = 'data'):
    files_list = os.listdir(directory)
    if file_name in files_list:
        os.remove(f"{directory}/{file_name}")


def slugify(value, allow_unicode=False):
    """
    Taken from https://github.com/django/django/blob/master/django/utils/text.py
    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value)
    return re.sub(r'[-\s]+', ' ', value).strip('-_')