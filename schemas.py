from pydantic import BaseModel  # ,constr


# Defines Various Schemas (JSON as calsses) for accepting request and returning response

class HealthCheck(BaseModel):
    project: str = 'EspApi'
    version: str = '0.2.0'


class nameInsert(BaseModel):
    name: str
    # or
    # name: constr(strip_whitespace=True, strict=True, max_length=100)
    message: str


class nameRead(BaseModel):
    name: str


class nameOut(BaseModel):
    name: str
    message: str
