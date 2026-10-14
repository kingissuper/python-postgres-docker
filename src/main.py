from dotenv import find_dotenv, dotenv_values

env = dotenv_values(find_dotenv())

print(env['test'])