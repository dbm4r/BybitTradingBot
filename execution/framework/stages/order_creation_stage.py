from execution.framework.base_executor import (
    BaseExecutor,
)

from execution.services.order_request_factory import (
    OrderRequestFactory,
)


class OrderCreationStage(
    BaseExecutor,
):

    def execute(
        self,
        engine,
        context,
    ):

        context.order = (
            OrderRequestFactory.create_market_buy(
                engine=engine,
                context=context,
            )
        )

        return context