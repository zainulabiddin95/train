import uvicorn
from fastapi import FastAPI

from user_router import user_router


def main() -> None:
    app = FastAPI()
    app.include_router(user_router)
    uvicorn.run(app=app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
