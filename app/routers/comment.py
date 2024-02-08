from fastapi import APIRouter, HTTPException, Depends
from ..models.model import CommentInput
from pymongo.errors import PyMongoError
from ..data.database import get_database_client

router = APIRouter(
    prefix="/comment",
    tags=["Comments"]
)

@router.post("/", response_model=dict)
async def save_comment(comment_input: CommentInput, db_client=Depends(get_database_client)):
    try:
        # Insertar el comentario y la calificación en la base de datos
        db_client.CoppelTest.comments.insert_one({
            "show_id": comment_input.show_id,
            "comment": comment_input.comment,
            "rating": comment_input.rating
        })
        return {"status": "Calificación y comentario guardados exitosamente"}
    except PyMongoError as e:
        # Manejar errores específicos de MongoDB
        raise HTTPException(status_code=500, detail=f"Error al guardar la calificación y comentario en la base de datos: {str(e)}")
    except Exception as e:
        # Manejar cualquier otro error
        raise HTTPException(status_code=500, detail=f"Error inesperado al guardar la calificación y comentario: {str(e)}")