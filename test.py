try:
    from decouple import config
    print("python-decouple is installed and can be imported!")
except ImportError:
    print("python-decouple cannot be imported.")
