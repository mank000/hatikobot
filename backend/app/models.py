from pydantic import BaseModel


class Imei(BaseModel):
    deviceId: str
