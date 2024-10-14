from handlers.basic import router as basic_router
from handlers.profile import router as profile_router
from handlers.help import router as help_router
from handlers.connect import router as connect_router
from handlers.tutors import router as tutors_router
from handlers import check

routers = [
    basic_router,
    profile_router,
    help_router,
    connect_router,
    tutors_router
]
