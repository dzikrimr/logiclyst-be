import os
from fastapi import Header, HTTPException, status

APP_SECRET_KEY = os.getenv("APP_SECRET_KEY")

async def validate_api_key(x_api_key: str = Header(None)):
    # Cek key di server
    if not APP_SECRET_KEY:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Server Error: Secret Key belum dikonfigurasi di backend."
        )
    
    # 2. Validasi key
    if x_api_key != APP_SECRET_KEY:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="Unauthorized: API Key salah atau tidak ditemukan."
        )
    return x_api_key