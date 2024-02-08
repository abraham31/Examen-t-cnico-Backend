from fastapi import APIRouter, HTTPException, Depends
import time
from ..data.database import get_database_client

router = APIRouter(
    prefix="/rating",
    tags=["Ratings"]
)

@router.get("/{show_id}/average")
async def get_rating_average(show_id: int, db_client=Depends(get_database_client)):
    try:
        # Simular un retraso de 4 segundos antes de calcular el promedio
        time.sleep(4)
        
        # Obtener todos los ratings para el show desde la base de datos
        ratings_cursor = db_client.CoppelTest.comments.find({"show_id": show_id}, {"_id": 0, "rating": 1})
        
        # Convertir el cursor a una lista
        ratings_list = list(ratings_cursor)
        
        # Verificar si hay ratings para el show
        if len(ratings_list) == 0:
            raise HTTPException(status_code=404, detail="No se encontraron ratings para este show")
        
        # Calcular el promedio de los ratings
        total_ratings = sum(rating["rating"] for rating in ratings_list)
        rating_average = total_ratings / len(ratings_list)
        
        return {"rating_average": rating_average}
    
    except Exception as e:
        # Manejar cualquier error y retornar un mensaje de error
        raise HTTPException(status_code=500, detail=f"Error al calcular el promedio de rating: {str(e)}")