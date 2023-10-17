import os
import socket

from fastapi import FastAPI


api = FastAPI()


@api.get(f"/{os.getenv('VERSION', 'v0')}")
def main() -> dict[str, str]:
    return {
        "msg": "success",
        "version": os.getenv("VERSION", "v0"),
        "hostname": socket.gethostname()
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(api, host="0.0.0.0", port=8000)