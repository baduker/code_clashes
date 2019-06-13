def alias_gen(f_name, l_name):
    f = FIRST_NAME.get(f_name[0].upper())
    l = SURNAME.get(l_name[0].upper())
    return "{} {}".format(f, l) if f and l else \
            "Your name must start with a letter from A - Z."
