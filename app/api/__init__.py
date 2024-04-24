from flask import Blueprint, jsonify

from app.extensions import MENTAL_HEALTH_GPT

api_bp = Blueprint("api_bp", __name__)


@api_bp.get("/req")
def answer():
    pass


@api_bp.get("/test")
def test():
    prompt = "Question: Please give me 12 random digits. (i.g 1,2,1,2,3,1,2,1,1).\nAnswer: "
    result = MENTAL_HEALTH_GPT(prompt)
    return jsonify({
        "status": "success",
        "prompt": prompt,
        "result": result,
    })
