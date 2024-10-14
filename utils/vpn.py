import httpx
from marzban import MarzbanAPI, UserCreate, ProxySettings, UserResponse
from db.models import Server


async def get_server_token(server: Server) -> tuple[MarzbanAPI, str]:
    api = MarzbanAPI(server.address)

    token = await api.get_token(server.username, server.password)

    return api, token.access_token


async def add_user(user_id: int, server: Server) -> UserResponse:
    api, token = await get_server_token(server)
    try:
        new_user = UserCreate(username=f"tg{user_id}",
                              proxies={"vless": ProxySettings(flow="xtls-rprx-vision")},
                              inbounds={'vless': ['VLESS TCP REALITY']})
        added_user = await api.add_user(user=new_user, token=token)
        return added_user.links[0]
    except httpx.HTTPStatusError:
        return None


async def get_user(user_id: int, server: Server) -> UserResponse:
    api, token = await get_server_token(server)
    try:
        user_info = await api.get_user(username=f"tg{user_id}", token=token)
        return user_info.links[0]
    except httpx.HTTPStatusError:
        return None


async def remove_user(user_id: int, server: Server) -> bool:
    api, token = await get_server_token(server)
    try:
        await api.remove_user(username=f"tg{user_id}", token=token)
        return True
    except httpx.HTTPStatusError:
        return False


async def get_users_amount(server: Server) -> int:
    api, token = await get_server_token(server)
    users = await api.get_users(token=token)
    return len(users)