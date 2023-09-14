from typing import Optional

from pydantic import BaseSettings, EmailStr

INVESTED_AMOUNT = 0
FULLY_INVESTED = False
MAX_LENGTH_NAME = 100
MIN_STR_LENGTH = 1
MAX_LENGTH_DESCRIPTION = 300
TITLE = 'QRKot'
DESCRIPTION = 'Благотворительный фонд поддержки котиков'
DB = 'sqlite+aiosqlite:///./cat_fund.db'
SECRET = 'SECRET'


class Settings(BaseSettings):
    app_title: str = TITLE
    description: str = DESCRIPTION
    database_url: str = DB
    secret: str = SECRET
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None

    class Config:
        env_file = '.env'


settings = Settings()
