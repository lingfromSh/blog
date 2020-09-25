########################
#  STARTING CONTROL
########################

if __name__ == "__main__":
    import uvicorn
    import os

    os.environ["blog-setting"] = "conf.dev"
    uvicorn.run("conf.application:app", port=8088, reload=True)
