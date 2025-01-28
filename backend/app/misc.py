import os

import aiohttp

api_url = os.environ.get("api_url")
headers = {"Authorization": f"Bearer {os.environ.get('api_key')}"}
data = {"deviceId": None, "serviceId": 13}


async def get_data_imei(imei):
    async with aiohttp.ClientSession() as session:
        try:
            payload = data.copy()
            payload["deviceId"] = imei.deviceId
            async with session.post(api_url + "checks/", headers=headers,
                                    json=payload) as resp:
                if resp.status == 402:
                    return "Пополните баланс для операции."
                if resp.status == 403:
                    return "Доступ к API запрещен."
                if resp.status == 201:
                    return await resp.json()
                return f"Ошибка сервера {resp.status}"
        except aiohttp.ClientError:
            return "Ошибка сервера"
