# flake8: noqa
from event import EventEngine

from engine import MainEngine
from ui import MainWindow, create_qapp


from getway.ctp_getway import CtpGateway



def main():
    """"""
    qapp = create_qapp()

    event_engine = EventEngine()

    main_engine = MainEngine(event_engine)


    main_engine.add_gateway(CtpGateway)


    main_window = MainWindow(main_engine, event_engine)
    main_window.showMaximized()

    qapp.exec()


if __name__ == "__main__":
    main()