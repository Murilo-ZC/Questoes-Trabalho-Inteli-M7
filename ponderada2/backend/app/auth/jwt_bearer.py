from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from .jwt_handler import decodeJWT

class jwtBearer(HTTPBearer):
    def _init_(self, auto_error: bool = True):
        super(jwtBearer, self)._init_(auto_error=auto_error)

    async def _call_(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(jwtBearer, self)._call_(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Token inválido ou expirado.")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Token inválido ou expirado.")
        
    def verify_jwt(self, jwttoken:str):
        isTokenValid: bool = False
        payload = decodeJWT(jwttoken)
        if payload:
            isTokenValid = True
        return isTokenValid