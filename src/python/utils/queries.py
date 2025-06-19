"""SQL query loader using aiosql for clean separation of SQL and Python code."""

import aiosql
from pathlib import Path

# Navigate from utils folder to project root, then to sql folder
_PROJECT_ROOT = Path(__file__).parent.parent.parent
_SQL_PATH = _PROJECT_ROOT / "sql"

# Load all .sql files as methods - supports nested folders for organization
queries = aiosql.from_path(_SQL_PATH, "psycopg2")

# Abstraction hint: Consider organizing SQL files by domain:
# sql/
#   elections/
#     get_results.sql
#     get_turnout.sql
#   demographics/
#     get_population.sql
#   analysis/
#     compare_regions.sql
#
# Usage in notebooks:
# from wahlen.src.python.utils.queries import queries
# results = queries.get_results(conn, election_id=123)
