from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

# Initialize FastAPI application

api = FastAPI()

# Configure CORS to allow external access
api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_methods=["GET"],  # Allow GET method
)


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
