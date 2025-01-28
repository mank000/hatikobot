import os
import aiohttp
import json
from aiogram import filters, types, Router
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
import database.requests as rq
from .misc import is_valid_imei

router = Router()


class Allow(StatesGroup):
    key = State()


@router.message(filters.CommandStart())
async def cmd_start(message: types.Message, state: FSMContext):
    await rq.set_user(message.from_user.id)
    await state.set_state(Allow.key)
    await message.answer(
        "Привет! Для того, чтобы получить доступ "
        "к боту вам необходимо отправить API_KEY.")


@router.message(Allow.key)
async def allow_access(message: types.Message, state: FSMContext):
    access = False
    if message.text == os.environ.get("api_key"):
        access = await rq.allow_access(message.from_user.id)
    if access:
        await message.answer("Доступ разрешен")
        await state.clear()
        return
    await message.answer("Неверный ключ")


@router.message()
async def check_imei(message: types.Message):
    if not (is_valid_imei(message.text)):
        await message.answer("Некорректный IMEI")
        return
    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(
                    os.environ.get("backend_url") + "check_imei/",
                    json={"deviceId": str(message.text)}) as res:
                answer = await res.json()
                if res.status == 200:
                    await message.answer(
                        f"Ваши данные: {json.dumps(answer, indent=4, ensure_ascii=False)}")
                    return
                await message.answer(f"Ошибка на сервере. {res.status}")
        except Exception as e:
            await message.answer(f"Ошибка на сервере.{e}")
