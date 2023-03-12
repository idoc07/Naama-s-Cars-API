import uvicorn
import app_config

# Auto run uvicorn 2
if __name__ == "__main__":
    uvicorn.run(app_config.APP_NODE, host=app_config.APP_HOST, port=app_config.APP_PORT)
