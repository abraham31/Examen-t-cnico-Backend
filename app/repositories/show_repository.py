from typing import List
from ..models.model import Show, Comment
from ..data.database import get_database_client
from fastapi import HTTPException, Query, Depends
import requests, asyncio

#Search

async def search_shows(search_query: str = Query(..., description="Criterio de búsqueda"),
                       db_client=Depends(get_database_client)):
    try:
        existing_show = db_client.CoppelTest.shows_cache.find_one({"id": search_query})
        if existing_show:
            existing_show["comments"] = []  # Inicializar lista de comentarios
            return [existing_show]
        else:
            api_url = f"http://api.tvmaze.com/search/shows?q={search_query}"
            response = requests.get(api_url)
            response.raise_for_status()
            data = response.json()
            
            shows = []
            for item in data:
                show_data = item.get("show", {})
                summary = show_data.get("summary", "")
                if summary is None:
                    summary = ""
                channel = ""
                network = show_data.get("network")
                web_channel = show_data.get("webChannel")
                if network is not None:
                    channel = network.get("name", "")
                elif web_channel is not None:
                    channel = web_channel.get("name", "")
                    
                show = Show(
                    id=show_data.get("id"),
                    name=show_data.get("name"),
                    channel=channel,
                    summary=summary,
                    genres=show_data.get("genres")
                )
                
                # Obtener comentarios para el show desde MongoDB
                comments = db_client.CoppelTest.comments.find({"show_id": show.id})
                show_comments = [comment for comment in comments]
                
                show.comments = [Comment(**comment) for comment in show_comments]
                
                shows.append(show)
            
            db_client.CoppelTest.shows_cache.insert_many([show.dict() for show in shows])
            
            return shows
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error al realizar la solicitud a la API: {str(e)}")
    

# ShowById
    
async def search_and_cache_show_by_id(show_id: int, db_client):
    try:
        response = requests.get(f"http://api.tvmaze.com/shows/{show_id}")
        if response.status_code == 200:
            show_data = response.json()
            db_client.CoppelTest.shows_cache.insert_one(show_data)
    except Exception as e:
        print(f"Error al buscar y almacenar el show por ID {show_id}: {str(e)}")

async def search_show_by_id(show_id: int, db_client):
    try:
        cached_show = db_client.CoppelTest.shows_cache.find_one({"id": show_id})
        if cached_show:
            del cached_show["_id"]
            cached_show["id"] = str(cached_show["id"])
            return cached_show

        await search_and_cache_show_by_id(show_id, db_client)

        await asyncio.sleep(0.5)
        cached_show = db_client.CoppelTest.shows_cache.find_one({"id": show_id})
        if cached_show:
            del cached_show["_id"]
            cached_show["id"] = str(cached_show["id"])
            return cached_show

        raise HTTPException(status_code=404, detail="Show no encontrado en el caché")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al buscar el show por ID: {str(e)}")


async def search_shows(search_query: str = Query(..., description="Criterio de búsqueda"),
                       db_client = Depends(get_database_client)):
    try:
        existing_show = db_client.CoppelTest.shows_cache.find_one({"id": search_query})
        if existing_show:
            existing_show["comments"] = []
            return [existing_show]
        else:
            api_url = f"http://api.tvmaze.com/search/shows?q={search_query}"
            response = requests.get(api_url)
            response.raise_for_status()
            data = response.json()

            shows = []
            for item in data:
                show_data = item.get("show", {})
                summary = show_data.get("summary", "")
                if summary is None:
                    summary = ""
                channel = ""
                network = show_data.get("network")
                web_channel = show_data.get("webChannel")
                if network is not None:
                    channel = network.get("name", "")
                elif web_channel is not None:
                    channel = web_channel.get("name", "")

                show = Show(
                    id=show_data.get("id"),
                    name=show_data.get("name"),
                    channel=channel,
                    summary=summary,
                    genres=show_data.get("genres")
                )

                comments = db_client.CoppelTest.comments.find({"show_id": show.id})
                show_comments = [comment for comment in comments]

                show.comments = [Comment(**comment) for comment in show_comments]

                shows.append(show)

            db_client.CoppelTest.shows_cache.insert_many([show.dict() for show in shows])

            return shows
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error al realizar la solicitud a la API: {str(e)}")