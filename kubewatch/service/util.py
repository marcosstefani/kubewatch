def treat_null(value):
    if value in ['<none>', '', None]:
        return None
    return value
