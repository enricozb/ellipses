import colorlog

handler = colorlog.StreamHandler()
handler.setFormatter(
    colorlog.ColoredFormatter("%(log_color)s%(levelname)s: %(message)s")
)

logger = colorlog.getLogger()
logger.addHandler(handler)
