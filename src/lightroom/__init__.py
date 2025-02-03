from .utils.LightroomApp import LightroomApp
from .utils.get_lightroom_win import get_lightroom_win
from lightroom.exports.run_exports import run_exports


def init(username="정의되지않음"):

    # ✅ 전역 상태 확인

    lightroomApp = LightroomApp()
    lightroomApp.start()

    app = lightroomApp.get_app()
    lightroom = get_lightroom_win(app)

    run_exports(lightroom=lightroom)


__all__ = ["init"]
