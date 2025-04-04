from datetime import date, datetime, timedelta, time
from decimal import Decimal
from pathlib import Path
import mysql.connector
from dotenv import load_dotenv
import os
import logging
from typing import cast, Iterable

logging.basicConfig(level=logging.DEBUG)

load_dotenv()


def run_sql_file(sql_path: str, replacements: dict = None):
    try:
        sql = Path(sql_path).read_text(encoding='utf-8')
        logging.debug(f"SQL original: {sql}")

        if replacements:
            for key, value in replacements.items():
                sql = sql.replace(key, f"'{value}'")
        logging.debug(f"SQL após substituições: {sql}")

        db_config = {
            "host": os.getenv("DB_HOST", "localhost"),
            "port": int(os.getenv("DB_PORT", 3306)),
            "user": os.getenv("DB_USER", "root"),
            "password": os.getenv("DB_PASSWORD", "root123"),
            "database": os.getenv("DB_NAME", "careintuitive")
        }
        logging.debug(f"Conectando ao DB com configuração: {db_config}")

        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        try:
            cursor.execute(sql, multi=True)
            result = []
            for res in cast(Iterable, cursor):
                if res.with_rows:
                    fetched = res.fetchall()
                    result.extend(fetched)
                    logging.debug(f"Resultado da execução: {fetched}")
                else:
                    logging.debug(f"Comando executado; rowcount: {res.rowcount}")
            conn.commit()

            # Checa warnings
            cursor.execute("SHOW WARNINGS")
            warnings = cursor.fetchall()
            if warnings:
                logging.warning(f"Warnings: {warnings}")

            return result
        except Exception as e:
            conn.rollback()
            error_msg = f"Erro ao executar SQL: {str(e)}"
            logging.error(error_msg)
            return {"error": error_msg}
        finally:
            cursor.close()
            conn.close()

    except Exception as e:
        error_msg = f"Erro na execução de run_sql_file: {str(e)}"
        logging.error(error_msg)
        return {"error": error_msg}


def run_select_sql_file(sql: str) -> list[tuple[Decimal | bytes | date | datetime | float | int | set[
    str] | str | timedelta | None | time, ...] | dict[str, Decimal | bytes | date | datetime | float | int | set[
    str] | str | timedelta | None | time]] | dict[str, str] | dict[str, str]:

    try:
        db_config = {
            "host": os.getenv("DB_HOST", "localhost"),
            "port": int(os.getenv("DB_PORT", 3306)),
            "user": os.getenv("DB_USER", "root"),
            "password": os.getenv("DB_PASSWORD", "root123"),
            "database": os.getenv("DB_NAME", "careintuitive")
        }
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            conn.commit()
            return result
        except Exception as e:
            conn.rollback()
            return {"error": str(e)}
        finally:
            cursor.close()
            conn.close()
    except Exception as e:
        return {"error": str(e)}
