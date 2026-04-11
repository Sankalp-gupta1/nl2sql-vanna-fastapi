from fastapi import FastAPI
from pydantic import BaseModel

from vanna_setup import vn

app = FastAPI()

# Request model
class QueryRequest(BaseModel):
    question: str

# Home route
@app.get("/")
def home():
    return {"message": "NL2SQL API is running 🚀"}

# Query route
@app.post("/ask")
def ask_query(request: QueryRequest):

    question = request.question

    try:
        # Generate SQL
        sql = vn.generate_sql(question)

        # Run SQL
        result = vn.run_sql(sql)

        return {
            "question": question,
            "sql": sql,
            "result": result.to_dict(orient="records")
        }

    except Exception as e:
        return {
            "error": str(e)
        }
@app.post("/visualize")
def visualize_query(request: QueryRequest):

    question = request.question

    try:
        # Generate SQL
        sql = vn.generate_sql(question)

        # Run SQL
        df = vn.run_sql(sql)

        # Create chart
        fig = vn.generate_plotly_figure(
            question=question,
            sql=sql,
            df=df
        )

        return {
            "sql": sql,
            "chart": fig.to_json()
        }

    except Exception as e:
        return {
            "error": str(e)
        }