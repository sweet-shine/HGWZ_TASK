import time


def test_logging():
    import logging
    logging.basicConfig(level=logging.DEBUG)

    logging.error("出现了错误")
    time.sleep(2)
    print('aaa')
    logging.info("打印信息")
    time.sleep(2)
    logging.warning("警告信息")
