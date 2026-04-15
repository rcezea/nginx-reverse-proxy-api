from fastapi import FastAPI
from fastapi.responses import JSONResponse

# Initialize FastAPI application

api = FastAPI()


@api.get("/")
def root():
    """
        Root endpoint to verify that the API is running.
    """
    return JSONResponse(
        status_code=200,
        content={
            "message":
                "API is running"
        }
    )


@api.get("/health")
def status():
    """
        Health check endpoint.
    """
    return JSONResponse(
        status_code=200,
        content={
            "message":
                "healthy"
        }
    )


@api.get("/me")
def profile():
    """
        Returns basic profile information.
    """
    return JSONResponse(
        status_code=200,
        content={
            "name": "Richard Ezea",
            "email": "rclancing@gmail.com",
            "github": "https://github.com/rcezea"
        }
    )
