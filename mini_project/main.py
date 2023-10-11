from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import asyncpg

app = FastAPI()

# Pydantic model for input data validation
class DataInput(BaseModel):
    name: str
    surname: str
    age: int

async def get_database_connection():
    return await asyncpg.connect(
        user="your_user",
        password="your_password",
        database="your_database",
        host="your_host",
        port="your_port",
    )

@app.post("/store-data")
async def store_data(data: DataInput):
    try:
        conn = await get_database_connection()
        await conn.execute(
            "INSERT INTO mock_table VALUES ($1, $2)",
            data.value1,
            data.value2,
        )
        await conn.close()
        return {"message": "Data stored successfully"}
    except asyncpg.exceptions.UniqueViolationError as e:
        raise HTTPException(status_code=400, detail="Data already exists")
    except asyncpg.exceptions.ForeignKeyViolationError as e:
        raise HTTPException(status_code=400, detail="Invalid foreign key")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")

# Custom error handling for specific error types
@app.exception_handler(asyncpg.exceptions.PostgresError)
async def handle_postgres_error(request, exc):
    return JSONResponse(content={"error": "PostgreSQL error"}, status_code=500)

# Custom error handling for all other exceptions
@app.exception_handler(Exception)
async def handle_general_error(request, exc):
    return JSONResponse(content={"error": "An unexpected error occurred"}, status_code=500)

