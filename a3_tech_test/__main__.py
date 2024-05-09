from a3_tech_test.app.main import app
import uvicorn

if __name__ == "__main__":
    print("Application Started")
    
    uvicorn.run(
        app=app,
        host="0.0.0.0",
        port="8000",
        reload=True
    )