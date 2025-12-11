from openai import AsyncOpenAI
from sqlalchemy import text

from core.config import settings
from core.db.session import async_session_maker
from .prompt import PROMPT


SYSTEM_MESSAGE = [{"role": "system", "content": PROMPT}]


client = AsyncOpenAI(
    api_key=settings.llm.key,
    base_url=settings.llm.base_url,
)


async def get_raw_sql(question: str) -> str | None:
    for attempt in range(1, settings.llm.attempts_count + 1):
        try:
            response = await client.chat.completions.create(
            model=settings.llm.model,
            messages=SYSTEM_MESSAGE + [{"role": "user", "content": question}]  # NOQA
            )
            return response.choices[0].message.content
        except Exception as e:
            if attempt == settings.llm.attempts_count:
                print(f"An exception occurred when making a request to the LLM. {e}")
    return None


async def get_answer(question: str) -> str:
    raw_sql = await get_raw_sql(question)
    if raw_sql and raw_sql != "null":
        async with async_session_maker() as session:
            response = await session.execute(text(raw_sql))
            return str(response.scalar())
    else:
        return ("Не смог сгенерировать ответ по вашему запросу,"
                " попробуйте задать вопрос иначе или попробуйте позже...")
