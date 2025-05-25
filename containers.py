from dependency_injector import containers, providers
from user.infa.repository.user_repo import UserRepository
from user.application.user_service import UserService

class Container(containers.DeclarativeContainer):
    # wiring_config = containers.WiringConfiguration(modules=["user.application.user_service"]) # 특정 모듈만 하고싶을 때
    wiring_config = containers.WiringConfiguration(
        packages=["user"] # 해당 패키지 하위에 있는 모듈 모두 포함된다.
    )

    user_repo = providers.Factory(UserRepository)
    user_service = providers.Factory(UserService, user_repo=user_repo)