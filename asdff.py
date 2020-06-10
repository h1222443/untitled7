import os



class PortfolioStrategyApp:
    """"""

    app_name = APP_NAME
    app_module = __module__
    app_path = os.getcwd(__file__).parent
    display_name = "组合策略"
    engine_class = StrategyEngine
    widget_name = "PortfolioStrategyManager"
    icon_name = "strategy.ico"