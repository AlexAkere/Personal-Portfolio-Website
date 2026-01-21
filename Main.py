from fastapi import FastAPI

# Initialize the App
app = FastAPI()

# Create a "Route" (an endpoint)
# When someone goes to /, run this function
@app.get("/")
def home():
    return {"message": "Welcome to Alex's Iron Calculator API"}

# Create a route to get workout info
@app.get("/workouts")
def get_workouts():
    # In the future, we will pull this from a SQL database.
    # For now, we return fake data (JSON).
    return [
        {"id": 1, "exercise": "Bench Press", "weight": 225, "reps": 5},
        {"id": 2, "exercise": "Squat", "weight": 315, "reps": 3}
    ]