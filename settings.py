"""File with settings and configs for the project"""
from envparse import Env

env = Env()

# REAL_DATABASE_URL = env.str(
#     "REAL_DATABASE_URL",
#     default="postgresql+asyncpg://postgres:postgres@0.0.0.0:5432/postgres",
# )  # connect string for the real database

TEST_DATABASE_URL = "postgresql+asyncpg://postgres:postgres@195.19.51.156:5432/monolith_dataset_bayes_clusters_iforest_tree"

# APP_PORT = env.int("APP_PORT")