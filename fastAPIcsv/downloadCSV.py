from fastapi import FastAPI, Response
from fastapi.responses import StreamingResponse

app = FastAPI()

@app.get("/download")
def download_csv():
    # Open the CSV file for reading
    with open("data.csv", "r") as file:
        # Set the response headers
        headers = {
            "Content-Disposition": "attachment; filename=data.csv",
            "Content-Type": "text/csv",
        }

        # Return the file as a streaming response
        return StreamingResponse(file, headers=headers)
