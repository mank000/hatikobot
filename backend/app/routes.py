from fastapi import APIRouter

from .misc import get_data_imei
from .models import Imei

router = APIRouter(prefix="/api", tags=["items"])


@router.post("/check_imei/")
async def get_imei_from_api(imei: Imei):
    answer = await get_data_imei(imei)
    return answer
