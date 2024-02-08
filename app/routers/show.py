from fastapi import APIRouter, HTTPException, Query, Depends
from ..data.database import get_database_client
from ..models.model import Show
from ..repositories.show_repository import search_shows, search_show_by_id
from typing import List
import requests

router = APIRouter(
    prefix="/show",
    tags=["Shows"]
)


@router.get("/search/", response_model=List[Show])
async def search_shows_handler(search_query: str = Query(..., description="Criterio de búsqueda"),
                                db_client=Depends(get_database_client)):
    return await search_shows(search_query, db_client)
    
    

# Request para buscar el show por ID
@router.get("/searchbyid/{show_id}")
async def search_show_by_id_endpoint(show_id: int, db_client=Depends(get_database_client)):
    try:
        return await search_show_by_id(show_id, db_client)
    except HTTPException as e:
        return e
